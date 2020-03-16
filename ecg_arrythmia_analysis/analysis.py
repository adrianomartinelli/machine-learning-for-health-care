#%%

from ecg_arrythmia_analysis.code.dataloader import *
from ecg_arrythmia_analysis.code.architectures import *
from ecg_arrythmia_analysis.code.visualization import *
from ecg_arrythmia_analysis.code.functions import *
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from sklearn.metrics import f1_score, accuracy_score

#%%

MODEL_PATH = 'models/'
DATA_PATH = 'data/'

MODEL_DICT = {'cnn': CNNmodel, 'rcnn': RCNNmodel, 'rnn': RNNmodel, 'ensemble': Ensemble_FFL_block}
# %%
CNN_SPECS = (4, [5, 3, 3, 3], [16, 32, 32, 256], 1)
RCNN_SPECS = (4, 3, [3, 12, 48, 192], 2, 1)
RNN_SPECS = (2, False, 3, 16, 256, 'LSTM', 2, 1)
ENSEMBLE_SPECS = (3, 64, 1)
SPEC_LIST = {'cnn': CNN_SPECS,
             'rcnn': RCNN_SPECS,
             'rnn': RNN_SPECS,
             'ensemble': ENSEMBLE_SPECS}

#%%

# VISUALIZATION
print("VISUALIZATION")

vis_data('mitbih', 5)



# Individual visualization mitbih
# Individual visualization ptbdb

# Global visualization mitbih
# Global visualization ptbdb

print("")
#%%

# Run Convolutional Networks
print("CONVOLUTIONAL NETWORKS")

# Run CNN on mitbih
# architect(mode='training', data='mitbih', type='cnn', run_id=100)
# architect('testing', 'mitbih', 'cnn', 100)

# Run CNN on ptbdb
# architect(mode='training', data='ptbdb', type='cnn', run_id=150)
# architect('testing', 'ptbdb', 'cnn', 150)

print("")
#%%

# Run Residual Networks
print("RESIDUAL CONVOLUTIONAL NETWORKS")

# Run RCNN on mitbih
# architect('training', 'mitbih', 'rcnn', 200)
# architect('testing', 'mitbih', 'rcnn', 200)

# Run RCNN on ptbdb
# architect('training', 'ptbdb', 'rcnn', 250)
# architect('testing', 'ptbdb', 'rcnn', 250)

print("")
#%%
# Run Recurrent Networks
print("RECURRENT NETWORKS")

# Run RNN on mitbih
# architect('training', 'mitbih', 'rnn', 300)
# architect('testing', 'mitbih', 'rnn', 300)

# Run RNN on ptbdb
# architect('training', 'ptbdb', 'rnn', 350)
# architect('testing', 'ptbdb', 'rnn', 350)

print("")
#%%

# Run Ensemble of Networks
print("ENSEMBLE NETWORKS")

# define stacked model from multiple member input models
# architect('ensemble', 'mitbih', 'ensemble', 500, type_ids = [('rcnn', 200), ('cnn', 100)])
# architect('ensemble', 'mitbih', 'ensemble', 500, type_ids = [('rcnn', 200), ('cnn', 100)])

# Run RNN on ptbdb
# architect('ensemble', 'ptbdb', 'ensemble', 550, type_ids = [('rcnn', 250), ('cnn', 150)])
# architect('ensemble', 'ptbdb', 'ensemble', 550, type_ids = [('rcnn', 250), ('cnn', 150)])

print("")
#%%

# Use TFL
print("TRANSFER LEARNING")

# Pretraining on MIT

# Freeze RNN layers
# transfer_learning(data='mitbih', type_id=('cnn', 100), id=700)
# Train whole model
# transfer_learning(data='ptbdb', type_id=('cnn', 100), id=750)

print("")
#%%


#%%