




class Fretboard(object):
    """Fretboard class to handle the visulization of scales and chords in a given tuning
    """

    def __init__(self, tuning, scale_length="full"):
        """Constructor of fretboard instance. 
        """

    def coordinates(self, notes):
        """Find all coordinates on fretboard of note, chord or scale. 

        e.g. PB = Fretboard('DADGAD'), PB.coordinates(Am7) returns all coordinates of notes in Am7 on a DADGAD (Pierre Bensusan) tuning fretboard.

        :param notes: str or scale instance or chord instance
        :rtype: dict of (note name, coordinates, relative degree), e.g. a term in the returned result might look like ('G#', (6, 4), 4), this means 
        G# is the major third of E, one location is on the sixth string and fourth fret.

        """
        pass

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

