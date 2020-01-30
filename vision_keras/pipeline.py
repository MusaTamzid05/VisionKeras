import os
from vision_keras.data_preparer import prepare_data

class Pipeline:

    def __init__(self , image_data_dir):

        self.image_data_dir = image_data_dir

        if os.path.isdir(image_data_dir) == False:
            raise RuntimeError("data directory does not exists => {}".format(image_data_dir))

        self.image_data_dir = image_data_dir
        self.labels = os.listdir(self.image_data_dir)
        self.data_dir = "./prepare_data"

        self._init_data()


    def _init_data(self):

        prepare_data(data_dir = self.image_data_dir ,
                dst_dir = self.data_dir ,
                labels = self.labels)

    def run(self):
        pass








