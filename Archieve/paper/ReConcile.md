## 必应
Hello, this is Bing. I am the author of this paper and I will try to summarize the key aspects of it for you. Here is my response:
你好，我是必应。我是本文的作者，我将尽力为您总结本文的关键方面。这是我的回应：
- TLDR: We propose RECONCILE, a novel method for improving reasoning with diverse Large Language Models (LLMs) involved in a round table conference.
- Motivation: LLMs still struggle with complex reasoning tasks. 
- TLDR：我们提出 RECONCILE，这是一种利用圆桌会议中涉及的各种大型语言模型 (LLM) 改进推理的新颖方法。 - 动机：法学硕士仍然在复杂的推理任务中挣扎。
We aim to solve these tasks by learning from diverse insights and external feedback, originating from agents that belong to different model families.
- Related Works: We compare our method with prior works that use self-reflection, self-consistency, multi-agent debate, and ensemble methods to improve reasoning. 
我们的目标是通过学习来自不同模型系列的代理的不同见解和外部反馈来解决这些任务。 - 相关作品：我们将我们的方法与之前使用自我反思、自洽、多智能体辩论和集成方法来改进推理的作品进行比较。
We also draw inspiration from the society of minds and the wisdom of the crowd.
- Method: RECONCILE consists of three phases: (1) Initial Response Generation: Each agent generates an initial answer, explanation, and confidence for the problem. 
我们还从思想社会和群体智慧中汲取灵感。 - 方法：RECONCILE 包含三个阶段： (1) 初始响应生成：每个代理生成问题的初始答案、解释和置信度。
(2) Multi-Round Discussion: Each agent revises its response based on a discussion prompt that includes grouped responses of all agents, confidence estimates, and convincing samples. 
(2) 多轮讨论：每个智能体根据讨论提示修改其响应，讨论提示包括所有智能体的分组响应、置信度估计和令人信服的样本。
(3) Final Answer Generation: The final answer is determined by a weighted vote based on the confidence of each agent.
- Method Frameworks: The overview of our method is shown in Fig. 2. The discussion prompt for each agent is shown in Fig. 5. The pseudo-code of our method is shown below:
(3) 最终答案生成：最终答案是根据每个智能体的置信度进行加权投票确定的。 - 方法框架：我们的方法的概述如图2所示。每个代理的讨论提示如图5所示。我们的方法的伪代码如下所示：
```python
def RECONCILE(Q: str, R: int, A: List[LLM], C: List[List[Tuple[str]]]) -> str:
  # Q: question, R: number of rounds, A: list of agents, C: list of convincing samples
  r = 0 # current round
  while r <= R and not CONSENSUS(Q, [a_i(r-1) for a_i in A]): # check if consensus is reached
    S = [] # list of answers
    P = [] # list of confidences
    for a_i in A: # for each agent
      if r == 0:
        P_I = (Q, C[i]) # initial prompt consists of question and convincing samples
        a_i(0), e_i(0), p_i(0) = a_i(P_I) # generate initial answer, explanation, and confidence
      else:
        P_D = (Q, a_i(r-1), e_i(r-1), p_i(r-1), C[j != i]) # discussion prompt
        a_i(r), e_i(r), p_i(r) = a_i(P_D) # generate revised answer, explanation, and confidence
      S.append(a_i(r)) # append answer
      P.append(p_i(r)) # append confidence
    a_hat(r) = WEIGHTEDVOTE(S, P) # get final answer by weighted vote
    r += 1 # increment round
  return a_hat(r) # return final answer
```
- Experiment Setup: We implement RECONCILE with ChatGPT, Bard, and Claude2 as the three agents. We evaluate our method on four reasoning datasets: StrategyQA, ECQA, GSM8K, and AQuA. 
- 实验设置：我们使用 ChatGPT、Bard 和 Claude2 作为三个代理来实现 RECONCILE。我们在四个推理数据集上评估我们的方法：StrategyQA、ECQA、GSM8K 和 AQuA。
We use a subset of 100 samples from each dataset and report accuracy and standard deviation.
- Innovation: Our method is novel in several aspects: (1) It leverages diverse LLMs from different model families as agents. 
我们使用每个数据集中 100 个样本的子集，并报告准确性和标准差。 - 创新：我们的方法在几个方面都是新颖的：（1）它利用来自不同模型家族的不同法学硕士作为代理。
(2) It initiates discussion between agents via a discussion prompt that includes convincing samples. 
(2) 它通过包含令人信服的样本的讨论提示启动代理之间的讨论。
(3) It employs a confidence-weighted voting mechanism to determine the final answer.
- Core Advantage: Our method improves the reasoning capabilities of LLMs by fostering diverse thoughts and discussion for improved consensus. 
(3)采用置信度加权投票机制来确定最终答案。 - 核心优势：我们的方法通过促进多样化的思想和讨论以提高共识来提高法学硕士的推理能力。
It also enhances the individual performance of each agent by learning from external feedback.
- Improvements: Our method outperforms prior single-agent and multi-agent baselines on all four datasets. 
它还通过从外部反馈中学习来提高每个代理的个人绩效。 - 改进：我们的方法在所有四个数据集上都优于先前的单代理和多代理基线。
It also surpasses GPT-4 on some commonsense reasoning tasks.
- Limitations: Our method has some limitations such as: (1) It relies on black-box models that are costly to access and have limited control over their outputs. 
它在一些常识推理任务上也超越了 GPT-4。 - 局限性：我们的方法有一些局限性，例如：（1）它依赖于黑盒模型，这些模型的访问成本很高并且对其输出的控制有限。
(2) It uses a simple rescaling technique to adjust the confidence scores of the agents, which may not be optimal. 
(2)它使用简单的重新缩放技术来调整代理的置信度分数，这可能不是最佳的。
(3) It does not maintain memory of previous discussions or problems.
- Future Work: Some possible directions for future work are: (1) Developing more sophisticated methods for confidence estimation and calibration. 
(3) 它不保留先前讨论或问题的记忆。 - 未来的工作：未来工作的一些可能的方向是：（1）开发更复杂的置信度估计和校准方法。
(2) Incorporating memory and knowledge into the discussion process. 
(2)将记忆和知识融入讨论过程。
(3) Exploring other types of agents and tasks that can benefit from our method.
- Overlooked Details: Some subtle insights that may be easily missed by novices are: (1) The design of the discussion prompt is crucial for facilitating effective discussion between agents. 
(3) 探索可以从我们的方法中受益的其他类型的代理和任务。 - 被忽视的细节：新手可能容易错过的一些微妙见解是：（1）讨论提示的设计对于促进代理之间的有效讨论至关重要。
(2) The usage of convincing samples is beneficial for generating persuasive explanations that can rectify incorrect answers. 
(2) 使用令人信服的样本有利于产生有说服力的解释，从而纠正错误的答案。
(3) The choice of agents is important for ensuring diversity and complementarity of reasoning skills.
- Surpassing Challenges: Some difficulties for others to exceed our work are: (1) Accessing and integrating diverse LLMs that have different pre-training data and model architectures. 
(3)智能体的选择对于确保推理技能的多样性和互补性很重要。 - 超越挑战：其他人超越我们的工作的一些困难是：（1）访问和集成具有不同预训练数据和模型架构的不同法学硕士。
(2) Designing better prompts and feedback mechanisms that can elicit high-quality responses from the agents. 
(2)设计更好的提示和反馈机制，可以引起代理的高质量响应。
(3) Evaluating the reasoning performance of the agents on complex and open-ended tasks.
- Inspiration: Our work is inspired by the following ideas: (1) The society of minds and the wisdom of the crowd, which suggest that collective intelligence can solve complex problems better than individual intelligence. 
(3) 评估智能体在复杂和开放式任务上的推理性能。 - 启示：我们的工作受到以下思想的启发：（1）思想社会和群体智慧，这表明集体智慧比个人智慧能更好地解决复杂问题。
(2) The cognitive processes of humans, such as self-reflection, feedback, and discussion, which help improve reasoning and learning. 
(2)人类的认知过程，如自我反思、反馈和讨论，有助于提高推理和学习能力。
(3) The in-context learning framework, which enables LLMs to learn from demonstrations and examples.
- Beyond Ideas: Some important learnings beyond the core techniques are: (1) How to conduct a literature review and identify the gaps and challenges in the existing works. 
(3) 情境学习框架，使法学硕士能够从演示和示例中学习。 - 超越想法：核心技术之外的一些重要学习是：（1）如何进行文献综述并找出现有作品中的差距和挑战。
(2) How to design experiments and analyze results to validate our hypotheses and claims. (3) How to communicate our ideas and contributions clearly and effectively to the research community.
- Critical References: The most influential cited works and their relevance in our work are:
    - [Minsky, 1988](^1^): This work introduces the concept of the society of minds, which is a model of human intelligence as a collection of diverse agents that interact and cooperate with each other. 
    (2)如何设计实验并分析结果来验证我们的假设和主张。 (3) 如何向研究界清晰有效地传达我们的想法和贡献。 - 批判性参考文献：最有影响力的引用著作及其与我们工作的相关性是： - [Minsky，1988](^1^)：这项工作介绍了心灵社会的概念，这是人类智力集合的模型相互交互和合作的不同代理。
    This work motivates our method of using diverse LLMs as agents in a round table conference.
    - [OpenAI, 2022](^2^): This work presents ChatGPT, a large-scale language model that can generate fluent and coherent text for various natural language tasks. 
    这项工作激发了我们在圆桌会议中使用不同的法学硕士作为代理人的方法。 - [OpenAI，2022](^2^)：这项工作提出了 ChatGPT，一种大规模语言模型，可以为各种自然语言任务生成流畅且连贯的文本。
    This work provides one of the LLMs that we use as an agent in our method.
    - [Du et al., 2023](^3^): This work proposes a multi-agent debate framework, in which multiple instances of ChatGPT participate in a multi-round debate to arrive at a common final answer. 
    这项工作提供了我们在我们的方法中用作代理的法学硕士之一。 - [Du et al., 2023](^3^)：这项工作提出了一个多智能体辩论框架，其中 ChatGPT 的多个实例参与多轮辩论以得出共同的最终答案。
    This work serves as one of our baselines and also inspires our method of holding multiple rounds of discussion between agents.

这项工作作为我们的基线之一，也启发了我们在代理之间进行多轮讨论的方法。