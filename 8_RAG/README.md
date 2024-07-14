## 1. RAG Overview

| Concept | Description |
|---------|-------------|
| Definition | RAG combines retrieval from a corpus with language model generation |
| Key Components | 1. Large corpus of text data <br> 2. Embedding model <br> 3. Vector database <br> 4. Nearest neighbor search <br> 5. Large language model |
| Workflow | 1. Embed corpus texts and user query <br> 2. Find nearest neighbors to query <br> 3. Retrieve top matching texts <br> 4. Pass retrieved texts + query to LLM <br> 5. LLM generates final response |
| Advantage | Improves responses by grounding LLM in relevant retrieved information |

## 2. RAG Implementation

| Step | Description |
|------|-------------|
| Database Setup | Use existing vector database with movie data |
| Querying Database | Create function to query vector DB and format results |
| LLM Setup | Configure OpenAI API and define system/user prompts |
| RAG Function | Combine DB query and LLM call into single function |
| Final Output | 1. Raw DB results <br> 2. LLM-generated response using DB results |

## 3. Code Components

| Component | Purpose |
|-----------|---------|
| ChromaDB | Vector database for storing and querying embeddings |
| OpenAI API | Access to GPT model for text generation |
| get_query_results() | Retrieve and format results from vector DB |
| rag() | Main function combining DB query and LLM generation |
| System Prompt | Instructions for LLM on how to use retrieved info |
| User Prompt | Combines user query with retrieved DB results |

## 4. Key Takeaways

| Point | Description |
|-------|-------------|
| Potential | RAG has significant potential for enhancing AI applications |
| Use Cases | Useful for question answering, information retrieval, and more |
| Customization | System prompts can be tailored for specific use cases |
| Efficiency | Uses GPT-3.5-turbo for cost-effectiveness |
| Practicality | Combines power of retrieval and generation for improved results |

Read more:

- https://pub.towardsai.net/advanced-rag-techniques-an-illustrated-overview-04d193d8fec6
- https://www.anyscale.com/blog/a-comprehensive-guide-for-building-rag-based-llm-applications-part-1
- https://parlance-labs.com/education/rag/ben.html