from encoder import encoded_dataset
from dataset_processing import BUFFER_SIZE
import pandas as pd
import numpy as np


VALIDATION_TAKE_SIZE = 2000
BATCH_SIZE = 40

# for the 'train_data' we take the 'all_encoded_data' and skip some for testing
train_data = encoded_dataset.skip(VALIDATION_TAKE_SIZE)
train_data = train_data.shuffle(BUFFER_SIZE)

# Batching and padding
train_data = train_data.padded_batch(BATCH_SIZE, padded_shapes=((None,), ()))

# for 'test_data' the once which where skipped by the 'train_data' are used
validation_data = encoded_dataset.take(VALIDATION_TAKE_SIZE)
validation_data = validation_data.shuffle(BUFFER_SIZE)

# Batching and padding
validation_data = validation_data.padded_batch(
    BATCH_SIZE, padded_shapes=((None,), ()))

for batch, clasifier in train_data.take(1):
    print(clasifier)
    print(batch)
