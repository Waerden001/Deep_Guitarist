# -*- coding: utf-8 -*-

from .constants import QUALITY_DICT, SCALE_QUALITY_DICT
from .quality import Quality, Scale_Quality
from .utils import NOTE_VAL_DICT, note_to_val, val_to_note
from collections import OrderedDict


def parse(chord):
    """ Parse a string to get chord component

    :param str chord: str expression of a chord
    :rtype: (str, pychord.Quality, str, str)
    :return: (root, quality, appended, on)
    """

    if len(chord) > 1 and chord[1] in ("b", "#"):
        root = chord[:2]
        rest = chord[2:]
    else:
        root = chord[:1]
        rest = chord[1:]

    check_note(root, chord)
    on_chord_idx = rest.find("/")
    if on_chord_idx >= 0:
        on = rest[on_chord_idx + 1:]
        rest = rest[:on_chord_idx]
        check_note(on, chord)
    else:
        on = None
    if rest in QUALITY_DICT:
        quality = Quality(rest)
    else:
        raise ValueError("Invalid chord {}: Unknown quality {}".format(chord, rest))
    # TODO: Implement parser for appended notes
    appended = []
    return root, quality, appended, on


def check_note(note, chord):
    """ Return True if the note is valid. e.g. M7 is not a valid chord, M is not a valid note.

    :param str note: note to check its validity
    :param str chord: the chord which includes the note
    :rtype: bool
    """
    if note not in NOTE_VAL_DICT:
        raise ValueError("Invalid chord {}: Unknown note {}".format(chord, note))
    return True




def parse_scale(scale):
    """ Parse a string to get scale component

    :param str chordscale: str expression of a scale, e.g. Cminblues, F#minpenta
    :rtype: (str, OrderedDict)
    :return: (root, quality), e.g. (majpenta, (0,2,4,7,9,12))
    """

    if len(scale) > 1 and scale[1] in ("b", "#"):
        root = scale[:2]
        rest = scale[2:]
    else:
        root = scale[:1]
        rest = scale[1:]
    

    check_scale(root, scale)
    if rest in SCALE_QUALITY_DICT:
        quality = Scale_Quality(rest)
    else:
        raise ValueError("Invalid scale{}: Unknown quality {}".format(scale, rest))
    return root, quality



def check_scale(note, scale):
    """ Return True if the note is valid. e.g. Mblues is not a valid scale, M is not a valid note.

    :param str note: note to check its validity
    :param str scale: the scale which includes the note
    :rtype: bool
    """
    if note not in NOTE_VAL_DICT:
        raise ValueError("Invalid scale {}: Unknown note {}".format(scale, note))
    return True

