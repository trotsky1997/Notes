## llm的发展现状


## llm agent的典型结构

## single agent

#### persona:embodied profile

### planning:chain of thought/tree/graph

### memory:in-context/RAG/web search/knowledge bank retrieval/Knowledge graph

### action:工具使用/ReAct/Reflexion/minedojo

## multi-agent

### fixed characters: chatdev,西部小镇

### generative agents

## applications in AI4Chem

### chatcrow

### chatgpt 4 MoF

### ours


```mermaid
flowchart LR
A[输入问题或声明] --> B[选择合适的提示方法]
B -->|ReAct|C[交替生成思考和行动]
B -->|CoT|D[仅生成思考]
B -->|Act|E[仅生成行动]
C --> F[思考用语言推理和规划]
C --> G[行动用语言与外部环境交互]
D --> H[思考用语言推理和回答]
E --> I[行动用语言与外部环境交互]
F --> J[更新上下文和目标]
G --> K[获取额外的信息和反馈]
H --> L[更新上下文和答案]
I --> M[获取额外的信息和反馈]
J --> N[判断是否完成任务或需要切换方法]
K --> N
L --> O[输出最终答案或判断是否需要切换方法]
M --> O
N -->|是|O
N -->|否|C
O --> P[结束任务或切换方法]
```
