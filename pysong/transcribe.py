
from copy import copy, deepcopy as copy, deepcopy
from pychord import Chord

class Bar:
    """Kind of a replacement of the Time class. 

    :param: _content: list of tuples to be added in the Section class.
    """
    def __init__(self, beat_per_measure = 4, tick_per_beat = 4):
        self.beat_per_measure = beat_per_measure
        self.tick_per_beat = tick_per_beat
        self._content = []

    def beat_per_measure(self):
        return self.beat_per_measure

    def tick_per_beat(self):
        return self.tick_per_beat



class Section:
    def __init_(self):
        """Dictionary of of bar instances

        """
        self._table = {} 
        self._num = 0
        pass

    def __repr__(self):
        info = ""
        for (num, bar) in self._table.item():
           info += "".join(" "*(index % 4 == 0) + "_" for index in range(bar.beat_per_measure*bar.tick_per_beat)) + "\n"       
        return info

    def add_bar(self, bar):
        if not isinstance(bar, Bar):
            raise TypeError("Expected {} type instead of {}".format(type(Bar), type(bar)))
        else:
            self._table[self._num] = deepcopy(bar)
            self._num += 1

    def add_bars(self, bar, num):
        for _ in range(num):
            self.add_bar(bar)

    def add_section(self, other):
        if not isinstance(other, Section):
            raise TypeError("Expected {} type instead of {} type".format(type(Section), type(other)))
        for measure in other._table:
            self.add_bar(other._table[measure])


    def replace_bar(self, bar, bar_num):
        """
        """
        if bar_num in self._table:
            self._table[bar_num] = deepcopy(bar) 

    def del_last(self):
        if self._num >= 1:
            del self._table[self._num]
            self._num -= 1

##song.py contains ChordTrack class, remember to delete it when it's necessary.
class ChordSection(Section):
    def __init__(self, frame):
        """
        TODO: might need deepcopy if we'll have more classes inherited from the Section class.
        :param: section: Section instance, gives the frame of a song section, e.g. verse of "How deep is your love"
        """
        if not isinstance(frame, Section):
            raise TypeError("Expected to initiate ChordTrack by an instance of {} instead of {}".format(type(Section), type(frame)))
        self._table = frame._table
        self._num = frame._num

    def insert(self, num, event):
        """
        :param: event, tuple of chord location and chord, e.g. ((1,4), Chord("E"))
        """
        assert num in self._frame, "Measure num out of range!"
        self._frame[num]._content.append(event)

    def fill_bar(self, num, events):
        for event in events:
            self.insert(event)



    def __repr__(self):
        info = ""
        for (num, bar) in self._table.item():
            chord_location = {}
            for event in bar:
                chord_location[(event[0][0]-1)*bar.beat_per_measure+(event[0][1]-1)*bar.tick_per_beat] = event[1]._name

            info += "".join(" "*(index % 4 == 0) + (chord_location[index] if index in chord_location else "_") 
                    for index in range(bar.beat_per_measure*bar.tick_per_beat))
            info += "\n"
        return info
            

class PercussionSection:
    def __init__(self, section):
        pass

    def __repr__(self):
        pass

class BassSection:
    def __init__(self, section):
        pass

    def __repr__:
        pass
        
#song.py contains another Song class, remember to delete it when it's necessary.
class Song:
    def __init__(self):
        self.structure = []
        self.chordtrack = {}
        pass
