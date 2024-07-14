## 1. Advanced Prompt Engineering

| Concept | Description |
|---------|-------------|
| Purpose | Improve coherence and quality of LM outputs for complex tasks |
| Key Idea | Provide more structure and guidance in prompts |
| Benefits | - Better reasoning capabilities  
| | - More relevant responses
| | - Avoids jumping to conclusions |

## 2. Few-Shot Prompting  

| Concept | Description |
|---------|-------------|
| Technique | Provide examples of task with expected outputs in prompt |
| Benefits | - Quick adaptation to new tasks
| | - Effective for well-defined tasks
| | - Allows customizing outputs |
| Drawbacks | - Performance depends on quality of examples
| | - Risk of overfitting |

## 3. Chain-of-Thought

| Concept | Description |
|---------|-------------|
| Technique | Break down complex tasks into intermediate reasoning steps |
| Benefits | - Improves performance on complex tasks
| | - Provides transparency into thought process
| | - Increases interpretability |
| Drawbacks | - Increased output length and computation
| | - Quality depends on model's ability to break down steps
| | - Risk of compounding errors |

## 4. Self-Consistency Chain-of-Thought

| Concept | Description |
|---------|-------------|
| Technique | Generate multiple chains of thought and use voting to select final answer |
| Key Steps | 1. Create multiple CoT paths
| | 2. Use voting algorithm to select most common answer
| | 3. Return selected answer as final output |
| Benefits | Improves coherence and consistency of answers |

## 5. Prompt Chaining

| Concept | Description |
|---------|-------------|
| Technique | Break task into subtasks, using output of previous step as input to next |
| Key Idea | Incrementally solve complex tasks |
| Use Cases | - Document Q&A
| | - Article writing 
| | - Programming tasks
| | - Travel planning |

## 6. Tree-of-Thought

| Concept | Description |
|---------|-------------|
| Technique | Explore different solution paths in a tree structure |
| Key Ideas | - Self-evaluation of progress
| | - Exploration of multiple solutions
| | - Evaluation before committing to final path |
| Analogy | Similar to decision trees in machine learning |

## 7. Self-Feedback

| Concept | Description |
|---------|-------------|
| Technique | Iteratively improve response quality through self-evaluation |
| Key Steps | 1. Generate initial output
| | 2. Evaluate and refine output 
| | 3. Repeat until stop criteria met |
| Components | - Rating of current output
| | - Feedback on how to improve
| | - Revised output |

## 8. Self-Critique

| Concept | Description |
|---------|-------------|
| Technique | Generate multiple ideas, critique them, select and improve best one |
| Key Steps | 1. Ideation - generate multiple outputs
| | 2. Critique - analyze and select best idea  
| | 3. Resolution - improve selected idea |
| Implementation | Can use LangChain's SmartLLMChain for easy setup |

Read more:
- https://www.promptingguide.ai/
- https://www.prompthub.us/blog/prompt-patterns-what-they-are-and-16-you-should-know