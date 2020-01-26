from .constants import TUNING_DICT, NOTE_VAL_DICT, VAL_NOTE_DICT, INTERVAL_COLOR_DICT, DEGREE_INTERVAL_DICT, NOTE_TEX_DICT
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
    
    
    #This is kind of like a decorator of the coordinates function. Should be optimized later.
    def note_tex(self, pattern, form = 'note'):
        """
        """
        note_tex = ''
        for ele in self.coordinates(pattern):
            node_type = INTERVAL_COLOR_DICT[ele[-1]]+'_node'
            text = NOTE_TEX_DICT[ele[1]] if form == 'note' else DEGREE_INTERVAL_DICT[ele[-1]]
            string_num = 7-ele[0][0]
            fret = ele[0][1]
            if fret != 0:#Need to modify the base.txt to handle the open strings, now let's just ignore it
                note_tex += """\\node[{}] at ({}-{})""".format(node_type, string_num, fret) + '{'+"\\textbf{{"+text + "}}"+"};\n"
        
        return note_tex
    
    ###Notice the difference of the orderings of strings between the python code and tex file
    def texify(self, pattern, form = 'note'):
        length_info = str(self._length)
        mark_info = "3,5,7,9,15,17" if self._length == 24 else "3,5,7,9"
        tuning_info = ', '.join([str(k)+'/'+ str(NOTE_VAL_DICT[self._notes[k-1]]) for k in range(1,7)])
        note_info = self.note_tex(pattern, form)

        fin = open("C:\\Users\\Waerden\\Desktop\\Deep_guitarist\\pychord\\constants\\base.txt", "rt")
        fout = open("C:\\Users\\Waerden\\Desktop\\Deep_guitarist\\pychord\\constants\\output.txt", "w")
        for line in fin:
            line = line.replace("SCALE_LENGTH", length_info)
            line = line.replace("MARK", mark_info)
            line = line.replace("TUNING", tuning_info)
            line = line.replace("%NOTES_INFORMATION%", note_info)
            print(line)
            fout.write(line)
        
        fin.close()
        fout.close()
        



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

