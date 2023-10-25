from __future__ import annotations

import Pyfemap
from Pyfemap import constants as fc
from Pyfemap import ISet as FeSet
from collections.abc import Iterable
from .helpers import fset_to_list, _resolve_entity_id_params, check_return_code

__all__ = ['create_groups_from_properties', 'create_cbush_group']


def create_groups_from_properties(
        femap:          Pyfemap.model,
        property_id:    int | Iterable[int] | FeSet = None,
        as_fset:        bool = False
) -> int | Iterable[int] | FeSet:
    """Creates one or more FEMAP groups by subdividing a mesh based on property_ids. One group created per ID.

    Parameters
    ----------
    femap
        FEMAP application object
    property_id
        ID or list of IDs that you want to create groups of (1 group per ID)
    as_fset
        Optional: Flag to indicate if you want the return type to be a FEMAP Set Object instead of a Python list

    Returns
    -------
    int | Iterable[int] | FeSet
        ID(s) of the new groups created

    """
    fe_prop_set = femap.feSet

    if property_id is None:
        fe_prop_set.AddAll(fc.FT_PROP)
    else:
        fe_prop_set = _resolve_entity_id_params(femap, property_id)

    fe_groups_created: FeSet = femap.feSet
    fe_group_tracking = femap.feTrackData
    fe_group_tracking.Start(fc.FT_GROUP)

    rc = femap.feGroupGenProp(fe_prop_set.ID)
    check_return_code(rc)
    fe_group_tracking.Created(fc.FT_GROUP, fe_groups_created.ID, False)

    femap.feViewRegenerate(0)

    if as_fset:
        return fe_groups_created

    else:
        group_ids = fset_to_list(fe_groups_created)
        if len(group_ids) == 1:
            group_id: int = group_ids[0]
            return group_id
        else:
            return group_ids


def create_cbush_group(
        femap:      Pyfemap.model,
        as_fset:    bool = False
) -> int | FeSet:
    """Creates a group that contains all the CBUSH elements in the model. Useful for output requests.

    Parameters
    ----------
    femap
        FEMAP application object
    as_fset
        Optional: Flag to indicate if you want the return type to be a FEMAP Set Object instead of a int

    Returns
    -------
    int
        ID of the newly created CBUSH group
    """
    fe_group_set = femap.feSet
    fe_group_set.AddRule(fc.FET_L_SPRING, fc.FGD_ELEM_BYTYPE)

    fe_group_created_set: FeSet = femap.feSet
    fe_group_tracking = femap.feTrackData
    fe_group_tracking.Start(fc.FT_GROUP)

    rc = femap.feGroupGenElemType(fe_group_set.ID)
    check_return_code(rc)

    femap.feViewRegenerate(0)
    fe_group_tracking.Created(fc.FT_GROUP, fe_group_created_set.ID, False)
    fe_group_created_set.Reset()
    group_id: int = fe_group_created_set.NextID()

    if as_fset:
        return fe_group_created_set
    else:
        return group_id
