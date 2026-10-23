# Chapter 2: Types of Artificial Intelligence

Status: Drafted (V1.0), awaiting peer review Author: Gandhi Bestin Dhammananda | Reviewer: Brian Djoni Suzanna Audience: Complete beginners. No programming or AI background needed.

## Learning Outcomes

After completing this chapter, readers should be able to:

- Explain why AI can be classified in different ways.
- Describe the capability-based categories: ANI, AGI, and ASI.
- Explain the four commonly discussed functionality-based categories.
- Distinguish Machine Learning from Generative AI.
- Explain how capability, functionality, Machine Learning, and Generative AI describe different aspects of AI.
- Classify familiar AI applications and justify their choices.
- Recognize the limitations of simplified AI classification frameworks.

## Chapter Map

| Section | Topic | Estimated time |
| --- | --- | --- |
| 2.1 | Introduction to AI Classification | 3 min |
| 2.2 | AI Based on Capability | 8 min |
| 2.3 | AI Based on Functionality | 10 min |
| 2.4 | Machine Learning and Generative AI | 8 min |
| 2.5 | Comparing the Classification Frameworks | 5 min |
| 2.6 | Classification Activity | 5 min |
| 2.7 | Common Misunderstandings | 3 min |
| 2.8 | Practice Questions and Answers | 10 min |
| 2.9 | Summary and References | 3 min |
| **Total** |  | **55 min** |

## 2.1 Introduction to AI Classification

In Chapter 1, we learned that Artificial Intelligence (AI) allows computers to perform tasks that normally require human intelligence. Examples include recognizing images, answering questions, detecting spam, and recommending videos.

However, AI systems differ in their abilities, designs, and uses of information. A spam filter has a different purpose from a conversational assistant, and a system that generates images performs a different task from one that predicts whether a transaction is suspicious.

To understand these differences, we use classification systems.

A classification system groups things according to shared characteristics. For example, animals can be classified by their habitats or diets. Similarly, AI systems can be described according to their capabilities, functionality, learning methods, or intended outputs.

This chapter introduces four useful perspectives:

1. **Capability:** How broadly can an AI system perform intellectual tasks?
2. **Functionality:** How does an AI system behave or use information, according to a commonly taught classification framework?
3. **Machine Learning:** How does a system learn patterns from data?
4. **Generative AI:** What kind of output can a system create?

These perspectives answer different questions. They are useful for introductory learning, but they do not form one universally standardized scientific taxonomy. The categories may overlap, and the best description of a system depends on its design and the framework being used (IBM, n.d.; Stanford HAI, n.d.-a).

## 2.2 AI Based on Capability

Capability refers to the range and level of tasks an AI system can perform. A commonly used capability framework distinguishes three categories:

- Artificial Narrow Intelligence (ANI)
- Artificial General Intelligence (AGI)
- Artificial Superintelligence (ASI)

These categories describe different levels of possible intellectual capability. They should not be understood as three equally developed technologies (IBM, n.d.; Stanford HAI, n.d.-b).

### 2.2.1 Artificial Narrow Intelligence (ANI)

Artificial Narrow Intelligence (ANI), also called narrow AI, is AI designed or developed to perform a specific task or a limited range of tasks.

Consider a calculator. It can perform calculations quickly, but it cannot automatically become a doctor, write a novel, or drive a car. Similarly, an AI system may perform its intended task very well without possessing general intelligence.

The term _weak AI_ is sometimes used for ANI. Weak does not necessarily mean poor performance. It refers to the limited scope of the system's abilities.

**Examples of ANI**

- **Facial recognition:** Compares facial information to help identify or verify a person.
- **Spam detection:** Identifies suspicious emails.
- **Recommendation systems:** Suggests videos, music, or products based on relevant information.
- **Conversational AI:** Answers questions, summarizes text, and assists with writing.
- **Image generation:** Produces images in response to instructions.

**Main characteristics**

- Performs a particular task or range of tasks.
- May outperform people on its intended task.
- Can still make mistakes.
- Does not automatically gain general intelligence by performing multiple tasks.

Modern conversational AI can handle many different requests, but this breadth alone does not establish that a system meets a particular definition of AGI. Current AI systems are generally discussed as narrow AI under this framework (IBM, n.d.; Stanford HAI, n.d.-a).

### 2.2.2 Artificial General Intelligence (AGI)

Artificial General Intelligence (AGI) refers to a proposed form of AI with broad, flexible intellectual abilities, potentially comparable to or exceeding human abilities across a wide range of tasks.

Imagine someone who learns to cook and then applies their general problem-solving abilities to learn a language, repair a bicycle, or plan a journey. AGI aims for similarly broad abilities to learn, reason, and transfer knowledge between different situations.

A system that meets a strong definition of AGI might be able to:

- Learn unfamiliar intellectual tasks with limited task-specific preparation.
- Apply knowledge from one area to another.
- Solve new problems it has not encountered before.
- Adapt flexibly to different situations.

Researchers and organizations do not all agree on the exact requirements for AGI, and there is no universally accepted test for establishing that a system has achieved it (Stanford HAI, n.d.-b).

For this chapter, AGI is treated as a proposed level of general intelligence whose achievement has not been universally confirmed.

### 2.2.3 Artificial Superintelligence (ASI)

Artificial Superintelligence (ASI) refers to a hypothetical form of AI that would surpass human intellectual abilities across many or most important domains.

The distinction is:

- **AGI:** Broad intellectual abilities comparable to humans, under a given definition.
- **ASI:** Intellectual abilities that surpass human abilities across many important domains.

A hypothetical ASI might solve difficult scientific problems, develop mathematical ideas, and plan complex projects beyond the abilities of the best human experts.

These are possible future scenarios, not descriptions of an AI system known to exist today.

If such a system were developed, it might offer scientific and social benefits, but it could also raise concerns about safety, control, accountability, and the consequences of its decisions. Its effects would depend on how it was designed, managed, and used.

ASI remains hypothetical. High performance does not automatically imply consciousness, emotions, or self-awareness; these are separate questions.

### 2.2.4 Comparing ANI, AGI, and ASI

| Feature | ANI | AGI | ASI |
| --- | --- | --- | --- |
| Main idea | Specific or limited tasks | Broad, flexible intellectual abilities | Intellectual abilities beyond humans across many domains |
| Scope | A defined or learned range of tasks | Broad and adaptable | Hypothetically beyond human capabilities in many areas |
| Status | Established in current AI applications | No universally accepted confirmation of achievement | Hypothetical |
| Example | Spam filter or facial recognition system | Hypothetical system with broad, flexible learning | Hypothetical system surpassing human experts across many fields |

**Key takeaway:** ANI is widely used today. AGI and ASI describe broader levels of possible capability whose achievement has not been universally established.

## 2.3 AI Based on Functionality

A second commonly taught framework groups AI into four categories according to how systems respond to information and their proposed cognitive characteristics:

1. Reactive Machines
2. Limited-Memory AI
3. Theory-of-Mind AI
4. Self-Aware AI

These categories are useful teaching concepts, not a universally standardized technical taxonomy. Actual systems may have more complex architectures and behaviors than these introductory descriptions suggest (IBM, n.d.).

### 2.3.1 Reactive Machines

Reactive machines are systems that respond to current inputs without relying on stored memories of past events to guide decisions in the way described by this category.

A classic example is IBM's Deep Blue chess computer, which defeated world chess champion Garry Kasparov in 1997. Deep Blue evaluated chess positions and selected moves using its computational methods. It is commonly used to illustrate reactive AI because it did not learn from a personal memory of previous games during play.

Deep Blue was technically complex. Its use as an example does not mean that every chess-playing system belongs to the same category.

**Main characteristics**

- Responds to currently available inputs.
- Does not use stored personal experiences in the way described by the limited-memory category.
- Can perform a specific task very well.
- Does not automatically gain broader abilities outside its intended task.

Reactive systems can be useful for tasks with defined conditions. However, a purely reactive system, as described here, cannot rely on a stored history of earlier situations in the way a memory-based system can.

### 2.3.2 Limited-Memory AI

Limited-Memory AI refers to systems that use previous observations, historical data, or stored contextual information when producing outputs or making decisions.

For example, a driving-assistance system may use recent sensor observations to track nearby vehicles and help determine when to slow down.

Other examples include:

- **Recommendation systems:** May use a person's earlier viewing or listening activity.
- **Conversational AI:** May use earlier messages in the same conversation.
- **Driver-assistance systems:** May use recent observations to track traffic and support decisions.

These examples illustrate different uses of past information. Not every system has the same memory design.

**An important clarification about memory**

Limited memory does not necessarily mean that information is retained for only a few seconds. Systems differ in what information they store, how long they retain it, and whether it is available in later interactions.

Using stored information is also different from learning automatically. A system may use historical records without changing its trained model. Model training and ordinary use of an existing model are distinct processes.

Many modern AI applications use historical or contextual information, but their implementations vary (IBM, n.d.).

### 2.3.3 Theory-of-Mind AI

Theory-of-Mind AI is a proposed category of AI that would understand other people's beliefs, intentions, emotions, and perspectives in a deeper and more flexible way.

For example, a teacher may recognize that a student is confused and change an explanation to help the student understand. This involves considering another person's possible mental state.

A hypothetical AI with strong theory-of-mind abilities might:

- Recognize that two people have different beliefs about the same situation.
- Consider what another person knows or does not know.
- Adjust explanations to account for another person's perspective.
- Reason about possible intentions while recognizing uncertainty.

AI systems can identify certain emotional cues or generate responses that sound empathetic. These abilities do not establish that a system understands another person's inner experience in the full human sense.

Full theory-of-mind AI, as described in this framework, remains an unestablished capability. Human emotions and intentions are complex, and systems may misinterpret words, behavior, or cultural context.

### 2.3.4 Self-Aware AI

Self-aware AI is a hypothetical form of AI that would possess meaningful awareness of its own existence and internal state.

Consider the difference between a machine that reports its battery level and a being that is aware of itself as an individual. A machine can monitor and report its battery level without this demonstrating consciousness.

A hypothetical self-aware system might possess:

- Meaningful awareness of itself as an entity.
- An understanding of its own internal states.
- Subjective experience, if consciousness is included in the definition being used.

There is no single agreed scientific definition or test for self-aware AI. There is also no widely accepted scientific demonstration that current AI systems possess consciousness or self-awareness in this strong sense.

An AI system may describe itself, monitor its performance, or produce statements such as "I think" and "I feel." Those statements alone do not prove that it has subjective experiences or a conscious sense of self.

### 2.3.5 Comparing the Four Functionality Categories

| Category | Main idea | Illustrative example | Status |
| --- | --- | --- | --- |
| Reactive Machines | Responds to current inputs without stored past experiences in the described sense | Deep Blue's chess-playing system | Classic examples exist |
| Limited-Memory AI | Uses previous observations or stored information | Driving system tracking nearby vehicles | Common in current applications |
| Theory-of-Mind AI | Would reason about other people's beliefs and perspectives | Hypothetical assistant that considers what another person knows | Full capability remains unestablished |
| Self-Aware AI | Would possess meaningful self-awareness or consciousness | Hypothetical conscious machine | Hypothetical; no accepted demonstration |

These categories describe the framework used in this chapter. They do not establish that all systems within a category share the same architecture or capabilities.

## 2.4 Machine Learning and Generative AI

Machine Learning and Generative AI are important concepts in modern AI. They describe different aspects of systems and should not be treated as additional levels in the capability framework or as extra categories in the four-part functionality framework.

### 2.4.1 What Is Machine Learning?

Machine Learning (ML) is an approach in which computer systems learn patterns from data to make predictions, classifications, recommendations, or other outputs. Instead of relying only on manually specified rules, a machine-learning model uses patterns learned during training (NIST, n.d.-a; Stanford HAI, n.d.-c).

Imagine teaching a system to distinguish between pictures of cats and dogs. Developers provide examples, and a model learns patterns that help it classify new images.

**Common applications of Machine Learning**

- **Spam detection:** Learns patterns associated with unwanted email.
- **Recommendation systems:** Uses relevant activity and other data to suggest content.
- **Fraud detection:** Identifies transactions that appear suspicious.
- **Image recognition:** Classifies or detects objects in pictures.
- **Forecasting:** Uses data to predict possible future values.

Machine Learning does not guarantee accurate results. Models depend on the quality and suitability of their data, training methods, and evaluation.

**How is ML related to AI?**

AI is the broader field. Machine Learning is one approach used to develop AI systems. Not every AI method necessarily uses Machine Learning, and not every machine-learning application is a content-generation system.

### 2.4.2 What Is Generative AI?

Generative AI (GenAI) refers to AI systems that create new content, such as text, images, audio, video, or computer code. These systems learn patterns from data and use them to produce new outputs (NIST, n.d.-b; Stanford HAI, n.d.-d).

Examples include:

- **Text generation:** Drafts explanations, stories, or summaries.
- **Image generation:** Creates pictures from text instructions.
- **Audio generation:** Produces speech or music.
- **Code generation:** Suggests or creates computer code.
- **Video generation:** Produces video content from prompts or other inputs.

Generative AI can produce useful and convincing content, but its output may contain factual errors, misleading information, or unsuitable material. Generated content should be checked when accuracy matters.

Generating content also does not prove that a system understands it as a human would or possesses consciousness.

### 2.4.3 How Are ML and Generative AI Different?

| Feature | Machine Learning | Generative AI |
| --- | --- | --- |
| What does it describe? | An approach for learning patterns from data | AI systems designed to generate content |
| Common outputs | Predictions, classifications, recommendations, and other results | Text, images, audio, video, code, and other content |
| Example | Predicting whether an email is spam | Generating an image from a text prompt |
| Relationship to AI | A major approach used to develop AI systems | A category of AI systems focused on generating content |
| Can they overlap? | Yes | Yes; many generative AI systems use Machine Learning |

**Key takeaway:** Machine Learning describes how a system learns patterns from data. Generative AI describes a type of system that creates content. Many generative AI systems use Machine Learning, but ML also supports applications that do not generate content.

## 2.5 Comparing the Classification Frameworks

The four perspectives discussed in this chapter answer different questions.

- **Capability:** How broad are the system's intellectual abilities?
- **Functionality:** How does it respond to information, or what proposed cognitive features does it illustrate?
- **Machine Learning:** Does it learn patterns from data using a machine-learning approach?
- **Generative AI:** Does it generate new content?

These perspectives are related, but they are not interchangeable. They also do not form one standardized hierarchy.

### 2.5.1 A Simplified Relationship Diagram

```
                     ARTIFICIAL INTELLIGENCE
                               |
             +-----------------+------------------+
             |                 |                  |
        CAPABILITY        FUNCTIONALITY      APPROACH / OUTPUT
             |                 |                  |
        ANI, AGI, ASI    Four commonly       Machine Learning
                         taught categories        |
                                              Generative AI
                                           (often uses ML)
```

**How to read the diagram**

- The capability and functionality frameworks describe AI from different perspectives.
- Machine Learning describes an approach to learning patterns from data.
- Generative AI describes systems that produce content and often use Machine Learning.
- The diagram is a simplified teaching aid, not a formal taxonomy. Its branches do not represent mutually exclusive categories, and Machine Learning and Generative AI are not subdivisions of the capability framework.

### 2.5.2 Applying the Four Perspectives

Consider a conversational AI system that can answer questions, summarize reports, and generate stories.

- **Capability:** It may be described as ANI under the framework used in this chapter; its broad performance alone does not establish AGI.
- **Functionality:** Its classification depends on how it uses inputs, context, and stored information. A chatbot should not automatically be assigned a category solely because it produces conversational responses.
- **Machine Learning:** It may use models trained on data to produce its outputs.
- **Generative AI:** It qualifies as generative AI when it generates content such as text or stories.

This example shows why one system can be described from several perspectives without those descriptions contradicting one another.

## 2.6 Classification Activity

**Instructions:** Read each example. Identify the most suitable category or perspective and explain your choice in one or two sentences. Some examples can fit more than one perspective.

| No. | Familiar application | Your task |
| --- | --- | --- |
| 1 | An email service identifies suspicious messages and moves them into a spam folder. | Identify its capability category and explain whether it may use ML. |
| 2 | A music application recommends songs based on listening history. | Explain how ML and stored information may be involved. |
| 3 | A chatbot writes a birthday greeting and summarizes a report. | Identify whether it is generative AI and explain why this does not automatically establish AGI. |
| 4 | A driving-assistance system uses recent observations of nearby cars to help determine when to slow down. | Identify the functionality category illustrated by its use of recent observations. |
| 5 | A tool creates an image from the instruction "Draw a house beside a lake." | Identify the type of output and explain how it relates to Generative AI. |
| 6 | A hypothetical AI reasons reliably about what different people believe and know. | Identify the proposed functionality category and state whether the full capability is established. |

### Suggested Answers and Explanations

1. **ANI; possibly ML.** The system performs a specific task. It may use a machine-learning model trained to recognize patterns in spam, although not every spam filter must use ML.
2. **ANI; potentially ML and stored information.** A recommendation system may learn patterns from listening activity and use historical data to suggest songs. Its exact design determines how it works.
3. **Generative AI; generally ANI under this chapter's framework.** The chatbot generates text, but the ability to perform several language tasks does not automatically establish AGI.
4. **Limited-Memory AI.** The example illustrates the use of recent observations to support decisions. Actual driving systems vary in design.
5. **Generative AI.** The tool generates an image from a prompt. This describes its output, not its general level of intelligence.
6. **Theory-of-Mind AI.** The example describes a proposed ability to reason about other people's mental states. Full theory-of-mind capability, in the sense used here, remains unestablished.

The purpose of this activity is not to force every application into a single label. It is to practise explaining which aspect of an AI system a category describes.

## 2.7 Common Misunderstandings About AI Types

### Misunderstanding 1: Every AI system has the same abilities.

**Reality:** AI systems are designed for different purposes. A spam filter and a conversational assistant have different tasks and capabilities.

### Misunderstanding 2: A powerful chatbot must be AGI.

**Reality:** A chatbot may handle many types of requests, but broad performance alone does not establish AGI. The definition and assessment criteria matter (Stanford HAI, n.d.-b).

### Misunderstanding 3: An AI that talks about emotions must feel them.

**Reality:** Generating emotional language does not prove that a system has emotional experiences or consciousness.

### Misunderstanding 4: All four functionality categories are established technologies.

**Reality:** Reactive and limited-memory systems have practical examples. Full theory-of-mind and self-aware AI, as described in this chapter, remain unestablished.

### Misunderstanding 5: Machine Learning and Generative AI mean the same thing.

**Reality:** Machine Learning is an approach to learning patterns from data. Generative AI describes systems that generate content. Many generative AI systems use ML, but the terms are not interchangeable (NIST, n.d.-a, n.d.-b).

### Misunderstanding 6: Every AI system belongs to exactly one category.

**Reality:** A system may be described from multiple perspectives. For example, a generative AI application may use Machine Learning and still be considered ANI under the capability framework.

## 2.8 Practice Questions and Answers

### Part A: Check Your Understanding

**Q1. What is the main difference between ANI and AGI?**

A. ANI is always a robot, while AGI is always software.

B. ANI is designed for specific or limited tasks, while AGI refers to broader, general intellectual abilities.

C. ANI is conscious, while AGI is not.

D. ANI can only perform calculations.

**Q2. Which capability category describes a hypothetical AI that surpasses human intellectual abilities across many important domains?**

A. ANI

B. AGI

C. ASI

D. Reactive Machines

**Q3. Why should we be careful when someone claims that an AI system has achieved AGI?**

**Q4. What is the main difference between reactive machines and limited-memory AI?**

**Q5. Does an AI system that says "I feel sad" prove that it has emotions? Explain your answer.**

### Part B: Apply the Ideas

**Q6.** A company creates an AI system that detects damaged products on a factory conveyor belt. Which capability category best describes this system, and why?

**Q7.** A driving system uses recent observations of nearby vehicles to help decide when to slow down. Which functionality category does this illustrate?

**Q8.** Imagine a future AI that could reliably consider what different people believe, what information they have, and why they may act differently. Which functionality category would this resemble? Is the full capability established in current AI?

**Q9.** A conversational assistant can write stories, answer questions, and summarize reports. Does this automatically make it AGI? Explain why or why not.

**Q10.** Explain in your own words why capability classification and functionality classification are different.

**Q11.** Explain the difference between Machine Learning and Generative AI. Give one example of each.

**Q12.** An AI system uses Machine Learning to generate pictures from text instructions. Which of the four perspectives introduced in this chapter describe it, and what does each perspective tell us?

### Answers and Explanations

**A1. B.** ANI is designed for specific or limited tasks, while AGI refers to broad intellectual abilities across different tasks and domains.

**A2. C.** ASI describes a hypothetical AI that would surpass human intellectual abilities across many or most relevant domains.

**A3.** There is no universally accepted definition or test for AGI. A system may perform well on many tasks without satisfying every proposed definition of general intelligence.

**A4.** A reactive machine responds to current information without relying on stored past experiences in the way described by this category. Limited-memory AI can use earlier observations or stored information to guide outputs or decisions.

**A5.** No. Producing words about emotions does not prove that a system experiences them. Language output and consciousness are different questions.

**A6. ANI.** The system is designed for a specific task: detecting damaged products. Performing that task well does not establish general intelligence.

**A7. Limited-Memory AI.** The example uses recent observations over time to help make a decision.

**A8. Theory-of-Mind AI.** The example describes the proposed ability to reason about people's beliefs and perspectives. The full capability described here has not been established in current AI.

**A9.** No. Handling several kinds of requests does not automatically establish AGI. The system must be assessed against a clear definition of general intelligence, and no universally accepted test exists.

**A10.** Capability classification describes how broadly an AI system can perform intellectual tasks. Functionality classification describes behavior, information use, or proposed features such as understanding other minds and self-awareness.

**A11.** Machine Learning is an approach in which systems learn patterns from data; a spam detector is one example. Generative AI produces content; an image generator is one example. Many generative AI systems use Machine Learning.

**A12.** All four perspectives can be relevant. Capability classification may describe the system as ANI if its abilities remain within the narrow-AI framework. Functionality classification depends on how it uses information and memory. Machine Learning describes how it learns patterns from data. Generative AI describes its ability to produce images.

## 2.9 Summary and References

### Key Takeaways

- AI can be classified in different ways because systems have different abilities, designs, and purposes.
- The capability framework distinguishes ANI, AGI, and ASI.
- ANI is established in current practical applications. AGI has no universally accepted confirmation of achievement, and ASI remains hypothetical.
- The commonly taught functionality framework distinguishes reactive machines, limited-memory AI, theory-of-mind AI, and self-aware AI.
- Reactive and limited-memory systems have practical examples. Full theory-of-mind and self-aware AI remain unestablished in the senses described here.
- Machine Learning is an approach to learning patterns from data.
- Generative AI describes systems that generate content such as text, images, audio, video, and code.
- Many generative AI systems use Machine Learning, but the terms describe different aspects of AI.
- One system can be described through multiple perspectives. No single framework explains every aspect of an AI system.
- Fluent language, broad task performance, or statements about feelings do not by themselves establish AGI, emotions, or consciousness.

### References

IBM. (n.d.). _Understanding the different types of artificial intelligence_. IBM Think. [https://www.ibm.com/think/topics/artificial-intelligence-types](<https://www.ibm.com/think/topics/artificial-intelligence-types>)

National Institute of Standards and Technology. (n.d.-a). _Machine learning_. CSRC Glossary. [https://csrc.nist.gov/glossary/term/ml](<https://csrc.nist.gov/glossary/term/ml>)

National Institute of Standards and Technology. (n.d.-b). _Generative artificial intelligence_. CSRC Glossary. [https://csrc.nist.gov/glossary/term/generative\_artificial\_intelligence](<https://csrc.nist.gov/glossary/term/generative_artificial_intelligence>)

Stanford Institute for Human-Centered Artificial Intelligence. (n.d.-a). _What is artificial intelligence (AI)?_ [https://hai.stanford.edu/ai-definitions/what-is-artificial-intelligence-ai](<https://hai.stanford.edu/ai-definitions/what-is-artificial-intelligence-ai>)

Stanford Institute for Human-Centered Artificial Intelligence. (n.d.-b). _What is AGI (artificial general intelligence)?_ https://hai.stanford.edu/ai-definitions/what-is-agi-artificial-general-intelligence

Stanford Institute for Human-Centered Artificial Intelligence. (n.d.-c). _Machine learning_. Artificial Intelligence Glossary. https://hai.stanford.edu/ai-definitions

Stanford Institute for Human-Centered Artificial Intelligence. (n.d.-d). _Generative AI_. Artificial Intelligence Glossary. https://hai.stanford.edu/ai-definitions

