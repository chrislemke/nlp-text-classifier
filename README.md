<img src="https://github.com/stoffy/RUAK/blob/master/The_School_of_Athens.jpg" alt="The School of Athens">

# RUAK - Are you a Hegel?
### [Bertrand Russell](https://en.wikipedia.org/wiki/Bertrand_Russell)

Philosophy is a fundamental human thought movement. Everyone is a philosopher. The only question is what kind of philosopher you are. This project tries to answer that question.
Using natural language processing (NLP), texts of different authors are used for categorization.
With the help of these texts any sentence can be categorically determined.

### Project structure
The project is based on muliple layers for different tasks. Most of the code can be found in [classification notebook](https://github.com/stoffy/RUAK/blob/master/notebooks/philo_text_classification.ipynb). This contains:

1. Preparation / normalization
2. Dataset managment
3. Tokenization
4. Encoding
5. Splitting
6. Hyperparameter tuning
7. TensorBoard preparations
8. Model preparation
9. Model training
10. Loading Model
11. Saving Model
12. Evaluate
13. Tensorboard analysis

The [ruakspider](https://github.com/stoffy/RUAK/tree/master/ruakspider) folder contain all stuff needed for crawling over certain websites to get text als training data for the classification model and text for the [training of the Word2Vec embedding model](https://github.com/stoffy/RUAK/blob/master/notebooks/embeddings_trainer.ipynb).
