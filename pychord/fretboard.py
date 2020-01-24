from .constants import TUNING_DICT, NOTE_VAL_DICT, VAL_NOTE_DICT
from .chord import Chord
from .scale import Scale
from collections import OrderedDict

###Do we actually need OrderedDict???




class Fretboard(object):
    """Fretboard class to handle the visulization of scales and chords in a given tuning
    """

    def __init__(self, tuning, scale_length=24):
        """Constructor of fretboard instance. 

        :param: str tuning, e.g. opend, dadgad this sets up the notes for the open strings
        :param: int scale_length, e.g. 12, 24, 14 which sets up the number of frets on the fretboard
        :param: OrderedDict of notes on each string, e.g. self.table[1]= (  ((1,0), 'E'), ((1,1), 'F'), ((1,2), 'F#'), ..., ((1,24), 'E') )
        """
        self._tuning =  tuning
        self._notes = TUNING_DICT[tuning]
        self._length = scale_length
        self._table = self._setup()
        
    def table(self):
        return self._table
    def coordinates(self, pattern):
        """Find all coordinates on fretboard of note, chord or scale. 

        e.g. PB = Fretboard('DADGAD'), PB.coordinates(Am7) returns all coordinates of notes in Am7 on a DADGAD (Pierre Bensusan) tuning fretboard.
             PB.coordinates(Cmaj) returns all coordinates of notes in the C major scale in the DADGAD tuning. 
        :param notes: str (for note) or scale instance or chord instance
        :rtype: dict of (note name, coordinates, relative degree), e.g. a term in the returned result might look like ('G#', (6, 4), 4), this means 
        G# is the major third of E, one location is on the sixth string and fourth fret.

        """
        if isinstance(pattern, str) and pattern in NOTE_VAL_DICT:
            """"""
            return [[coordinate[0], pattern, 0] for string_num in [1,2,3,4,5,6] for coordinate in self._table[string_num] if pattern in coordinate[1]]
        elif isinstance(pattern, Chord):
            relative_degree = pattern.quality.components
            ##TODO: Handle slash chords carefully
            notes = pattern.components()
            ans = []
            for string_num in [1,2,3,4,5,6]:
                for coordinate in self._table[string_num]:
                    for note in notes:
                        if note in coordinate[1]:
                            ans.append([coordinate[0], note, relative_degree[notes.index(note)]])
            return ans

            
        elif isinstance(pattern, Scale):
            ##TODO: implement the Scale class accordingly
            ##It seems that if we implement Scale class similarly to the chord class, this function is more or less the same.
            relative_degree = pattern.quality.components
            notes = pattern.components()
            ans = []
            for string_num in [1,2,3,4,5,6]:
                for coordinate in self._table[string_num]:
                    for note in notes:
                        if note in coordinate[1]:
                            ans.append([coordinate[0], note, relative_degree[notes.index(note)]])
            return ans
        else:
            raise ValueError("Expected valid note or chord instance or scale instance instead of {}, type = {} ".format(pattern, type(pattern)))

    def _setup(self):
        """"""
        table = []
        for string_num in [1,2,3,4,5,6]:
            start_val = NOTE_VAL_DICT[self._notes[-string_num]]
            string_layout = []
            for fret in range(0, self._length+1):
                current_note = VAL_NOTE_DICT[(start_val + fret) % 12]
                string_layout.append(((string_num, fret), current_note))
            table.append((string_num, string_layout))
        return OrderedDict(table)
        #return [((string, fret),VAL_NOTE_DICT[NOTE_VAL_DICT[self._notes[-string_num]]+fret % 12]) for string_num in [1,2,3,4,5,6] for fret in range(0, self._length + 1)]

    def info(self):
        """Get the name and notes of the tuning. e.g. PB = Fretboard('dropd'), PB.info() = ('dropd',('D', 'A', 'D', 'G', 'B', 'E'))
        """
        return """{} tuning, low to high = {}""".format(self._tuning, self._notes)

    def show():
        """Show the fretboard with all notes labeled.
        """
        pass

    def show_note(note):
        """Show all locations of a note on the fretboard.
        """
        pass

    def show_scale(scale):
        """Show all notes on the fretboard of a given scale.
        """
        pass

    def show_chord(chord):
        """Show all notes on the fretboard of a chord.
        """
        pass

    def save():
        """Save a plotted chord/note/scale on the fretboard as an .svg file. But how??

        """
        pass

