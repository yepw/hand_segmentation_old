import numpy as np

# DATASET PARAMETERS
TRAIN_DIR = './datasets/GTEA'
VAL_DIR = './datasets/GTEA'
TRAIN_LIST = ['./data/train.gtea'] * 3
VAL_LIST = ['./data/val.gtea'] * 3
SHORTER_SIDE = [350] * 3
CROP_SIZE = [500] * 3
'''
NORMALISE_PARAMS = [1./255, # SCALE
                    np.array([0.485, 0.456, 0.406]).reshape((1, 1, 3)), # MEAN
                    np.array([0.229, 0.224, 0.225]).reshape((1, 1, 3))] # STD
'''
NORMALISE_PARAMS = [1./255, # SCALE
                    np.array([0.55392909, 0.42849693, 0.1799708 ]).reshape((1, 1, 3)), # MEAN
                    np.array([0.1360823,  0.14253329, 0.12259706]).reshape((1, 1, 3))] # STD
BATCH_SIZE = [6] * 3
NUM_WORKERS = 16
NUM_CLASSES = [2] * 3
# NUM_CLASSES = [40] * 3
LOW_SCALE = [0.5] * 3
HIGH_SCALE = [2.0] * 3
IGNORE_LABEL = 0

# ENCODER PARAMETERS
ENC = '50'
ENC_PRETRAINED = True  # pre-trained on ImageNet or randomly initialised

# GENERAL
EVALUATE = False
FREEZE_BN = [True] * 3
NUM_SEGM_EPOCHS = [20] * 3
PRINT_EVERY = 10
RANDOM_SEED = 42
SNAPSHOT_DIR = './ckpt/'
CKPT_PATH = './ckpt/checkpoint.pth.tar'
VAL_EVERY = [5] * 3 # how often to record validation scores

# OPTIMISERS' PARAMETERS
LR_ENC = [5e-4, 2.5e-4, 1e-4]  # TO FREEZE, PUT 0
LR_DEC = [5e-3, 2.5e-3, 1e-3]
MOM_ENC = [0.9] * 3 # TO FREEZE, PUT 0
MOM_DEC = [0.9] * 3
WD_ENC = [1e-5] * 3 # TO FREEZE, PUT 0
WD_DEC = [1e-5] * 3
OPTIM_DEC = 'sgd'
