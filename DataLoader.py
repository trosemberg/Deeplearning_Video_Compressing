import numpy as np
from tensorflow import keras
import re
import pandas as pd


class DataGenerator(keras.utils.Sequence):
    'Generates data for Keras'
    def __init__(self,df,Map,batch_size=20,dim=64,norm=True,n_classes=2, shuffle=True,cte_height = 1080 ,cte_width = 1920):
        self.batch_size = batch_size
        self.df = df
        self.dim = (1,(dim*dim)+1)
        self.size = dim
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
            Input = (file[begin_Frame:end_Frame].reshape([self.cte_height,self.cte_width]))[self.df.loc[ID]['Height']:self.df.loc[ID]['Height']+self.size,self.df.loc[ID]['Width']:self.df.loc[ID]['Width']+self.size]
            if self.norm:
                Input = Input/255.0
                X[i,] = np.append(Input.reshape(1,self.size*self.size)[0],self.df.loc[ID]["QP"]/37.0)
            else:
                X[i,] = np.append(Input.reshape(1,self.size*self.size)[0],self.df.loc[ID]["QP"])
            # Store class
            y[i,] = self.df.loc[ID]['Split']

        return X.squeeze(), keras.utils.to_categorical(y, num_classes=self.n_classes)
    
    
class Predictions_Input():
    def __init__(self,folder):
        file = open("./{}/encoder_randomaccess_main.cfg".format(folder),"r")
        strings = file.readlines()
        file.close()
        resultados = re.search(r"(\/[a-zA-Z1-9]*_(\d+)x(\d+).*yuv)",strings[2])
        self.video  = resultados.group(1)
        self.width = int(resultados.group(2))
        self.height = int(resultados.group(3))
        resultados = re.search(r":\s(\d+)",strings[6])
        self.frame_start = int(resultados.group(1))
        resultados = re.search(r":\s(\d+)",strings[9])
        self.n_frames = int(resultados.group(1))
        resultados = re.search(r":\s(\d+)",strings[68])
        self.QP = int(resultados.group(1))
        
    def generate_input(self):
        Input = pd.DataFrame([],columns=["Frame","Height","Width"])
        for frame in range(self.frame_start,self.frame_start+self.n_frames):
            Input = pd.concat([Input,pd.DataFrame([[frame,h,w] for h in range(0,self.height,64) for w in range(0,self.width,64)],columns =["Frame","Height","Width"])],ignore_index=True)
        Video = np.fromfile("."+self.video,dtype='uint8')
        Input["Frame"] = Input["Frame"].astype("uint16")
        Input["Height"] = Input["Height"].astype("uint16")
        Input["Width"] = Input["Width"].astype("uint16")
        return Input,Video

    
def map_CU(df,cte_height,cte_width,size,file,QP):
    X = np.empty((1,size*size+1))
    begin_Frame = int(df['Frame'])*(cte_height*cte_width + cte_height*cte_width/2)
    end_Frame = (int(df['Frame']))*(cte_height*cte_width + cte_height*cte_width/2)+cte_height*cte_width
    begin_Frame = int(begin_Frame)
    end_Frame = int(end_Frame)
    Input = (file[begin_Frame:end_Frame].reshape([cte_height,cte_width]))[df['Height']:df['Height']+size,df["Width"]:df['Width']+size]
    Input = Input/255.0
    X[0,] = np.append(Input.reshape(1,size*size)[0],QP/37.0)
    return X

def generate_Depth(df,num):
    data = []
    data1 = [{"Frame":df["Frame"],"Height":df["Height"],"Width":df["Width"]}]
    data2 = [{"Frame":df["Frame"],"Height":df["Height"],"Width":df["Width"]+num}]
    data3 = [{"Frame":df["Frame"],"Height":df["Height"]+num,"Width":df["Width"]}]
    data4 = [{"Frame":df["Frame"],"Height":df["Height"]+num,"Width":df["Width"]+num}]
    data = data1+data2+data3+data4
    return pd.DataFrame(data)