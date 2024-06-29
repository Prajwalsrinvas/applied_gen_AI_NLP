## 1. Vector Databases

| Concept | Description |
|---------|-------------|
| Definition | Special type of database able to store, manage, and query data represented in geometric formats |
| Main Use | Storing high-dimensional data (embeddings) for fast querying and similarity analysis |
| Applications | NLP, image similarities, clustering, real-time analytics |
| Advantage | Better suited for unstructured data (images, texts, videos, sounds) compared to traditional SQL databases |
| Popular Products | Pinecone, Chroma, Redis |

## 2. Tokenization

| Concept | Description |
|---------|-------------|
| Definition | Process of breaking down a sequence of words or text into individual units called tokens |
| Types | Word tokenization, sentence tokenization, subword tokenization |
| Importance | Fundamental first step in most NLP tasks |
| Rule of Thumb | In English, 1 token generally corresponds to roughly 4 characters |
| Implementation | Can use tools like recursive character text splitter or sentence transformers token text splitter |

## 3. Bible Vector Database Project

| Step | Description |
|------|-------------|
| Data Acquisition | Downloaded Bible text from Project Gutenberg |
| Text Preprocessing | Used recursive character text splitter and sentence transformers token text splitter |
| Embedding Creation | Used sentence transformer embedding function |
| Database Setup | Created a Chroma database instance |
| Data Insertion | Added tokenized texts to the database with unique IDs |
| Querying | Implemented function to query the database based on text input |

## 4. Movie Vector Database Project

| Step | Description |
|------|-------------|
| Data Acquisition | Used a subset of a movie dataset from Kaggle |
| Data Preprocessing | Filtered for non-null titles and descriptions, removed duplicates |
| Database Setup | Created a persistent Chroma database |
| Data Insertion | Added movie descriptions to the database in batches |
| Querying Function | Implemented get_title_by_description function to find movies based on plot description |

## 5. Multimodal Vector Database

| Concept | Description |
|---------|-------------|
| Definition | Vector database capable of handling multiple types of data (e.g., images and text) |
| Model Used | CLIP (Contrastive Language Image Pre-training) or Open CLIP |
| Data Handling | Stores both image representations and text embeddings |
| Querying Methods | Can query using either images or text |
| Implementation | Used Chroma DB with custom embedding function and image loader |
