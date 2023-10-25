from __future__ import annotations
from collections.abc import Iterable
import Pyfemap
from Pyfemap import constants as fc
from Pyfemap import ILoadSet as FeLoadSet
from Pyfemap import ILoadDefinition as FeLoadDef
from Pyfemap import ILoadMesh as FeLoadMesh
from .helpers import _resolve_entity_id_params, check_return_code


__all__ = ['delete_existing_loads_and_bc', 'create_load_set', 'create_load_definition', 'create_load_on_mesh']


def delete_existing_loads_and_bc(
        femap:          Pyfemap.model,
        loads:          bool = True,
        constraints:    bool = True,
        analysis_set:   bool = True
) -> None:
    """Deletes all existing loads, boundary conditions, and analysis set from the FEMAP database

    If you don't want to delete_entity some of this info, set the corresponding parameter to False

    Parameters
    ----------
    femap
        FEMAP application object
    loads
        Optional: Default=True
    constraints
        Optional: Default=True
    analysis_set
        Optional Default=True

    Examples
    --------
    >>> delete_existing_loads_and_bc(femap)

    >>> delete_existing_loads_and_bc(femap, constraints=False)
    """

    if loads:
        # Deletes all existing load set from FEMAP database
        fe_load_set = femap.feSet
        fe_load_set.AddAll(fc.FT_LOAD_DIR)
        femap.feDelete(fc.FT_LOAD_DIR, fe_load_set.ID)

    if constraints:
        # Deletes all existing boundary conditions from FEMAP database
        fe_constraint_set = femap.feSet
        fe_constraint_set.AddAll(fc.FT_BC_DIR)
        femap.feDelete(fc.FT_BC_DIR, fe_constraint_set.ID)

    if analysis_set:
        # Deletes all existing analysis cases
        fe_analysis_set = femap.feSet
        fe_analysis_set.AddAll(fc.FT_AMGR_DIR)
        femap.feDelete(fc.FT_AMGR_DIR, fe_analysis_set.ID)

    return


def create_load_set(
        femap:      Pyfemap.model,
        title:      str = None,
        case_id:    int = None,
) -> FeLoadSet:
    """Creates a new load set and returns a feLoadSet object

    This is the first step / top level object when defining a new set of loads in the model.
    **feLoadSet** ----------> feLoadDefinition  ----------> feLoadMesh or feLoadGeom

    Parameters
    ----------
    femap
        FEMAP application object
    title
        Optional: (Default=None)
    case_id
        Optional: (Default = None - Will use the next available ID)

    Returns
    -------
    FeLoadSet
        FEMAP Load Set Object

    Examples
    --------
    >>> fe_load_set = create_load_set(femap, 'MAC Loading')
    """
    # Creates Load Set
    fe_load_set = femap.feLoadSet
    fe_load_set.Reset()

    # Assign an ID
    fe_load_set.ID = fe_load_set.NextEmptyID() if case_id is None else case_id

    # Assign the title or create a default one
    fe_load_set.title = title if title else 'Untitled Load Set: ' + str(fe_load_set.ID)

    fe_load_set.Put(fe_load_set.ID)
    fe_load_set.Active = fe_load_set.ID

    return fe_load_set


def create_load_definition(
        femap:              Pyfemap.model,
        fe_load_set_obj:    FeLoadSet,
        data_type_constant: int,
        load_type_constant: int,
        title:              str = None,
        load_def_id:        int = None,
) -> FeLoadDef:
    """Creates and returns a new feLoadDefinition object. Requires a feLoadSet object.

    This is the second step in adding a new set of loads to the model.
    feLoadSet ----------> **feLoadDefinition**  ----------> feLoadMesh or feLoadGeom

    Parameters
    ----------
    femap
        FEMAP application object
    fe_load_set_obj
        FEMAP feLoadSet object
    data_type_constant
        FEMAP constant indicating the entity type you are applying the load to. (FT_NODE, FT_ELEMENT, FT_SURFACE, etc.)
    load_type_constant
        FEMAP constant indicating load type (FLT_NFORCE, FLT_EPRESSURE, etc)
    title
        Optional - Name you want to give the load definition
    load_def_id
        Optional - Defaults to next available ID (recommended)

    Returns
    -------
    FeLoadDef
        FEMAP Load Definition object

    Examples
    --------
    >>> fe_load_set = create_load_set(femap, 'Impact Load Case')
    >>> fe_load_definition = create_load_definition(femap, fe_load_set, fc.FT_NODE, fc.FLT_NFORCE, 'Point Load')
    """
    fe_load_def = femap.feLoadDefinition
    fe_load_def.SetID = fe_load_set_obj.ID
    load_def_id = fe_load_def.NextEmptyID if load_def_id is None else load_def_id

    if title is None:
        title = 'Untitled Load Def: ' + str(fe_load_def.ID)

    fe_load_def.PutAll(
        load_def_id, data_type_constant, load_type_constant, title
    )

    return fe_load_def


def create_load_on_mesh(
        femap:              Pyfemap.model,
        fe_load_def_obj:    FeLoadDef,
        entity_ids:         int | Iterable[int],
        csys_id:            int,
        load_values:        int | Iterable[float],
        function_id:        int | Iterable[int] = None,
        mesh_load_id:       int = None
) -> FeLoadMesh:
    """Assigns load values to nodes or elements via the feLoadMesh object.

    This is the final step in adding a new set of loads to the model.
    feLoadSet ----------> feLoadDefinition  ----------> **feLoadMesh** or feLoadGeom

    Parameters
    ----------
    femap
        FEMAP application object
    fe_load_def_obj
        FEMAP feLoadDefinition Object
    entity_ids
        Node or Element ID(s) that you want to apply the loads to
    csys_id
        ID of the CSYS which the loads will be applied in
    load_values
        Magnitude can be passed as a single value. Otherwise, a load vector must be passed in a list such as [x, y, z]
    function_id
        Optional: (Defaults to None -> 0 - meaning constant values). ID of the function used for each load value
    mesh_load_id
        Defaults to next available ID (recommended)

    Returns
    -------
    FeLoadMesh
        FEMAP feLoadMesh object.
    """
    # Type cast and store the IDs of the nodes/elements in a FEMAP Set
    fe_loaded_entities = _resolve_entity_id_params(femap, entity_ids, as_fset=True)

    # Type cast and set the load values to a list 5 elements long per the FEMAP API.
    # If value is a magnitude, it will be the first entry in the list and four 0's will be added to the end.
    load_values = [load_values] if isinstance(load_values, int) else list(load_values)
    while len(load_values) < 5:
        load_values.append(0)

    # Creates a 3 element vector flagging the DOFs to be used to define load. Think of it as checking the x, y, or z
    # boxes when defining a load in the GUI. Magnitude will only have the first element set to True
    dof_vector = [bool(value) for value in load_values[0:3]]

    # If no function is referenced setting it to 0 tells FEMAP to use constant values
    if function_id is None:
        function_id = 0
    # Otherwise, the length of the function_id list needs to match the load_values list (5 elements total).
    else:
        function_id = [function_id] if isinstance(function_id, int) else list(function_id)
        while len(function_id) < 5:
            function_id.append(0)

    fe_load_mesh = femap.feLoadMesh
    fe_load_mesh.ID = fe_load_mesh.NextEmptyID() if mesh_load_id is None else mesh_load_id
    fe_load_mesh.SetID = fe_load_def_obj.SetID          # These SetIDs correspond to the feLoadSet ID
    fe_load_mesh.LoadDefinitionID = fe_load_def_obj.ID
    rc = fe_load_mesh.Add(
            fe_loaded_entities.ID, fe_load_def_obj.LoadType, csys_id, dof_vector, load_values, function_id
    )

    check_return_code(rc)

    fe_load_mesh.Put(fe_load_mesh.ID)

    return fe_load_mesh
