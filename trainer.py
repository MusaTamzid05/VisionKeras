from keras import layers
from keras import models
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator


class Trainer:

    def __init__(self , **kwargs):

        self.train_dir = kwargs["train_dir"]
        self.test_dir = kwargs["test_dir"]
        self.validation_dir = kwargs["validation_dir"]
        self.epochs = kwargs["epochs"]
        self.batch_size = kwargs["batch_size"]
        self.validation_step = kwargs["validation_step"]



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

        history = self.model.fit_generator(
                self.train_generator ,
                steps_per_epoch = self.epochs ,
                epochs = self.epochs ,
                validation_data = self.validation_generator ,
                validation_steps = self.validation_step
                )

        if model_name == "":
            model_name = "training_model"

        model_name += ".h5"

        self.model.save(model_name)



