from outer import *


class BluePrintSample:
    def __init__(self, key='1'):
        self.ROOT = Dir(f'log{key}')
        # define file or dir
        self.LOG_MAIN = self.ROOT.sub_file('run.log')
        self.LOG_TENSORBOARD = self.ROOT.sub_dir('event')
        self.FILE_CHECKPOINT = self.ROOT.sub_file('model.pkl')

        self.TRAIN_DIR = self.ROOT.sub_dir('train')
        self.TRAIN_IMG_OUTPUT = self.TRAIN_DIR.sub_dir('image')
        self.TRAIN_LABEL_OUTPUT = self.TRAIN_DIR.sub_dir('label')
        self.TRAIN_GT_OUTPUT = self.TRAIN_DIR.sub_dir('gt')


if __name__ == '__main__':
    blue_print = BluePrintSample()
    print(blue_print.LOG_TENSORBOARD)
    print(blue_print.TRAIN_GT_OUTPUT)