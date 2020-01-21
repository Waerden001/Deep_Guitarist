import functools

def getPseudoHash(noteArray):
    pseudoHash = ''
    for i in range(0, 12, 3):
        seg = functools.reduce((lambda a,b : str(int(a))+str(int(b))), noteArray[i:i+3])
        pseudoHash += str(chr(int(seg, 2) + 97))

    return pseudoHash

def noteArrayToNoteContainer(noteArray):
    stepToNote = {i:("C" + "#" * i) for i in range(12)}
    n = note_container()

    for i, note in enumerate(noteArray):
        if note == 1:
            noteName = stepToNote(i)
            n.add_note(Note(noteName, "4"))

    return n