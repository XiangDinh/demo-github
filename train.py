import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from src.dataset import get_dataset
from src.utils import get_pre
from src.model import get_model

(train_images,train_labels),(test_images,test_labels)=get_dataset()
(train_images,test_images)=get_pre(train_images,test_images)
model = get_model()

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=10)

model.save("demo")
