from __future__ import annotations

import Pyfemap
from Pyfemap import constants as fc
from Pyfemap import OutputSet as FeOutputSet
from .helpers import resolve_brand_code, check_return_code


__all__ = [
    'attach_op2', 'get_output_set', 'get_cbush_result_vector_ids', 'get_plate_result_vector_ids',
    'get_plate_other_result_vector_id', 'get_vector_id_by_name'
]


def attach_op2(
        femap: Pyfemap.model,
        results_filepath: str,
        brand: int | str = 0
) -> None:
    """Attach op2 results file to current femap session

    Parameters
    ----------
    femap
        FEMAP application object
    results_filepath
        Relative or Absolute path to the .op2 file
    brand
        Optional: FEMAP code to designate specific brand of Nastran. Defaults to 0 (MSC).
        0='MSC', 1='NE', 2='UAI', 3='CSA', 4='SSS', 5='Cosmic', 6='ME', 7='VR', 8='NX'
    """

    brand_code = resolve_brand_code(brand)
    femap.feFileAttachResults(brand_code, results_filepath, False)
    femap.feViewRegenerate(0)
    return


def get_output_set(femap: Pyfemap.model, set_number: int = None) -> FeOutputSet:
    """Retrieves output set object from the loaded results via the set_number. Defaults to first available output_set.

    Parameters
    ----------
    femap
        FEMAP application object

    set_number
        Optional: Output set ID. If nothing passed, then will grab the first available output set.

    Returns
    -------
    FeOutputSet
        FEMAP Output Set Object
    """
    fe_output_set = femap.feOutputSet
    if set_number:
        fe_output_set.Get(set_number)
    else:
        fe_output_set.First()

    return fe_output_set


def get_cbush_result_vector_ids(femap: Pyfemap.model) -> tuple[int, int, int, int, int, int]:
    """Retrieves the Vector IDS associated with CBUSH forces and moments

    Parameters
    ----------
    femap
        FEMAP application object

    Returns
    -------
    tuple[int, int, int, int, int, int]
        Six total vector IDs returned: Fx, Fy, Fz, Mx, My, Mz
    """
    fe_results_query = femap.feResultsIDQuery
    vector_id_fx = int(fe_results_query.LineOther(fc.VLO_BUSHFAST_FORCE_X))
    vector_id_fy = int(fe_results_query.LineOther(fc.VLO_BUSHFAST_FORCE_Y))
    vector_id_fz = int(fe_results_query.LineOther(fc.VLO_BUSHFAST_FORCE_Z))
    vector_id_mx = int(fe_results_query.LineOther(fc.VLO_BUSHFAST_MOMENT_X))
    vector_id_my = int(fe_results_query.LineOther(fc.VLO_BUSHFAST_MOMENT_Y))
    vector_id_mz = int(fe_results_query.LineOther(fc.VLO_BUSHFAST_MOMENT_Z))
    return vector_id_fx, vector_id_fy, vector_id_fz, vector_id_mx, vector_id_my, vector_id_mz


def get_plate_result_vector_ids(
        femap:              Pyfemap.model,
        results_type:       int,
        sub_type_results:   int,
        plate_output_loc:   int,
        plate_top:          bool = True,
        plate_bottom:       bool = True,
        plate_mid:          bool = False,
) -> int | tuple[int]:
    """Retrieves result vector IDs for plate elements. Defaults to returning vector ids for top and bottom of plates

    Parameters
    ----------
    femap
        FEMAP application object
    results_type
        FEMAP constant for zVecPlateResult
    sub_type_results
        FEMAP constant for zVecPlateType
    plate_output_loc
        FEMAP constant for zVecPlateLoc
    plate_top
        Optional: Default = True. Gets plate results at bottom. Will use FEMAP Constant VPP_BOT for zVecPlatePly
    plate_bottom
        Optional: Default = True. Gets plate results at top. Will use FEMAP Constant VPP_TOP for zVecPlatePly
    plate_mid
        Optional: Default = False. Gets plate results at mid. Will use FEMAP Constant VPP_MID for zVecPlatePly

    Returns
    -------
    int | tuple[int]
        Plate result vector IDs

    """
    fe_results_query = femap.feResultsIDQuery
    plate_vectors_to_return = []
    if plate_top:
        vector_id_top = int(fe_results_query.Plate(results_type, sub_type_results, fc.VPP_TOP, plate_output_loc))
        if vector_id_top == fc.FE_FAIL:
            check_return_code(vector_id_top)
        else:
            plate_vectors_to_return.append(vector_id_top)

    if plate_bottom:
        vector_id_bottom = int(fe_results_query.Plate(results_type, sub_type_results, fc.VPP_BOT, plate_output_loc))
        if vector_id_bottom == fc.FE_FAIL:
            check_return_code(vector_id_bottom)
        else:
            plate_vectors_to_return.append(vector_id_bottom)

    if plate_mid:
        vector_id_mid = int(fe_results_query.Plate(results_type, sub_type_results, fc.VPP_MID, plate_output_loc))
        if vector_id_mid == fc.FE_FAIL:
            check_return_code(vector_id_mid)
        else:
            plate_vectors_to_return.append(vector_id_mid)

    # Return an int if only one vector is requested, otherwise return a tuple
    return plate_vectors_to_return[0] if len(plate_vectors_to_return) == 1 else tuple(plate_vectors_to_return)


def get_plate_other_result_vector_id(
        femap:                          Pyfemap.model,
        plate_scalar_output_constant:   int
) -> int:
    """Calls the method feResultsQuery.PlateOther() to get other result vector ids that involve a scalar output

    Parameters
    ----------
    femap
        FEMAP application object
    plate_scalar_output_constant
        FEMAP constant for zVecPlateScalar

    Returns
    -------
    int
        Output vector id
    """
    fe_results_query = femap.feResultsIDQuery
    vector_id = fe_results_query.PlateOther(plate_scalar_output_constant)
    if vector_id == fc.FE_FAIL:
        check_return_code(vector_id)
    return vector_id


def get_vector_id_by_name(
        femap:          Pyfemap.model,
        output_set_id:  int,
        name:           str
) -> int:
    """Uses the feResultsQuery.Find() method to search for a specific vector id by name

    Parameters
    ----------
    femap
        FEMAP application object
    output_set_id
        ID of Output Set to find output vector ID
    name
        Title of Output Vector to find in specified output set

    Returns
    -------
    int
        Output vector id
    """
    fe_results_query = femap.feResultsIDQuery
    vector_id = fe_results_query.Find(output_set_id, name)
    if vector_id == fc.FE_FAIL:
        check_return_code(vector_id)
        print('Vector ID could not be determined using entered text. See Remarks/Usage Section in API documentation')

    return vector_id
