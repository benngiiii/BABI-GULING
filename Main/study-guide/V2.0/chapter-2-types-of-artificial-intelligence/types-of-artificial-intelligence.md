# Chapter 2: Types of Artificial Intelligence

**Author:** Gandhi Bestin Dhammananda  
**Reviewer:** Brian Djoni Suzanna  
**Audience:** Complete beginners  
**Estimated learning time:** 60 minutes  
**Status:** Stage 2 draft — pending peer review and repository verification

---

## Learning Outcomes

After completing this chapter, readers should be able to:

- Explain why AI can be classified in different ways.
- Describe ANI, AGI, and ASI.
- Explain the four commonly taught functionality categories.
- Understand Machine Learning and its three main learning approaches.
- Describe neural networks and deep learning.
- Distinguish discriminative AI from Generative AI.
- Recognize symbolic AI, multimodal AI, and AI agents.
- Apply different AI classifications to familiar examples.

## Chapter Map

| Section | Topic | Time |
|---|---|---:|
| 2.1 | Introduction to AI Classification | 3 min |
| 2.2 | AI Based on Capability | 6 min |
| 2.3 | AI Based on Functionality | 7 min |
| 2.4 | Machine Learning and Generative AI | 18 min |
| 2.5 | Comparing AI Approaches and Applications | 8 min |
| 2.6 | Classification Activity | 5 min |
| 2.7 | Common Misunderstandings | 4 min |
| 2.8 | Practice Questions and Answers | 6 min |
| 2.9 | Summary and References | 3 min |
| **Total** | | **60 min** |

---

## 2.1 Introduction to AI Classification

AI systems have different abilities, designs, and purposes. Some recognize images, others recommend products, while some generate text or images.

To understand these differences, AI can be classified from several perspectives:

1. **Capability:** How broadly can an AI system perform intellectual tasks?
2. **Functionality:** How does it behave or use information?
3. **Learning approach:** How does it learn patterns from data?
4. **Output and application:** What does it produce or help accomplish?

These classifications describe different aspects of AI. They are not one universal taxonomy, and a single system may belong to several categories.

For example, an image generator may be classified as ANI based on its capabilities, use deep learning, and qualify as Generative AI because it creates images.

---

## 2.2 AI Based on Capability

The capability framework divides AI into three categories: ANI, AGI, and ASI.

### 2.2.1 Artificial Narrow Intelligence (ANI)

Artificial Narrow Intelligence (ANI), also called narrow AI, is designed to perform specific tasks or a limited range of tasks.

Examples include:

- Facial recognition systems.
- Spam filters.
- Recommendation systems.
- Conversational AI.
- Image generators.

An ANI system may perform its intended task extremely well, but that does not mean it possesses general human-level intelligence.

Most current AI applications are classified as ANI under this framework.

### 2.2.2 Artificial General Intelligence (AGI)

Artificial General Intelligence (AGI) refers to a proposed form of AI with broad, flexible intellectual abilities across different tasks and domains.

Unlike ANI, which focuses on specific tasks, AGI would ideally be able to learn unfamiliar tasks and transfer knowledge between different situations.

There is no universally accepted definition or test for AGI. Although modern AI systems can perform many impressive tasks, this alone does not establish that AGI has been achieved.

### 2.2.3 Artificial Superintelligence (ASI)

Artificial Superintelligence (ASI) refers to a hypothetical AI that would surpass human intellectual abilities across many important domains.

Such a system might outperform the best human experts in scientific research, problem-solving, and other intellectual activities.

ASI remains hypothetical, and there is no verified evidence that it currently exists.

### 2.2.4 Comparing the Three Categories

| Feature | ANI | AGI | ASI |
|---|---|---|---|
| Main idea | Specific tasks | Broad intellectual abilities | Beyond human intellectual abilities |
| Scope | Limited or defined | General and flexible | Hypothetically superior to humans |
| Status | Established | Not universally confirmed | Hypothetical |
| Example | Spam filter | Hypothetical general-purpose AI | Hypothetical superintelligent AI |

**Key takeaway:** ANI exists in practical applications today, while AGI and ASI describe broader levels of intelligence that have not been universally established.

---

## 2.3 AI Based on Functionality

Another commonly taught framework divides AI into four categories based on how systems respond to information and use memory.

### 2.3.1 Reactive Machines

Reactive machines respond to current inputs without using stored past experiences to guide decisions in the way described by this category.

A classic example is IBM's Deep Blue chess computer, which defeated world chess champion Garry Kasparov in 1997.

**Main characteristic:** Responds to current information without relying on stored personal experiences.

### 2.3.2 Limited-Memory AI

Limited-Memory AI uses previous observations or stored information to support decisions.

Examples include:

- Driving-assistance systems that track nearby vehicles.
- Recommendation systems that use previous activity.
- Conversational systems that use earlier messages as context.

Many modern AI applications use some form of historical or contextual information, although their designs differ.

### 2.3.3 Theory-of-Mind AI

Theory-of-Mind AI is a proposed form of AI that could understand other people's beliefs, intentions, emotions, and perspectives.

For example, a hypothetical system might recognize that two people have different beliefs about the same situation and adjust its explanation accordingly.

Current AI can recognize certain emotional cues and generate empathetic responses, but these abilities do not establish full theory-of-mind capability.

### 2.3.4 Self-Aware AI

Self-Aware AI refers to a hypothetical system with meaningful awareness of its own existence and internal state.

A machine can report its battery level or describe its own functions without necessarily being conscious.

There is currently no widely accepted scientific demonstration that AI systems possess self-awareness or consciousness in this strong sense.

### 2.3.5 Comparing the Four Categories

| Category | Main idea | Status |
|---|---|---|
| Reactive Machines | Respond to current information | Practical examples exist |
| Limited-Memory AI | Uses previous observations or stored information | Common in current applications |
| Theory-of-Mind AI | Understands other people's mental states | Full capability remains unestablished |
| Self-Aware AI | Possesses meaningful self-awareness | Hypothetical |

These categories are an introductory framework, not a complete technical description of every AI system.

---

## 2.4 Machine Learning and Generative AI

Machine Learning and Generative AI are important concepts in modern AI. They describe different aspects of AI systems rather than additional capability levels.

### 2.4.1 What Is Machine Learning?

Machine Learning (ML) is an approach in which computer systems learn patterns from data to make predictions, classifications, or other outputs.

For example, a spam filter can learn patterns from previously identified spam emails and use them to classify new messages.

Other applications include:

- Fraud detection.
- Image recognition.
- Recommendation systems.
- Price prediction.

Machine Learning is one approach within AI. Not every AI system uses Machine Learning.

### 2.4.2 Three Common Types of Machine Learning

**A. Supervised Learning**

Supervised learning uses labeled data, meaning that training examples include the correct answers.

Example: Training a model with pictures labeled "cat" and "dog" so it can classify new pictures.

Common tasks include classification and numerical prediction.

**B. Unsupervised Learning**

Unsupervised learning uses data without predefined answer labels. The system identifies patterns or groups within the data.

Example: Grouping customers according to similarities in their shopping habits.

A common technique is clustering.

**C. Reinforcement Learning**

Reinforcement learning allows a system to learn through interaction with an environment and feedback in the form of rewards or penalties.

Example: Training an AI to play a game by rewarding successful actions.

### Comparing the Three Approaches

| Feature | Supervised | Unsupervised | Reinforcement |
|---|---|---|---|
| Learning signal | Correct answers | Patterns in data | Rewards or penalties |
| Main purpose | Predict or classify | Discover patterns | Learn actions |
| Example | Spam detection | Customer grouping | Game-playing AI |

### 2.4.3 Training, Validation, and Testing Data

Machine Learning models are commonly developed using three types of data:

- **Training data:** Used to teach the model.
- **Validation data:** Used to compare models and adjust settings during development.
- **Testing data:** Used to evaluate the final model on separate examples.

A related problem is **overfitting**. This occurs when a model learns its training examples too closely and performs poorly on new data.

A good model should be able to generalize, meaning it can apply learned patterns to suitable examples it has not encountered before.

### 2.4.4 Neural Networks and Deep Learning

A neural network is a computing model made of connected processing units called artificial neurons. These units are organized into layers.

A simplified neural network has three main parts:

- **Input layer:** Receives information.
- **Hidden layers:** Process information and learn patterns.
- **Output layer:** Produces a result.

**Deep Learning** is a specialized area of Machine Learning that uses neural networks with multiple layers.

For example, a deep-learning model can learn visual patterns from images and use them to recognize objects.

**Relationship between AI, ML, and Deep Learning:**

```text
Artificial Intelligence
        |
        +-- Machine Learning
                 |
                 +-- Deep Learning
                         |
                         +-- Multi-layer Neural Networks
```

This is a simplified conceptual relationship. Not every AI system uses Machine Learning, and not every ML system uses deep learning.

### 2.4.5 What Is Generative AI?

Generative AI refers to AI systems that create new content, such as:

- Text and stories.
- Images and illustrations.
- Audio and music.
- Videos.
- Computer code.

For example, an image generator can create a picture from the instruction "Draw a house beside a lake."

Many modern Generative AI systems use deep learning. However, generating convincing content does not automatically mean that the system understands it like a human or always produces correct information.

### 2.4.6 Discriminative AI vs. Generative AI

Discriminative models focus on identifying categories or predicting answers. Generative models focus on producing new content or data.

| Feature | Discriminative | Generative |
|---|---|---|
| Main purpose | Classify or predict | Generate new content |
| Example | Spam detection | Image generation |
| Main question | "Which category fits?" | "What can be created?" |

Some AI applications combine both approaches.

### 2.4.7 Symbolic AI and Rule-Based Systems

Not all AI systems learn from data. **Symbolic AI** represents knowledge using symbols, facts, and logical rules.

A simple example is:

```text
IF temperature is below 0°C
THEN water may freeze.
```

The system uses the written rule to reach a conclusion.

Examples include expert systems and troubleshooting programs.

**Advantages:** Rules can be inspected and are useful for problems with clear conditions.

**Limitations:** Systems may struggle with unexpected situations and require people to maintain their rules.

Symbolic AI and Machine Learning are different approaches, but they can also be combined in hybrid systems.

---

## 2.5 Comparing AI Approaches and Applications

The concepts introduced in this chapter answer different questions:

- Capability describes the breadth of an AI system's abilities.
- Functionality describes its behavior and use of information.
- Machine Learning describes how it learns patterns.
- Generative AI describes its content-generation ability.
- Symbolic AI describes its use of explicit rules and knowledge.

### 2.5.1 Relationship Diagram

```text
                    ARTIFICIAL INTELLIGENCE
                              |
          +-------------------+-------------------+
          |                   |                   |
      CAPABILITY          FUNCTIONALITY       APPROACHES
          |                   |                   |
     ANI, AGI, ASI      Four commonly       +------+------+
                        taught categories   |             |
                                       Symbolic AI    Machine Learning
                                                          |
                                                   Deep Learning


             OTHER DESCRIPTIONS OF AI SYSTEMS
                         |
          +--------------+--------------+
          |              |              |
     Generative AI   Multimodal AI   AI Agents
```

**Important relationship:**

```text
Machine Learning <------ Often used together ------> Generative AI
```

Many Generative AI systems use Machine Learning, but Generative AI is not simply a subdivision of Machine Learning. They describe different aspects of AI.

The diagram is a simplified teaching aid, not a formal or universally standardized taxonomy.

### 2.5.2 Multimodal AI

Multimodal AI refers to systems that can process or generate more than one type of information, such as text, images, audio, and video.

For example, an AI assistant may receive a photograph and a written question, then generate a text response.

Multimodal AI describes the types of information a system works with. It does not automatically mean that the system has AGI.

### 2.5.3 AI Agents and Agentic AI

An AI agent is a system designed to pursue a goal through planning and actions.

For example, a travel-planning agent might:

1. Identify a destination and travel dates.
2. Search for transportation options.
3. Compare available choices.
4. Prepare an itinerary.

Unlike a basic chatbot that only responds to a message, an agent may complete several connected steps and use external tools.

AI agents may use Generative AI, but the concepts are different. Generative AI creates content, while an agent focuses on completing goals through actions.

Agents can also make mistakes or take unintended actions, so permissions and human oversight are important.

### 2.5.4 Applying Multiple Perspectives to One System

Consider an AI assistant that answers questions, summarizes reports, analyzes photographs, and generates text.

It may be described as:

- **ANI:** If its abilities remain within the narrow-AI framework.
- **Limited-Memory AI:** If it uses previous messages or stored information.
- **Machine Learning:** If its models learn patterns from data.
- **Deep Learning:** If it uses multi-layer neural networks.
- **Generative AI:** If it creates text or other content.
- **Multimodal AI:** If it processes multiple types of information.
- **AI agent:** If it can plan and take actions toward a goal.

This demonstrates why one AI system can have several classifications.

---

## 2.6 Classification Activity

**Instructions:** Identify the most suitable category or perspective for each example. Some examples may fit more than one.

| No. | Example | Your task |
|---|---|---|
| 1 | An email service identifies suspicious messages. | Identify its capability category and whether it may use ML. |
| 2 | A music application recommends songs based on listening history. | Explain how ML and stored information may be involved. |
| 3 | A chatbot writes a birthday greeting and summarizes a report. | Identify whether it is Generative AI and whether this proves AGI. |
| 4 | A driving system uses recent observations of nearby cars. | Identify its functionality category. |
| 5 | A tool creates an image from a written instruction. | Identify the type of AI output. |
| 6 | A model learns from pictures labeled "cat" and "dog." | Identify its learning approach. |
| 7 | A system groups customers without predefined categories. | Identify its learning approach. |
| 8 | An assistant searches, compares, and organizes information through several steps. | Explain why it may be an AI agent. |

### Suggested Answers

1. **ANI; possibly ML.** It performs a specific task and may learn patterns from spam examples.
2. **ANI; potentially ML and stored information.** It uses listening history to recommend songs.
3. **Generative AI; generally ANI.** Generating text does not automatically establish AGI.
4. **Limited-Memory AI.** It uses recent observations to support decisions.
5. **Generative AI.** It creates an image from a prompt.
6. **Supervised Learning.** The pictures contain predefined labels.
7. **Unsupervised Learning.** The system discovers groups without predefined labels.
8. **AI agent.** It pursues a goal through multiple steps and uses tools.

The purpose is to understand what each category describes, not to force every AI system into only one category.

---

## 2.7 Common Misunderstandings About AI Types

**1. Every AI system has the same abilities.**

Reality: AI systems are designed for different purposes and have different capabilities.

**2. A powerful chatbot must be AGI.**

Reality: Performing many tasks does not automatically establish general intelligence.

**3. An AI that talks about emotions must feel them.**

Reality: Emotional language does not prove consciousness or emotional experience.

**4. All four functionality categories are established technologies.**

Reality: Reactive and limited-memory systems have practical examples. Full theory-of-mind and self-aware AI remain unestablished.

**5. Machine Learning and Generative AI mean the same thing.**

Reality: Machine Learning describes learning patterns from data, while Generative AI describes content generation.

**6. Every Machine Learning system uses deep learning.**

Reality: Deep learning is only one approach within Machine Learning.

**7. Generative AI always produces correct information.**

Reality: Generative AI can produce convincing but incorrect information, sometimes called hallucinations. Important information should be verified.

**8. Multimodal AI is the same as AGI.**

Reality: Multimodal AI describes the types of information a system processes, while AGI describes a proposed level of general intelligence.

**9. Every AI system must learn from data.**

Reality: Symbolic AI can use explicitly written rules and logical representations.

---

## 2.8 Practice Questions and Answers

### Part A: Check Your Understanding

**Q1. What is the main difference between ANI and AGI?**

A. ANI is always a robot.  
B. ANI performs specific tasks, while AGI refers to broader intellectual abilities.  
C. ANI is conscious.  
D. ANI can only calculate numbers.

**Q2. Which category describes a hypothetical AI that surpasses human intellectual abilities across many important domains?**

A. ANI  
B. AGI  
C. ASI  
D. Reactive Machines

**Q3. What is the difference between reactive machines and limited-memory AI?**

**Q4. What are the three common Machine Learning approaches?**

**Q5. What is the difference between Machine Learning and deep learning?**

**Q6. Explain the difference between discriminative and generative models.**

### Part B: Apply the Ideas

**Q7.** A company develops an AI system that detects damaged products on a factory conveyor belt. Which capability category best describes it?

**Q8.** A hypothetical AI can reason about what different people believe and know. Which functionality category does this resemble?

**Q9.** An AI system generates pictures from text instructions. Which perspectives introduced in this chapter can describe it?

**Q10.** A program uses predefined rules to identify possible causes of machine failure. Which AI approach does this illustrate?

**Q11.** An AI system receives a photograph and a voice instruction. Which AI perspective does this illustrate?

**Q12.** Why does the ability to generate convincing text not prove that an AI has consciousness?

### Answers and Explanations

**A1. B.** ANI performs specific or limited tasks, while AGI refers to broad intellectual abilities.

**A2. C.** ASI describes a hypothetical AI that surpasses human intellectual abilities across many domains.

**A3.** Reactive machines respond to current information. Limited-memory AI can use previous observations or stored information.

**A4.** Supervised learning, unsupervised learning, and reinforcement learning.

**A5.** Machine Learning is a broad approach to learning patterns from data. Deep learning uses multi-layer neural networks.

**A6.** Discriminative models classify or predict, while generative models produce new content or data.

**A7. ANI.** It is designed for a specific task: detecting damaged products.

**A8. Theory-of-Mind AI.** It describes the proposed ability to reason about other people's mental states.

**A9.** It may be ANI under the capability framework, use Machine Learning, and qualify as Generative AI because it creates images.

**A10. Symbolic AI or a rule-based system.** It uses explicitly written rules to reach conclusions.

**A11. Multimodal AI.** It processes different types of information, including images and audio.

**A12.** Producing convincing language does not demonstrate subjective experience or consciousness. Language generation and consciousness are separate questions.

---

## 2.9 Summary and References

### Key Takeaways

- AI can be classified according to capability, functionality, learning approach, and application.
- ANI is established in current applications, while AGI and ASI remain unconfirmed or hypothetical.
- The commonly taught functionality framework includes reactive machines, limited-memory AI, theory-of-mind AI, and self-aware AI.
- Machine Learning allows systems to learn patterns from data.
- Supervised, unsupervised, and reinforcement learning are three common learning approaches.
- Deep learning uses neural networks with multiple layers.
- Generative AI creates content, while discriminative models focus on classification or prediction.
- Symbolic AI uses explicit knowledge and rules.
- Multimodal AI processes multiple types of information.
- AI agents pursue goals through planning and actions.
- One AI system can be described through several perspectives.
- AI outputs can be incorrect and should be verified when accuracy matters.

### References

IBM. (n.d.). *Understanding the different types of artificial intelligence*. IBM Think.  
https://www.ibm.com/think/topics/artificial-intelligence-types

IBM. (n.d.). *What is Machine Learning?* IBM Think.  
https://www.ibm.com/think/topics/machine-learning

National Institute of Standards and Technology. (n.d.-a). *Machine learning*. CSRC Glossary.  
https://csrc.nist.gov/glossary/term/machine_learning

National Institute of Standards and Technology. (n.d.-b). *Generative artificial intelligence*. CSRC Glossary.  
https://csrc.nist.gov/glossary/term/generative_artificial_intelligence

National Institute of Standards and Technology. (2024). *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1).*  
https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf

Google for Developers. (n.d.). *What is Machine Learning?*  
https://developers.google.com/machine-learning/intro-to-ml/what-is-ml

Google for Developers. (n.d.). *Machine Learning Crash Course*.  
https://developers.google.com/machine-learning/crash-course/

Stanford Institute for Human-Centered Artificial Intelligence. (n.d.-a). *What is artificial intelligence (AI)?*  
https://hai.stanford.edu/ai-definitions/what-is-artificial-intelligence-ai

Stanford Institute for Human-Centered Artificial Intelligence. (n.d.-b). *What is AGI (artificial general intelligence)?*  
https://hai.stanford.edu/ai-definitions/what-is-agi-artificial-general-intelligence

Stanford Institute for Human-Centered Artificial Intelligence. (n.d.-c). *What is Machine Learning (ML)?*  
https://hai.stanford.edu/ai-definitions/what-is-machine-learning

Stanford Institute for Human-Centered Artificial Intelligence. (n.d.-d). *What is Generative AI?*  
https://hai.stanford.edu/ai-definitions/what-is-generative-ai

Stanford Institute for Human-Centered Artificial Intelligence. (n.d.-e). *What is Multimodal AI?*  
https://hai.stanford.edu/ai-definitions/what-is-multimodal-ai

Google Cloud. (n.d.). *What are AI agents?*  
https://cloud.google.com/discover/what-are-ai-agents

---

**Draft completion note:** This version is a condensed Stage 2 revision of the approved Stage 1 baseline. The two findings from QR-002-I02 have been addressed in the draft: the Machine Learning and Generative AI relationship is presented separately, and more topic-specific references have been added. Final Markdown rendering, reference destinations, and the revised diagram still require verification before approval.
