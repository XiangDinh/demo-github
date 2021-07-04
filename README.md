## demo-github
Tạo dự án trên github và quản lý dự án
## Instalation
Create virtual environment
```bash
conda create -n myenv python=3.7
conda activate myenv
```

Install dependencies:
```bash
pip install -r requirements.txt
```
### Usage
Run 
```bash
python train.py
```
Expected Output:
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
flatten (Flatten)            (None, 784)               0
_________________________________________________________________
dense (Dense)                (None, 128)               100480
_________________________________________________________________
dense_1 (Dense)              (None, 10)                1290
=================================================================
Total params: 101,770
Trainable params: 101,770
Non-trainable params: 0
_________________________________________________________________
```
```
Epoch 1/10
1875/1875 [==============================] - 2s 713us/step - loss: 0.5006 - accuracy: 0.8234
Epoch 2/10
1875/1875 [==============================] - 1s 729us/step - loss: 0.3755 - accuracy: 0.8645
Epoch 3/10
1875/1875 [==============================] - 1s 695us/step - loss: 0.3367 - accuracy: 0.8773
Epoch 4/10
1875/1875 [==============================] - 1s 663us/step - loss: 0.3132 - accuracy: 0.8856
Epoch 5/10
1875/1875 [==============================] - 1s 696us/step - loss: 0.2931 - accuracy: 0.8913
Epoch 6/10
1875/1875 [==============================] - 1s 727us/step - loss: 0.2834 - accuracy: 0.8943
Epoch 7/10
1875/1875 [==============================] - 1s 700us/step - loss: 0.2697 - accuracy: 0.8998
Epoch 8/10
1875/1875 [==============================] - 1s 693us/step - loss: 0.2592 - accuracy: 0.9024
Epoch 9/10
1875/1875 [==============================] - 1s 708us/step - loss: 0.2503 - accuracy: 0.9065
Epoch 10/10
1875/1875 [==============================] - 1s 728us/step - loss: 0.2405 - accuracy: 0.9106
```
### Test
Run 
```bash
python test.py
```
Test accuracy: 0.8787999749183655

Test loss: 0.3333036005496979
```


