import os
import tensorflow as tf
import datetime
import tensorflow.keras.layers as layers
import tensorflow.keras.activations as activations
import tensorflow.keras.losses as losses
import tensorflow.keras as keras
import tensorflow.keras.optimizers as optimizers
from dataset_processing import FILE_NAMES
import splitter as splitter
import word_embedding.word2vec2flow as w2f
import tensorboarder as tb

MODELS_PATH = os.path.abspath(
    __file__ + f"/../../output/models")

SESSION_ID = datetime.datetime.now().strftime("%d%m%Y-%H%M")

checkpoint_path = f"{MODELS_PATH}/{SESSION_ID}/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

word2vec2_model = 'full_700_iter100_win7_8.model'
model_name = word2vec2_model.replace('.model', '')
model_path = f"{MODELS_PATH}/{model_name}.h5"

cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)


class Callbacks(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('val_loss') < 0.2):
            print("\nTraining val. loss reached 0.2. Stoped!")
            self.model.stop_training = True


epoch_callbacks = Callbacks()

EMBEDDING_DIMS = 700
NUM_LSTM_UNITS = 512
NUM_UNITS = 256
DROPOUT = 0.2
OUTPUT = len(FILE_NAMES)
LEARNING_RATE = 0.0001
OPTIMIZER = optimizers.Adamax(learning_rate=LEARNING_RATE)
EPOCHS = 30

embedding_matrix = w2f.embedding_matrix(word2vec2_model)

model = keras.Sequential([
    layers.Embedding(len(embedding_matrix), EMBEDDING_DIMS, weights=[
                     embedding_matrix], trainable=False),
    layers.Bidirectional(layers.LSTM(
        NUM_LSTM_UNITS, return_sequences=True)),
    layers.Dropout(DROPOUT),
    layers.Bidirectional(layers.LSTM(
        NUM_LSTM_UNITS, return_sequences=True)),
    layers.Dropout(DROPOUT),
    layers.Bidirectional(layers.LSTM(NUM_LSTM_UNITS)),
    layers.Dropout(DROPOUT),
    layers.Dense(NUM_UNITS, activation=activations.relu),
    layers.Dense(NUM_UNITS, activation=activations.relu),
    layers.Dense(OUTPUT)
])
# 'SparseCategoricalCrossentropy' is used because every sample belongs to one class only
model.compile(optimizer=OPTIMIZER, loss=losses.SparseCategoricalCrossentropy(
    from_logits=True), metrics=['accuracy'])
model.summary()

model.fit(splitter.train_data, epochs=EPOCHS, validation_data=splitter.validation_data,
          callbacks=[epoch_callbacks, cp_callback, tb.tensorboard_callback])

model.save(model_path)
