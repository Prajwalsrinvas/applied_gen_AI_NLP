## 1: Overview of Open Source LLMs

| Model | Creator | Sizes | Language Support | Token Limit |
|-------|---------|-------|------------------|-------------|
| LLaMA 2 | Meta | 7B - 70B parameters | Mainly English | ~2000 tokens |
| Mistral | Mistral AI | 7B, 8x7B (MoE) | English, French, Italian, German, Spanish | 32,000 tokens |

## 2: Advantages and Disadvantages of Open Source vs Closed Source LLMs

| Aspect | Open Source | Closed Source |
|--------|-------------|---------------|
| Confidentiality | + (can run locally) | - (data sent externally) |
| Transparency | + (more open about training/methods) | - (less transparent) |
| Control | + (full control) | - (limited control) |
| Cost | - (high fixed costs) | + (pay-per-use model) |
| Performance | - (generally lower than top closed models) | + (higher performance) |
| Maintenance | - (self-maintained) | + (no maintenance required) |
| Operation | - (self-operated) | + (managed service) |

## 3: Using Open Source LLMs - Key Points

| Aspect | Details |
|--------|---------|
| Prompt Formatting | Specific formatting required (e.g., XML tags for LLaMA 2) |
| Local Deployment | Can be run on CPU, even with limited resources |
| Model Versions | Different sizes available (e.g., 7B, 13B for LLaMA 2) |
| Implementation | Various libraries available (e.g., llama.cpp) |
| Performance Considerations | Larger models generally perform better but require more resources |

## 4: Code Implementation (LLaMA 2 Example)

| Step | Description |
|------|-------------|
| Import Libraries | Import necessary packages (e.g., llama.cpp) |
| Load Model | Specify model path and parameters |
| Format Prompt | Use correct prompt template (with XML tags) |
| Run Inference | Pass formatted prompt to the model |
| Process Output | Receive and process model's response |
