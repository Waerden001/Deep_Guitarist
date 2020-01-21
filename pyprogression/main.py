from __future__ import print_function
import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Activation, Embedding, Dropout, TimeDistributed, Flatten, LSTM
from keras import backend as K
from keras.utils.vis_utils import plot_model
from Generators import KerasBatchGenerator
import os
import json

data_path = "/Users/paulbiberstein/Desktop/FormattedChordDatasets"

def load_data():
    # get the data paths
    train_path = os.path.join(data_path, "RealBookTrainDataset.txt")
    valid_path = os.path.join(data_path, "RealBookValidDataset.txt")
    test_path = os.path.join(data_path, "RealBookTestDataset.txt")

    # build the complete vocabulary, then convert text data to list of integers
    with open(train_path, "r") as f:
        train_data = json.load(f)
    with open(valid_path, "r") as f:
        valid_data = json.load(f)
    with open(test_path, "r") as f:
        test_data = json.load(f)

    print(train_data[0:200])

    return train_data, valid_data, test_data

train_data, valid_data, test_data = load_data()

num_steps = 5
batch_size = 20
features = 12
use_dropout=False
train_data_generator = KerasBatchGenerator(train_data, num_steps, batch_size, features,
                                           skip_step=num_steps)
valid_data_generator = KerasBatchGenerator(valid_data, num_steps, batch_size, features,
                                           skip_step=num_steps)
test_data_generator = KerasBatchGenerator(test_data, num_steps, 1, features,
                                           skip_step=1)




model = Sequential()
model.add(Dense(features, input_shape=(num_steps, features) ))
model.add(LSTM(features, return_sequences=True))
model.add(LSTM(features, return_sequences=True))
if use_dropout:
    model.add(Dropout(0.5))
model.add(TimeDistributed(Dense(features)))
model.add(Activation('sigmoid'))

model.compile(loss=keras.losses.binary_crossentropy,
    optimizer='adam',
    metrics=[keras.metrics.binary_accuracy])

print(model.summary())
#plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)
checkpointer = keras.callbacks.ModelCheckpoint(filepath=data_path + '/model/model-{epoch:02d}.hdf5', verbose=1)
num_epochs = 50

model.fit_generator(train_data_generator.generate(), len(train_data)//(batch_size*num_steps), num_epochs,
                        validation_data=valid_data_generator.generate(),
                        validation_steps=len(valid_data)//(batch_size*num_steps),
                        callbacks=[checkpointer])
model.save(data_path + "/model" + "/final_model.hdf5")


score = model.evaluate_generator(test_data_generator, verbose=1)
print('Test loss:', score[0])
print('Test accuracy:', score[1])