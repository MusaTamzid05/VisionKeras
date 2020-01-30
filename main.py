from vision_keras.pipeline  import Pipeline


def main():

    pipeline = Pipeline(
            image_data_dir = "./data"
            )
    pipeline.run()



if __name__ == "__main__":
    main()
