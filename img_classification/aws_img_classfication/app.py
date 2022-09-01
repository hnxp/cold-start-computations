from tensorflow.keras.models import load_model
import numpy as np
import tensorflow as tf
import tensorflow_datasets as tfds
import boto3
import os

s3 = boto3.client('s3')
bucket = 'python-package-bucket-ex1'
key = 'cifar10-model-v1.h5'

batch_size = 64

# CIFAR-10 classes
categories = {
    0: "airplane",
    1: "automobile",
    2: "bird",
    3: "cat",
    4: "deer",
    5: "dog",
    6: "frog",
    7: "horse",
    8: "ship",
    9: "truck"
}


def load_data():
    """
    This function loads CIFAR-10 dataset, and preprocess it
    """
    def preprocess_image(image, label):
        # convert [0, 255] range integers to [0, 1] range floats
        image = tf.image.convert_image_dtype(image, tf.float32)
        return image, label
    # loading the CIFAR-10 dataset, splitted between train and test sets
    ds_train, info = tfds.load(
        "cifar10", with_info=True, split="train[:1%]", as_supervised=True)
    ds_test = tfds.load("cifar10", split="test[:1%]", as_supervised=True)
    # repeat dataset forever, shuffle, preprocess, split by batch
    ds_train = ds_train.shuffle(1024).map(
        preprocess_image).batch(batch_size)
    ds_test = ds_test.shuffle(1024).map(preprocess_image).batch(batch_size)
    return ds_train, ds_test, info


def handler(event, context):
    ds_train, ds_test, info = load_data()
    path_to_file = '/tmp/model.h5'
    if (os.path.exists(path_to_file)):
        os.remove(path_to_file)

    s3.download_file(bucket, key, '/tmp/model.h5')

    # load the model with final model weights
    model = load_model('/tmp/model.h5')

    # evaluation
    loss, accuracy = model.evaluate(ds_train, steps=10)

    # get prediction for this image
    data_sample = next(iter(ds_test))
    sample_image = data_sample[0].numpy()[0]
    sample_label = categories[data_sample[1].numpy()[0]]

    prediction = np.argmax(model.predict(
        sample_image.reshape(-1, *sample_image.shape))[0])

    response = {
        "predicted label": categories[prediction],
        "true-label": sample_label,
        "accuracy": accuracy,
        "loss": loss
    }
    return response
