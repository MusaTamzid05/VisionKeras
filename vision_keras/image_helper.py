from PIL import Image
import os

def get_size(image_path):

    img = Image.open(image_path)

    if img is None:
        raise FileNotFoundError("{} does not exits!!".format(image_path))

    return img.size

def get_label_image_size(train_dir):

    label_dir = os.listdir(train_dir)

    if len(label_dir) == 0:
        raise RuntimeError("There are no labels in train directory")

    label_path = os.path.join(train_dir , label_dir[0])
    train_images = os.listdir(label_path)


    if len(train_images) == 0:
        raise RuntimeError("There are no images in {} directory.".formar(label_path))
    image_path = os.path.join(label_path , train_images[0])

    return get_size(image_path)


def main():

    print(get_label_image_size("./train"))


if __name__ == "__main__":
    main()
