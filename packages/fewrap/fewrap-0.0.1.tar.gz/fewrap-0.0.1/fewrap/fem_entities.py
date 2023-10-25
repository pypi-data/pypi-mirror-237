from __future__ import annotations
import Pyfemap
from Pyfemap import constants as fc
from Pyfemap import ISet as FeSet
import math
from collections.abc import Iterable
from .helpers import list_to_fset, fset_to_list, flatten, _resolve_entity_id_params, check_return_code

from typing import cast

__all__ = [
    'get_all', 'get_nodes_from_elements', 'get_elements_from_nodes', 'get_elements_from_property',
    'get_nodes_in_search_radius', 'get_nodes_and_elements_connected_to_rigids', 'get_normal_vector_at_node',
    'delete_entity', 'get_node_coords', 'get_elements_on_surfaces', 'rotate_by', 'check_element_normals'
]


def get_all(
        femap:              Pyfemap.model,
        entity_constant:    int,
        as_fset:            bool = False
) -> list[int] | FeSet:
    """Gets all the IDS of an entity in the current FEMAP model. Works for both fem and geometry.

    Parameters
    ----------
    femap
        FEMAP application object.
    entity_constant
        FEMAP API constant denoting the type of entity to get.
    as_fset
        (Optional) Flag to indicate if you want the return type to be a FEMAP Set Object instead of a Python list

    Returns
    -------
    list[int] | FeSet
        Python list or FEMAP Set object (feSet) containing all the IDs of the entity requested.

    Examples
    --------
    >>> list_of_properties = get_all(femap, fc.FT_PROP)

    >>> fe_point_set = get_all(femap, fc.FT_POINT)
    """
    fe_set = femap.feSet
    fe_set.AddAll(entity_constant)

    if as_fset:
        return fe_set
    else:
        entity_ids = fset_to_list(fe_set)
        return entity_ids


def get_nodes_from_elements(
        femap:      Pyfemap.model,
        elements:   int | Iterable[int] | FeSet,
        as_fset:    bool = False
) -> list[int] | FeSet:
    """Returns a list of nodes that belong to the element(s) specified

    - Can pass a single element or multiple elements.
    - The list returned contains only unique nodes (nodes are not double counted if they belong to multiple elements)

    Parameters
    ----------
    femap
        FEMAP application object
    elements
        ID(s) of the element or elements to retrieve nodes from
    as_fset
        Optional: Flag to indicate if you want the return type to be a FEMAP Set Object instead of a Python list

    Returns
    -------
    list[int] | FeSet
        List or FEMAP Set (feSet) of unique nodes belonging to the element(s) passed

    Examples
    --------
    >>> node_ids = get_nodes_from_elements(femap, [41968921, 41968922, 41968923])
    """

    fe_element_set: FeSet = _resolve_entity_id_params(femap, elements, as_fset=True)
    fe_node_set: FeSet = femap.feSet

    fe_node_set.AddSetRule(fe_element_set.ID, fc.FGD_NODE_ONELEM)

    if as_fset:
        return fe_node_set
    else:
        nodes: list[int] = fset_to_list(fe_node_set)
        return nodes


def get_elements_from_nodes(
        femap:      Pyfemap.model,
        nodes:      int | Iterable[int] | FeSet,
        as_fset:    bool = False
) -> list[int] | FeSet:
    """Returns a list of elements that are associated with the node(s) specified

    Parameters
    ----------
    femap
        FEMAP application object
    nodes
        Node or nodes to search.
    as_fset
        Optional: Flag to indicate if you want the return type to be a FEMAP Set Object instead of a Python list

    Returns
    -------
    list[int] | FeSet
        List or FEMAP Set object of elements IDs that contain the specified nodes.

    Examples
    --------
    >>> node_list = [410, 411, 412]
    >>> element_ids = get_elements_from_nodes(femap, node_list)
    """

    fe_element_set: FeSet = femap.feSet
    fe_node_set: FeSet = _resolve_entity_id_params(femap, nodes, as_fset=True)

    fe_element_set.AddSetRule(fe_node_set.ID, fc.FGD_ELEM_BYNODE)

    if as_fset:
        return fe_element_set
    else:
        found_elements: list[int] = fset_to_list(fe_element_set)
        return found_elements


def get_elements_from_property(
        femap:      Pyfemap.model,
        prop_id:    int,
        as_fset:    bool = False
) -> list[int] | FeSet:
    """Returns a list of all elements that are assigned to a specified property id.

    Parameters
    ----------
    femap
        FEMAP application object
    prop_id
        Nastran property id
    as_fset
        (Optional) Flag to indicate if you want the return type to be a FEMAP Set Object instead of a Python list
    Returns
    -------
    list[int] | FeSet
        List or FEMAP Set object of element IDs that belong to the specified property ID

    Examples
    --------
    >>> bulkhead_elements = get_elements_from_property(femap, 1001)

    """
    fe_prop = femap.feProp
    if not fe_prop.Exist(prop_id):
        raise AttributeError(f'Property ID: {prop_id} does not exist in this model')

    fe_set: FeSet = femap.feSet
    fe_set.AddRule(int(prop_id), fc.FGD_ELEM_BYPROP)

    if fe_set.IsEmpty():
        print(f'No Elements are associated with Property ID: {prop_id}')
        elements = []
    else:
        elements: list[int] = fset_to_list(fe_set)

    if as_fset:
        return fe_set
    else:
        return elements


def get_nodes_in_search_radius(
        femap:              Pyfemap.model,
        search_radius:      int | float,
        location:           int | Iterable[float, float, float],
        nodes_to_search:    Iterable[int] | FeSet = None,
        as_fset:            bool = False
) -> list[int] | FeSet:
    """Searches and returns a list of node IDs that are located within a specified search radius and location

    'location' can be passed in a couple ways:
        - If you want to set a Node ID as the search radius origin, pass the node ID as an int
        - Global Coordinates (as a tuple or list)

    'nodes_to_search' is optional. This narrows the search pool of nodes that meet the search criteria.
        - For instance: If you only want the nodes on a plate, then this should contain the list of nodes on the plate
        - If 'nodes_to_search' is not specified then all the nodes in the model will be searched

    Returns list of Node IDs found. If no nodes are found, then an empty list is returned.

    Parameters
    ----------
    femap
        FEMAP application object
    search_radius
        Distance from the location provided (loc) to search
    location
        Origin to search from. Can be passed as global coordinates (x,y,z), or a node ID
    nodes_to_search : int | Iterable[int|float] | None
        Optional: A subset of nodes (i.e. a search pool) to filter the search results.
    as_fset
        Optional: Flag to indicate if you want the return type to be a FEMAP Set Object instead of a Python list

    Returns
    -------
    list[int] | FeSet
        List or FEMAP Set (feSet) object of Node IDs that meet the search criteria.

    Examples
    --------
    >>> node_search_pool = [400, 401]
    >>> location_coords = (0, 0, 0)
    >>> search_distance = 0.5
    >>> node_ids = get_nodes_in_search_radius(femap, search_distance, location_coords, node_search_pool)

    >>> search_distance = 0.5
    >>> location_node_id = 1001
    >>> fe_node_ids = get_nodes_in_search_radius(femap, search_distance, location_coords, as_fset=True)
    """

    # Logic to check valid params ----------------------------------------------------------------------------------
    if location is None:  # Need to provide location param to proceed.
        raise AttributeError('Provide loc as either a node ID, or a list of global coordinates [x, y, z]')

    # Type-checking location to ensure proper coordinate definition
    if isinstance(location, (tuple, list, set)):
        location = tuple(location)
        if len(location) != 3:
            raise AttributeError('Provide loc as either a node ID, or a 3 element list of global coords[x, y, z]')
        else:
            location = tuple(float(loc) for loc in location)  # Convert to a tuple[float, float, float]

    # Assume int or str passed is meant to represent a node ID instead of a location
    elif isinstance(location, (int, str)):
        node = int(location)
        fe_node = femap.feNode
        if not fe_node.Exist(node):
            raise AttributeError(f'location param passed as Node: {location} and it does not exist')
        fe_node.Get(node)
        location = (fe_node.x, fe_node.y, fe_node.z)  # Get the global coords for the node

    # Type-checking nodes_to_search if this param is passed
    if nodes_to_search:
        nodes_to_search = _resolve_entity_id_params(femap, nodes_to_search)
    # Otherwise, assume user wants to search all the nodes in the model, rather than a subset
    else:
        fe_set = femap.feSet
        fe_set.AddAll(fc.FT_NODE)
        if fe_set.IsEmpty() == fc.FE_OK:
            raise AttributeError('FEMAP model has no nodes. Is it really even a model then?')
        else:
            nodes_to_search = fe_set.GetArray()[2]  # Stores all the nodes in the model as a tuple

    fe_search_set: FeSet = femap.feSet
    fe_filtered_set: FeSet = femap.feSet

    fe_node_set = list_to_fset(femap, nodes_to_search)

    # 1 = nMode = Select Below Minimum (Closer Than)
    # 0 = dMax = Throw away value, not used since we are using 'Below Minimum' for nMode
    # See FEMAP API explanation of this function for more info.
    fe_search_set.AddAroundPoint2(fc.FT_NODE, location, 1, float(search_radius), 0)

    fe_filtered_set.AddCommon(fe_search_set.ID, fe_node_set.ID)

    if as_fset:
        return fe_filtered_set
    else:
        found_nodes = fset_to_list(fe_filtered_set)
        return found_nodes


def get_nodes_and_elements_connected_to_rigids(
        femap:          Pyfemap.model,
        node_list:      Iterable[int] | FeSet = None,
        as_fset:        bool = False,
) -> tuple[list[int], list[int]] | tuple[FeSet, FeSet]:
    """Searches the model and returns a list of nodes and elements that are connected to rigid elements.

    This can be useful in certain applications, such as:
        -   Filtering stress results if you want to omit artificial stresses typically associated with rigids.
        -   Refining your mesh without touching rigid elements - as you would need to add logic to redefine
            the rigid connections if the refinement process alters the nodes associated with each rigid element.

    Passing a node list as an optional argument filters which nodes/elements are returned. For instance, if you only
    want to know all the nodes and elements connected to rigids in a specific subcomponent of your model, then pass
    the subcomponent node ids in a list.

    Parameters
    ----------
    femap
        FEMAP application object
    node_list
        Optional: List of nodes to search for any rigid connections. If nothing is passed, then the function will
        search the entire model for rigid connections
    as_fset
        Optional: Flag to indicate if you want the return type to be a FEMAP Set Object instead of a Python list

    Returns
    -------
    tuple[list[int], list[int]] | tuple[FeSet, FeSet]
        List of unique Node IDs and Element IDs that belong to rigid elements (or have a node associated with a rigid)

    Examples
    --------
    >>> node_id_list = [500, 501]
    >>> rigid_node_ids, rigid_element_ids = get_nodes_and_elements_connected_to_rigids(femap, node_id_list)

    >>> rigid_node_ids, rigid_element_ids = get_nodes_and_elements_connected_to_rigids(femap)
    """

    # Assume that all the nodes in the model should be searched for rigid association if nothing is passed
    if node_list is None:
        fe_nodes_to_check: FeSet = femap.feSet
        fe_nodes_to_check.AddAll(fc.FT_NODE)
    else:
        fe_nodes_to_check: FeSet = _resolve_entity_id_params(femap, node_list, as_fset=True)

    # FEMAP API logic --------------------------------------------------------------------------------------------------
    fe_rigid_set: FeSet = femap.feSet

    # Get a list of all the rigids in the model
    fe_rigid_set.AddRule(fc.FET_L_RIGID, fc.FGD_ELEM_BYTYPE)
    rigid_list: list[int] = fset_to_list(fe_rigid_set)

    if not rigid_list:  # If no rigids exist in the model, raise error
        raise AttributeError(f'No rigids exist in the model')

    # Add elements that reference 'nodes_to_check' to a femap set
    elements_to_check = get_elements_from_nodes(femap, fe_nodes_to_check)
    fe_elements_to_check: FeSet = list_to_fset(femap, elements_to_check)

    # Get all nodes connected to rigids in the model
    fe_all_rigid_nodes: FeSet = get_nodes_from_elements(femap, rigid_list, as_fset=True)

    # Get all elements that reference nodes connected to rigids and add them to a set
    all_elements_with_rigids = get_elements_from_nodes(femap, fset_to_list(fe_all_rigid_nodes))
    fe_all_elements_with_rigids: FeSet = list_to_fset(femap, all_elements_with_rigids)

    # Filter the node results by checking to see if they also belong to the optional 'node_list' param
    fe_nodes_with_rigids: FeSet = femap.feSet
    fe_nodes_with_rigids.AddCommon(fe_all_rigid_nodes.ID, fe_nodes_to_check.ID)

    # Filter the element results
    fe_elements_with_rigids: FeSet = femap.feSet
    fe_elements_with_rigids.AddCommon(fe_elements_to_check.ID, fe_all_elements_with_rigids.ID)
    
    if as_fset:
        return fe_nodes_with_rigids, fe_elements_with_rigids
    else:
        elements_with_rigids = [] if fe_elements_with_rigids.IsEmpty() else fset_to_list(fe_elements_with_rigids)
        nodes_with_rigids = [] if fe_nodes_with_rigids.IsEmpty() else fset_to_list(fe_nodes_with_rigids)
        return nodes_with_rigids, elements_with_rigids


def get_normal_vector_at_node(
        femap:          Pyfemap.model,
        target_node_id: int
) -> tuple[float, float, float]:
    """Gets an approximate normal vector at a specified node through summation of the neighboring element normal vectors

    Parameters
    ----------
    femap
        FEMAP application object
    target_node_id
        Node ID at which the normal vector is desired.

    Returns
    -------
    tuple[float, float, float]
        Vector returned in the format of (x, y, z)

    Examples
    --------
    >>> node_id = 1001
    >>> norm_vec_at_node = get_normal_vector_at_node(femap, node_id)
    """

    # Logic to check valid params ----------------------------------------------------------------------------------
    fe_elem = femap.feElem
    fe_node = femap.feNode

    if fe_node.Exist(target_node_id):
        fe_node.Get(target_node_id)
    else:
        raise AttributeError(f'Node: {target_node_id} does not exist')

    if fe_node.NumberOfElements == 0:
        raise ValueError(
            f'Target Node {target_node_id} is not associated with any elements which are needed to '
            f'infer a normal vector.'
        )

    # Finds elements that reference this node
    elements_with_target_node = get_elements_from_nodes(femap, target_node_id)

    # Iterates through the list of elements that reference the target node and gets the normal vector at each face
    normal_vectors = []
    for elem in elements_with_target_node:
        fe_elem.Get(elem)
        rc, vec = fe_elem.GetFaceNormal(1)
        if len(vec) == 3:
            vector: list[float] = [vec[0], vec[1], vec[2]]
            normal_vectors.append(vector)
        else:
            raise AttributeError('could not find normal vector')

    # Sum the element face normal vectors element-wise
    sum_vectors: list[float] = [sum(x) for x in zip(*normal_vectors)]

    # Calculate the magnitude of the vector sum
    magnitude: float = math.sqrt(sum(component ** 2 for component in sum_vectors))

    # Normalize the vector - cast the type as a 3 element tuple
    normalized_vector = cast(tuple[float, float, float], tuple(component / magnitude for component in sum_vectors))
    return normalized_vector


def delete_entity(
        femap:          Pyfemap.model,
        entity_type:    int,
        entity_ids:     int | Iterable[int] | FeSet
) -> None:
    """Deletes a single entity or a list of entities by passing their IDs and the femap constant for entity type.

    Femap API contains a list of entity types.

    You can therefore call the constant for a Node by using the syntax:
        fc.FT_NODE

    Parameters
    ----------
    femap
        FEMAP application object
    entity_type
        FEMAP constants can be called using the syntax: fc.FT_NODE, fc.FT_ELEM, fc.FT_CURVE, etc.
    entity_ids
        ID of entity or entities to be deleted. Can be a Femap Set object as well

    Examples
    --------
    >>> delete_entity(femap, fc.FT_NODE, [41800000, 41800001])

    >>> delete_entity(femap, fc.FT_SURFACE, 10)
    """

    if not isinstance(entity_type, int):
        raise AttributeError(f'entity_type: {entity_type} is not a valid FEMAP constant.'
                             f'Try: \'import Pyfemap.constants as fc\' and call the correct constant for'
                             f'the entity. (example: fc.FT_NODE would pass the correct constant for Nodes.)')

    fe_set = _resolve_entity_id_params(femap, entity_ids, as_fset=True)

    femap.feDelete(entity_type, fe_set.ID)
    femap.feViewRegenerate(0)

    return


def get_elements_on_surfaces(
        femap:          Pyfemap.model,
        surface_ids:    int | Iterable[int],
        as_fset:        bool
) -> list[int] | FeSet:
    """Searches and returns a list of elements that are associated with specified surface(s).

    Parameters
    ----------
    femap
        FEMAP application object
    surface_ids
        Surface IDs to query for elements
    as_fset
        (Optional) Flag to indicate if you want the return type to be a FEMAP Set Object instead of a Python list

    Returns
    -------
    list[int] | FeSet
        Elements on the surface(s)

    Examples
    ---------
    >>> elements = get_elements_on_surfaces(femap, [1, 2])

    >>> fe_element_set = get_elements_on_surfaces(femap, [1, 2], as_fset=True)
    """
    surface_ids = (int(surface_ids),) if isinstance(surface_ids, (int, str)) else tuple(surface_ids)

    fe_surface = femap.feSurface
    element_list = []

    for surface in surface_ids:
        fe_surface.Get(surface)
        rc, num_elements, elem_ids = fe_surface.Elements()
        element_list.append(elem_ids)

    # Flattens the list, converts to a set to remove duplicates, and converts back to list.
    element_list = list(set(flatten(element_list)))

    if as_fset:
        return list_to_fset(femap, element_list)

    else:
        return element_list


def rotate_by(
        femap:          Pyfemap.model,
        entity_type:    int,
        entity_ids:     int | Iterable[int],
        axis_location:  Iterable[float],
        axis_vector:    Iterable[float],
        angle:          float,
        thrust:         float = None
) -> None:
    """Rotates an entity or entities by an angle around an axis of rotation

    Parameters
    ----------
    femap
        FEMAP application object
    entity_type
        FEMAP Entity Constant
    entity_ids
        ID(s) of the entities to be rotated
    axis_location
        Coordinates of the origin of the axis of rotation in global coords (x,y,z)
    axis_vector
        Components of the axis of rotation, in global coords [x,y,z]
    angle
        About the rotation axis in degrees
    thrust
        Optional: (Default=0) Total thrust distance along the axis of rotation. Not typically used.

    Examples
    --------
    >>> rotate_by(femap, fc.FT_CSYS, 1, axis_location=(0, 0, 0), axis_vector=[0, 1, 0], angle=20)
    """
    axis_location = [float(value) for value in axis_location]
    axis_vector = [float(value) for value in axis_vector]
    thrust = 0.0 if thrust is None else float(thrust)

    fe_entity_set = _resolve_entity_id_params(femap, entity_ids, as_fset=True)

    rc = femap.feRotateBy(entity_type, fe_entity_set.ID, axis_location, axis_vector, float(angle), thrust)
    check_return_code(rc, 'Error during feRotateBy operation')

    femap.feViewRegenerate(0)
    return


def filter_deleted_nodes(
        femap:              Pyfemap.model,
        node_ids_to_check:  Iterable[int] | FeSet,
        as_fset:            bool = False
) -> list[int] | FeSet:
    """Takes a list or FeSet of node ids and returns a list or FeSet with the IDs of the nodes that exist.

    Parameters
    ----------
    femap
        FEMAP application object
    node_ids_to_check
        IDs of the nodes you want to see if they exist
    as_fset
        Optional: Flag to indicate if you want the return type to be a FEMAP Set Object instead of a Python list

    Returns
    -------
    list[int] | FeSet
        Node IDs that currently exist in the model

    Examples
    --------
    >>> fe_filtered_node_set = filter_deleted_nodes(femap, [1, 2, 3, 4, 5], as_fset=True)

    >>> fe_node_set = femap.feSet
    >>> fe_node_set.Add(1)
    >>> fe_node_set.Add(2)
    >>> filtered_node_list = filter_deleted_nodes(fe_node_set)
    """
    node_ids = _resolve_entity_id_params(femap, node_ids_to_check)

    fe_node = femap.feNode
    node_ids_that_exist = [node for node in node_ids if fe_node.Exist(node)]

    if as_fset:
        fe_nodes_that_exist: FeSet = list_to_fset(femap, node_ids_that_exist)
        return fe_nodes_that_exist
    else:
        return node_ids_that_exist


def check_element_normals(
        femap:          Pyfemap.model,
        element_ids:    int | Iterable[int] | FeSet,
        normal_vector:  Iterable[int],
        csys_id:        int = 0,
        fix:            bool = True
) -> None:
    """Checks element normals against the direction of a provided normal vec. Defaults to reversing elements that fail.

    Parameters
    ----------
    femap
        FEMAP application object
    element_ids
        IDs of the elements to check
    normal_vector
        Representing the "correct" direction you want your normals to be.
    csys_id
        Optional: Default: 0 (Global Coordinates). ID of the CSYS that the normal vector is defined in.
    fix
        Optional: Default=True - Reverses elements that fail the check. Setting this to False will just print the bad
        elements to the FEMAP message window

    Examples
    --------
    >>> check_element_normals(femap, [1, 2, 3, 4, 5], normal_vector=[0, 1, 0])
    """
    do_list = True   # Prints the elements that fail the normal check the FEMAP message window.

    # This tells FEMAP to use the normal_vector as its criteria instead inferring from the first element in the list.
    # The inferred method that is used when this is set to True seems buggy, so I don't recommend using it.
    auto_normal = False

    fe_element_set = _resolve_entity_id_params(femap, element_ids, as_fset=True)
    rc = femap.feCheckElemNormal(fe_element_set.ID, csys_id, do_list, fix, auto_normal, normal_vector)
    check_return_code(rc)

    femap.feViewRegenerate(0)
    femap.set_undo_checkpoint()

    return


def get_node_coords(
        femap:      Pyfemap.model,
        node_id:    int
) -> tuple[float, float, float]:
    """Returns global coordinates (x, y, z) of a Node.

    Parameters
    ----------
    femap
        FEMAP application object
    node_id

    Returns
    -------
    tuple[float, float, float]
        (x, y, z)

    Examples
    --------
    >>> rigid_node_coords = get_node_coords(femap, 52)
    """
    fe_node = femap.feNode
    if fe_node.Exist(node_id):
        fe_node.Get(node_id)
        coords = fe_node.xyz
        return coords
    else:
        raise ValueError(f'Node {node_id} does not exist')
