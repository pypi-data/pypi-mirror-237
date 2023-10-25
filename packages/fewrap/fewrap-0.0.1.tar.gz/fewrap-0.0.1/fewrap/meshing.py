from __future__ import annotations

import Pyfemap
from Pyfemap import constants as fc
from Pyfemap import ISet as FeSet
from collections.abc import Iterable
from .helpers import list_to_fset, fset_to_list, _resolve_entity_id_params, check_return_code

__all__ = ['size_surfaces_to_mesh', 'size_curves_to_mesh', 'mesh_surface', 'equivalence_nodes']


def size_surfaces_to_mesh(
        femap:              Pyfemap.model,                      # Required Param
        surface_list:       int | Iterable[int] | FeSet,        # Required Param
        mesh_size:          float = 0.0,
        replace_all:        bool = True,
        min_edge:           int = 0,
        max_angle:          float = 0.0,
        max_on_small:       int = 0,
        small_size:         float = 0.0,
        vertex_aspect:      float = 0.0,
        mapped_refinement:  bool = True,
        growth_factor:      float = 0.0,
        refine_ratio:       float = 0.0,
        refine_surf:        bool = True
) -> None:
    """Sets a mesh size on a surface prior to meshing

    Optional params have default values of 0, 0.0, or True, which tells FEMAP to use its own defaults.

    - See FEMAP API feMeshSizeSurface() for more info on the optional params

    Parameters
    ----------
    femap
        FEMAP application object
    surface_list
        ID(s) of the surface(s) to size
    mesh_size
        Optional - Default is set to let FEMAP calculate the mesh size.

    replace_all
    min_edge
    max_angle
    max_on_small
    small_size
    vertex_aspect
    mapped_refinement
    growth_factor
    refine_ratio
    refine_surf

    Examples
    --------
    >>> size_surfaces_to_mesh(femap, [1, 2, 3, 4, 5])

    >>> size_surfaces_to_mesh(femap, 6, mesh_size=0.025, mapped_refinement=False)
    """
    fe_surface_set: FeSet = _resolve_entity_id_params(femap, surface_list, as_fset=True)

    rc = femap.feMeshSizeSurface(
        fe_surface_set.ID, replace_all, mesh_size, min_edge, max_angle, max_on_small, small_size, vertex_aspect,
        mapped_refinement, growth_factor, refine_ratio, refine_surf
    )

    check_return_code(rc)

    femap.feViewRegenerate(0)

    return


def size_curves_to_mesh(
        femap:              Pyfemap.model,              # Required Param
        curve_list:         int | Iterable[int],        # Required Param
        num_elem:           int = 0,
        mesh_size:          float = 0.0,
        min_line:           int = 0,
        min_closed:         int = 0,
        min_other:          int = 0,
        spacing:            int = 1,
        bias_method:        int = 0,
        bias:               float = 1.0,
        bias_loc:           int = 0,
        custom_size:        bool = False,
        propagate:          bool = False
) -> None:
    """Sizes geometric curves in FEMAP to a specified number of elements or mesh_size specified

    Pass either *num_elem* **or** *mesh_size* to set a custom size for your curve(s). Other optional params have been
    set to FEMAP defaults.

    See FEMAP API - feMeshSizeCurve2 method for more details

    Parameters
    ----------
    femap
        FEMAP application object
    curve_list
        Curve ID(s) to be sized
    num_elem
        Optional: Number of elements per curve - If this value is 0 (default), mesh_size will be used
    mesh_size
        Optional: Size of elements on the curve. Only used if num_elem=0. Default is to let FEMAP determine the sizing

    min_line
    min_closed
    min_other
    spacing
    bias_method
    bias
    bias_loc
    custom_size
    propagate : bool

    Examples
    --------
    >>> size_curves_to_mesh(femap, [10, 11, 12, 13], 3)

    >>> size_curves_to_mesh(femap, 6, mesh_size=0.025, propagate=True)
    """

    fe_curve_set = _resolve_entity_id_params(femap, curve_list, as_fset=True)

    rc = femap.feMeshSizeCurve2(
        fe_curve_set.ID, num_elem, mesh_size, min_line, min_closed, min_other, spacing, bias_method, bias, bias_loc,
        custom_size, propagate
    )

    check_return_code(rc, 'Curve Sizing Operation Error')

    femap.feViewRegenerate(0)

    return


def mesh_surface(
        femap:              Pyfemap.model,                       # Required Param
        surface_list:       int | Iterable[int],                 # Required Param
        prop_id:            int,                                 # Required Param
        elem_shape:         int = fc.FTO_QUAD4,
        allow_map:          bool = False,
        default_sizing:     bool = False,
        as_fset:            bool = False,
) -> tuple[list[int], list[int]] | tuple[FeSet, FeSet]:
    """Calls the FEMAP command Mesh->Geometry->Surface. Returns list of nodes and elements created during the process.

    Returns empty lists if the meshing process failed.

    elem_shape must point to of the following FEMAP constants:
        - 2=Tri3
        - 3=Tri6
        - 4=Quad4 - FTO_QUAD4 - **Default**
        - 5=Quad8

    Parameters
    ----------
    femap
        FEMAP application object
    surface_list
        Surface ID(s) to be meshed
    prop_id
        Property ID that will be assigned to the newly meshed surface(s)
    elem_shape
        Optional: (Default=4) Femap entity constant for quad or tri elements
    allow_map
        Optional: (Default=False) Allow mapped meshing of surfaces if True. Ignored if element_shape=0
    default_sizing
        Optional: (Default: False) Clears any predetermined sizing and calculates a new default mesh size
    as_fset
        Optional: Flag to indicate if you want the return type to be a FEMAP Set Object instead of a Python list

    Returns
    -------
    list[int], list[int] | FeSet, FeSet
        Python lists or FEMAP Set Ojects containing the IDs of the nodes and elements created

    Examples
    --------
    >>> new_nodes, new_elements = mesh_surface(femap, [10, 11, 12, 13], 100)

    >>> new_nodes, new_elements = mesh_surface(femap, 10, 100, fc.FTO_TRIA3, True, True)

    """
    # Checks if elem_shape was passed as a valid FEMAP Entity Constant
    if isinstance(elem_shape, int) and elem_shape not in [fc.FTO_QUAD4, fc.FTO_QUAD8, fc.FTO_TRIA3, fc.FTO_TRIA6]:
        raise AttributeError(
            f'The param elem_shape was passed as {elem_shape}, which is a not a valid entity constant '
            f'in FEMAP. Use one of the following: \n'
            f'{fc.FTO_QUAD4} for QUAD4, {fc.FTO_QUAD8} for QUAD8, {fc.FTO_TRIA3} for TRI3, or '
            f'{fc.FTO_TRIA6} for TRI6.'
        )

    # Checks if elem_shape was passed as a string, and tries to reassign it as a valid FEMAP Constant
    elif isinstance(elem_shape, str):
        if elem_shape.lower() == 'quad4':
            elem_shape = fc.FTO_QUAD4
        elif elem_shape.lower() == 'quad8':
            elem_shape = fc.FTO_QUAD8
        elif elem_shape.lower() == 'tri3':
            elem_shape = fc.FTO_TRIA3
        elif elem_shape.lower() == 'tri6':
            elem_shape = fc.FTO_TRIA6
        else:
            raise AttributeError(
                f'The param elem_shape was passed as {elem_shape}, which is a not a valid entity constant '
                f'in FEMAP. Use one of the following: \n'
                f'{fc.FTO_QUAD4} for QUAD4, {fc.FTO_QUAD8} for QUAD8, {fc.FTO_TRIA3} for TRI3, or '
                f'{fc.FTO_TRIA6} for TRI6.')

    # Formats surface_list to a tuple[int]
    surface_list_formatted = (int(surface_list),) if isinstance(surface_list, (int, str)) else tuple(surface_list)

    if isinstance(surface_list_formatted, (list, tuple)):
        mesh_tracking = femap.feTrackData
        mesh_tracking.StartMesh()
        fe_surface_set = list_to_fset(femap, surface_list_formatted)
        rc = femap.feMeshSurface2(fe_surface_set.ID, prop_id, elem_shape, allow_map, default_sizing)
    else:
        raise AttributeError(
            f'The param surface_list was passed as {surface_list}, which is a {type(surface_list)}. '
            f'Pass this param as an int for a single surface ID or a list[int] for multiple surface '
            f'IDs'
        )
    mesh_tracking.StopAll()

    femap.feViewRegenerate(0)

    check_return_code(rc, 'Error occurred while attempting to mesh surfaces')

    # Stores newly created nodes and elements in FEMAP Sets.
    fe_nodes_created = femap.feSet
    fe_elements_created = femap.feSet
    mesh_tracking.Created(fc.FT_NODE, fe_nodes_created.ID, False)
    mesh_tracking.Created(fc.FT_ELEM, fe_elements_created.ID, False)

    if as_fset:
        return fe_nodes_created, fe_elements_created
    else:
        nodes_created = fset_to_list(fe_nodes_created)
        elements_created = fset_to_list(fe_elements_created)
        return nodes_created, elements_created


def equivalence_nodes(
        femap:                      Pyfemap.model,                             # Required Param
        node_list:                  Iterable[int] = None,
        tolerance:                  float = 0.000001,
        as_fset:                    bool = False,
        merge:                      bool = True,
        merge_into_all:             bool = False,
        max_angle_distortion:       float = 10.0,
        merge_mode:                 int = 0,
        merge_loc:                  int = 0,
        merge_across_connect:       bool = True,
        merge_across_output_csys:   bool = True,
        merge_across_csys_id:       int = -1,
        message_mode:               int = 2,
        save_groups:                bool = False
) -> list[int] | FeSet:
    """Calls FEMAP Command: Tool-->Check-->Coincident Nodes and equivalences them.

    Don't be intimidated by all the params. Default values are set to merge all nodes with a tolerance of 0.000001.
    See FEMAP API feCheckCoincidentNode5() method for further details on the parameters.

    Parameters
    ----------
    femap
        FEMAP application object
    node_list
        Optional: List of nodes to check for equivalence. If not provided, **all** the nodes in the FEM are checked.
    tolerance
        Optional: (Default = 0.000001) Equivalence tolerance.
    as_fset
        Optional: Flag to indicate if you want the return type to be a FEMAP Set Object instead of a Python list

    ----Other Optional Params----
    merge
    merge_into_all
    max_angle_distortion
    merge_mode
    merge_loc
    merge_across_connect
    merge_across_output_csys
    merge_across_csys_id
    message_mode
    save_groups

    Returns
    -------
    list[int] | FeSet
        Python list or FEMAP Set containging the node IDs that were deleted during the equivalence process.

    Examples
    --------
    >>> deleted_nodes = equivalence_nodes(femap)

    >>> deleted_nodes = equivalence_nodes(femap, [1001, 1002, 1003, 1004], 0.0001, merge_mode=1, save_groups=True)
    """
    fe_node_equivalence_set = femap.feSet

    # If node_list is not passed, then assume all the nodes (default behavior)
    if node_list is None:
        fe_node_equivalence_set.AddAll(fc.FT_NODE)
    else:
        node_list = (int(node_list),) if isinstance(node_list, (int, str)) else tuple(node_list)
        fe_node_equivalence_set = list_to_fset(femap, node_list)

    # Track changes during the equivalence process
    mesh_tracking = femap.feTrackData

    mesh_tracking.StartMesh()

    rc = femap.feCheckCoincidentNode5(
        fe_node_equivalence_set.ID, merge_into_all, tolerance, max_angle_distortion, merge, merge_mode, merge_loc,
        merge_across_connect, merge_across_output_csys, merge_across_csys_id, message_mode, save_groups
    )
    mesh_tracking.StopAll()

    check_return_code(rc, 'Error during node equivalence')

    # Transfer the node IDs deleted from the tracking object to a FEMAP Set
    fe_nodes_deleted = femap.feSet
    mesh_tracking.Deleted(fc.FT_NODE, fe_nodes_deleted.ID, False)

    femap.feViewRegenerate(0)

    if as_fset:
        return fe_nodes_deleted
    else:
        deleted_nodes = fset_to_list(fe_nodes_deleted) if fe_nodes_deleted.IsNotEmpty() else []
        return deleted_nodes
