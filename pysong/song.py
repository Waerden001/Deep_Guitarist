from typing import List

from attr import attrs, attrib
from pychord import Chord


@attrs
class Time:
    measure = attrib(type=int)
    beat = attrib(type=int, default=0)
    tick = attrib(type=int, default=0)

    def __str__(self):
        return f"{self.measure}:{self.beat}:{self.tick}"

    def as_seconds(self, tempo, tick_per_beat, beat_per_measure):
        return (self.tick / tick_per_beat + self.beat + self.measure * beat_per_measure) / tempo * 60

    def as_num(self, tick_per_beat = 4, beat_per_measure = 4):
        return self.tick + (self.beat + self.measure*beat_per_measure)*tick_per_beat
    
    @classmethod
    def tick_per_measure(cls, tick_per_beat = 4, beat_per_measure = 4):
        return beat_per_measure*tick_per_beat

    def as_moment(self):
        if self.measure >= 1:
            self.measure -= 1
        if self.beat >= 1:
            self.beat -= 1
        if self.tick >=1:
            self.tick -= 1

class ChordEvent:
    def __init__(self, time_: Time, duration: Time, chord: Chord):
        """Note the difference between (time_= first measure/beat/tick) and (duration = 1 measure/beat/tick)
           e.g. Song starts on the 0th measure and 0th beat, which is not exactly the same as the musical notation
           TODO: maybe we should change this, not a big deal
        :param: time_: Time instance of the momoment of the event
        :param: duration: Time instance of the duration of the event
        :chord: chord: Chord instance, content of the even 
        """
        self.time = time_.as_moment()
        self.duration = duration
        self.chord = chord

    def from_input(self):
        pass 


class ChordTrack:
    def __init__(self):
        self.chords: List[ChordEvent] = []

    def append(self, chord: ChordEvent):
        self.chords.append(chord)
    def __repr__(self):
        """represent the ChordTrack in nice way.

        remember that chord._chord is the str representation of the chord instance

        """
        info = []
        for event in self.chords:
            info.append(event.chord._chord)
            info += ["_" for _ in range(event.duration.as_num()-1)]
        return "".join("\n"*(index % (Time.tick_per_measure())==0) + ele for index, ele in enumerate(info))



class Song:
    """class to handle songs in a key-signature-free style. i.e. we don't specify the key, tempo type of things 
    """

    def __init__(self):
        """
        structure: list of str, the structure of the song, e.g ["A", "A, "B", "A"]
        _chordtrack: dict of ChordTrack instances, chord tracks of every section, e.g. {"A": ChordTrack instance, "B": ChordTrack instance}
        TODO:
        self._drumtrack: dict of DrumTrack instances
        self._bassline: dict of Bassline instances
    
        """
        self._name = ""
        self._structure = []
        self._chordtrack = {}
        
    def add_track(self, name, chord_track):
        self._chordtrack[name] = chord_track

    def structure(self):
        return "".join(self.sturcture)

    def part(self, part_name):
        if part_name in self._chordtrack:
            return self._chordtrack[part_name]
        else:
            raise ValueError("{} is not a section of {}".format(part, self.name)) 
    

