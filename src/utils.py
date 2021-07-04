import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def get_pre(train_images,test_images):
	train_images = train_images / 255.0
	test_images = test_images / 255.0
	print('okie')
	return(train_images,test_images)
