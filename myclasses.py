import numpy as np
from tensorflow import keras

class DataGenerator(keras.utils.Sequence):
    'Generates data for Keras'
    def __init__(self,df,Map,batch_size=20,dim=(1,4097),norm=True,n_classes=2, shuffle=True,cte_height = 1080 ,cte_width = 1920):
        self.batch_size = batch_size
        self.df = df
        self.dim = dim
        self.Map = Map
        self.cte_height = cte_height
        self.cte_width = cte_width
        self.n_classes = n_classes
        self.shuffle = shuffle
        self.norm = norm
        self.on_epoch_end()

    def __len__(self):
        'Denotes the number of batches per epoch'
        return int(np.floor(len(self.df) / self.batch_size))

    def __getitem__(self, index):
        'Generate one batch of data'
        # Generate indexes of the batch
        indexes = self.df.iloc[index*self.batch_size:(index+1)*self.batch_size].index

        # Generate data
        X, y = self.__data_generation(indexes)

        return X, y

    def on_epoch_end(self):
        'Updates indexes after each epoch'
        self.indexes = np.arange(len(self.df))
        if self.shuffle == True:
            self.df = self.df.sample(frac=1)

    def __data_generation(self, indexes):
        'Generates data containing batch_size samples' # X : (n_samples, *dim, n_channels)
        # Initialization
        X = np.empty((self.batch_size, *self.dim))
        y = np.empty((self.batch_size), dtype=int)
        print
        # Generate data
        i=0
        for i, ID in enumerate(indexes):
            # Store sample
            file = self.Map[self.df.loc[ID]['Origem']]
            begin_Frame = int(self.df.loc[ID]['Frame'])*(self.cte_height*self.cte_width + self.cte_height*self.cte_width/2)
            end_Frame = (int(self.df.loc[ID]['Frame']))*(self.cte_height*self.cte_width + self.cte_height*self.cte_width/2)+self.cte_height*self.cte_width
            begin_Frame = int(begin_Frame)
            end_Frame = int(end_Frame)
            Input = (file[begin_Frame:end_Frame].reshape([self.cte_height,self.cte_width]))[self.df.loc[ID]['Height']:self.df.loc[ID]['Height']+64,self.df.loc[ID]['Width']:self.df.loc[ID]['Width']+64]
            if self.norm:
                Input = Input/255.0
                X[i,] = np.append(Input.reshape(1,64*64)[0],self.df.loc[ID]["QP"]/37.0)
            else:
                X[i,] = np.append(Input.reshape(1,64*64)[0],self.df.loc[ID]["QP"])
            # Store class
            y[i,] = self.df.loc[ID]['Split']

        return X, keras.utils.to_categorical(y, num_classes=self.n_classes)