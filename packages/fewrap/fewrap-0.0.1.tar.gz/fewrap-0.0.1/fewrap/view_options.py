from __future__ import annotations

import Pyfemap
import os
from Pyfemap import constants as fc
from collections.abc import Iterable
from .helpers import list_to_fset, check_return_code
import numpy as np
import math

__all__ = [
    'highlight', 'take_screenshot', 'rotate_view_to_point', 'black_edges', 'show_color_by_property',
    'background_color_swap', 'free_edge_flip', 'show_only', 'show_hide_all'
]


def highlight(
        femap:          Pyfemap.model,
        entity_type:    int,
        entity_ids:     int | Iterable[int],
        autoscale:      bool = False
) -> None:
    """Highlights entities in the user's FEMAP Window.  Equivalent to 'Window-->Show Entities'

    Parameters
    ----------
    femap
        FEMAP application object
    entity_type
        FEMAP constants can be called using the syntax: fc.FT_NODE, fc.FT_ELEM, fc.FT_CURVE, etc.
    entity_ids
        IDs of the corresponding entites you want to highlight
    autoscale
        Optional: Default=False. Set to True if you want to autoscale the current view as well.

    Examples
    --------
    >>> highlight(femap, fc.FT_NODE, [41800000, 41800001])

    """

    entity_ids = (int(entity_ids),) if isinstance(entity_ids, (int, str)) else tuple(entity_ids)

    # Ensures transparent view and colored highlight
    femap.Info_ViewShowTransparent = True
    femap.Info_ViewShowUseColor = True

    if len(entity_ids) > 0:
        fe_set = list_to_fset(femap, entity_ids)
        if autoscale:
            fe_set.ShowAutoscale(entity_type)
        else:
            fe_set.Show(entity_type)
    femap.feViewRegenerate(0)

    return


def take_screenshot(
        femap:          Pyfemap.model,
        filename:       str,
        directory:      str = None,
        file_format:    int = 4,
        use_dlg:        bool = False,
        save_region:    int = 0
) -> None:
    """Calls the File-->Picture-->Save command to take a screenshot. Defaults to .jpg in the current working directory

    Parameters
    ----------
    femap
        FEMAP application object
    filename
        Name of the picture file with extension included.
    directory
        Optional (Default: current working directory) Path of the directory where you save the image.
    file_format
        Options are:
        1 = Bitmap
        2 = Metafile
        3 = Placeable Metafile
        4 = JPEG                    (*Default*)
        5 = Bitmap Series
        6 = AVI
        7 = JT
        9 = GIF
        10 = Animated GIF
        11 = TIF
        12 = PNG
    use_dlg
        Optional: Flag to bring up a dialog box where the user can select picture type / name / etc

    save_region
        Options are:
        0 = Graphics Window         (*Default*)
        1 = Layout
        2 = Entire Desktop

    Examples
    --------
    >>> take_screenshot(femap, 'picture.jpg')
    """

    if directory is None:
        directory = os.getcwd()

    picture_path = os.path.join(directory, filename)
    rc = femap.feFilePictureSave2(use_dlg, save_region, file_format, picture_path)

    check_return_code(rc, 'Screenshot Error')

    femap.feViewRegenerate(0)

    return


def rotate_view_to_point(
        femap:          Pyfemap.model,
        coords:         tuple[float, float, float] | list[float] = None,
        point_id:       int = None,
        node_id:        int = None,
        oblique_angle:  float = 0.0
) -> None:
    """Rotates the active view around the Y axis so that the point specified is between the camera and the Y Axis.
    TODO: Implement better logic to allow user to select different CSYS and different rotation axis and test it out

    One of the three location parameters (coords, point_id, or node_id) must be passed to determine the location to
    rotate to. Passing none or passing more than one will cause an early return without rotating the model.

    Parameters
    ----------
    femap
        FEMAP application object
    coords
        Optional: Coordinates of interest to rotate to.
    point_id
        Optional: If you want to rotate to a geometric FEMAP point.
    node_id
        Optional: If you want to rotate to a node
    oblique_angle
        Optional: Oblique angle value will tilt the view "up" or "down".

    Examples
    --------
    >>> rotate_view_to_point(femap, (1.0, 5.0, 0.0))
    """
    fe_view = femap.feView
    fe_view_orient = femap.feViewOrient

    location_params = (coords, point_id, node_id)

    # Checks if only one param was passed. Sums up the boolean values (True = 1)
    if sum(param is not None for param in location_params) != 1:
        print(
            f'You passed the values: coords: {coords}, point_id: {point_id}, and node_id: {node_id}.'
            f'Only one of these can be used to find the location.\n'
            f'For example, the function should be passed like one of these examples:'
            f'    rotate_view_to_point(femap, coords=(0.0, 1.5, 2.0)'
            f'    rotate_view_to_point(femap, point_id=5) '
            f'    rotate_view_to_point(femap, node_id=100) '
        )
        print('Model was not rotated')
        return

    coordinates = []

    # Makes sure coordinates are passed as three floats
    if coords is not None:
        for i in coords:
            coordinates.append(float(i))
        if len(coordinates) != 3:
            print(f'Passed coords as {coords} which has {len(coords)} values. Enter only 3 coordinates (x,y,z) ')
            print('Model was not rotated')
            return

    # Gets coordinates from point_id
    elif point_id is not None:
        fe_point = femap.fePoint
        if fe_point.Exists(point_id):
            fe_point.Get(point_id)
            coordinates = [fe_point.x, fe_point.y, fe_point.z]
        else:
            print(f'Point: {point_id} does not exist.')
            print('Model was not rotated')
            return

    # Gets coordinates from node_id
    elif node_id is not None:
        fe_node = femap.feNode
        if fe_node.Exists(node_id):
            fe_node.Get(node_id)
            coordinates = [fe_node.x, fe_node.y, fe_node.z]
        else:
            print(f'Node: {node_id} does not exist.')
            print('Model was not rotated')
            return

    view_id = femap.feAppGetActiveView()[1]
    fe_view.Get(view_id)
    fe_view_orient.Get(view_id)

    angle = np.arctan2(coordinates[2], coordinates[0]) * 180 / math.pi - 90.0

    fe_view_orient.SetRotationAngles(oblique_angle, angle, 0)

    fe_view.Put(view_id)
    fe_view_orient.Put(view_id)
    femap.feViewRegenerate(0)

    return


def black_edges(
        femap:      Pyfemap.model,
        view_id:    int = None
) -> None:
    """Alters the FEMAP View to display black edges

    Parameters
    ----------
    femap
        FEMAP application object
    view_id
        Optional: If nothing is passed, assume the current active view
    """

    fe_view = femap.feView
    if view_id:
        fe_view.Get(view_id)
    else:
        view_id = femap.feAppGetActiveView()[1]
        fe_view.Get(view_id)

    fe_view.Setcolor(fc.FVI_FILLED_EDGES, fc.FCL_BLACK)
    fe_view.Put(fe_view.ID)
    femap.feViewRegenerate(0)
    return


def show_color_by_property(
        femap:      Pyfemap.model,
        randomize:  bool = True
) -> None:
    """Alters FEMAP view to display FEM colors by property

    Parameters
    ----------
    femap
        FEMAP application object
    randomize
        Optional: (Default=True). Generate random colors for each property in the model
    """
    if randomize:
        fe_set = femap.feSet
        fe_set.AddAll(fc.FT_PROP)
        rc = femap.feModifyColor(fc.FT_PROP, fe_set.ID, fc.FCL_GREEN, True)  # Green is just an initialization value
        check_return_code(rc)

    # Command for color by props
    # TODO: Check to see if this changes between versions of FEMAP / change this to a more programmatic API call
    femap.feRunCommand(2447, True)

    femap.feViewRegenerate(0)

    return


def background_color_swap(femap: Pyfemap.model) -> None:
    """Color swap the background

    Parameters
    ----------
    femap
        FEMAP application object
    """
    fe_view = femap.feView
    view_id = femap.feAppGetActiveView()[1]
    fe_view.Get(view_id)

    if fe_view.WindowShadeBack:                                 # Background is shaded, standard FEMAP, must flip things
        fe_view.WindowBackColor = fc.FCL_WHITE
        fe_view.WindowShadeBack = False                         # Turns shaded background off
        fe_view.vColor = [fc.FVI_LABEL, fc.FCL_BLACK]           # Label Parameter color
        fe_view.vColor = [fc.FVI_VIEW_LEGEND, fc.FCL_BLACK]     # View Legend - View Color
        fe_view.vColor = [fc.FVI_POST_TITLES, fc.FCL_BLACK]     # Post Titles - View Color
        fe_view.vColorMode = [fc.FVI_CONTOUR_LEGEND, 1]         # Contour Legend - Label Color = 1..Use View Color
        fe_view.vColor = [fc.FVI_CONTOUR_LEGEND, fc.FCL_BLACK]  # Contour Legend - View Color
        fe_view.vColor = [fc.FVI_XY_AXES_STYLE, fc.FCL_BLACK]   # XY Axes Style - Axes Color
        fe_view.vColor = [fc.FVI_XY_TITLES, fc.FCL_BLACK]       # XY Titles - View Color
        fe_view.vColor = [fc.FVI_XY_XAXIS, fc.FCL_BLACK]        # XY X Range/Grid - Grid Color
        fe_view.vColor = [fc.FVI_XY_YAXIS, fc.FCL_BLACK]        # XY Y Range/Grid - Grid Color

    else:
        fe_view.WindowBackColor = fc.FCL_BLACK
        fe_view.WindowShadeBack = True
        fe_view.vColor = [fc.FVI_LABEL, fc.FCL_WHITE]
        fe_view.vColor = [fc.FVI_VIEW_LEGEND, fc.FCL_WHITE]
        fe_view.vColor = [fc.FVI_POST_TITLES, fc.FCL_WHITE]
        fe_view.vColorMode = [fc.FVI_CONTOUR_LEGEND, 0]         # Contour Legend - Label Color = 0..Contour Colors
        fe_view.vColor = [fc.FVI_XY_AXES_STYLE, fc.FCL_WHITE]
        fe_view.vColor = [fc.FVI_XY_TITLES, fc.FCL_WHITE]
        fe_view.vColor = [fc.FVI_XY_XAXIS, fc.FCL_BLUE]
        fe_view.vColor = [fc.FVI_XY_YAXIS, fc.FCL_BLUE]

    fe_view.Put(view_id)
    femap.feViewRegenerate(0)

    return


def free_edge_flip(femap: Pyfemap.model) -> None:
    """Flips the current view to show free edges

    Parameters
    ----------
    femap
        FEMAP application object
    """
    fe_view = femap.feView
    view_id = femap.feAppGetActiveView()[1]
    fe_view.Get(view_id)
    if fe_view.Mode == fc.FVM_FREE:
        fe_view.Mode = fc.FVM_HIDE
    else:
        fe_view.Mode = fc.FVM_FREE
    fe_view.Put(view_id)
    femap.feViewRegenerate(0)

    return


def show_only(
        femap:          Pyfemap.model,
        entity_type:    int,
        entity_list:    int | Iterable[int]
) -> None:
    """Turns off all other visible entities except for the entities defined in entity_type / entity_list

    This is similar to utilizing the visibility toggle boxes on the Model Info window pane on the left side of the GUI

    Parameters
    ----------
    femap
        FEMAP application object
    entity_type
        FEMAP constant for the entity type
    entity_list
        Which entities you want to only show in the current view
    """
    fe_set = femap.feSet

    # Type cast to tuple
    entity_list = (int(entity_list),) if isinstance(entity_list, (int, str)) else tuple(entity_list)

    # Get current visibility settings for entity_type in the current view and store it in a FeSet
    femap.feEntityGetVisibility(entity_type, fe_set.ID, True)

    fe_set.AddAll(entity_type)
    fe_set.RemoveArray(len(entity_list), entity_list)

    entity_to_hide = fe_set.GetArray()[2]  # Convert FeSet to a tuple

    # Creates a corresponding tuple set to False for each entry in entities_to_hide
    entity_visible_toggle = (False,) * len(entity_to_hide)

    femap.feEntitySetVisibility2(entity_type, len(entity_to_hide), entity_to_hide, entity_visible_toggle, True)
    femap.feViewRegenerate(0)

    return


def show_hide_all(
        femap:              Pyfemap.model,
        entity_type:        int,
        show_hide_toggle:   bool
) -> None:
    """Shows or hides all off the entities that belong to the entity_type.

    Parameters
    ----------
    femap
        FEMAP application object
    entity_type
        FEMAP constant for entity type
    show_hide_toggle
        True = Show All, False = Hide All
    """
    fe_set = femap.feSet
    fe_set.AddAll(entity_type)
    entities_to_show = fe_set.GetArray()[2]
    toggle_array = (show_hide_toggle,) * len(entities_to_show)

    femap.feEntitySetVisibility2(entity_type, len(entities_to_show), entities_to_show, toggle_array, True)
    femap.feViewRegenerate(0)

    return



