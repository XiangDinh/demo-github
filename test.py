import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from src.dataset import get_dataset
from src.utils import get_pre
from src.model import get_model


(train_images,train_labels),(test_images,test_labels)=get_dataset()
(train_images,test_images)=get_pre(train_images,test_images)

model= keras.models.load_model('demo')
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\nTest accuracy:', test_acc)
print('\nTest loss:', test_loss)
