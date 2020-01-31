
class Bar:
    """Kind of a replacement of the Time class. 

    :param: _content: list of tuples to be added in the Section class.
    """
    def __init__(self, beat_per_measure, tick_per_beat):
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
        pass

    def __repr__(self):
        pass

    def __add__(self, other):
        """Add two sections to get a bigger section
        """
        pass

    def add_bar(self, bar):
        pass

    def add_bars(self, bar, num):
        for _ in range(num):
            self.add_bar(bar)

    def del_bar(self, num):
        """delete a bar from a section
            TODO: be careful, delete a particular bar from a section is a wired operation, 
            the numbering of the bars needs to be changed accordingly
        """

##song.py contains ChordTrack class, remember to delete it when it's necessary.
class ChordSection:
    def __init__(self, section):
        """
        :param: section: Section instance, gives the frame of a song section, e.g. verse of "How deep is your love"
        """
        pass

    def __repr__(self):
        pass

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
        pass
