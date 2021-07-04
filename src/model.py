import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def get_model():
	model = tf.keras.Sequential([
    		tf.keras.layers.Flatten(input_shape=(28, 28)),
    		tf.keras.layers.Dense(128, activation='relu'),
    		tf.keras.layers.Dense(10)
	])	
	model.summary()
	print('okie')
	return model
