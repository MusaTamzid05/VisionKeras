from keras import layers
from keras import models
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import image
import numpy as np
import os

class Trainer:

    def __init__(self ,
            train_dir = "./train_dir",
            test_dir = "./test_dir",
            validation_dir = "./validation_dir",
            epochs = 30,
            batch_size = 20,
            validation_step = 50):

        self.train_dir = train_dir
        self.test_dir = test_dir
        self.validation_dir = validation_dir
        self.epochs = epochs
        self.batch_size = batch_size
        self.validation_step = validation_step



    def _init_model(self):

        self.model = models.Sequential()

        self.model.add(layers.Conv2D(32 , (3 , 3) , activation = "relu" , input_shape = ( 150 , 150 , 3 )))
        self.model.add(layers.MaxPooling2D((2 , 2)))


        self.model.add(layers.Conv2D(64, (3 , 3) , activation = "relu" ))
        self.model.add(layers.MaxPooling2D((2 , 2)))


        self.model.add(layers.Conv2D(128 , (3 , 3) , activation = "relu" ))
        self.model.add(layers.MaxPooling2D((2 , 2)))


        self.model.add(layers.Conv2D(128 , (3 , 3) , activation = "relu" ))
        self.model.add(layers.MaxPooling2D((2 , 2)))

        self.model.add(layers.Flatten())
        self.model.add(layers.Dense(512 , activation = "relu"))
        self.model.add(layers.Dense(1 , activation = "sigmoid"))

        self.model.summary()
        self.model.compile(loss = "binary_crossentropy" ,
                optimizer = optimizers.RMSprop(lr = 1e-4) ,
                metrics = ["acc"])


    def _init_data(self):

        train_datagen = ImageDataGenerator(
                rescale = 1. / 255 ,
                rotation_range = 40 ,
                width_shift_range = 0.2 ,
                height_shift_range = 0.2 ,
                shear_range = 0.2 ,
                zoom_range = 0.2 ,
                horizontal_flip = True
                )

        test_datagen = ImageDataGenerator(rescale = 1. / 255)


        self.train_generator = train_datagen.flow_from_directory(
                self.train_dir,
                target_size = (150 , 150),
                batch_size = self.batch_size,
                class_mode = "binary"
                )


        self.validation_generator = test_datagen.flow_from_directory(
                self.validation_dir,
                target_size = (150 , 150),
                batch_size = self.batch_size,
                class_mode = "binary"
                )

    def train(self , model_name = ""):

        self._init_model()
        self._init_data()

        if model_name == "":
            model_name = "training_model"

        model_name += ".h5"

        self.model.save(model_name)

    def predict(self , image_path):


        if os.path.isfile(image_path) == False:
            print("{} does not exists!!".format(image_path))
            return

        img = image.load_img(image_path , target_size = (150 , 150))
        img = image.img_to_array(img)
        image_tensor = np.expand_dims(img, axis = 0)
        image_tensor /= 255

        return self.model.predict_classes(image_tensor)

    def load_model(self , model_name):
        self.model = models.load_model(model_name)



def main():
    trainer = Trainer()
    trainer.load_model("training_model.h5")
    files = os.listdir("./validation/cat")

    for current_file in files:
        print(current_file)
        print(trainer.predict("./validation/cat/{}".format(current_file)))

if __name__ == "__main__":
    main()
