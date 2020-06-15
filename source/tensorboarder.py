import tensorboard
import datetime
import os
import tensorflow as tf
import tensorflow.keras.callbacks as callbacks
from tensorflow.python.keras.callbacks import TensorBoard

LOG_PATH = os.path.abspath(
    __file__ + f"/../../output/logs")

log_dir = os.path.join(
    LOG_PATH, datetime.datetime.now().strftime("%d.%m.%Y - %H:%M:%S"))

tensorboard_callback = callbacks.TensorBoard(
    log_dir=log_dir, histogram_freq=1)
