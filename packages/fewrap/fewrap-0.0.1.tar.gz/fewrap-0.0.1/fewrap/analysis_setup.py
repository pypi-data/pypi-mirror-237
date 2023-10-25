from __future__ import annotations

import Pyfemap
from Pyfemap import constants as fc
from .helpers import check_return_code, resolve_brand_code

__all__ = ['write_analysis_deck']


def write_analysis_deck(
        femap:      Pyfemap.model,
        filename:   str = 'python_model_out.bdf',
        brand:      int | str = 'MSC',
        sol_type:   int = fc.FAT_STATIC
) -> None:
    """Writes the analysis deck for the current active analysis set. See FEMAP API for sol_type constants

    Parameters
    ----------
    femap
        FEMAP application object
    filename
        Optional (default: python_model_out.bdf)
    brand
        FEMAP constant indicating the solver brand (MSC, NX, etc.). Can pass as an int or a string
        0='MSC', 1='NE', 2='UAI', 3='CSA', 4='SSS', 5='Cosmic', 6='ME', 7='VR', 8='NX'
    sol_type
        FEMAP constant indicating the analysis type (Linear Static, Modes, Non-linear Implicit, etc.)
        Use FEMAP Constants: Example: Pyfemap.constants.FAT_STATIC

    Examples
    --------
    >>> write_analysis_deck(femap, 'model.bdf', sol_type=fc.FAT_RANDOM) # Generates MSC input deck for Random Freq Resp

    >>> write_analysis_deck(femap, 'model.bdf')  # Generates a MSC input deck for Liner Static (default values)

    >>> write_analysis_deck(femap, 'model.bdf', 'NX', fc.FAT_MODES )  # Generates NX input deck for Modes

    """
    code = resolve_brand_code(brand)
    femap.Pref_AnalysisProg = code
    femap.Pref_AnalysisType = sol_type

    rc = femap.feFileWriteNastran(code, filename)
    check_return_code(rc, 'Error writing analysis deck')

    return





