from __future__ import annotations
import os
import sys
import pythoncom
import pywintypes
import Pyfemap
import win32com.client as win32
from .helpers import resolve_brand_code
win32.gencache.is_readonly = False

__all__ = ['connect_to_femap', 'open_model', 'import_fem', 'kill_femap']


def connect_to_femap(
        file_path:      str = None,
        visible:        bool = True
) -> Pyfemap.model:
    """Establishes the connection between Python and FEMAP and opens a blank model, or a modfem database if provided

    Parameters
    ----------
    file_path
        Optional: Relative or absolute path to an existing database (.modfem) you want to open. Will open a blank model
        by default.
    visible
        Optional: Flag to indicate if you want FEMAP visible on your desktop or hidden as a background process.

    Returns
    -------
    Pyfemap.model
        FEMAP application object

    Examples
    --------
    >>> femap = connect_to_femap()

    >>> femap = connect_to_femap('database.modfem', visible=False)
    """

    try:

        pycom_obj = pythoncom.connect(Pyfemap.model.CLSID)  # Tries to connect to FEMAP if already open
        existing_session = True
    except pywintypes.com_error:  # If FEMAP isn't already open, we catch the error and open a new session of FEMAP
        try:
            pycom_obj = pythoncom.new(Pyfemap.model.CLSID)
            existing_session = False
        except pywintypes.com_error as e:
            print('Error occurred opening FEMAP', e)
            sys.exit()
        pass

    femap = Pyfemap.model(pycom_obj)  # Gets the femap application object

    # Opens a .modfem if file_path was passed. Otherwise, we start with a blank file.
    if existing_session:
        femap.feFileNew() if file_path is None else open_model(femap, file_path)
    if not existing_session and file_path is not None:
        femap.feFileClose(False)
        open_model(femap, file_path)

    femap.feAppShowWindow(visible)
    femap.feAppVisible(visible)

    if not visible:
        print(f'FEMAP is now running as a background process.')
        print(f'Use the API call: feAppVisible(True) if you want to display the GUI on your screen')

    femap.feAppUndoCheckpoint('Undo Python Script')

    femap.feAppMessage(1, f"Python-FEMAP API Connection Successful")
    print(f'Python-FEMAP API Connection Successful')
    print(f'Running FEMAP Version {femap.feAppVersion()}')
    return femap


def open_model(
        femap:      Pyfemap.model,
        file_path:  str = None
) -> None:
    """Opens an existing modfem database in the current femap session, or prompts user to select one via dialog box

    Parameters
    ----------
    femap
        FEMAP application object.
    file_path
        Relative or absolute path of the modfem database

    Examples
    --------
    >>> open_model(femap, 'database.modfem')
    """
    use_dlg = True  # Default to using a dialog box before checking if the file_path supplied exists

    if file_path is not None:
        # Checks if database_path is a relative path, and if so, converts it to absolute
        if not os.path.isabs(file_path):
            file_path = os.path.abspath(file_path)

        # Checks if path actually exists and if so, disable the dialog box prompt
        if os.path.exists(file_path):
            print(f'Opening..{file_path}')
            use_dlg = False
        else:
            print(f'File_path: {file_path} does not exist')
            print('Select database from dialog box or try again with the correct file.')

    femap.feFileOpen(use_dlg, file_path)


def import_fem(
        femap:      Pyfemap.model,
        file_path:  str,
        brand:      int | str = 'MSC'
) -> None:
    """Imports a .bdf or a .dat file to import into an active FEMAP session.

    brand:  0='MSC', 1='NE', 2='UAI', 3='CSA', 4='SSS', 5='Cosmic', 6='ME', 7='VR', 8='NX'.

    Parameters
    ----------
    femap
        FEMAP application object.
    file_path
        Relative or absolute filepath to the nastran input deck (.bdf or .dat)
    brand
        FEMAP constant specifying the format of the input file. Defaults to MSC if left blank.
        0='MSC', 1='NE', 2='UAI', 3='CSA', 4='SSS', 5='Cosmic', 6='ME', 7='VR', 8='NX'

    Examples
    --------
    >>> import_fem(femap, 'model.dat', 'NX')
    """

    code = resolve_brand_code(brand)

    femap.feFileReadNastran(code, file_path)
    femap.feAppMessage(1, "BDF import from Python successful")
    femap.feViewRegenerate(0)

    return


def kill_femap() -> None:
    """Closes all FEMAP instances running on your computer

    Examples
    --------
    >>> kill_femap()
    """
    os.system(f'taskkill /f /im femap.exe ')
