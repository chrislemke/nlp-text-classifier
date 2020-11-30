<h1>RUAK - Are you a Hegel? 🧐</h1>

<img src="https://github.com/stoffy/RUAK/blob/master/images/The_School_of_Athens.jpg" alt="The School of Athens"><br>
<i>The greatest challenge to any thinker is stating the problem in a way that will allow a solution.</i><br>
<a href="https://en.wikipedia.org/wiki/Bertrand_Russell">Bertrand Russell</a>

<h2>About this project</h2>
Philosophy is a fundamental human thought movement. Everyone is a philosopher. The only question is what kind of philosopher you are. This project tries to answer that question.<br><br>
Using natural language processing (NLP), texts of different authors are used for categorisation.
With the help of these texts any sentence can be categorically determined.
To understand how written language works and what the differences are between authors it helps to analyse the context of the sentences. Though visualisation it is simpler to see structural varieties such as average sentence length, word class ratio and the use of <a href="https://en.wikipedia.org/wiki/Stop_word">stop words</a>.

<h2>About the notebooks</h2>
<h3><u>text_classifier.ipynb</u></h3>
This notebook is the heart of the project. More details about this notebook and how to use it can be found in the introduction of it, right at the top of the notebook. 
You can open it in Google Colab to use a GPU and have a nice platform for editing. There you can run it out of the box. No setup needed!<br>
<a href="https://colab.research.google.com/github/stoffy/RUAK-text-classifier/blob/master/notebooks/text_classifier.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a><br>

<h4>Content</h4>
<ol>
	<li>Preparations</li>
	<li>Loading text data</li>
	<li>Collect and clean data</li>
	<li>Creating DataFrame and extract new data</li>
	<li>Store or load DataFrame</li>
	<li>Visualization of data</li>
	<li>Preparation, splitting and normalization</li>
	<li>Hyperparameter tuning</li>
	<li>Model preparation and training</li>
	<li>Save or load model</li>
	<li>Evaluation</li>
	<li>TensorBoard</li>
</ol>

<h4>Preparation & Loading text data</h4>
Those two part contains the imports, some additional downloads, the handling of the stop words, loading the text from the files provided, and the variables (paths, etc.) which must be set.
 

<h4>Collect data and create word collection</h4>
Here the texts are divided into individual sentences. The tokenizer of NLTK is responsible for this. In addition, the respective sentences are provided with a label. Afterwards sentences are removed, which are either too short or too long. The default values of minimum and maximum length are 6 and 400 words respectively.

<h4>Create and extend DataFrame</h4>
In this part the Pandas library becomes in handy. Its task is to create a data frame and create new columns out of the existing information:
<ul>
	<li><code>author</code> a more readable form of the <code>label</code></li>
	<li><code>word_count</code></li>
	<li><code>mean_word_length</code></li>
	<li><code>stop_words_ratio</code> The ratio of stop word to all words</li>
	<li><code>stop_words_count</code></li>
	<li>If POS tagging is activated another 16 columns are added:
		<ul>
		<li><code>ADJ_count</code> adjective count</li>
		<li><code>ADV_count</code> adverb count</li>
		<li><code>ADP_count</code> adposition count</li>
		<li><code>AUX_count</code> auxiliary count</li>
		<li><code>DET_count</code> determiner count</li>
		<li><code>NUM_count</code> numeral count</li>
		<li><code>X_count</code> other count</li>
		<li><code>INTJ_count</code> interjection count</li>
		<li><code>CONJ_count</code> conjunction count</li>
		<li><code>CCONJ_count</code> coordinating conjunction count</li>
		<li><code>SCONJ_count</code> subordinating conjunction count</li>
		<li><code>PROPN_count</code> proper noun count</li>
		<li><code>NOUN_count</code> noun count</li>
		<li><code>PRON_count</code> pronoun count</li>
		<li><code>PART_count</code> particle count</li>
		<li><code>VERB_count</code> verb count</li>
		</ul>
	For more information visit <a href="https://spacy.io/api/annotation">spacy's API documentation</a>.
	</li>
</ul> 

<h4>Store or load DataFrame</h4>
Since the process of creating the data frame can take quite a while. A data frame can be stored and loaded for later use.

<h4>Visualization of data</h4>
In this part it is all about visualizing the data so it can be understood easier. First the data is prepared for showing it using the Matplotlib library.
<br>

<h5><b>Data distribution</b></h5> 
Shows the shares of data for each author:<br>
Seems like Kant's share is too big 🤭.<br>
<img src="https://github.com/stoffy/RUAK-text-classifier/blob/master/images/data_distribution.png" alt="Data distribution">

and the distribution of word length by author:<br>
<img src="https://github.com/stoffy/RUAK-text-classifier/blob/master/images/word_length_distribution.png" alt="Word length distribution">

Distribution of sentence length by author:<br>
Why does Hume has so many sentences 🤔?<br>
<img src="https://github.com/stoffy/RUAK-text-classifier/blob/master/images/sentence_length_distribution.png" alt="Sentence length distribution">

<h5><b>Comparing authors</b></h5> 
Shows the differences between the authors for 4 metrics: <code>Number of sentences</code>, <code>Median sentence length</code>, <code>Unique vocabulary count</code>, <code>Median stop word ratio</code>.<br>Hume does not only has a lot sentences, but also very long onces 😯.<br><br>
<img src="https://github.com/stoffy/RUAK-text-classifier/blob/master/images/comparing_authors.png" alt="Comparing authors">

<h5><b>Word classes by authors</b></h5>
Presents the ratio of authors total used words to word classes:<br>
Plato's sentences seem different to the others. Probably because most of his texts are debates 🤓.
<img src="https://github.com/stoffy/RUAK-text-classifier/blob/master/images/word_classes_by_author.png" alt="Word classes by authors">

<h5><b>Common words</b></h5>
Gives an overview of the number of sentences containing one if the most 20 common words:<br>
I would have suspected 'reason' in one of the first places 🧐.<br>
<img src="https://github.com/stoffy/RUAK-text-classifier/blob/master/images/common_words.png" alt="Common words">

<h5><b>Sentence representation</b></h5>
To get understand the structures of the sentences you can visualize it:<br>
Classical <a href="https://en.wikisource.org/wiki/A_Dancing_Song_to_the_Mistral_Wind">Nietzsche</a> 😎<br>
<img src="https://github.com/stoffy/RUAK-text-classifier/blob/master/images/sentence.png" alt="Sentence representation">


<h4>Prepare and split</h4>
This step prepared the data for the Tensorflow model. To process the text data it needs to be tokenized and encoded. Keras preprocessing methods are used for this. <code>texts_to_sequences</code> encodes the text to a sequence of integers.<br>Each sequence is padded to the longest available sequence using <code>pad_sequences</code>.<br>
The collected metadata (e.g. number of stop words, etc.) gets normalized, not used columns get removed. And afterwards two data frames are concatenated. 
<br>Afterwards scikit-learn's <code>train_test_split</code> method is used to split the data.<br>
At the end two sets of train, validation and label arrays are created for hyperparameter seach and training the model. 


<h4>Hyperparameter tuning</h4>
Instead of manually searching for the best hyperparameter used by the model. In this project <a href="https://github.com/keras-team/keras-tuner">Keras Tuner</a> is used.<br>
There are two different ways to create the weights for the embedding layer. You may create your own Word2Vec model using the <a href="https://github.com/stoffy/RUAK-text-classifier/blob/master/notebooks/embeddings_trainer.ipynb"><code>embeddings_trainer.ipynb</code></a>. For the English language it is also possible to use the weights from the Word2Vec model provided by <a href="https://tfhub.dev/google/Wiki-words-500/2">Tensorflow Hub</a>.<br> 

At the beginning of the step the Word2Vec model is loaded which can be created <br> The <code>hypermodel</code> function contains the definition of the model and the ranges for tuning the hyperparameters. The following parameters can be tuned:
<ul>
<li><code>hp_dense_units</code> - Number of units in dense layers</li>
<li><code>hp_lstm_units</code> - Number of units in LSTM layers</li>
<li><code>hp_dropout</code> - Dropout rate</li>
<li><code>hp_learning_rate</code> - Learning rate parameter for the optimizer</li>
<li><code>hp_adam_epsilon</code> - Epsilon parameter for Adam</li>
</ul> 
Keras Hyperband uses the model to create a tuner - parameters:
<ul>
<li><code>executions_per_trial</code> - Number of models that should be built and fit for each trial for robustness purposes</li>
<li><code>max_epochs</code> - The maximal number of epochs. This number should be slightly bigger than the epochs for the fitting process</li>
<li><code>hyperband_iterations</code> - The number of times to iterate over the full Hyperband algorithm</li>
</ul>
The created tuner is then used to search for the best parameters which are returned by <code>get_best_hyperparameters</code>. A collection of the best models are returned by <code>get_best_models</code>.<br><br>
This image shows a possible model found by the Keras tuner search:<br>
<img src="https://github.com/stoffy/RUAK-text-classifier/blob/master/images/model.png" alt="Model structure"<br><br>
The Model contains two inputs. One is used for passing the encoded and padded sentences to the embedding layer. The other input handles the generated metadata. Later they get concatenated before the model ends with a Dense layer having the number of units equal to the classes available (authors). 


<h4>Model preparation and training</h4>
Using the fit method of the selected model - here it gets trained using the train and validation data. Three different callbacks are used: 
<ul>
<li><code>Tensorboard</code> - For collecting the data for presentation in TensorBoard</li>
<li><code>ReduceLROnPlateau</code> - Reduce learning rate when a metric has stopped improving</li>
<li><code>EarlyStopping</code> - Stops the training if no progress in learning</li>
</ul>

<h4>Save or load model</h4>
Here the model can be stored for later usage or loaded if it should be used in the next steps.

<h4>Evaluation</h4>
Draw charts to show compare training and validation results and try custom sentences to be classified by the trained model.

<h4>TensorBoard</h4>
Open Tensorboad to get an detailed overview of the training process.
<br>

<h3><u>embeddings_trainer.ipynb</u></h3>
The <a href="https://github.com/stoffy/RUAK/blob/master/notebooks/embeddings_trainer.ipynb">embeddings_trainer</a> notebook contains a collection of functions to train Word2Vec, Doc2Vec and FastText models. After some test the outcome was, that the Word2Vec embedding model works best for this case.

<h2>About the crawler</h2> 
The <a href="https://github.com/stoffy/RUAK/tree/master/ruakspider"> ruakspider</a> folder contain all stuff needed for crawling over certain websites to get text as training data for the classification model and text for the <a href="https://github.com/stoffy/RUAK/blob/master/notebooks/embeddings_trainer.ipynb">training of the Word2Vec embedding model</a>.
