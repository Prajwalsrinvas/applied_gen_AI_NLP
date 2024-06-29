## 1. Fine-tuning Overview:

| Concept | Description |
|---------|-------------|
| Purpose of fine-tuning | Adapt pre-trained model to custom dataset or new task |
| Approaches | 1. Extract features and train simple model  2. Retrain part or all of network |
| Process | Pass custom data through pre-trained network during training over multiple epochs |
| Benefits | Fine-tuned model outperforms simpler approaches |

## 2. Simple Model Approach:

| Step | Description |
|------|-------------|
| 1. Tokenization | Convert text to input IDs and attention masks |
| 2. Feature extraction | Pass tokenized input through pre-trained model, extract last hidden layer |
| 3. Training | Use extracted features as input to simple classifier (e.g. logistic regression) |
| 4. Inference | Pass new data through same process to get predictions |

## 3. Fine-tuning Model:

| Step | Description |
|------|-------------|
| 1. Data preparation | Split data into train/test sets |
| 2. Model setup | Load pre-trained model, modify output layer for new task |
| 3. Training | Use Hugging Face Trainer to fine-tune model on custom data |
| 4. Evaluation | Assess performance on test set |
| 5. Inference | Use fine-tuned model to make predictions on new data |

## 4. Hugging Face Trainer:

| Component | Description |
|-----------|-------------|
| Trainer class | Simplified API for training Transformer models |
| Key parameters | Model, training arguments, train/eval datasets |
| Usage | Create Trainer instance, call train() method |
| Benefits | Handles distributed training, optimized for Transformers |

## 5. Saving and Loading Model:

| Step | Description |
|------|-------------|
| 1. Login to Hugging Face | Use CLI to authenticate |
| 2. Create model card | Document model details |
| 3. Push to Hub | Upload model to Hugging Face Hub |
| 4. Load model | Use model ID to load from Hub for inference |