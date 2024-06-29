## 1: Introduction to Natural Language Processing (NLP)

| Concept | Description |
|---------|-------------|
| Natural Language Processing (NLP) | A field of AI focused on enabling computers to understand, interpret, and generate human language |
| Applications | Chatbots, sentiment analysis, translation, speech recognition, etc. |
| Key Steps | 1. Text input 2. Convert to numerical representation (word embeddings) 3. Process with neural network 4. Generate output/prediction |
| Challenges | Converting text to numbers, preserving word order and meaning |
| Key Terms | Tokenization: Splitting text into individual words/tokens<br>Document: A single text sample (e.g. one review)<br>Corpus: A collection of documents |

## 2: Word Embeddings

| Concept | Description |
|---------|-------------|
| Word Embeddings | Numerical representations of words as vectors in high-dimensional space |
| Purpose | Allow neural networks to process text by converting words to numbers |
| Types | One-hot encoding, Frequency-based, Neural network-based |
| One-hot Encoding | Represents each word as a vector of 0s with a single 1<br>Simple but leads to very large, sparse matrices |
| Neural Network Embeddings | Learn dense vector representations that capture semantic meaning |
| Examples | Word2Vec, GloVe, BERT |

## 3: GloVe Word Embeddings

| Concept | Description |
|---------|-------------|
| GloVe | Global Vectors for Word Representation |
| Approach | Based on word co-occurrence matrix from large corpus |
| Output | Dense, low-dimensional word vectors |
| Capabilities | Captures semantic relationships and analogies between words |
| Visualization | Can be reduced to 2D and plotted to show word clusters |
| Advantages | Pre-trained on large datasets, captures word meanings well |

## 4: Sentiment Analysis with Embeddings

| Concept | Description |
|---------|-------------|
| Process | 1. Convert text to embeddings<br>2. Use embeddings as input to neural network<br>3. Train network to predict sentiment |
| Advantages | More compact representation than one-hot encoding<br>Captures semantic meaning of words |
| Model Used | Sentence transformer to get 768-dim sentence embeddings |
| Results | Outperformed one-hot encoding with 97% less data |

## 5: Transformers

| Concept | Description |
|---------|-------------|
| Transformers | Neural network architecture introduced in 2017 |
| Key Components | Positional encoding, Attention, Self-attention |
| Advantages | Handles long sequences well, parallelizable, no vanishing gradients |
| Positional Encoding | Preserves word order information |
| Attention | Allows model to focus on relevant parts of input |
| Self-attention | Improves internal word representations |
| Applications | NLP, computer vision, time series prediction |
| Examples | BERT, GPT-3, LaMDA |