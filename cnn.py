from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing import image
from tensorflow import keras
import numpy as np

#from keras.layers import Dropout
classifier = Sequential()
# create neuronal network
def createCNN():

    classifier.add(Conv2D(32, (3, 3), activation = 'relu',
                        input_shape = (128, 128, 3)))

    classifier.add(MaxPooling2D(pool_size = (2,2)))

    classifier.add(Conv2D(64, (3, 3), activation='relu'))
    classifier.add(MaxPooling2D(pool_size = (2,2)))

    classifier.add(Conv2D(128, (3, 3), activation='relu'))
    classifier.add(MaxPooling2D((2, 2)))

    classifier.add(Conv2D(128, (3, 3), activation='relu'))
    classifier.add(MaxPooling2D((2, 2)))


    ## hiden layer
    classifier.add(Flatten())

    classifier.add(Dense(512, activation='relu'))

    classifier.add(Dense(512, activation='relu'))

    classifier.add(Dense(256, activation='relu'))

    classifier.add(Dense(3, activation='softmax'))
    #classifier.add(Dense(3, activation='sigmoid'))
    #classifier.add(Dense(3, activation='relu'))

    # Compile neuronal network
    classifier.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

# Training
def trainCNN():    
    ## get data
    from keras.preprocessing.image import ImageDataGenerator

    train_datagen = ImageDataGenerator(
            rescale=1./255,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True)

    test_datagen = ImageDataGenerator(rescale=1./255)

    batch_size = 6

    training_dataset = train_datagen.flow_from_directory(r'C:\Users\arnol\Desktop\Tesis\Code\training_set',
                                                        target_size=(128,128),
                                                        batch_size=batch_size,
                                                        class_mode='binary')

    testing_dataset = test_datagen.flow_from_directory(r'C:\Users\arnol\Desktop\Tesis\Code\test_set',
                                                    target_size=(128,128),
                                                    batch_size=batch_size,
                                                    class_mode='binary')

    classifier.fit(training_dataset,
                        steps_per_epoch=int(50/batch_size),
                        epochs=140,
                        validation_data=testing_dataset,
                        validation_steps=int(10/batch_size))
    classifier.save("my_model2")

# test
def test():
    import numpy as np
    from keras.preprocessing import image
    for x in range(18):
        path = r'C:\Users\arnol\Desktop\Tesis\Code\single_prediction\p'+str(x)+'.jpg'
        test_image = image.load_img(path, target_size = (128,128))
        
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = classifier.predict(test_image)
        print(result)
        break
    
def getPredictionCNN():
    classifier = keras.models.load_model("my_model2")
    path = 'img.jpg'
    test_image = image.load_img(path, target_size = (128,128))    
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = classifier.predict(test_image)
    print(result[0])
    return result[0]

#createCNN()
#trainCNN()