import os


class Settings:
    PPATH = os.getcwd()
    print(PPATH)
    TARGET_SIZE = (224, 224)
    EPOCHS = 30
    MODEL_PATH_INCEPTION = PPATH+'/src/models/inception_model.h5'
    MODEL_PATH_VGG = PPATH+'/src/models/vgg16_model.h5'
