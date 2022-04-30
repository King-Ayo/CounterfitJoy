from keras.models import load_model
import numpy as np
from keras.models import Sequential
import keras

# Generated by counterfit #

from counterfit.core.targets import Target


class Goodvillain(Target):
    target_name = "GoodVillain"
    target_data_type = "image"
    target_endpoint = f"savory_unsavory_model3.h5"
    target_input_shape = (460, 670, 3)
    target_output_classes = ['savory', 'unsavory']
    sample_input_path = f"final3.npx.npz"
    target_classifier = "BlackBox"
    X = []

    def load(self):
        self.data = np.load(self.fullpath(
            self.sample_input_path), allow_pickle=True)
        self.X = self.data["X"].astype(np.float32) / 505.
        self.model = load_model(self.fullpath(self.target_endpoint))

    def get_device(self):
        return 'cpu'

    def predict(self, x):
        self.model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        l = []
        #print(x.shape)
        #ximg = [x[i,...] for i in range(len(x[0]))]
        #img = np.vstack(ximg)
        img = np.array(x)
        #print(img.shape)
        pre = (self.model.predict(x) > 0.5).astype('int32')
        for s in pre:
            if s == 1:
                s = 'unsavory'
            else:
                s = 'savory'
            l.append([s])
        return pre