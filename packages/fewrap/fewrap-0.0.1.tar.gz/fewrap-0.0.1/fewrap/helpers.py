from __future__ import annotations
import Pyfemap
from Pyfemap import constants as fc
from Pyfemap import ISet as FeSet
from collections.abc import Iterable
from time import sleep


__all__ = [
    'fset_to_list', 'list_to_fset', 'check_return_code', 'flatten', 'resolve_brand_code', 'get_user_commands',
    'run_command', '_resolve_entity_id_params'
]


def fset_to_list(fe_set: FeSet) -> list[int]:
    """Converts the IDs contained in the FEMAP Set object into a Python list.

    Parameters
    ----------
    fe_set
        FEMAP Set object

    Returns
    -------
    list[int]
        Python list containing all the IDs in the FEMAP Set

    Examples
    --------
    >>> fe_set = femap.feSet
    >>> fe_set.Add(1)
    >>> fe_set.Add(2)
    >>> fset_to_list(fe_set)
    [1, 2]
    """
    if not isinstance(fe_set, FeSet):
        raise TypeError(f'{fe_set} is not a FEMAP Set object')

    tuple_of_ids: tuple[int, ...] = fe_set.GetArray()[2]

    list_of_ids = list(tuple_of_ids)

    return list_of_ids


def list_to_fset(
        femap:          Pyfemap.model,
        list_of_ids:    Iterable[int]
) -> FeSet:
    """Converts an Iterable of IDs into a new FEMAP Set

    Parameters
    ----------
    femap
        FEMAP Application object
    list_of_ids
        IDs to add to a new FEMAP Set object

    Returns
    -------
    FeSet
        FEMAP Set object

    Examples
    --------
    >>> fe_element_set = list_to_fset(femap, [1, 2, 3, 4, 5])
    """
    fe_set: FeSet = femap.feSet
    tuple_of_ids = tuple(list_of_ids)
    if len(tuple_of_ids) == 0:
        return fe_set
    else:
        fe_set.AddArray(len(tuple_of_ids), tuple_of_ids)
        return fe_set


def check_return_code(
        code:       int,
        message:    str = None
) -> bool:
    """Checks return codes from FEMAP API calls. If RC is not FE_OK, this indicates an error and prints code to console.

    Parameters
    ----------
    code
        Return Code (rc) from FEMAP API calls
    message
        Optional: Custom message you can pass whenever you call this method. Useful for debugging.

    Returns
    -------
    bool
        True if FE_OK, False otherwise

    Examples
    --------
    >>> check_return_code(fc.FE_OK)
    True
    >>> check_return_code(fc.FE_FAIL)
    FEMAP API return code indicates an error: FE_FAIL
    False
    """
    rc_dict = {
        fc.FE_OK: 'FE_OK',
        fc.FE_FAIL: 'FE_FAIL',
        fc.FE_CANCEL: 'FE_CANCEL',
        fc.FE_INVALID: 'FE_INVALID',
        fc.FE_NOT_EXIST: 'FE_NOT_EXIST',
        fc.FE_SECURITY: 'FE_SECURITY',
        fc.FE_NOT_AVAILABLE: 'FE_NOT_AVAILABLE',
        fc.FE_TOO_SMALL: 'FE_TOO_SMALL',
        fc.FE_BAD_TYPE: 'FE_BAD_TYPE',
        fc.FE_BAD_DATA: 'FE_BAD_DATA',
        fc.FE_NO_MEMORY: 'FE_NO_MEMORY',
        fc.FE_NEGATIVE_MASS_VOLUME: 'FE_NEGATIVE_MASS_VOLUME',
        fc.FE_INVALID_DEVELOPER: 'FE_INVALID_DEVELOPER',
        fc.FE_NO_VALID_GRAPHICS_WINDOW: 'FE_NO_VALID_GRAPHICS_WINDOW',
        fc.FE_NO_VALID_GRAPHIC_VIEW: 'FE_NO_VALID_GRAPHIC_VIEW',
        fc.FE_FILE_OPEN_FAILED: 'FE_FILE_OPEN_FAILED',
        fc.FE_NO_FILENAME: 'FE_NO_FILENAME',
        fc.FE_FILE_WRITE_FAILED: 'FE_FILE_WRITE_FAILED'
    }

    if code == fc.FE_OK:
        return True
    else:
        print(f'FEMAP API return code indicates an error: {rc_dict[code]}')
        if message is not None:
            print(message)
        return False


def flatten(nested_list: list) -> list:
    """Flatten a nested list

    Examples
    --------
    >>> nest_list = [1, [2, 3, [4, 5], 6], 7, [8]]
    >>> flatten(nest_list)
    [1, 2, 3, 4, 5, 6, 7, 8]

    Returns
    -------
    list
        One dimensional list
    """
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list


def resolve_brand_code(code: int | str) -> int:
    """Checks to see if brand code passed is valid. Resolves code to int if str is passed.

    Parameters
    ----------
    code
        FEMAP Constant for brand (Example: FTR_MSC_NASTRAN), or a string version ('MSC')

    Returns
    -------
    brand_code
        FEMAP constant pointing to the specific brand

    Examples
    --------
    >>> resolve_brand_code('nx')
    8
    >>> resolve_brand_code('MSC')
    0
    >>> resolve_brand_code(0)
    0
    """
    # Specific to FEMAP API
    brand_dict = {
        'MSC': 0,
        'NE': 1,
        'UAL': 2,
        'CSA': 3,
        'SSS': 4,
        'COSMIC': 5,
        'ME': 6,
        'VR': 7,
        'NX': 8
    }
    if isinstance(code, int) and code in brand_dict.values():
        brand_code = code
    elif isinstance(code, str) and code.upper() in brand_dict:
        brand_code = brand_dict[code.upper()]
    else:
        brand_code = brand_dict['MSC']  # Assume MSC if cannot parse 'brand' param.

    return brand_code


def get_user_commands(femap: Pyfemap.model) -> list[str]:
    """Gets paths for user defined commands (to include custom program files and custom APIs already in the GUI)

    Returns a list of commands

    Parameters
    ----------
    femap
        FEMAP application object

    Returns
    -------
    list[str]
        List of commands that can be passed to the run_command() function

    Examples
    --------
    >>> command_list = get_user_commands(femap)
    """
    rc, num_cmd, title, command, command_arg, starting_dir = femap.feGetUserCommands()

    return list(command)


def run_command(
        femap:      Pyfemap.model,
        commands:   str | int | Iterable[str, int]
) -> None:
    """Runs a user command code, custom program_file (.pro) or API file (.bas)

    Parameters
    ----------
    femap
        FEMAP application object

    commands
        Command code, path to a .pro/.bas file, or a list containing any combinations of these

    Returns
    -------
    None

    Examples
    --------
    >>> command_list = get_user_commands(femap)
    >>> run_command(femap, command_list[2])

    >>> run_command(femap, r"C:\\Program Files\\Siemens\\Femap 2022.2\\api\\User Tools\\RBE_CTE_CHECK.bas")

    >>> run_command(femap, r"C:\\Program Files\\Siemens\\Femap 2022.2\\api\\User Tools\\Color Props.pro")

    >>> run_command(femap, 2428)  # Numeric command to toggle nodes on and off in the view
    """
    if not isinstance(commands, (list, tuple)):
        commands = [commands]

    for cmd in commands:
        # If cmd is a code, FEMAP runs it and moves to the next command in the list
        if isinstance(cmd, int):
            femap.feRunCommand(cmd, True)
            continue

        # Runs the API (.bas) or Program (.pro) file
        extension_check = cmd.lower()
        if extension_check.endswith('.bas') or extension_check.endswith('.pro'):
            femap.feFileProgramRun(False, True, True, cmd)
            while femap.feFileProgramRunning():
                sleep(1.0)
    return


def _resolve_entity_id_params(
        femap: Pyfemap.model,
        entity_ids: int | Iterable[int] | FeSet,
        as_fset: bool = False
) -> tuple[int, ...] | FeSet:
    """Internal function to check a param that is supposed to contain Entity IDs. Can return a tuple or FeSet.

    Raises ValueError or Attribute Error exceptions if param cannot be resolved or has erroneous values.

    Parameters
    ----------
    femap
        FEMAP application object
    entity_ids
        Value coming from another function that is being checked
    as_fset
        Optional: Default=False which will return value as a tuple. Set to True if you want a FeSet

    Returns
    -------
    tuple[int] | FeSet
        Tuple of int(s) or a FEMAP Set object containing the resolved IDs
    """

    resolved_ids: tuple = ()    # For type-hinting

    # Check integer for non-zero value > Cast to tuple. Allows negative int because some FEMAP functions allow that
    if isinstance(entity_ids, int):
        if entity_ids == 0:
            raise ValueError(f'Param was passed as an integer with a value of 0')
        else:
            resolved_ids = (int(entity_ids),)

    # Try to cast a passed string to tuple[int]
    elif isinstance(entity_ids, str):
        try:
            resolved_ids = (int(entity_ids),)
        except ValueError as e:
            print(
                f'Param was passed as a str with the value of {entity_ids}. Expecting int, Iterable[int], or'
                f'FeSet', e
            )

    # Casts entity_ids as a tuple with unique values.
    # Throws exception if values are missing, or if values are not positive integers
    elif isinstance(entity_ids, Iterable):
        resolved_ids = tuple(set(entity_ids))

        if len(resolved_ids) == 0:
            raise ValueError(f'Param was passed as {type(entity_ids)} with no values)')

        elif not all(isinstance(item, int) for item in resolved_ids):
            raise TypeError(f'Param was passed as {type(entity_ids)}, but its values were not all integers')

        elif not all(num > 0 for num in resolved_ids):
            raise ValueError(f'Param was passed as {type(entity_ids)} and contains values that are negative or zero')

    # Checks FeSet to make sure it contains something, then turns it into a tuple
    elif isinstance(entity_ids, FeSet):
        if entity_ids.IsNotEmpty():
            resolved_ids = tuple(fset_to_list(entity_ids))
        else:
            raise ValueError(f'Param was passed as a FeSet, but contains no IDs')

    # Throws exception if some other type was passed.
    else:
        raise TypeError(f'Param was passed as a {type(entity_ids)}. Expecting int, Iterable[int], or FeSet')

    # Returns either a FeSet or a tuple depending on the value of as_fset param
    if as_fset:
        fe_resolved_ids = list_to_fset(femap, resolved_ids)
        return fe_resolved_ids
    else:
        return resolved_ids
