import IPython
import datetime
import os
import kerastuner as kt
from tensorflow import keras
import tensorflow.keras.layers as layers
from encoder import encoder
from dataset_processing import FILE_NAMES
import splitter

SESSION_ID = datetime.datetime.now().strftime("%d%m%Y-%H%M")

PATH = os.path.abspath(
    __file__ + f"/../../output/hp_tuning/")


def model_builder(hp):
    hp_units = hp.Int('units', min_value=128, max_value=256, step=64)
    hp_lstm_units = hp.Int('lstm_units', min_value=256,
                           max_value=512, step=64)
    hp_embedding_dims = hp.Choice('embedding_dims', values=[700])
    hp_dropout = hp.Choice('dropout', values=[0.0, 0.1, 0.2])
    hp_learning_rate = hp.Choice('learning_rate', values=[0.01, 0.001])

    hypermodel = keras.Sequential([
        layers.Embedding(encoder.vocab_size, hp_embedding_dims),
        layers.Bidirectional(layers.LSTM(
            hp_lstm_units, return_sequences=True)),
        layers.Dropout(hp_dropout),
        layers.Bidirectional(layers.LSTM(
            hp_lstm_units, return_sequences=True)),
        layers.Dropout(hp_dropout),
        layers.Bidirectional(layers.LSTM(hp_lstm_units)),
        layers.Dropout(hp_dropout),
        layers.Dense(hp_units, activation=keras.activations.relu),
        layers.Dense(hp_units, activation=keras.activations.relu),
        layers.Dense(len(FILE_NAMES))
    ])
    hypermodel.compile(optimizer=keras.optimizers.Adamax(learning_rate=hp_learning_rate),
                       loss=keras.losses.SparseCategoricalCrossentropy(
        from_logits=True),
        metrics=['accuracy'])

    return hypermodel


class ClearTrainingOutput(keras.callbacks.Callback):
    def on_train_end(self, *args, **kwargs):
        IPython.display.clear_output(wait=True)


tuner = kt.Hyperband(model_builder,
                     objective='val_accuracy',
                     max_epochs=2,
                     factor=3,
                     directory=PATH,
                     project_name={SESSION_ID},
                     overwrite=True)

tuner.search(splitter.train_data, epochs=1,
             validation_data=splitter.validation_data, callbacks=[ClearTrainingOutput()])

best_hps = tuner.get_best_hyperparameters(1)[0]

print(f"""
Optimal values:
- number of units in densely-connected layers {best_hps.get('units')}
- number of units in lstm {best_hps.get('lstm_units')}
- embedding dim {best_hps.get('embedding_dims')} 
- learning rate {best_hps.get('learning_rate')}
- dropout rate {best_hps.get('dropout')}
""")
