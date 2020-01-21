import keras
from keras.models import load_model
from keras import backend as K
from Generators import KerasBatchGenerator
import os, json
import numpy as np
from util import *

MINIMUM_NOTES = 4

directory_path = "/home/paul/Development/SeniorProject/MusicalDatasets"
model_path = directory_path + "/model/final_model.hdf5"
train_path = directory_path + "/RealBookTrainDataset.txt"
default_reversed_dictionary_path = directory_path + "/defaultReverseDict.json"
hashed_reversed_dictionary_path = directory_path + "/hashedReverseDict.json"

with open(default_reversed_dictionary_path, "r") as f:
    default_reversed_dictionary = json.load(f)
with open(hashed_reversed_dictionary_path, "r") as f:
    hashed_reversed_dictionary = json.load(f)
with open(train_path, "r") as f:
    train_data = json.load(f)

model = load_model(model_path)

dummy_iters = 10
num_steps = 5
batch_size = 20
features = 12
example_training_generator = KerasBatchGenerator(train_data, num_steps, 1, features,
                                                 skip_step=1)

for i in range(dummy_iters):
    dummy = next(example_training_generator.generate())

num_predict = 1
true_print_out = "Actual words: "
pred_print_out = "Predicted words: "

for i in range(num_predict):
    data = next(example_training_generator.generate())[0]
    
    predictions = model.predict(data)

    for prediction in predictions[0]:
        for threshold in range(5, 0, -1):
            noteArray = (prediction > (threshold/10)).astype(np.int)
            if (noteArray == 1).sum() >= MINIMUM_NOTES:
                break
        try:
            chord = hashed_reversed_dictionary[getPseudoHash(noteArray.tolist())]
            pred_print_out += " " + str(chord)
        except KeyError:
            print("Could not find chord that corresponds to: " + str(noteArray.tolist()))
            pred_print_out += " <unk>"

    trueNoteArrays = train_data[dummy_iters + i : num_steps + dummy_iters + i]
    for noteArray in trueNoteArrays:
        try:
            chord = hashed_reversed_dictionary[getPseudoHash(noteArray)]
            true_print_out += " " + str(chord)
        except KeyError:
            print("Could not find chord that corresponds to\n" + str(list(noteArray)))
            true_print_out += " <unk>"

print("-"*20)
print(true_print_out)
print(pred_print_out)
print("-"*20)