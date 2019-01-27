import os
import shutil
import sys
import argparse


def create_dir_from(dst_dir , name):

    new_dir =  os.path.join(dst_dir , name)

    if os.path.isdir(new_dir):
        print("{} already exists!!.".format(new_dir))
        return new_dir

    print("Creating {}.".format(new_dir))
    os.mkdir(new_dir)
    return new_dir


def get_files_with_name(path , name):

    files = os.listdir(path)
    dst_files = []

    for current_file in files:
        if current_file.startswith(name):
            dst_files.append(os.path.join(path , current_file))

    return dst_files


def prepare_data(data_dir , dst_dir , labels , train_percentise = 80):

    if os.path.isdir(dst_dir) == False:

        print("Creating {}.".fotmat(dst_dir))
        os.mkdir(dst_dir)

    train_dir = create_dir_from(dst_dir , "train")
    validation_dir = create_dir_from(dst_dir , "validation")
    test_dir =  create_dir_from(dst_dir , "test")



    for label in labels:

        label_train_dir = create_dir_from(train_dir , label)
        label_validation_dir = create_dir_from(validation_dir, label)
        label_test_dir = create_dir_from(test_dir, label)

        data_file = get_files_with_name(data_dir , label)
        train_size =  (train_percentise/ 100 ) * len(data_file)
        validation_size = 0.2 * train_size

        print("Total {} train data : {}".format(label , train_size))
        print("Total {} test data : {}".format(label , len(data_file) - train_size))
        print("Total {} validation data : {}".format(label , validation_size ))

        for i , src in enumerate(data_file):

            dst_image_name = src.split("/")[-1]

            if i < train_size:
                if i < validation_size:
                    dst_path = os.path.join(label_validation_dir, dst_image_name)
                else:
                    dst_path = os.path.join(label_train_dir , dst_image_name)
            else:
                dst_path = os.path.join(label_test_dir , dst_image_name)

            if os.path.isfile(dst_path):
                print("Error: The data file already exists.Aborting,Please remove the train , test , validation dir first")
                sys.exit(1)


            shutil.copyfile( src , dst_path )









def main():


    parser = argparse.ArgumentParser(description = "Prepares data ")
    parser.add_argument("-data" , required = True , dest = "data_dir")
    parser.add_argument("-label1" , required = True , dest = "label1")
    parser.add_argument("-label2" , required = True , dest = "label2")

    args = parser.parse_args()


    data_dir = args.data_dir
    label1 = args.label1
    label2 = args.label2

    if os.path.isdir(data_dir) == False:
        print("{} does not exists !!!".format(data_dir))
        sys.exit(1)

    current_dir = os.getcwd()



    prepare_data( data_dir , current_dir , [label1 , label2 ])

if __name__ == "__main__":
    main()
