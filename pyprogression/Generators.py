from keras.utils import to_categorical
import numpy as np

class KerasBatchGenerator(object):
    def __init__(self, data, num_steps, batch_size, features, skip_step=5):
        self.data = data
        self.num_steps = num_steps
        self.batch_size = batch_size
        self.features = features
        # this will track the progress of the batches sequentially through the
        # data set - once the data reaches the end of the data set it will reset
        # back to zero
        self.current_idx = 0
        # skip_step is the number of words which will be skipped before the next
        # batch is skimmed from the data set
        self.skip_step = skip_step
    
    def generate(self):
        x = np.zeros((self.batch_size, self.num_steps, self.features))
        y = np.zeros((self.batch_size, self.num_steps, self.features))
        batch = 0
        while True:
            batch+=1
            for i in range(self.batch_size):
                if self.current_idx + self.num_steps >= len(self.data):
                    # reset the index back to the start of the data set
                    self.current_idx = 0
                
                for j in range(self.num_steps+1):
                    if self.data[self.current_idx+j]==[-1]:
                        self.current_idx = self.current_idx + j + 1
                
                try:
                    x[i, :] = self.data[self.current_idx:self.current_idx + self.num_steps]
                except:
                    pass
                    # print("=========================\nX ERROR\n=========================")
                    # print(self.data[self.current_idx:self.current_idx + self.num_steps])
                    # print(i)
                try:
                    y[i, :] = self.data[self.current_idx + 1:self.current_idx + self.num_steps + 1]
                except:
                    pass
                    # print("=========================\nY ERROR\n=========================")
                    # print(self.data[self.current_idx + 1:self.current_idx + self.num_steps + 1])
                    # print(i)
                self.current_idx += self.skip_step
            # print("batch: " + str(batch))
            yield x, y