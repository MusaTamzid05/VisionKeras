
Please read the chapter 5 of "Deep Learning with Python" by Francois Chollet.I wrote this code reading that book.

Suppose you have a folder name "data" which contains all the images.data folder must images with their respective lebel name.
Suppose data folder has images of cats name cat1.jpg , cat2.jpg and so on.It also has images names dog1.jpg , dog2.jpg and so on..
to prepare data , need to run python data_prepare.py -data data_dir -label1 label1_name  -label2 label2_name

run python data_prepare.py -data data -label1 cat -label2 dog
This will create train , test and validation dir.

to train , run python main.py -train train_dir -test test_dir -validation validation_dir

this create a .h5 file.

TODO:
  Need to plot training vs validation accuracy and loss.

PS : Plan to add a yaml file so that we can change parameters of the model in the future.


