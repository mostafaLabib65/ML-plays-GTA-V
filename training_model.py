import numpy as np
from alexNet import alexnet


WEIDTH = 80
HIGHT = 60
LR = 1e-3
EPOCHS = 8
MODEL_NAME = 'pygta5-car-{}-{}-{}-epochs.model'.format(LR, 'alexnet', EPOCHS)

model = alexnet(WEIDTH, HIGHT, LR)

trainData = np.load('training_data.npy')
train = trainData[:-500]
test = trainData[-500:]

X = np.array([i[0] for i in train]).reshape(-1, WEIDTH, HIGHT, 1)
Y = [i[1] for i in train]

X_test = np.array([i[0] for i in test]).reshape(-1, WEIDTH, HIGHT, 1)
Y_test = [i[1] for i in test]

model.fit({'input': X}, {'targets': Y}, n_epoch=EPOCHS,
          validation_set=({'input': X_test}, {'targets': Y_test}), snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

model.save(MODEL_NAME)