import os
from shutil import copyfile

class ImageFileLabeler:
    '''
    image_dir_path: the path that has all the images.
    charecter_count: will create the labels from the
    given image file names.By default we will will
    take the first 4 character count
    '''
    def __init__(self , image_dir_path , character_count = 3):

        self.image_dir_path = image_dir_path
        self.character_count = character_count

        self._load_files()
        self.files = self._load_files()

    def _load_files(self):
        return  os.listdir(self.image_dir_path)


    def prepare(self , dst_dir):

        if os.path.exists(dst_dir) == False:
            os.makedirs(dst_dir)

        for current_file in self.files:
            current_label = current_file[0:self.character_count]
            current_dst_dir = os.path.join(dst_dir , current_label)

            if os.path.exists(current_dst_dir) == False:
                os.makedirs(current_dst_dir)

            src_path = os.path.join(self.image_dir_path , current_file)
            dst_path = os.path.join(current_dst_dir , current_file)
            print("{} => {}".format(src_path , dst_path))
            copyfile(src_path , dst_path)






def main():

    image_file_labeler = ImageFileLabeler(image_dir_path = "./data")
    image_file_labeler.prepare(dst_dir = "./label_data")

if __name__ == "__main__":
    main()
