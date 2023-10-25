from __future__ import annotations
import Pyfemap
from Pyfemap import constants as fc
from Pyfemap import ISet as FeSet
from Pyfemap import ISolid as FeSolid
from .fem_entities import get_normal_vector_at_node
from .helpers import list_to_fset, fset_to_list, _resolve_entity_id_params, check_return_code
from collections.abc import Iterable

__all__ = [
    'create_points_at_nodes', 'create_surfaces_from_mesh', 'get_free_edge_curves', 'adjust_workplane_to_normal',
    'create_csys', 'cleanup_surfaces', 'create_ellipse', 'project_curves_onto_solid', 'stitch_surfaces',
    'get_point_coords', 'break_curve_at_point', 'find_surfaces_on_solid'
]


def create_points_at_nodes(
        femap:      Pyfemap.model,
        node_list:  int | Iterable[int],
        as_fset:    bool = False
) -> int | list[int] | FeSet:
    """Creates geometric points at existing node locations specified.

    If only one point is desired, node_list can be an int, and you will receive an int back. Otherwise, for multiple
    nodes, pass a list of node IDs, and a list of point IDs will be returned

    Parameters
    ----------
    femap
        FEMAP application object
    node_list
        Node(s) that you want to create points at.
    as_fset
        Optional: (Default=False) Indicates if you want return type to be a FEMAP Set Object instead of a Python list

    Returns
    -------
    int | list[int] | FeSet:
        An int (for one point created), list (for multiple IDs) or Femap Set (single ID or mutliple IDs) containing the
        ID(s) of the point or points created

    Examples
    --------
    >>> node_id = 41800000
    >>> point_id = create_points_at_nodes(femap, node_id)

    >>> list_of_nodes = [41800000, 41800001, 41800002]
    >>> point_ids = create_points_at_nodes(femap, list_of_nodes)
    """

    node_list = _resolve_entity_id_params(femap, node_list)

    fe_point = femap.fePoint
    fe_node = femap.feNode

    point_list: list[int] = []

    # Iterate through the list and create a geometric point at the same location
    for node in node_list:
        if fe_node.Exist(node):
            fe_node.Get(node)
            fe_point.ID = fe_point.NextEmptyID()
            fe_point.x = fe_node.x
            fe_point.y = fe_node.y
            fe_point.z = fe_node.z
            fe_point.Put(fe_point.ID)
            point_list.append(fe_point.ID)
        else:
            print(f'Node {node} does not exist.')
            continue

    femap.feViewRegenerate(0)

    if as_fset:
        fe_point_set = list_to_fset(femap, point_list)
        return fe_point_set

    # Return an int if only 1 point was created, otherwise return a list of ints
    if len(point_list) == 1:
        point_id: int = point_list[0]
        return point_id
    else:
        return point_list


def create_surfaces_from_mesh(
        femap:          Pyfemap.model,
        element_ids:    int | Iterable[int],
        delete_elem:    bool = True,
        as_fset:        bool = False,
) -> tuple[list[int], list[int]] | tuple[FeSet, FeSet]:
    """Creates individual geometric surfaces at each specified element and returns surfaces and curves created.

    Parameters
    ----------
    femap
        FEMAP application object
    element_ids
        Elements IDs that are to be converted to a surface
    delete_elem
        Optional: Default=True. Deletes the element used to create the surface.
    as_fset
        Optional: Default=False. Indicates if you want return type to be a FEMAP Set Object instead of a Python list

    Returns
    -------
    tuple[list[int], list[int]] | tuple[FeSet, FeSet]:
        Python lists or FEMAP Set Objects containing the surface IDs and curve IDs created during the process.

    Examples
    --------
    >>> elements = [1001, 1002]
    >>> surface_ids, curve_ids = create_surfaces_from_mesh(femap, elements, as_fset=True)

    >>> surface_ids, curve_ids = create_surfaces_from_mesh(femap, 41940821)
    """

    # Logic to check valid params --------------------------------------------------------------------------------------
    element_ids = _resolve_entity_id_params(femap, element_ids)

    # Femap function to track new geometry being created
    geo_tracking = femap.feTrackData
    geo_tracking.StartGeometry()

    # Adds an individual element to a FEMAP set, and creates a surface from the element
    set_eids = femap.feSet
    for elem in element_ids:
        set_eids.clear()
        set_eids.Add(elem)
        femap.feSurfaceFromMesh2(set_eids.ID, delete_elem, False, 0.000001, False, 0.0, 1.0)

    # Stops tracking function and puts the ids of surfaces and curves created into a FEMAP Set
    geo_tracking.StopAll()
    fe_surfaces_created: FeSet = femap.feSet
    fe_curves_created: FeSet = femap.feSet
    geo_tracking.Created(fc.FT_SURFACE, fe_surfaces_created.ID, False)
    geo_tracking.Created(fc.FT_CURVE, fe_curves_created.ID, False)

    femap.feViewRegenerate(0)

    if as_fset:
        return fe_surfaces_created, fe_curves_created
    else:
        surfaces_created = fset_to_list(fe_surfaces_created)
        curves_created = fset_to_list(fe_curves_created)
        return surfaces_created, curves_created


def get_free_edge_curves(
        femap:      Pyfemap.model,
        curve_ids:  int | Iterable[int] | FeSet = None,
        as_fset:    bool = False
) -> list[int] | FeSet:
    """Checks a list of curves to see if they are considered free edges. If no curve ids are passed, checks all curves

    Parameters
    ----------
    femap
        FEMAP application object
    curve_ids
        Optional: (Defaults to None->Will check all curves) Curve IDs to test if they are free edges.
    as_fset
        Optional: (Default=False) Indicates if you want return type to be a FEMAP Set Object instead of a Python list

    Returns
    -------
    list[int] | FeSet
        Python list or FEMAP Set object containing the IDs of geometric curves that are free edges
    """
    if curve_ids is None:
        fe_curve_set = femap.feSet
        fe_curve_set.AddAll(fc.FT_CURVE)
        curve_ids = fset_to_list(fe_curve_set)
    elif isinstance(curve_ids, FeSet):
        curve_ids = fset_to_list(curve_ids)
    else:
        curve_ids = (int(curve_ids),) if isinstance(curve_ids, (int, str)) else tuple(curve_ids)

    fe_curve = femap.feCurve
    free_edge_curves = []

    for curve in curve_ids:
        fe_curve.Get(curve)
        if fe_curve.IsFreeEdge():
            free_edge_curves.append(curve)

    if as_fset:
        return list_to_fset(femap, free_edge_curves)
    else:
        return free_edge_curves


def adjust_workplane_to_normal(
        femap:          Pyfemap.model,
        normal_vector:  tuple[float, float, float] | list[float],
        location:       tuple[float, float, float] | list[float] | int,
        return_curve:   bool = False
) -> None | int:
    """Orients the FEMAP workplane to a normal vector specified, and moves the workplane origin.

    This is similar to the built-in FEMAP API 'Move Workplane Tangent to Curve' under 'GeometryProcessing' in the custom
    tools API menu.

    This ensures the user can create and project new geometry onto a desired surface, given the surface normal vector,
    and the approximate location of the surface. The workplane origin is moved to the location provided offset by
    the unit vector. This ensures the user can correctly use the geometric 'Project onto..' functions.

    Parameters
    ----------
    femap
        FEMAP application object
    normal_vector
        (x, y, z) in global coordinates of the desired normal vector to adjust the workplane to.
    location
        Base point of the normal vector, ideally located on the surface you wish to project new geometry on.
            - For global coords: pass this as 3-element tuple or list
            - For a geometric point: pass the point ID as an int
    return_curve
        Optional: Default=False. Set to True if you want to keep the geometric curve representing the normal vector at
        the location provided and return the ID of that curve, otherwise False will delete_entity the geoemetry created
        from this method.

    Returns
    -------
    int
        Optional: A geometric curve representing the normal vector at the location provided is generated during this
        method to help adjust the workplane. If the user wants to keep it in their model, then the Curve ID is returned.
        Otherwise, all geometry created during this method is deleted from the database.

    Examples
    --------
    >>> norm_vec = get_normal_vector_at_node(femap, 41974070)
    >>> point_id = create_points_at_nodes(femap, 41974070)
    >>> norm_curve = adjust_workplane_to_normal(femap, norm_vec, point_id, True)
    """

    fe_point_base = femap.fePoint
    fe_point_tip = femap.fePoint

    # If 'location' is passed as an int, assume it means point ID, and check to see if it exists.
    if isinstance(location, int):
        point_provided = True
        if fe_point_base.Exist(location):
            fe_point_base.Get(location)
        else:
            raise AttributeError(
                f'Point ID: {location} does not exist. Either pass a valid point ID, or pass the '
                f'location as global coordinates coordinates (x, y, z)'
            )
    else:
        point_provided = False
        fe_point_base.ID = fe_point_base.NextEmptyID()
        fe_point_base.x = location[0]
        fe_point_base.y = location[1]
        fe_point_base.z = location[2]
        fe_point_base.Put(fe_point_base.ID)

    # Add the components of the normal vector to the 'location' or base point coords to generate a second point.
    # This serves as the offset for the workplane as well as the tip point for a curve that represents the normal vector
    # and helps us move the workplane
    fe_point_tip.ID = fe_point_tip.NextEmptyID()

    fe_point_tip.x = fe_point_base.x + normal_vector[0]
    fe_point_tip.y = fe_point_base.y + normal_vector[1]
    fe_point_tip.z = fe_point_base.z + normal_vector[2]

    # Store the point in the database
    fe_point_tip.Put(fe_point_tip.ID)

    # Create the helper curve
    fe_curve = femap.feCurve
    femap.feLinePoints(False, fe_point_base.xyz, [fe_point_tip.xyz], True)
    fe_curve.Last()
    femap.feViewRegenerate(0)
    normal_curve_id: int = fe_curve.ID

    # Generates vectors which are needed to define the workplane
    v1 = fe_curve.Tangent(False, fe_point_base.xyz)[1]
    v2 = femap.feVectorPerpendicular(v1)[1]
    v3 = femap.feVectorCrossProduct(v2, v1)[1]

    # Set the workplane origin as the 'tip' of the normal vector.
    femap.vInfo_WorkplaneOrigin = [fe_point_tip.x, fe_point_tip.y, fe_point_tip.z]

    # Set the vectors that define the orientation of the workplane
    femap.vInfo_WorkplaneX = [-1 * value for value in v2]  # Reverse the signs on v2
    femap.vInfo_WorkplaneY = v3
    femap.vInfo_WorkplaneZ = v1

    if return_curve:
        femap.feViewRegenerate(0)
        return normal_curve_id

    else:
        fe_point_tip.Delete(fe_point_tip.ID)
        fe_curve.Delete(fe_curve.ID)
        if not point_provided:
            fe_point_base.Delete(fe_point_base.ID)
        femap.feViewRegenerate(0)
        return


def create_csys(
        femap:          Pyfemap.model,
        csys_type:      int,
        axis_method:    int,
        origin:         int | Iterable[float],
        axis_1:         tuple[float, float, float] | list[float],
        axis_2:         tuple[float, float, float] | list[float]
) -> int | None:
    """Creates a new coordinate system at the location specified. Utilizes 'Two Axes' method of defining CSYS.

    get_normal_vector_at_node() is a good helper method if you want to create a local CSYS at a specific node.

    csys_type is an integer flag specific to the FEMAP API that dictates what *type* of CSYS you want
        - 0 = Rectangular
        - 1 = Cylindrical
        - 2 = Spherical

    axis_method is an integer flag specific to the FEMAP API that dictates *how* you want to define the CSYS
        - 0 --> X = normal, axis1 = Y, axis2 = YZ plane
        - 1 --> Y = normal, axis1 = X, axis2 = XZ plane
        - 2 --> Z = normal, axis1 = X, axis2 = XY plane

    Parameters
    ----------
    femap
        FEMAP application object
    csys_type
        Integer flagging what type of coord system to use.
    axis_method
        Integer which specifies how to define the CSYS
    origin
        Location of origin in the new CSYS. Can be passed as a Point ID (int), or a 3-element list or tuple containing
        the global coordinates (x, y, z)
    axis_1
        Axis 1 vector in global coords. Dependent on axis method.
    axis_2
        Axis 2 vector in global coords. Dependent on axis method.

    Returns
    -------
    int
        ID of newly created CSYS

    Examples
    --------
    >>> new_csys_id = create_csys(femap, 0, 0, origin=(0.0, 0.0, 0.0), axis_1=(0.0, 1.0, 0.0), axis_2=(0.0, 0.0, 1.0))
    """

    # If passed as a point ID, convert to coordinates
    if isinstance(origin, (int, str)):
        fe_point = femap.fePoint
        if not fe_point.Exist():
            print(f'Point {origin} does not exist')
            return
        else:
            fe_point.Get(int(origin))
            origin = (fe_point.x, fe_point.y, fe_point.z)

    fe_csys = femap.feCSys
    fe_csys.ID = fe_csys.NextEmptyID()
    fe_csys.TwoAxes(csys_type, axis_method, tuple(origin), tuple(axis_1), tuple(axis_2))
    fe_csys.Put(fe_csys.ID)
    csys_id: int = fe_csys.ID

    femap.feViewRegenerate(0)

    return csys_id


def cleanup_surfaces(
        femap:          Pyfemap.model,
        surface_ids:    int | Iterable[int],
        redundant:      bool = True,
        sliver:         bool = True,
        check:          bool = True
) -> None:
    """Performs the Geo->Solid->Cleanup action in FEMAP.

    Parameters
    ----------
    femap
        FEMAP application object
    surface_ids
        Surface ID(s) to clean up. Can pass a single surface ID as an int, or a list of surface IDs
    redundant
        Optional: Default=True. Redundant geometry will be removed
    sliver
        Optional: Default=True. Attempt will be made to remove any and all small sliver surfaces
    check
        Optional: Default=True. Solids will be checked to ensure they are still valid

    Examples
    --------
    >>> cleanup_surfaces(femap, [1, 2])
    """
    fe_set = _resolve_entity_id_params(femap, surface_ids, as_fset=True)

    femap.feAppUndoCheckpoint("Undo solid cleanup")

    rc = femap.feSolidCleanup(fe_set.ID, redundant, sliver, check)

    check_return_code(rc, 'Error cleaning up geometry')
    femap.feViewRegenerate(0)

    return


def create_ellipse(
        femap:              Pyfemap.model,
        location:           int | Iterable[float],
        major_axis_vector:  Iterable[float],
        major_radius:       float,
        minor_radius:       float,
        as_fset:            bool = False
) -> list[int] | FeSet:
    """Creates splines in the workplane that form an ellipse through the feSplineEllipse function.

    Parameters
    ----------
    femap
        FEMAP application object
    location
        Point ID **or** the global coordinates (x, y, z) where the center of the ellipse will be located
    major_axis_vector
        Vector coordinates representing the direction of the major axis of the ellipse [x, y, z]
    major_radius
        Length of ellipse major radius
    minor_radius
        Length of ellipse minor radius
    as_fset
        Optional: (Default=False) Indicates if you want return type to be a FEMAP Set Object instead of a Python list

    Returns
    -------
    list[int] | FeSet
        Python list or FEMAP Set Object containing the IDs of the curves_created
    """
    fe_curves_created_set = femap.feSet
    geo_tracking = femap.feTrackData

    # Assume location is a point ID if passed as an int
    if isinstance(location, int):
        fe_point = femap.fePoint
        if fe_point.Exist(location):
            fe_point.Get(location)
            coordinates = (fe_point.x, fe_point.y, fe_point.z)
        else:
            raise AttributeError(
                f'Location passed as Point ID: {location} which does not exist in the database. '
                f'Cannot create ellipse'
            )

    # Type casting to a tuple with 3 floats if passed as coordinates
    elif isinstance(location, (list, tuple, set)):
        if len(location) == 3:
            coordinates = tuple(float(value) for value in location)
        else:
            raise AttributeError(f'Error with location coordinates. Expected (x, y, z) but got {location}')
    else:
        raise TypeError(f'location was passed as a {type(location)}. Expected int or Iterable[float]')

    geo_tracking.StartGeometry()
    femap.feSplineEllipse(coordinates, major_axis_vector, major_radius, minor_radius, True)
    geo_tracking.StopAll()

    geo_tracking.Created(fc.FT_CURVE, fe_curves_created_set.ID, False)

    if as_fset:
        return fe_curves_created_set
    else:
        return fset_to_list(fe_curves_created_set)


def project_curves_onto_solid(
        femap:              Pyfemap.model,
        curve_ids:          int | Iterable[int] | FeSet,
        solid_id:           int | FeSolid,
        projection_vector:  Iterable[float] = None,
        split_solid:        bool = True
) -> None:
    """Projects a curve or list of curves onto a solid / sheet-solid.

    If a projection_vector is not passed, then the projection is done to the closest location on the solid. If
    projecting on a flat plate, this is usually ok, but if you are projecting onto a curved surface, recommend you
    pass a vector, otherwise the resulting shape might be warped.

    Parameters
    ----------
    femap
        FEMAP application object
    curve_ids
        Curves IDs to be projected
    solid_id
        Either a Solid, or Sheet-Solid (surface)
    projection_vector
        Optional: Projection Vector. Default value will project to the closest location on the solid.
    split_solid
        Optional: Default=True. Set to False if you don't want to split the solid with the projected curves
    """
    # Transform the curve_ids to a FEMAP Set object (FeSet)
    fe_curve_ids: FeSet = _resolve_entity_id_params(femap, curve_ids, as_fset=True)

    # Checking to see if the solid exists. If FeSolid object is passed, get its ID as an int
    fe_solid = femap.feSolid
    if isinstance(solid_id, int):
        if not fe_solid.Exist(solid_id):
            raise ValueError(f'Solid ID: {solid_id} does not exist')
    elif isinstance(solid_id, FeSolid):
        if fe_solid.Exist(solid_id.ID):
            solid_id: int = solid_id.ID
    else:
        raise TypeError(f'Solid_id was passed as {solid_id}. Needs to be an int.')

    # Toggles the projectNormal boolean in FEMAP API to False if a projection_vector has been supplied.
    project_normal = False if projection_vector else True

    # split_solid param is used in this method. Default=True - will split surfaces as curves are projected onto them.
    femap.feCurveUpdateSurfaces(split_solid, True)
    femap.feCurveProjectOntoSolid(project_normal, projection_vector, solid_id, fe_curve_ids.ID, True)

    return


def stitch_surfaces(
        femap:          Pyfemap.model,
        surface_ids:    Iterable[int] | FeSet,
        cleanup:        bool = True,
        tolerance:      float = 0.000001,
) -> None:
    """Stitch a list of surfaces (i.e. sheet-solids) together

    Parameters
    ----------
    femap
        FEMAP application object
    surface_ids
        List or FEMAP Set containing the IDs of the surfaces to stitch together
    cleanup
        Optional: Default=True. Set to False if you don't want to perform the Solid->Cleanup operation after stitching
    tolerance
        Optional: Default=0.000001 - Stitching tolerance.
    """
    fe_surface_set = _resolve_entity_id_params(femap, surface_ids)

    if cleanup:
        rc = femap.feSolidStitch(fe_surface_set.ID, tolerance)
    else:
        rc = femap.feSolidStitchNoCleanup(fe_surface_set.ID, tolerance)

    check_return_code(rc, 'Could not stitch selected surfaces')

    femap.feViewRegenerate(0)

    return


def get_point_coords(
        femap:      Pyfemap.model,
        point_id:   int
) -> tuple[float, float, float] | None:
    """Returns global coordinates (x, y, z) of a FEMAP geometric point.

    Parameters
    ----------
    femap
        FEMAP application object
    point_id

    Returns
    -------
    tuple
        Coords in the form (x, y, z)

    """
    fe_point = femap.fePoint
    if fe_point.Exist(point_id):
        fe_point.Get(point_id)
        coords = fe_point.xyz
        return coords
    else:
        print(f'Point {point_id} does not exist')
        return None


def break_curve_at_point(
        femap: Pyfemap.model,
        curve_id: int,
        location: int | Iterable[float]
) -> None:
    """Breaks a geometric curve at a point or coordinate.

    Parameters
    ----------
    femap
        FEMAP application object
    curve_id
        Curve to break
    location
        Point ID, or (x,y,z) coordinates at the break location
    """
    if isinstance(location, int):
        break_coords = get_point_coords(femap, location)
    elif isinstance(location, (tuple, list, set)) and len(location) == 3:
        break_coords = tuple(float(value) for value in location)
    else:
        raise TypeError(
            f'location passed as {location} which is a {type(location)}. Expected a point ID or a coordinate (x,y,z)'
        )

    if isinstance(curve_id, (int, str)):
        fe_curve = femap.feCurve
        if not fe_curve.Exist(int(curve_id)):
            raise ValueError(f'curve {curve_id} does not exist')
    else:
        raise TypeError(f'Curve_id passed as {curve_id} which is a {type(curve_id)}. Expected int.')

    femap.feCurveBreak(curve_id, break_coords)
    femap.feViewRegenerate(0)


def find_surfaces_on_solid(
        femap:              Pyfemap.model,
        solid_id:           int,
        n_combined_mode:    int = 0,
        as_fset:            bool = False,
) -> list[int] | FeSet:
    """Identifies individual surface IDs on a single sheet-solid or solid. Returns empty list if solid does not exist.

    Parameters
    ----------
    femap
        FEMAP application object
    solid_id
        Sheet-Solid or Solid to find surfaces on.
    n_combined_mode
        Optional: Default=0. Integer flag denoting FEMAP constant for surface selection options.

            - 0 = List contains the basic surfaces that are on the solid
            - 1 = Surfaces on the solid that are in a Combined Surface are replaced by the ID of the Combined Surface
            - 2 = List contains both the underlying and combined surfaces.
    as_fset
        Optional: Flag to indicate if you want the return type to be a FEMAP Set Object instead of a Python list

    Returns
    -------
    list[int] | FeSet
        Python list or FEMAP Set containing the surface IDs found

    Examples
    --------
    >>> find_surfaces_on_solid(femap, 5)
    """
    fe_solid = femap.feSolid

    if fe_solid.Exist(solid_id):
        fe_solid.Get(solid_id)
    else:
        print(f'Solid ID: {solid_id} does not exist')
        return []

    rc, num_surf, surface_list = fe_solid.Surfaces(n_combined_mode)

    if check_return_code(rc, f'Unable to get the surface list. Possibly data is not stored or ID is not set correctly'):
        surface_list = list(surface_list)
        if as_fset:
            fe_surface_set = list_to_fset(femap, surface_list)
            return fe_surface_set
        else:
            return surface_list
    else:
        return []

