<h1>RUAK - Are you a Hegel?</h1>

<img src="https://github.com/stoffy/RUAK/blob/master/images/The_School_of_Athens.jpg" alt="The School of Athens"><br>
<cite>The greatest challenge to any thinker is stating the problem in a way that will allow a solution.</cite><br>
<a href="https://en.wikipedia.org/wiki/Bertrand_Russell">Bertrand Russell</a>

<h2>About this project</h2>
Philosophy is a fundamental human thought movement. Everyone is a philosopher. The only question is what kind of philosopher you are. This project tries to answer that question.<br><br>
Using natural language processing (NLP), texts of different authors are used for categorization.
With the help of these texts any sentence can be categorically determined.
To understand how written language works and what the differents are between authors it helps to analyse the context of the sentences. Though visualization it is simpler to see structural varieties such as average sentence length, word class ratio and the use of <a href="https://en.wikipedia.org/wiki/Stop_word">stop words</a>.

<h2>About the notebooks</h2>
<h3><u>text_classifier.ipynb</u></h3>
<h4>Content</h4>
<ol>
	<li>Preparations</li>
	<li>Loading text data</li>
	<li>Collect data and create word collection</li>
	<li>Create and extend DataFrame</li>
	<li>Store or load DataFrame</li>
	<li>Visualization of data</li>
	<li>Prepare and split</li>
	<li>Hyperparameter tuning</li>
	<li>Model preparation and training</li>
	<li>Save or load model</li>
	<li>Evaluation</li>
	<li>TensorBoard</li>
</ol>

You can open this Jupyter notebook in Google Colab to use a GPU and have a nice platform for editing.

<a href="https://colab.research.google.com/github/stoffy/RUAK-text-classifier/blob/master/notebooks/text_classifier.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a><br><br>

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

<h5>Data distribution</h5> 
Shows the shares of data for each author:<br>
<img src="https://github.com/stoffy/RUAK-text-classifier/blob/master/images/data_distribution.png" alt="Data distribution">

<h5>Comparing authors</h5> 
Shows the differences between the authors for 4 metrics: <code>Mumber of sentences</code>, <code>Median sentence length</code>, <code>Unique vocabulary count</code>, <code>Median stop word ratio</code>.<br>
<img src="https://github.com/stoffy/RUAK-text-classifier/blob/master/images/comparing_authors.png" alt="Comparing authors">

<h5>Word classes by authos</h5>
Presents the ratio of authors total used words to word classes:<br>
<img src="https://github.com/stoffy/RUAK-text-classifier/blob/master/images/word_classes_by_author.png" alt="Word classes by authors">

<h5>Common words</h5>
Gives an overview of the number of sentences containing one if the most 20 common words:<br>
<img src="https://github.com/stoffy/RUAK-text-classifier/blob/master/images/common_words.png" alt="Common words">


<h4>Prepare and split</h4>
<h4>Hyperparameter tuning</h4>
<h4>Model preparation and training</h4>
<h4>Save or load model</h4>
<h4>Evaluation</h4>
<h4>TensorBoard</h4>

 

<h3><u>embeddings_trainer.ipynb</u></h3>
The <a href="https://github.com/stoffy/RUAK/blob/master/notebooks/embeddings_trainer.ipynb">embeddings_trainer</a> notebook contains a collection of functions to train Word2Vec, Doc2Vec and FastText models. After some test the outcome was, that the Word2Vec embedding model works best for this case.

<h2>About the crawler</h2> 
The <a href="https://github.com/stoffy/RUAK/tree/master/ruakspider"> ruakspider</a> folder contain all stuff needed for crawling over certain websites to get text als training data for the classification model and text for the <a href="https://github.com/stoffy/RUAK/blob/master/notebooks/embeddings_trainer.ipynb">training of the Word2Vec embedding model</a>.

<h2>More information</h2> 
The Jupyter notebooks are hooked up the Google Drive to load and store different types of data. If you are not using Google Drive you need the change the paths in the notebooks (1.2.1. Set variables and paths).