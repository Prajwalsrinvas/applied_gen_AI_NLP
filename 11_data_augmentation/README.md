**Data Augmentation Overview**

| Concept | Description |
|---------|-------------|
| Purpose | Used when fine-tuning a model with insufficient data |
| Analogy | Similar to image augmentation in computer vision |
| Challenge in NLP | Changing words can alter meaning, requiring careful augmentation |
| Techniques | Back translation, random insertion, contextual word embeddings, synonym replacement, random deletion, contrastive learning |

**Back Translation**

| Step | Description |
|------|-------------|
| 1. Original sentence | Start with sentence in original language |
| 2. Translate | Convert to another language |
| 3. Translate back | Convert back to original language |
| Result | New sentence with similar meaning but different wording |

**Synonym Replacement**

| Concept | Description |
|---------|-------------|
| Process | Replace words in original sentence with synonyms |
| Effect | Creates new sentence with same context but different wording |

**Random Deletion**

| Concept | Description |
|---------|-------------|
| Process | Randomly remove words from the original sentence |
| Purpose | Help model learn with incomplete information |

**Word Embedding Augmentation**

| Step | Description |
|------|-------------|
| 1. Choose model | Use embedding models like GloVe, Word2Vec, FastText, BERT |
| 2. Find neighbors | Identify words close to target in embedding space |
| 3. Replace | Substitute original word with close neighbor |

**Coding Implementation**

| Technique | Implementation Details |
|-----------|------------------------|
| Back Translation | Used Facebook's M2M100 model for multilingual translation |
| Synonym Replacement | Used NLPAug package with WordNet as augmentation source |
| Random Cropping | Used NLPAug with random word deletion |
| Contextual Augmentation | Used BERT model to find contextually close words |
| Word Embeddings | Used GloVe embeddings to find similar words |
| Fill-Mask | Used Hugging Face pipeline for masked language modeling |
