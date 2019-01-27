import argparse
import os
import sys
from images_helper import get_size


def dir_check(train_dir , test_dir , validation_dir):

    if os.path.isdir(train_dir) == False:

        print("Train directory does not exits!!")
        sys.exit(1)


    if os.path.isdir(test_dir) == False:

        print("Test directory does not exits!!")
        sys.exit(1)


    if os.path.isdir(validation_dir) == False:

        print("Validation directory does not exits!!")
        sys.exit(1)

def main():

    parser = argparse.ArgumentParser(description = "Train from images.")
    parser.add_argument("-train" , required = True , dest = "train_dir")
    parser.add_argument("-test" , required = True , dest = "test_dir")
    parser.add_argument("-validation" , required = True , dest = "validation_dir")

    args = parser.parse_args()
    train_dir = args.train_dir
    test_dir = args.test_dir
    validation_dir = args.validation_dir


    dir_check(train_dir , test_dir , validation_dir)





if __name__ == "__main__":
    main()
