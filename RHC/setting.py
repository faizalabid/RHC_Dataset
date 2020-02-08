from easydict import EasyDict as edict

# init
__C_RHC = edict()

cfg_data = __C_RHC

__C_RHC.STD_SIZE = (360,640)
__C_RHC.TRAIN_SIZE = (360,640) # 2D tuple or 1D scalar
__C_RHC.DATA_PATH = '../ProcessedData/RHC'               

__C_RHC.MEAN_STD = ([0.410824894905, 0.370634973049, 0.359682112932], [0.278580576181, 0.26925137639, 0.27156367898])

__C_RHC.LABEL_FACTOR = 1
__C_RHC.LOG_PARA = 100.

__C_RHC.RESUME_MODEL = ''#model path
__C_RHC.TRAIN_BATCH_SIZE = 1 #imgs

__C_RHC.VAL_BATCH_SIZE = 1 # must be 1


