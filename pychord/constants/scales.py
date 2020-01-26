NOTE_VAL_DICT = {
    'Ab': 8,
    'A': 9,
    'A#': 10,
    'Bb': 10,
    'B': 11,
    'Cb': 11,
    'C': 0,
    'C#': 1,
    'Db': 1,
    'D': 2,
    'D#': 3,
    'Eb': 3,
    'E': 4,
    'F': 5,
    'F#': 6,
    'Gb': 6,
    'G': 7,
    'G#': 8,
}

NOTE_TEX_DICT = {
    'Ab': 'A$\\flat$',
    'A': 'A',
    'A#': 'A$\\sharp$',
    'Bb': 'B$\\flat$',
    'B': 'B',
    'Cb': 'C$\\flat$',
    'C': 'C',
    'C#': 'C$\\sharp$',
    'Db': 'D$\\flat$',
    'D': 'D',
    'D#': 'D$\\sharp$',
    'Eb': 'E$\\flat$',
    'E': 'E',
    'F': 'F',
    'F#': 'F$\\sharp$',
    'Gb': 'G$\\flat$',
    'G': 'G',
    'G#': 'G$\\sharp$',
}




VAL_NOTE_DICT = {
    0: ['C'],
    1: ['Db', 'C#'],
    2: ['D'],
    3: ['Eb', 'D#'],
    4: ['E'],
    5: ['F'],
    6: ['F#', 'Gb'],
    7: ['G'],
    8: ['Ab', 'G#'],
    9: ['A'],
    10: ['Bb', 'A#'],
    11: ['B', 'Cb']
}

SHARPED_SCALE = {
    0: 'C', 1: 'C#', 2: 'D', 3: 'D#',
    4: 'E', 5: 'F', 6: 'F#', 7: 'G',
    8: 'G#', 9: 'A', 10: 'A#', 11: 'B'
}

FLATTED_SCALE = {
    0: 'C', 1: 'Db', 2: 'D', 3: 'Eb',
    4: 'E', 5: 'F', 6: 'Gb', 7: 'G',
    8: 'Ab', 9: 'A', 10: 'Bb', 11: 'B'
}

SCALE_VAL_DICT = {
    'Ab': FLATTED_SCALE,
    'A': SHARPED_SCALE,
    'A#': SHARPED_SCALE,
    'Bb': FLATTED_SCALE,
    'B': SHARPED_SCALE,
    'Cb': FLATTED_SCALE,
    'C': FLATTED_SCALE,
    'C#': SHARPED_SCALE,
    'Db': FLATTED_SCALE,
    'D': SHARPED_SCALE,
    'D#': SHARPED_SCALE,
    'Eb': FLATTED_SCALE,
    'E': SHARPED_SCALE,
    'F': FLATTED_SCALE,
    'F#': SHARPED_SCALE,
    'Gb': FLATTED_SCALE,
    'G': SHARPED_SCALE,
    'G#': SHARPED_SCALE,
}

RELATIVE_KEY_DICT = {
    'maj': [0, 2, 4, 5, 7, 9, 11, 12],
    'min': [0, 2, 3, 5, 7, 8, 10, 12],
}

#Need to be updated for tension notes
INTERVAL_COLOR_DICT = {
    0: 'black',
    1: 'red',
    2: 'red',
    3: 'blue',
    4: 'blue',
    5: 'orange',
    6: 'orange',
    7: 'white',
    8: 'pink',
    9: 'yellow', 
    10: 'green',
    11: 'green',
    12: 'black',
    13: 'red',
    14: 'red',
    15: 'blue',
    16: 'blue',
    17: 'orange',
    18: 'orange',
    19: 'white',
    20: 'pink',
    21: 'yellow', 
}

##need to consider the sharp/flat keys and extended notes
DEGREE_INTERVAL_DICT = {
    0: '0',
    1: 'b2',
    2: '2',
    3: 'b3',
    4: '3',
    5: '4',
    6: 'b5',
    7: '5',
    8: 'b6',
    9: '6',
    10: 'b7',
    11: '7',
    12: '0',
    13: 'b9',
    14: '9',
    15: '#9',
    16: '3',
    17: '11',
    18: '#11',
    19: '5',
    20: 'b13',
    21: '13',
 }
