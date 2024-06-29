## 1: Hugging Face Overview

| Aspect | Description |
|--------|-------------|
| Definition | Platform for machine learning and data science |
| Purpose | Help users build, deploy, and train machine learning models |
| Key Features | - Hosts majority of machine learning models<br>- Provides infrastructure for running and deploying models<br>- Largest community for machine learning |
| Ecosystem | - Models<br>- Datasets<br>- Metrics<br>- Documentation and tutorials |
| Model Types | - Multimodal<br>- Computer vision<br>- Natural Language Processing (NLP)<br>- Audio<br>- Tabular data<br>- Reinforcement learning |

## 2: Hugging Face Pipelines

| Aspect | Description |
|--------|-------------|
| Definition | Simple API for model inference |
| Types | 1. Task-based pipeline<br>2. Model-specific pipeline |
| Basic Usage | 1. Import pipeline from transformers<br>2. Create pipeline instance with task or model<br>3. Pass data to pipeline for inference |
| Input Flexibility | Can accept single string or list of strings |
| Key Parameters | - Task<br>- Model (optional)<br>- Tokenizer (optional) |

## 3: NLP Tasks and Pipelines

| Task | Pipeline Name | Description |
|------|---------------|-------------|
| Text Classification | "text-classification" | Assign predefined categories or labels to text |
| Named Entity Recognition (NER) | "ner" | Classify named entities into predefined categories |
| Question Answering | "question-answering" | Extract relevant information from documents based on questions |
| Text Summarization | "summarization" | Distill essential information from source text |
| Translation | "translation" or "translation_xx_to_yy" | Translate text from one language to another |
| Fill-Mask | "fill-mask" | Predict masked or missing words in a sentence |
| Zero-Shot Classification | "zero-shot-classification" | Classify text into unseen categories without retraining |

## 4: Zero-Shot Classification

| Aspect | Description |
|--------|-------------|
| Definition | Apply a model to tasks it wasn't explicitly trained on |
| Benefits | - Avoid retraining for new classes<br>- Generalize to unseen classes<br>- Useful for frequently changing or numerous classes |
| Approaches | 1. Attribute-based<br>2. Word embeddings<br>3. Transfer learning (e.g., Natural Language Inference) |
| Implementation | Use Hugging Face pipeline with "zero-shot-classification" task |
| Key Parameters | - Candidate labels<br>- Multi-label option |
