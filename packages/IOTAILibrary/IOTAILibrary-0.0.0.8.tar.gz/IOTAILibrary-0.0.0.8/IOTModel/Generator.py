import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.optimizers import SGD
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
from tensorflow import keras
import IOTData.Structure as dt
import os as _os
import keras.utils as image
import tensorflow as tf

class IOTModelGenerator(object):
    """description of class"""

    def __init__(self):
        print("Initial Model Generator")
        self._train_data = ""
        self._test_data = ""
        self._epoch = 10
        self._batchsize = 8
        self._activation = 'relu'
        self._neuron_level = [1000,1000,1000]
        self._model = ""
        self._plot_size = (8,8)

    def train(self):
        
        print('Start training model')
        get_first_column = dt.IOTDataStructure()
        get_first_column = self._train_data[0]

        input_size = len(get_first_column.variable_list)
        output_size = len(get_first_column.class_name_list)

        train_x, trian_y = self._get_data_format(self._train_data)
        test_x, test_y = self._get_data_format(self._test_data)

        self._model = Sequential()
        if len(self._neuron_level)>0:
            self._model.add(Dense(units = self._neuron_level[0],activation= self._activation,input_dim=input_size))
            for level_Index in range(1,len(self._neuron_level),1):
                self._model.add(Dense(units = self._neuron_level[level_Index],activation= self._activation))

            self._model.add(Dense(units = output_size,activation='softmax'))
        else:
            print('Linear Regression model')
            self._model.add(Dense(units = output_size,activation= 'softmax',input_dim=input_size))
        self._model.compile(loss='categorical_crossentropy', optimizer=SGD(lr=0.01, momentum=0.9, nesterov=True), metrics=['accuracy'])
        self._model.summary()#顯示目前建立的模型結構
        
        self._train_history = self._model.fit (train_x, trian_y,      #輸入 與 輸出
                                              epochs = self._epoch,       #子代數
                                             batch_size = self._batchsize,#批量大小 一次參考多少的數據 4=> 00 01 10 11一同參考
                                             verbose = 1 ,           #是否顯示訓練過程 1=>是  2=>否
                                             validation_data=(test_x, test_y))

        score = self._model.evaluate(train_x, trian_y)

        self._predict_data(self._train_data)
        self._predict_data(self._test_data)

        train_acc = score[1]
        print ('\nTrain Acc:', score[1])
        score = self._model.evaluate(test_x, test_y)
        test_acc = score[1]
        print ('\nTest Acc:', score[1])
        print('End training model')
        self._show_model_train_history()

    def _predict_data(self, input_data):
        if self._model != "":
            convert_test_x, convert_test_y = self._get_data_format(input_data)
            test_predict_result = self._model.predict(convert_test_x)
            for index in range(0,len(test_predict_result),1):
                input_data[index].set_predict_label(self._probabilityToClass(test_predict_result[index]))
        else:
            print('predict model fail')

    def _probabilityToClass(self, proabilitysList):

        max_index = 0
        probability = 0
        for index in range(0, len(proabilitysList),1):
            if proabilitysList[index] > probability:
                max_index = index
                probability = proabilitysList[index]

        return max_index


    def evaluate(self, evaluate_data):
        print('start evaluating model')
        self._predict_data(evaluate_data)

        correctCount = 0
        total = len(evaluate_data)

        for data in evaluate_data:
            if data.predict_label == data.true_label:
                correctCount = correctCount + 1

        print('Acc:' + (str)(format((correctCount/total * 100), '.2f')) + " %")
        print('end evaluating model')

    def infer(self, variable):

        train_data_len = len(self._train_data[0].variables)
        input_data_len = len(variable)

        if train_data_len != input_data_len:
            print('This model needs '+ str(len(self._train_data[0].variables)) + ' variables')
            if train_data_len > input_data_len:
                print('But you only give '+ str(input_data_len) + ' variables')
            else:
                print('But you give '+ str(input_data_len) + ' variables')
            return

        newData = dt.IOTDataStructure()

        newData.set_class_name_list(self._train_data[0].class_name_list)
        newData.set_variable(variable)
        newData.set_true_label(0)

        dataList = []
        dataList.append(newData)
        self._predict_data(dataList)
        print('Predict => ' + str(newData.predict_label))

    def save_model(self, path, file_name):
        print('start to save model')
        if not _os.path.exists(path):
            _os.mkdir(path)
        self._model.save(path + '//' + file_name + '.h5')
        print('End to save model')

    def load_model(self, model_path):
        print('start to load model')
        
        isFinishLoadModel = False;

        if _os.path.exists(model_path):
            try:
                self._model = keras.models.load_model(model_path)
                isFinishLoadModel = True
            except:
                isFinishLoadModel = False

        if(isFinishLoadModel):
            print('Load Model Finished')
        else:
            print('Load Model Fail')

    def _get_data_format(self, input_data_list):

        data_variables = []
        data_classes = []

        for single_data in input_data_list:
            data_classes.append(single_data.true_label)
            data_variables.append(single_data.variables)

        return (np.array(data_variables)).astype('float32'), to_categorical(np.array(data_classes))

    def _show_model_train_history(self):
        print('Show Training History')
        plt.figure(figsize=(8,6))
        plt.rcParams['axes.titlesize'] = 16
        plt.rcParams['axes.labelsize'] = 14
        plt.rcParams['xtick.labelsize'] = 12
        plt.rcParams['ytick.labelsize'] = 12
        plt.rcParams['legend.fontsize'] = 12

        plt.subplot(211)
        plt.plot(self._train_history.history['accuracy'])
        plt.plot(self._train_history.history['val_accuracy'])
        plt.axis([0,self.epoch,0,1])
        plt.title('Training History')
        plt.ylabel('Accuracy')
        plt.legend(['train_acc', 'test_acc'], loc='lower right')

        plt.subplot(212)
        plt.plot(self._train_history.history['loss'])
        plt.plot(self._train_history.history['val_loss'])
        plt.ylim(bottom=0)
        plt.xlim(left=0,right=self.epoch)
        plt.ylabel('Loss')
        plt.xlabel('Epoch')
        plt.legend(['train_loss', 'test_loss'], loc='upper right')
        plt.show()


    #region Property 
    @property
    def train_data(self):
        return self._train_data

    def set_train_data(self, train_data):
        self._train_data = train_data

    @property
    def test_data(self):
        return self._test_data

    def set_test_data(self, test_data):
        self._test_data = test_data

    @property
    def epoch(self):
        return self._epoch

    def set_epoch(self, epoch):
        if epoch > 10000:
            print('Epoch Limit <= 10000')
            self._epoch = 10000
        elif epoch < 0:
            print('Epoch Limit > 0')
            self._epoch = 1
        else:
            self._epoch = epoch

    @property
    def batchsize(self):
        return self._batchsize

    def set_batchsize(self, batchsize):
        
        if batchsize > 16:
            print('Batchsize Limit <= 16')
            self._batchsize = 16
        elif batchsize < 0:
            print('Batchsize Limit > 0')
            self._batchsize = 1
        else:
            self._batchsize = batchsize

    @property
    def activation(self):
        return self._activation

    def set_activation(self, activation):

        if((activation != 'relu') and (activation != 'sigmoid') and (activation != 'tanh') ):
            print('There is no activation call : ' + activation)
        else:
            self._activation = activation

    @property
    def neuron_level(self):
        return self._neuron_level

    def set_neuron_level(self, neuron_level):
        
        length = len(neuron_level)
        if length > 10000:
            print('Neuron_level Limit <= 10000')
            print('Set Error')
        else:
           self._neuron_level = neuron_level

    #endregion Property

class IOTCNNModelGenerator(object):
    
    def __init__(self):
        print("Initial CNNModel Generator")
        self._layers = []
        self._train_data = []
        self._test_data = []
        self._batchsize = 8
        self._model = ""
        self._height = 128
        self._width = 128
        self._train_onehot = {}

    @property
    def train_data(self):
        return self._train_data

    def set_train_data(self, train_data):
        self._train_data = train_data

    @property
    def test_data(self):
        return self._test_data

    def set_test_data(self, test_data):
        self._test_data = test_data

    @property
    def batchsize(self):
        return self._batchsize

    def set_batchsize(self, batchsize):
        
        if batchsize > 16:
            print('Batchsize Limit <= 16')
            self._batchsize = 16
        elif batchsize < 0:
            print('Batchsize Limit > 0')
            self._batchsize = 1
        else:
            self._batchsize = batchsize

    @property
    def height(self):
        return self._height

    def set_height(self, height = 128):
        self._height = height

    @property
    def width(self):
        return self._width

    def set_width(self, width = 128):
        self._width = width


    def add_convolution(self, neuron, matrix = (3,3), activation = 'relu'):
        print('Add Convolution')
        self._layers.append([neuron, matrix, activation])

    def add_pooling(self, matrix = (3,3)):
        print('Add Pooling')
        self._layers.append([matrix[0],matrix[1]])

    def add_flatten(self):
        print('Add flatten')
        self._layers.append("Flatten")

    def add_neuron(self, neuron = 10):
        print('Add neuron')
        self._layers.append(neuron)

    def train(self):
        print('Start Training')
        print('Loading datas')
        if len(self.train_data) == 0:
            return
        self._train_onehot = {}
        print('Check one hot')
        for image_data_index in range(0, len(self.train_data), 1):
            each_image_data = dt.IOTImageStructure()
            each_image_data = self.train_data[image_data_index]

            if not(each_image_data.output_name in self._train_onehot):
                self._train_onehot[each_image_data.output_name] = len(self._train_onehot)

        train_value, train_label = self._load_picture(self.train_data, 3, self._train_onehot)
        test_value, test_label = self._load_picture(self.test_data, 3, self._train_onehot)

        self._model = models.Sequential()
        self._model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(self.height, self.width, 3)))
        self._model.add(layers.MaxPooling2D((2, 2)))
        self._model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        self._model.add(layers.MaxPooling2D((2, 2)))
        self._model.add(layers.Conv2D(64, (3, 3), activation='relu'))

        self._model.add(layers.Flatten())
        self._model.add(layers.Dense(64, activation='relu'))
        self._model.add(layers.Dense(100))

        self._model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

        self._model.summary()

        history = self._model.fit(train_value, train_label, epochs=20, 
                            validation_data=(test_value, test_label))
        #for each_layer in self._layers:
        #    if type(each_layer) == int:
        #        self._model.add(layers.Dense(each_layer))
        #    elif type(each_layer) == str:
        #        self._model.add(layers.Flatten())
        #    else:
        #        print()
        print('Train Finished')
        input()

    def evaluate(self):
        print()

    def infer(self):
        print()

    def load_model(self):
        print()

    def save_model(self):
        print()

    def show_model(self):
        print()
        
    def _load_picture(self, data_path_list, color, one_hot):

        images = []
        labels = []

        color_style = 'grayscale'
        if color == 3 :
            color_style = 'rgb'

        
        for image_data_index in range(0, len(data_path_list), 1):
            each_image_data = dt.IOTImageStructure()
            each_image_data = data_path_list[image_data_index]

            img = image.load_img(each_image_data.path, color_mode = color_style, # use keras.preprocessing.image
                                    target_size = (self.height, self.width, color))
            img_array = image.img_to_array(img) # set image to array format
            images.append(img_array) # "append" to reshape and update
    
            labels.append(one_hot[each_image_data.output_name])
        
        data = np.array(images) # saving images
        labels = np.array(labels) # saving labels
        
        return data, labels