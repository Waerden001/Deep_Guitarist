# -*- coding: utf-8 -*-
from .constants import NOTE_VAL_DICT, VAL_NOTE_DICT
from .constants.scales import RELATIVE_KEY_DICT
from .parser import parse, parse_scale
from .utils import transpose_note, note_to_val

#### import check
#### Scale_Quality class check


class Scale(object):
    """ Class to handle a scale.

    :param str _scale: Name of the chord. (e.g. Cmaj, Aminblues, F#majpenta)
    :param str _root: The root note of scale.
    :param pychord.Scale_Quality _quality: The quality of scale. (e.g. min, maj, harmonicmin, ...)
    """
    def __init__(self, scale):
        """ Constructor of Chord instance

        :param str chord: Name of chord.
        """
        self._scale = scale
        self._root, self._quality = "", ""
        ##Use the scale parser accordingly
        self._parse(scale)

    def __unicode__(self):
        return self._scale

    def __str__(self):
        return self._scale

    def __repr__(self):
        return "<Scale: {}>".format(self._scale)

    def __eq__(self, other):
        if not isinstance(other, Scale):
            raise TypeError("Cannot compare Scale object with {} object".format(type(other)))
        if note_to_val(self._root) != note_to_val(other.root):
            return False
        if self._quality != other.quality:
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    @classmethod
    def diatonic(self):
        """rtype: Chord instances, e.g. diatonic(Cmaj) = (Cmaj, Dmin, Emin, Fmaj, Gmaj, Amin, Bm7-5)"""
        pass

    @property
    def scale(self):
        """ The name of scale"""
        return self._scale

    @property
    def root(self):
        """ The root note of scale """
        return self._root

    @property
    def quality(self):
        """ The quality of scale """
        return self._quality

    def info(self):
        """ Return information of scale to display """
        return """{}
root={}
quality={}
""".format(self._scale, self._root, self._quality)

    def transpose(self, trans, scale="C"):
        """ Transpose the scale

        :param int trans: Transpose key
        :param str scale: key scale
        :return:
        """
        if not isinstance(trans, int):
            raise TypeError("Expected integers, not {}".format(type(trans)))
        self._root = transpose_note(self._root, trans, scale)
        self._rename_scale()

    def components(self, visible=True):
        """ Return the component notes of scale

        :param bool visible: returns the name of notes if True else list of int
        :rtype: list[(str or int)]
        :return: component notes of scale
        """
        ##Note that we still have to implement the Scale_Quality class properly
        return self._quality.get_components(root=self._root, visible=visible)

    def _parse(self, scale):
        """ parse a scale

        :param str scale: Name of scale.
        """
        ##TODO: be careful! parse_scale returns a multi-list not just several differnt values
        root, quality = parse_scale(scale)
        self._root = root
        self._quality = quality

    def _rename_scale(self):
        self._scale = "{}{}".format(self._root, self._quality._quality)


def as_scale(scale):
    """ convert from str to Scale instance if input is str

    :type scale: str|pychord.Scale
    :param scale: scale name or Chord instance
    :rtype: pychord.Scale
    :return: Scale instance
    """
    if isinstance(scale, Scale):
        return scale
    elif isinstance(scale, str):
        return Scale(chord)
    else:
        raise TypeError("input type should be str or Scale instance.")
