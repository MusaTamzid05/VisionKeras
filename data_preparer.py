import os


def create_dir_from(dst_dir , name):

    new_dir =  os.path.join(dst_dir , name)

    if os.path.isdir(new_dir):
        print("{} already exists!!.".format(new_dir))
        return

    print("Creating {}.".format(new_dir))
    os.mkdir(new_dir)
    return new_dir



def prepare_data( dst_dir , labels):

    if os.path.isdir(dst_dir) == False:

        print("Creating {}.".fotmat(dst_dir))
        os.mkdir(dst_dir)

    train_dir = create_dir_from(dst_dir , "train")
    validation_dir = create_dir_from(dst_dir , "validation")
    test_dir =  create_dir_from(dst_dir , "test")

    if train_dir == None:
        return

    for label in labels:

        create_dir_from(train_dir , label)
        create_dir_from(validation_dir, label)
        create_dir_from(test_dir, label)



def main():
    prepare_data(os.getcwd() , [ "Cats" , "Dogs" ])

if __name__ == "__main__":
    main()
