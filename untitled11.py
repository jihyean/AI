import numpy as np
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.layers import Input, Activation, Dense, Flatten, Reshape, Conv2D, Dropout, BatchNormalization, UpSampling2D
from tensorflow.keras.models import Model
import matplotlib.pyplot as plt



(x_train, y_train),(x_test,y_test)=fashion_mnist.load_data()
x_train = x_train[np.isin(y_train,[9])]
x_train = (x_train.astype('float32')/255.0)*2.0-1.0
x_test = (x_train.astype('float32')/255.0)*2.0-1.0
x_train = np.reshape(x_train, (len(x_train), 28, 28, 1))
x_test = np.reshape(x_test, (len(x_test), 28, 28, 1))

batch_siz = 64
epochs = 5000
dropout_rate=0.4
batch_norm=0.9
zdim=100

discriminator_input=Input(shape=(28,28,1))
x=Conv2D(64,(5,5),activation='relu',padding='same',strides=(2,2))(discriminator_input)
x=Dropout(dropout_rate)(x)
x=Conv2D(64,(5,5),activation='relu',padding='same',strides=(2,2))(x)
x=Dropout(dropout_rate)(x)
x=Conv2D(128,(5,5),activation='relu',padding='same',strides=(2,2))(x)
x=Dropout(dropout_rate)(x)
x=Conv2D(128,(5,5),activation='relu',padding='same',strides=(1,1))(x)
x=Dropout(dropout_rate)(x)
x=Flatten()(x)
discriminator_ouput=Dense(1, activation='sigmoid')(x)
discriminator= Model(discriminator_input, discriminator_ouput)

generator_input = Input(shape=(zdim,))
x=Dense(3136)(generator_input)
x=BatchNormalization(momentum=batch_norm)(x)
x=Activation('relu')(x)
x=Reshape((7,7,64))(x)
x=UpSampling2D()(x)
x=Conv2D(128,(5,5),padding='same')(x)
x=BatchNormalization(momentum=batch_norm)(x)
x=Activation('relu')(x)
x=UpSampling2D()(x)
x=Conv2D(64,(5,5),padding='same')(x)
x=BatchNormalization(momentum=batch_norm)(x)
x=Activation('relu')(x)
x=Conv2D(64,(5,5),padding='same')(x)
x=BatchNormalization(momentum=batch_norm)(x)
x=Activation('relu')(x)
x=Conv2D(1,(5,5),activation='tanh',padding='same')(x)
generator_output=x
generator= Model(generator_input, generator_output)

discriminator.compile(optimizer='Adam', loss='binary_crossentropy', metrics=['accuracy'])

discriminator.trainable=False
gan_input = Input(shape=(zdim,))
gan_output = discriminator(generator(gan_input))
gan = Model(gan_input, gan_output)
gan.compile(optimizer='Adam', loss='binary_crossentropy', metrics=['accuracy'])

def train_discriminator(x_train):
    c= np.random.randint(0,x_train.shape[0],batch_siz)
    real=x_train[c]
    discriminator.train_on_batch(real,np.ones((batch_siz,1)))
    
    p=np.random.normal(0,1,(batch_siz,zdim))
    fake=generator.predict(p)
    discriminator.train_on_batch(fake,np.zeros((batch_siz,1)))

def train_generator():
    p=np.random.normal(0,1,(batch_siz,zdim))
    gan.train_on_batch(p,np.ones((batch_siz,1)))

for i in range(epochs+1):
    train_discriminator(x_train)
    train_generator()
    if(i%100==0):
        plt.figure(figsize=(20,4))
        plt.suptitle('epoch'+str(i)+'_2270005_kjh')
        for k in range(20):
            plt.subplot(2,10,k+1)
            img=generator.predict(np.random.normal(0,1,(1,zdim)))
            plt.imshow(img[0].reshape(28,28),cmap='gray')
            plt.xticks([]); plt.yticks([])
        plt.show()

imgs = generator.predict(np.random.normal(0,1,(50,zdim)))
plt.figure(figsize=(20,10))
for i in range(50):
    plt.subplot(5,10,i+1)
    plt.imshow(img[i].reshape(28,28),cmap='gray')
    plt.xticks([]); plt.yticks([]) 

# 훈련 집합
def most_similar(img, xtrain):
    vmin = 1.0e10
    for i in range(len(x_train)):
        dist = np.mean(np.abs(img-x_train[i]))
        if dist<vmin:
            imin,vmin=i,dist
    return x_train[imin]

# 50개의 영상에 대해 가장 가까운
plt.figure(figsize=(20,10))
for k in range(50):
    plt.subplot(5,10,k+1)
    plt.imshow(most_similar(imgs[k], x_train).reshape(28,28),cmap='gray')
    plt.xticks([]); plt.yticks([]) 
plt.show()