# Module Outline and Development Status

> **Project:** Babi Guling – AI Overview  
> **Module:** AI Overview (Introduction to Computer Science and Artificial Intelligence)  
> **Intended learners:** Beginners with no background in AI or programming. Learners need only basic computer and internet literacy.  
> **Version:** v4.0 (Stage 2: Markdown V2.0 of all four chapters, rewritten around the lecturer's topics)  
> **Last updated:** 2026-11-05

## Structure of the Module

The module has **four chapters, one for each course chapter provided by the lecturer**. Each chapter takes its title and the order of its topics from the lecturer's slides. Stage 1 gave the structure and a first version (1.1) of every chapter. Stage 2 develops each chapter into **Markdown V2.0**: it keeps the lecturer's topics in the lecturer's order and explains each of them in full.

The four chapters tell one story. Chapter 1 gives the words and the map. Chapter 2 shows the first way of building AI, in which people write the rules. Chapter 3 shows the second way, in which the machine learns the rules from data (and where the data comes from). Chapter 4 shows the third way, in which the machine learns by trying actions and receiving rewards. Each chapter opens with a section called *Where This Chapter Fits* that says what was learned before, what is learned now, and what comes next.

| Our chapter | Title | Course source (lecturer's slides) | Study time |
|---|---|---|---|
| 1 | Introduction to CS and AI | chap1: Intro to CS and AI | 3 h |
| 2 | Symbolic AI | chap4: Symbolic AI | 4.5 h |
| 3 | Connectionist AI and Big Data | chap5: Connectionist AI and Big Data Overview | 6 h |
| 4 | Behaviorist AI | chap6: Behaviorist AI | 5 h |

## Module Learning Outcomes

After completing this module, learners should be able to:

1. Define Computer Science and Artificial Intelligence, describe their history and main areas, and explain the three families of machine learning.
2. Explain Symbolic AI: logic, knowledge representation, rule-based and expert systems, planning and search, and symbolic natural language processing, with its benefits and limits.
3. Explain Connectionist AI (neurons, learning, architectures, deep learning) and Big Data (the Vs, technologies, processing, visualization, ethics).
4. Explain Behaviorist AI: reinforcement learning, Markov decision processes, algorithms such as Q-learning, applications in robotics and games, and its challenges.
5. Compare the three approaches, match them to suitable applications, and identify typical risks of each (wrong rules, biased data, reward hacking, privacy).

Chapter 1 supports outcome 1, Chapter 2 outcome 2, Chapter 3 outcome 3, and Chapter 4 outcome 4. Outcome 5 is supported by the closing sections of Chapters 3 and 4, and above all by the *Module Wrap-Up* in Chapter 4.

## Development Status Labels

| Label | Meaning |
|---|---|
| **Outline only** | The structure exists, but explanations are not developed. |
| **Drafted** | Substantive content is written in the chapter's Markdown file, but no signed review exists. |
| **Checked** | A review report signed by the reviewer exists for the current version. |
| **Needs revision** | A review found unresolved issues. |

A chapter may be marked **Checked** only when a signed review report exists. The "Verified by / date" column records who confirmed the status and when.

## Chapter Overview

| Chapter | Title | Version | Status | Verified by / date | Words (approx.) | Lecturer's topics | Figures (numbered) | "Check yourself" questions | Hands-on activities | Practice questions | References | Author | Reviewer |
|---|---|---|---|---|--:|--:|--:|--:|--:|--:|--:|---|---|
| 1 | Introduction to CS and AI | 2.0 | Drafted | Awaiting Quality Lead | 12,254 | 5 | 14 | 14 | 3 | 17 | 12 | Jonathan Sugianto | Brian Djoni Suzanna |
| 2 | Symbolic AI | 2.0 | Drafted | Awaiting Quality Lead | 12,959 | 6 | 13 | 18 | 2 | 17 | 11 | Gandhi Bestin Dhammananda | Brian Djoni Suzanna |
| 3 | Connectionist AI and Big Data | 2.0 | Drafted | Awaiting Quality Lead | 15,067 | 12 | 22 | 22 | 1 | 17 | 13 | Benedict Subhata | Brian Djoni Suzanna |
| 4 | Behaviorist AI | 2.0 | Drafted | Awaiting Quality Lead | 10,891 | 7 | 17 | 12 | 1 | 17 | 11 | Joseph Lokman | Brian Djoni Suzanna |
| **Total** | | | | | **51,171** | **30** | **66** | **66** | **7** | **68** | **47** | | |

The authors are proposed owners and can be changed by the team. Counts were taken from the files on 5 November 2026 by a script. Word counts include tables, answers, the glossary, and the references. Chapter 3 has 12 topics because the lecturer's slides have two groups of six (Part A: Connectionist AI; Part B: Big Data). A chapter may be marked **Checked** only when a signed review report exists for the current version. The earlier "Checked" labels applied to the old five-chapter version and do not apply here.

## How Each Chapter Is Written

The chapters are meant to be read on GitHub by a person who has never studied AI. Every chapter is written the same way, so that a learner who has finished Chapter 1 knows how to read Chapters 2, 3, and 4.

| Part | What it does |
|---|---|
| **Header block, navigation, contents** | The module, chapter, version, author, reviewer, audience, study time, and the lecturer's slide set it follows. A table links to the previous and next chapter. A collapsed contents list links to every section. |
| **Where This Chapter Fits** | A figure of the four chapters with the current one highlighted, and a table with three columns: *Before this chapter* (what you already know), *In this chapter* (what is new), and *In the next chapter* (what it leads to). It replaces the roadmap of earlier versions. A reader always knows "previously this, now this, next that". |
| **What You Will Learn** | A short list of outcomes, each pointing to the topic that teaches it. |
| **Topics, in the lecturer's order** | Each topic opens with a question the reader can already imagine, then explains the idea in plain sentences with one running example. Every figure is followed by a paragraph called **How to read this figure**, which says what each part of the picture means. Each topic ends with one to three *Check yourself* questions (the answer is hidden until the reader opens it) and a short **In short** box. |
| **Hands-On Activity** | A small task that can be done with pen and paper, written so that the reader does the steps and sees the result. |
| **Common Misconceptions, Key Takeaways** | The frequent mistakes with the correct idea, and the main points to remember. |
| **Practice Questions and Answer Key** | Seventeen questions per chapter in four parts: A multiple choice, B short answer, C apply it, D compute or trace. Every question has an explained answer. |
| **What Comes Next** | A short bridge that states the problem the chapter leaves open and how the next chapter answers it. Chapter 4 ends with a *Module Wrap-Up* that compares the three approaches. |
| **Key Terms in Chinese, Glossary, References** | Key terms in Chinese for readers at a Chinese university (to be checked by a Chinese-speaking teammate); a glossary; linked references, each with its check status. |

**What is deliberately not in the chapters.** There are no games, no mascot, no emoji, and no interactive pages. There are no optional deep-dive or case-study sections stacked on top of the lecturer's topics; real examples are placed inside the topic where they explain something. Sub-sections are kept few, so that the reader can see the path through a chapter. Exercises are fewer than in earlier versions, and each one belongs to the idea it practises.

## What Changed in This Edition

This edition replaces the first Stage 2 packages. The lecturer's feedback on 5 November 2026 was that earlier versions were hard to understand, explained too little, had too many numbered sub-sections, a weak roadmap, and mostly exercises. The changes are listed in the [Stage 2 Revision Summary](stage2-revision-summary.md). In short: the chapters follow the lecturer's topics exactly; each topic is explained at length before any exercise; "Where This Chapter Fits" replaces the roadmap; every figure is explained in words; and the exercises are fewer.

## Topics of Each Chapter

The headings below are the sections of each chapter, in order. The topics follow the lecturer's slides.

### Chapter 1: Introduction to CS and AI

| # | Section | What it covers |
|--:|---|---|
| 1 | [Where This Chapter Fits](study-guide/v2.0/chapter-1-introduction-to-cs-and-ai/introduction-to-cs-and-ai.md#where-this-chapter-fits) | Before, now, and next; how the four chapters connect |
| 2 | [What You Will Learn](study-guide/v2.0/chapter-1-introduction-to-cs-and-ai/introduction-to-cs-and-ai.md#what-you-will-learn) | Outcomes of the chapter |
| 3 | [Topic 1: Computer Science](study-guide/v2.0/chapter-1-introduction-to-cs-and-ai/introduction-to-cs-and-ai.md#topic-1-computer-science) | What CS is, a short history, a map of CS, algorithms and data |
| 4 | [Topic 2: Artificial Intelligence](study-guide/v2.0/chapter-1-introduction-to-cs-and-ai/introduction-to-cs-and-ai.md#topic-2-artificial-intelligence) | What AI is, a short history, a map of AI, AI versus machine learning versus deep learning |
| 5 | [Topic 3: Machine Learning, a First Look](study-guide/v2.0/chapter-1-introduction-to-cs-and-ai/introduction-to-cs-and-ai.md#topic-3-machine-learning-a-first-look) | Learning from examples, three families, training and testing, nearest neighbour, what can go wrong |
| 6 | [Topic 4: Hands-On Activity, Machine Learning](study-guide/v2.0/chapter-1-introduction-to-cs-and-ai/introduction-to-cs-and-ai.md#topic-4-hands-on-activity-machine-learning) | Rock Paper Scissors, Smart Classroom, nearest neighbour |
| 7 | [Topic 5: Using an AI Assistant for Study](study-guide/v2.0/chapter-1-introduction-to-cs-and-ai/introduction-to-cs-and-ai.md#topic-5-using-an-ai-assistant-for-study) | Questions to ask an AI assistant and how to check its answers |
| 8 | [Common Misconceptions](study-guide/v2.0/chapter-1-introduction-to-cs-and-ai/introduction-to-cs-and-ai.md#common-misconceptions) | Frequent mistakes and the correct idea |
| 9 | [Key Takeaways](study-guide/v2.0/chapter-1-introduction-to-cs-and-ai/introduction-to-cs-and-ai.md#key-takeaways) | The main points |
| 10 | [Practice Questions](study-guide/v2.0/chapter-1-introduction-to-cs-and-ai/introduction-to-cs-and-ai.md#practice-questions) | 17 questions in four parts |
| 11 | [Answer Key](study-guide/v2.0/chapter-1-introduction-to-cs-and-ai/introduction-to-cs-and-ai.md#answer-key) | Explained answers |
| 12 | [What Comes Next: From Words to Rules](study-guide/v2.0/chapter-1-introduction-to-cs-and-ai/introduction-to-cs-and-ai.md#what-comes-next-from-words-to-rules) | Bridge to Chapter 2 |

### Chapter 2: Symbolic AI

| # | Section | What it covers |
|--:|---|---|
| 1 | [Where This Chapter Fits](study-guide/v2.0/chapter-2-symbolic-ai/symbolic-ai.md#where-this-chapter-fits) | Before, now, and next; how the four chapters connect |
| 2 | [What You Will Learn](study-guide/v2.0/chapter-2-symbolic-ai/symbolic-ai.md#what-you-will-learn) | Outcomes of the chapter |
| 3 | [Topic 1: Introduction to Symbolic AI](study-guide/v2.0/chapter-2-symbolic-ai/symbolic-ai.md#topic-1-introduction-to-symbolic-ai) | The symbolic idea, GOFAI, a rule example, benefits and limits |
| 4 | [Topic 2: Logic and Reasoning](study-guide/v2.0/chapter-2-symbolic-ai/symbolic-ai.md#topic-2-logic-and-reasoning) | Propositional and predicate logic, inference rules, valid and invalid reasoning |
| 5 | [Topic 3: Knowledge Representation](study-guide/v2.0/chapter-2-symbolic-ai/symbolic-ai.md#topic-3-knowledge-representation) | Logic, semantic networks, frames and scripts, rules, ontologies |
| 6 | [Topic 4: Rule-Based Systems and Expert Systems](study-guide/v2.0/chapter-2-symbolic-ai/symbolic-ai.md#topic-4-rule-based-systems-and-expert-systems) | Facts and rules, forward and backward chaining, parts of an expert system |
| 7 | [Topic 5: Planning and Problem Solving](study-guide/v2.0/chapter-2-symbolic-ai/symbolic-ai.md#topic-5-planning-and-problem-solving) | State space, BFS, DFS, A*, minimax, the size of game trees |
| 8 | [Topic 6: Natural Language Processing in Symbolic AI](study-guide/v2.0/chapter-2-symbolic-ai/symbolic-ai.md#topic-6-natural-language-processing-in-symbolic-ai) | Grammar, parse trees, meaning as logic, ELIZA |
| 9 | [Hands-On Activity: A Rule-Based Smart Classroom](study-guide/v2.0/chapter-2-symbolic-ai/symbolic-ai.md#hands-on-activity-a-rule-based-smart-classroom) | Write rules, test them, find where they break |
| 10 | [Common Misconceptions](study-guide/v2.0/chapter-2-symbolic-ai/symbolic-ai.md#common-misconceptions) | Frequent mistakes and the correct idea |
| 11 | [Key Takeaways](study-guide/v2.0/chapter-2-symbolic-ai/symbolic-ai.md#key-takeaways) | The main points |
| 12 | [Practice Questions](study-guide/v2.0/chapter-2-symbolic-ai/symbolic-ai.md#practice-questions) | 17 questions in four parts |
| 13 | [Answer Key](study-guide/v2.0/chapter-2-symbolic-ai/symbolic-ai.md#answer-key) | Explained answers |
| 14 | [What Comes Next: From Written Rules to Learned Weights](study-guide/v2.0/chapter-2-symbolic-ai/symbolic-ai.md#what-comes-next-from-written-rules-to-learned-weights) | Bridge to Chapter 3 |

### Chapter 3: Connectionist AI and Big Data

| # | Section | What it covers |
|--:|---|---|
| 1 | [Where This Chapter Fits](study-guide/v2.0/chapter-3-connectionist-ai-and-big-data/connectionist-ai-and-big-data.md#where-this-chapter-fits) | Before, now, and next; how the four chapters connect |
| 2 | [What You Will Learn](study-guide/v2.0/chapter-3-connectionist-ai-and-big-data/connectionist-ai-and-big-data.md#what-you-will-learn) | Outcomes of the chapter |
| 3 | [Part A, Topic 1: Introduction to Connectionist AI](study-guide/v2.0/chapter-3-connectionist-ai-and-big-data/connectionist-ai-and-big-data.md#part-a-topic-1-introduction-to-connectionist-ai) | Inspiration from the brain, a short history |
| 4 | [Part A, Topic 2: Basics of Neural Networks](study-guide/v2.0/chapter-3-connectionist-ai-and-big-data/connectionist-ai-and-big-data.md#part-a-topic-2-basics-of-neural-networks) | Neuron, weights, activation, layers, learning loop, gradient descent, XOR |
| 5 | [Part A, Topic 3: Architectures of Neural Networks](study-guide/v2.0/chapter-3-connectionist-ai-and-big-data/connectionist-ai-and-big-data.md#part-a-topic-3-architectures-of-neural-networks) | Feed-forward, CNN, RNN, transformers |
| 6 | [Part A, Topic 4: Deep Learning and Advanced Concepts](study-guide/v2.0/chapter-3-connectionist-ai-and-big-data/connectionist-ai-and-big-data.md#part-a-topic-4-deep-learning-and-advanced-concepts) | Depth, the 2012 breakthrough, overfitting |
| 7 | [Part A, Topic 5: Key Applications of Connectionist AI](study-guide/v2.0/chapter-3-connectionist-ai-and-big-data/connectionist-ai-and-big-data.md#part-a-topic-5-key-applications-of-connectionist-ai) | Images, speech, language, recommendation |
| 8 | [Part A, Topic 6: Ethical Considerations and Challenges](study-guide/v2.0/chapter-3-connectionist-ai-and-big-data/connectionist-ai-and-big-data.md#part-a-topic-6-ethical-considerations-and-challenges) | Bias, explainability, data needs, Gender Shades |
| 9 | [Part B, Topic 1: Introduction to Big Data](study-guide/v2.0/chapter-3-connectionist-ai-and-big-data/connectionist-ai-and-big-data.md#part-b-topic-1-introduction-to-big-data) | The five Vs and why averages hide things |
| 10 | [Part B, Topic 2: Big Data Technologies](study-guide/v2.0/chapter-3-connectionist-ai-and-big-data/connectionist-ai-and-big-data.md#part-b-topic-2-big-data-technologies) | Storage, MapReduce |
| 11 | [Part B, Topic 3: Data Processing and Analytics](study-guide/v2.0/chapter-3-connectionist-ai-and-big-data/connectionist-ai-and-big-data.md#part-b-topic-3-data-processing-and-analytics) | The data pipeline, four levels of analytics |
| 12 | [Part B, Topic 4: Data Analysis and Visualization](study-guide/v2.0/chapter-3-connectionist-ai-and-big-data/connectionist-ai-and-big-data.md#part-b-topic-4-data-analysis-and-visualization) | Choosing a chart, misleading charts |
| 13 | [Part B, Topic 5: Big Data Use Cases](study-guide/v2.0/chapter-3-connectionist-ai-and-big-data/connectionist-ai-and-big-data.md#part-b-topic-5-big-data-use-cases) | Where Big Data is used |
| 14 | [Part B, Topic 6: Big Data Ethics and Privacy](study-guide/v2.0/chapter-3-connectionist-ai-and-big-data/connectionist-ai-and-big-data.md#part-b-topic-6-big-data-ethics-and-privacy) | Re-identification, k-anonymity, the Sweeney case |
| 15 | [Hands-On Activity: A Learner You Train and Then Break](study-guide/v2.0/chapter-3-connectionist-ai-and-big-data/connectionist-ai-and-big-data.md#hands-on-activity-a-learner-you-train-and-then-break) | A word-vote learner on paper |
| 16 | [Common Misconceptions](study-guide/v2.0/chapter-3-connectionist-ai-and-big-data/connectionist-ai-and-big-data.md#common-misconceptions) | Frequent mistakes and the correct idea |
| 17 | [Key Takeaways](study-guide/v2.0/chapter-3-connectionist-ai-and-big-data/connectionist-ai-and-big-data.md#key-takeaways) | The main points |
| 18 | [Practice Questions](study-guide/v2.0/chapter-3-connectionist-ai-and-big-data/connectionist-ai-and-big-data.md#practice-questions) | 17 questions in four parts |
| 19 | [Answer Key](study-guide/v2.0/chapter-3-connectionist-ai-and-big-data/connectionist-ai-and-big-data.md#answer-key) | Explained answers |
| 20 | [What Comes Next: From Labelled Examples to Rewards](study-guide/v2.0/chapter-3-connectionist-ai-and-big-data/connectionist-ai-and-big-data.md#what-comes-next-from-labelled-examples-to-rewards) | Bridge to Chapter 4 |

### Chapter 4: Behaviorist AI

| # | Section | What it covers |
|--:|---|---|
| 1 | [Where This Chapter Fits](study-guide/v2.0/chapter-4-behaviorist-ai/behaviorist-ai.md#where-this-chapter-fits) | Before, now, and next; how the four chapters connect |
| 2 | [What You Will Learn](study-guide/v2.0/chapter-4-behaviorist-ai/behaviorist-ai.md#what-you-will-learn) | Outcomes of the chapter |
| 3 | [Topic 1: Introduction to Behaviorist AI](study-guide/v2.0/chapter-4-behaviorist-ai/behaviorist-ai.md#topic-1-introduction-to-behaviorist-ai) | Learning from consequences, where the name comes from |
| 4 | [Topic 2: Basics of Reinforcement Learning](study-guide/v2.0/chapter-4-behaviorist-ai/behaviorist-ai.md#topic-2-basics-of-reinforcement-learning) | Agent, environment, reward, return, discounting, exploration and exploitation |
| 5 | [Topic 3: RL Algorithms and Techniques](study-guide/v2.0/chapter-4-behaviorist-ai/behaviorist-ai.md#topic-3-rl-algorithms-and-techniques) | Families of methods, Q-learning, a grid world, deep RL |
| 6 | [Topic 4: Markov Decision Processes (MDPs)](study-guide/v2.0/chapter-4-behaviorist-ai/behaviorist-ai.md#topic-4-markov-decision-processes-mdps) | The five parts, policy and value, slippery moves, expected value |
| 7 | [Topic 5: Behavioral AI in Robotics and Games](study-guide/v2.0/chapter-4-behaviorist-ai/behaviorist-ai.md#topic-5-behavioral-ai-in-robotics-and-games) | Layers of behaviour, TD-Gammon, DQN, AlphaGo, AlphaZero |
| 8 | [Topic 6: Applications and Use Cases of Behaviorist AI](study-guide/v2.0/chapter-4-behaviorist-ai/behaviorist-ai.md#topic-6-applications-and-use-cases-of-behaviorist-ai) | Where RL is used, RLHF |
| 9 | [Topic 7: Challenges and Limitations](study-guide/v2.0/chapter-4-behaviorist-ai/behaviorist-ai.md#topic-7-challenges-and-limitations) | Reward hacking and eight other challenges |
| 10 | [Hands-On Activity: Train a Learner, Then Try to Fool It](study-guide/v2.0/chapter-4-behaviorist-ai/behaviorist-ai.md#hands-on-activity-train-a-learner-then-try-to-fool-it) | The corridor by hand, spotting a reward hack |
| 11 | [Module Wrap-Up: Three Ways to Build AI](study-guide/v2.0/chapter-4-behaviorist-ai/behaviorist-ai.md#module-wrap-up-three-ways-to-build-ai) | Comparison of the three approaches |
| 12 | [Common Misconceptions](study-guide/v2.0/chapter-4-behaviorist-ai/behaviorist-ai.md#common-misconceptions) | Frequent mistakes and the correct idea |
| 13 | [Key Takeaways](study-guide/v2.0/chapter-4-behaviorist-ai/behaviorist-ai.md#key-takeaways) | The main points |
| 14 | [Practice Questions](study-guide/v2.0/chapter-4-behaviorist-ai/behaviorist-ai.md#practice-questions) | 17 questions in four parts |
| 15 | [Answer Key](study-guide/v2.0/chapter-4-behaviorist-ai/behaviorist-ai.md#answer-key) | Explained answers |
| 16 | [Where to Go Next](study-guide/v2.0/chapter-4-behaviorist-ai/behaviorist-ai.md#where-to-go-next) | Where to take the module further |

## Stage 2 Requirements and Where the Markdown Meets Them

| Requirement | Where it is met | Status |
|---|---|---|
| Overview and learning outcomes | *Where This Chapter Fits* and *What You Will Learn* in each chapter | Present |
| Order of topics and explained terms | The lecturer's order in each chapter; terms explained where first used; glossary in each chapter and a [shared glossary](study-guide/v2.0/shared-glossary.md) | Present |
| Worked examples | Throughout: binary conversion, nearest neighbour, truth tables, forward chaining, the farmer–wolf–goat–cabbage search, a neuron by hand, gradient descent, a perceptron learning OR, backpropagation on the smallest network, Q-learning, expected value | Present; numbers recomputed by script |
| Visuals (diagrams or tables) | 66 numbered PNG figures (list below), each with a "How to read this figure" paragraph, plus tables | Present; GitHub rendering to confirm |
| Activities with checked answers | 7 hands-on activities, 66 *Check yourself* questions, and 68 practice questions with explained answers | Key numbers recomputed by script on 5 November 2026; the reviewer must confirm |
| References | 47 references; every reference except the lecturer's slides has a link | Most links not yet opened; see the reference register |
| No placeholders or promises | A search for TODO, TBD, "will be added", and similar found none on 5 November 2026 | Present |
| Example and practice in every major topic | Each topic has an example and at least one *Check yourself* question, or is practised in the hands-on activity | Present |
| Continuity between chapters | *Where This Chapter Fits*, *What Comes Next*, shared terms, and the Smart Classroom thread (Chapters 1, 2, 3) | Present; reviewer to confirm |
| Checked by someone other than the author | QR-221-I01 to QR-224-I01 | **Pending Review** |

## Hands-On Activities and Practice (inventory)

| Chapter | Hands-on activities | Practice questions (A + B + C + D) | "Check yourself" |
|--:|---|---|--:|
| 1 | 3 (A Rock Paper Scissors, B Smart Classroom, C optional nearest neighbour) | 8 + 3 + 1 + 5 = 17 | 14 |
| 2 | 2 (A exact-match rules then "contains" rules; B repair the rules, then break them again) | 8 + 4 + 2 + 3 = 17 | 18 |
| 3 | 1 in three steps (train a word-vote learner, classify new sentences, fix it with more examples and look again) | 9 + 3 + 2 + 3 = 17 | 22 |
| 4 | 1 in two parts (train the corridor by hand; spot the reward hack) | 9 + 3 + 2 + 3 = 17 | 12 |

Every activity has a version that needs no software, so no learner is blocked by a tool that is missing. Chapter 1 mentions the lecturer's block-based tool and two optional online tools as alternatives. Those tools were not run while the chapter was written.

## Figures and Assets

Every diagram is a PNG file. Each chapter keeps its figures in an `assets/` folder next to its Markdown file, and the Markdown links to them with a relative path such as `assets/fig-2-5-semantic-network.png`. The file names below are exact. Keep them unchanged when uploading to GitHub, because GitHub paths are case-sensitive.

| Figure | File name | Shows | Folder |
|---|---|---|---|
| 1.1 | `fig-1-1-how-the-chapters-connect.png` | How the four chapters build on each other | `chapter-1-introduction-to-cs-and-ai/assets/` |
| 1.2 | `fig-1-2-two-histories.png` | Computing and AI side by side. The top lane is the history of CS from the table above. The bottom lane is the history of AI that you will meet in Topic 2 | `chapter-1-introduction-to-cs-and-ai/assets/` |
| 1.3 | `fig-1-3-cs-map.png` | A map of Computer Science. Each card is one area, with its main question and typical topics | `chapter-1-introduction-to-cs-and-ai/assets/` |
| 1.4 | `fig-1-4-steps-growth.png` | How the work grows with the size of the list. Both axes are logarithmic, which means each gridline is ten times the one before | `chapter-1-introduction-to-cs-and-ai/assets/` |
| 1.5 | `fig-1-5-pixel-face.png` | A small picture stored as bits. Each row of eight bits is one number: 129, 195, 126, 219, 255, 102, 126, 60 | `chapter-1-introduction-to-cs-and-ai/assets/` |
| 1.6 | `fig-1-6-ai-map.png` | A map of AI by capability. The tag at the bottom of each card shows where this module explains the main idea | `chapter-1-introduction-to-cs-and-ai/assets/` |
| 1.7 | `fig-1-7-ai-ml-dl.png` | AI contains machine learning, which contains deep learning. Symbolic AI is inside AI but outside machine learning | `chapter-1-introduction-to-cs-and-ai/assets/` |
| 1.8 | `fig-1-8-rules-vs-learning.png` | In traditional programming a person writes the rules. In machine learning the computer finds the rules from examples | `chapter-1-introduction-to-cs-and-ai/assets/` |
| 1.9 | `fig-1-9-three-learning-families.png` | The three families of machine learning | `chapter-1-introduction-to-cs-and-ai/assets/` |
| 1.10 | `fig-1-10-train-test-inference.png` | The three phases in the life of a model | `chapter-1-introduction-to-cs-and-ai/assets/` |
| 1.11 | `fig-1-11-nearest-neighbour.png` | The new fruit "?" and its distance to each training fruit | `chapter-1-introduction-to-cs-and-ai/assets/` |
| 1.12 | `fig-1-12-confusion-matrix.png` | A confusion matrix for a spam filter tested on 100 emails, 40 of which are really spam | `chapter-1-introduction-to-cs-and-ai/assets/` |
| 1.13 | `fig-1-13-hands-on-steps.png` | The four steps of the Rock Paper Scissors activity. The same steps apply to any image classifier | `chapter-1-introduction-to-cs-and-ai/assets/` |
| 1.14 | `fig-1-14-ask-then-verify.png` | Ask, then verify | `chapter-1-introduction-to-cs-and-ai/assets/` |
| 2.1 | `fig-2-1-how-the-chapters-connect.png` | How the four chapters build on each other. You are in Chapter 2 | `chapter-2-symbolic-ai/assets/` |
| 2.2 | `fig-2-2-symbolic-system.png` | How a symbolic AI system works, using the pneumonia rule | `chapter-2-symbolic-ai/assets/` |
| 2.3 | `fig-2-3-valid-invalid.png` | Two valid rules and one common mistake, all starting from "If it rains, the ground is wet." | `chapter-2-symbolic-ai/assets/` |
| 2.4 | `fig-2-4-five-representations.png` | One piece of knowledge in five forms. Each form suits a different job | `chapter-2-symbolic-ai/assets/` |
| 2.5 | `fig-2-5-semantic-network.png` | A semantic network. Properties are passed down along "is a" links, and a more specific property overrides the inherited one | `chapter-2-symbolic-ai/assets/` |
| 2.6 | `fig-2-6-forward-chaining.png` | Forward chaining on the umbrella example | `chapter-2-symbolic-ai/assets/` |
| 2.7 | `fig-2-7-expert-system.png` | The parts of an expert system and the people around it | `chapter-2-symbolic-ai/assets/` |
| 2.8 | `fig-2-8-farmer-states.png` | The farmer puzzle as a path through states. F = farmer, W = wolf, G = goat, C = cabbage | `chapter-2-symbolic-ai/assets/` |
| 2.9 | `fig-2-9-bfs-dfs.png` | BFS and DFS on the same tree, goal B. The numbers give the order of visiting | `chapter-2-symbolic-ai/assets/` |
| 2.10 | `fig-2-10-astar.png` | A\* decides between two roads using f = g + h | `chapter-2-symbolic-ai/assets/` |
| 2.11 | `fig-2-11-minimax.png` | Minimax on a small tree, with alpha-beta pruning | `chapter-2-symbolic-ai/assets/` |
| 2.12 | `fig-2-12-tictactoe-explosion.png` | The number of positions in the tic-tac-toe game tree after each number of moves. The total is 549,946 | `chapter-2-symbolic-ai/assets/` |
| 2.13 | `fig-2-13-parse-tree.png` | The grammar structure and the meaning of one sentence | `chapter-2-symbolic-ai/assets/` |
| 3.1 | `fig-3-1-how-the-chapters-connect.png` | How the four chapters build on each other. You are in Chapter 3 | `chapter-3-connectionist-ai-and-big-data/assets/` |
| 3.2 | `fig-3-2-parts-connect.png` | The two parts of this chapter. Part B prepares the data. Part A learns from it | `chapter-3-connectionist-ai-and-big-data/assets/` |
| 3.3 | `fig-3-3-timeline.png` | Four dates in the history of the connectionist idea | `chapter-3-connectionist-ai-and-big-data/assets/` |
| 3.4 | `fig-3-4-neuron-anatomy.png` | One artificial neuron with real numbers | `chapter-3-connectionist-ai-and-big-data/assets/` |
| 3.5 | `fig-3-5-activations.png` | Three common activation functions. Each graph shows the output (up) for each value of z (across) | `chapter-3-connectionist-ai-and-big-data/assets/` |
| 3.6 | `fig-3-6-layers.png` | Layers, from pixels to an answer. Every line is a connection with its own weight | `chapter-3-connectionist-ai-and-big-data/assets/` |
| 3.7 | `fig-3-7-xor.png` | Why one neuron fails at XOR, and how a hidden layer fixes it | `chapter-3-connectionist-ai-and-big-data/assets/` |
| 3.8 | `fig-3-8-learning-loop.png` | The learning loop | `chapter-3-connectionist-ai-and-big-data/assets/` |
| 3.9 | `fig-3-9-gradient-descent.png` | The same loss with two learning rates | `chapter-3-connectionist-ai-and-big-data/assets/` |
| 3.10 | `fig-3-10-architectures.png` | Four architectures and the data each one fits | `chapter-3-connectionist-ai-and-big-data/assets/` |
| 3.11 | `fig-3-11-deep-and-2012.png` | What each layer learns, and why deep learning took off around 2012 | `chapter-3-connectionist-ai-and-big-data/assets/` |
| 3.12 | `fig-3-12-overfitting.png` | Underfitting, a good fit, and overfitting, on the same ten points | `chapter-3-connectionist-ai-and-big-data/assets/` |
| 3.13 | `fig-3-13-applications.png` | Where you meet connectionist AI | `chapter-3-connectionist-ai-and-big-data/assets/` |
| 3.14 | `fig-3-14-average-hides.png` | An average can hide who is being failed | `chapter-3-connectionist-ai-and-big-data/assets/` |
| 3.15 | `fig-3-15-five-vs.png` | The five Vs of Big Data and the three kinds of data | `chapter-3-connectionist-ai-and-big-data/assets/` |
| 3.16 | `fig-3-16-storing-big-data.png` | Storing very large data | `chapter-3-connectionist-ai-and-big-data/assets/` |
| 3.17 | `fig-3-17-mapreduce.png` | Word count with MapReduce | `chapter-3-connectionist-ai-and-big-data/assets/` |
| 3.18 | `fig-3-18-data-pipeline.png` | A data pipeline, and two ways to run step 4 | `chapter-3-connectionist-ai-and-big-data/assets/` |
| 3.19 | `fig-3-19-four-levels.png` | The four levels of analytics | `chapter-3-connectionist-ai-and-big-data/assets/` |
| 3.20 | `fig-3-20-chart-chooser.png` | Choose the chart that fits the question | `chapter-3-connectionist-ai-and-big-data/assets/` |
| 3.21 | `fig-3-21-misleading-axis.png` | The same two numbers, drawn with an axis that starts at 0 (left) and at 90 (right) | `chapter-3-connectionist-ai-and-big-data/assets/` |
| 3.22 | `fig-3-22-reidentification.png` | How a table without names can still identify a person | `chapter-3-connectionist-ai-and-big-data/assets/` |
| 4.1 | `fig-4-1-how-the-chapters-connect.png` | How the four chapters build on each other. You are in Chapter 4 | `chapter-4-behaviorist-ai/assets/` |
| 4.2 | `fig-4-2-learning-by-consequences.png` | Learning from consequences, and where the idea comes from | `chapter-4-behaviorist-ai/assets/` |
| 4.3 | `fig-4-3-rl-loop.png` | The reinforcement learning loop, with a robot vacuum as the example | `chapter-4-behaviorist-ai/assets/` |
| 4.4 | `fig-4-4-discounting.png` | Discounting, and how gamma can change a decision | `chapter-4-behaviorist-ai/assets/` |
| 4.5 | `fig-4-5-explore-exploit.png` | Exploration versus exploitation, with a 3-button experiment | `chapter-4-behaviorist-ai/assets/` |
| 4.6 | `fig-4-6-rl-families.png` | Families of reinforcement-learning methods, and how deep RL replaces a table with a network | `chapter-4-behaviorist-ai/assets/` |
| 4.7 | `fig-4-7-corridor-spread.png` | How a reward at the goal spreads backward through the corridor | `chapter-4-behaviorist-ai/assets/` |
| 4.8 | `fig-4-8-gridworld.png` | The best action and value of each square, and how the learner improved | `chapter-4-behaviorist-ai/assets/` |
| 4.9 | `fig-4-9-mdp-parts.png` | The five parts of an MDP, with a robot vacuum as the example | `chapter-4-behaviorist-ai/assets/` |
| 4.10 | `fig-4-10-slippery-corridor.png` | The same corridor, but moves can fail | `chapter-4-behaviorist-ai/assets/` |
| 4.11 | `fig-4-11-subsumption.png` | Layers of behaviour for a robot vacuum. A higher layer overrides the ones below it | `chapter-4-behaviorist-ai/assets/` |
| 4.12 | `fig-4-12-games-timeline.png` | Game-playing systems, from backgammon to Go | `chapter-4-behaviorist-ai/assets/` |
| 4.13 | `fig-4-13-applications.png` | Where reinforcement learning is used | `chapter-4-behaviorist-ai/assets/` |
| 4.14 | `fig-4-14-rlhf.png` | Reinforcement learning from human feedback (RLHF) | `chapter-4-behaviorist-ai/assets/` |
| 4.15 | `fig-4-15-challenges.png` | Nine challenges of reinforcement learning, in three groups | `chapter-4-behaviorist-ai/assets/` |
| 4.16 | `fig-4-16-reward-hack.png` | What the designers wanted, and what the agent learned | `chapter-4-behaviorist-ai/assets/` |
| 4.17 | `fig-4-17-three-approaches.png` | Three ways to build AI, side by side | `chapter-4-behaviorist-ai/assets/` |

Besides the numbered figures, each chapter folder holds a banner (`fig-N-0-banner.png`). The README banner is in `Main/assets/brand/`. The project figures are `Main/assets/fig-main-1-stage-timeline.png` and `Main/assets/fig-main-2-workflow.png`.

Upload order for each chapter: put the `assets/` folder and the `.md` file in the same chapter folder, then open the Markdown preview on GitHub and confirm that every figure appears.

## Shared Terms and Consistency

The terms *data, algorithm, rule, knowledge base, model, training, inference, label, agent,* and *reward* are explained where they first appear (Chapter 1 for most of them) and used with the same meaning in all chapters. The [shared glossary](study-guide/v2.0/shared-glossary.md) lists all 138 terms with one meaning each. A script compared the four chapter glossaries on 5 November 2026. It found two terms (*Overfitting* and *State*) whose wording differed between chapters, and the wording was made identical.

## Prerequisites

No prior knowledge of AI or programming is required. Read the chapters in order. Chapter 1 gives the vocabulary. Chapter 2 introduces knowledge written as rules. Chapter 3 shows the learning alternative and the data it needs. Chapter 4 introduces learning from reward and ends with a comparison of the three approaches.

## The Repeated Examples

| Example | Chapters | How it develops |
|---|---|---|
| **Smart Classroom** (fan and lamp commands) | 1, 2, 3 | Chapter 1, Activity B: predict what four exact-match rules do. Chapter 2: test the rules and find their limits. Chapter 3: a small program that learns from example sentences, and breaks on others. |
| **Spam filter** | 1, 2 | Chapter 1 shows a filter written as rules and a filter learned from examples. Chapter 2 returns to the rule-based way. |
| **Corridor** (A – B – C – D with a goal) | 4 | Discounting, Q-learning updates, the values of the states, and the hands-on activity. |
| **Robot vacuum** | 4 | States, actions, and rewards; layers of behaviour; reward hacking. |

## Source Verification

The chapters list the lecturer's slides as the primary source (no public link). Every other reference has a link. **Most links could not be opened when the chapters were written**, because the working environment blocks most outside sites. A few were read with a fetch tool on 5 November 2026; those are marked in the chapter with the date. The author or reviewer must open each link, confirm that it leads to the cited work and supports the sentence that cites it, and then change the label in the chapter from "not opened" to "opened" with the date. The register to fill in is [reference-check-register-DRAFT.md](../quality/reviews/detailed-review-Stage2-V2.0-DRAFT/reference-check-register-DRAFT.md).

| Chapter | Reference | Link |
|:-:|---|---|
| 1 | Course slides, "chap1: Intro to CS and AI". Lecturer's course materials (no public link). Primary source for t… | none (lecturer's slides) |
| 1 | McCarthy, J. (2007). *What is Artificial Intelligence?* Stanford University. | <http://jmc.stanford.edu/artificial-intelligence/what-is-ai/> |
| 1 | OECD. *AI Principles* and the OECD description of an AI system. | <https://www.oecd.org/en/topics/ai-principles.html> |
| 1 | Russell, S., and Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson. | <https://aima.cs.berkeley.edu/> |
| 1 | Turing, A. M. (1950). Computing Machinery and Intelligence. *Mind*, 59(236), 433–460. | <https://doi.org/10.1093/mind/LIX.236.433> |
| 1 | Association for Computing Machinery. *ACM Computing Classification System.* | <https://dl.acm.org/ccs> |
| 1 | Encyclopedia pages linked in the history tables of Topics 1 and 2, for example ENIAC and Dartmouth workshop. | <https://en.wikipedia.org/wiki/ENIAC> |
| 1 | Machine Learning for Kids (Dale Lane). | <https://machinelearningforkids.co.uk/> |
| 1 | Teachable Machine (Google). | <https://teachablemachine.withgoogle.com/> |
| 1 | Britannica. "Deep Blue." | <https://www.britannica.com/print/article/155485> |
| 1 | Wikipedia. "AlphaGo versus Lee Sedol." | <https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol> |
| 1 | Silver, D., Huang, A., et al. (2016). "Mastering the game of Go with deep neural networks and tree search." *N… | <https://doi.org/10.1038/nature16961> |
| 2 | Course slides, "chap4: Symbolic AI". Lecturer's course materials (no public link). Primary source for the stru… | none (lecturer's slides) |
| 2 | Russell, S., and Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson. | <https://aima.cs.berkeley.edu/> |
| 2 | Haugeland, J. (1985). *Artificial Intelligence: The Very Idea*. MIT Press. Overview of the term GOFAI: | <https://en.wikipedia.org/wiki/GOFAI> |
| 2 | Shortliffe, E. H. (1976). *Computer-Based Medical Consultations: MYCIN*. Elsevier. Overview: | <https://en.wikipedia.org/wiki/Mycin> |
| 2 | Weizenbaum, J. (1966). ELIZA: a computer program for the study of natural language communication between man a… | <https://doi.org/10.1145/365153.365168> |
| 2 | Wolf, goat and cabbage problem. | <https://en.wikipedia.org/wiki/Wolf,_goat_and_cabbage_problem> |
| 2 | Stanford Encyclopedia of Philosophy. *Classical Logic.* | <https://plato.stanford.edu/entries/logic-classical/> |
| 2 | Wikipedia. "A* search algorithm." | <https://en.wikipedia.org/wiki/A*_search_algorithm> |
| 2 | Wikipedia. "ELIZA." | <https://en.wikipedia.org/wiki/ELIZA> |
| 2 | Wikipedia. "Game complexity." | <https://en.wikipedia.org/wiki/Game_complexity> |
| 2 | ChessWorld. "What Is the Shannon Number in Chess?" | <https://www.chessworld.net/what-is-the-shannon-number-in-chess.asp> |
| 3 | Course slides, "chap5: Connectionist AI and Big Data Overview". Lecturer's course materials (no public link). … | none (lecturer's slides) |
| 3 | McCulloch, W. S., and Pitts, W. (1943). A logical calculus of the ideas immanent in nervous activity. *Bulleti… | <https://doi.org/10.1007/BF02478259> |
| 3 | Rosenblatt, F. (1958). The perceptron: a probabilistic model for information storage and organization in the b… | <https://doi.org/10.1037/h0042519> |
| 3 | Rumelhart, D. E., Hinton, G. E., and Williams, R. J. (1986). Learning representations by back-propagating erro… | <https://doi.org/10.1038/323533a0> |
| 3 | LeCun, Y., Bengio, Y., and Hinton, G. (2015). Deep learning. *Nature*, 521, 436–444. | <https://doi.org/10.1038/nature14539> |
| 3 | Goodfellow, I., Bengio, Y., and Courville, A. (2016). *Deep Learning*. MIT Press. | <https://www.deeplearningbook.org/> |
| 3 | Krizhevsky, A., Sutskever, I., and Hinton, G. E. (2012). ImageNet classification with deep convolutional neura… | <https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html> |
| 3 | Neurohive. "AlexNet – ImageNet Classification with Deep Convolutional Neural Networks." | <https://neurohive.io/en/popular-networks/alexnet-imagenet-classification-with-deep-convolutional-neural-networks/> |
| 3 | Buolamwini, J., and Gebru, T. (2018). Gender Shades: Intersectional accuracy disparities in commercial gender … | <https://proceedings.mlr.press/v81/buolamwini18a.html> |
| 3 | Dean, J., and Ghemawat, S. (2004). MapReduce: Simplified data processing on large clusters. *OSDI '04*. | <https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/> |
| 3 | Sweeney, L. (2000). *Simple Demographics Often Identify People Uniquely*. Carnegie Mellon University, Data Pri… | <https://dataprivacylab.org/projects/identifiability/paper1.pdf> |
| 3 | Wikipedia. "Latanya Sweeney." | <https://en.wikipedia.org/wiki/Latanya_Sweeney> |
| 3 | European Union. Regulation (EU) 2016/679 (General Data Protection Regulation). | <https://eur-lex.europa.eu/eli/reg/2016/679/oj> |
| 4 | Course slides, "chap6: Behaviorist AI", Introduction to Computer Science and Artificial Intelligence. Lecturer… | none (lecturer's slides) |
| 4 | Sutton, R. S., and Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press. | <http://incompleteideas.net/book/the-book-2nd.html> |
| 4 | Brooks, R. A. (1991). Intelligence without representation. *Artificial Intelligence*, 47(1–3), 139–159. | <https://doi.org/10.1016/0004-3702(91> |
| 4 | Mnih, V., et al. (2015). Human-level control through deep reinforcement learning. *Nature*, 518, 529–533. | <https://doi.org/10.1038/nature14236> |
| 4 | Silver, D., et al. (2016). Mastering the game of Go with deep neural networks and tree search. *Nature*, 529, … | <https://doi.org/10.1038/nature16961> |
| 4 | Silver, D., et al. (2017). Mastering chess and shogi by self-play with a general reinforcement learning algori… | <https://arxiv.org/abs/1712.01815> |
| 4 | Tesauro, G. (1995). Temporal difference learning and TD-Gammon. *Communications of the ACM*, 38(3), 58–68. | <https://doi.org/10.1145/203330.203343> |
| 4 | Krakovna, V., et al. (2020). Specification gaming: the flip side of AI ingenuity. DeepMind. | <https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/> |
| 4 | Clark, J., and Amodei, D. (2016). Faulty reward functions in the wild. OpenAI. | <https://openai.com/index/faulty-reward-functions/> |
| 4 | Ouyang, L., et al. (2022). Training language models to follow instructions with human feedback. | <https://arxiv.org/abs/2203.02155> |
| 4 | Wikipedia. "AlphaGo versus Lee Sedol." | <https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol> |

Secondary sources such as encyclopedia pages are starting points, not final sources. Haugeland (1985) and Shortliffe (1976) are books, and their links lead to overview pages, so the reviewer should confirm the claims from the books or from another source that can be opened. The AlexNet error rates in Chapter 3 come from a secondary source (Neurohive) next to the original paper, and should be checked against the paper. The existence of Silver et al. (2016) was confirmed through a web search on 5 November 2026, but the paper was not opened.

## Known Gaps and Uncertainties

- The lecturer's slides for course Chapters 5 and 6 (our Chapters 3 and 4) were available only as topic outlines. The explanations come from standard textbook knowledge and must be compared with the lecture notes.
- No chapter has a signed review of version 2.0 (QR-221-I01 to QR-224-I01 are pending).
- Most reference links have not been opened (see above). Facts about people, dates, and events (for example the Sweeney re-identification case, the AlphaGo match, and the dates of early neural-network papers) must be checked against sources that can be opened.
- The figures are PNG files that were checked by eye on contact sheets, but not yet on the live repository. Confirm file names, relative links, and appearance after upload, in the light and dark themes and on a phone.
- Learner testing has not been run, so confusing passages may remain. The most useful test is to ask a person who has not studied AI to read one topic and say what each figure means.
- The optional tools (the lecturer's block tool, Machine Learning for Kids, Teachable Machine) are only mentioned in Chapter 1 and were not run. Every activity has a paper version.
- The team has not recorded a review of at least three previous-year projects (symbolic, connectionist, behaviorist).
- The exact text of the lecturer's assignment is not in the repository. The Project Plan's "five content parts" and the Stage 2 file names must be compared with it.
- The layout (banner, navigation table, callout boxes, collapsible answers) was written for the GitHub preview but has not yet been looked at on the live repository.
- The Chinese key terms were not checked by a Chinese-speaker.
- The visual style in `Main/style-guide.md` is a proposal that the team has not yet confirmed.

## Revision History

| Date | Version | Change | Related review |
|---|---|---|---|
| Before 2026-10-23 | v1.0 | Initial chapter overview, prerequisites, activities and known gaps | None |
| 2026-10-23 – 2026-10-24 | v1.1 – v1.5 | Learning outcomes, status labels, source table, and suggested answers for the old five-chapter structure | QR-009 series |
| 2026-11-05 | v2.0 – v2.1 | Rebuilt on the lecturer's four course chapters; PNG figures and linked references | Pending (QR-121-I01 to QR-125-I01) |
| 2026-11-05 | v3.0 – v3.2 | First Stage 2 packages (Markdown V2.0): many exercises, deep dives, case studies, a code example, chapter reviews, a one-page summary | Superseded |
| 2026-11-05 | v4.0 | Chapters rewritten from the lecturer's topics after the feedback that the text was hard to understand, too short in its explanations, split into too many numbered branches, and had a weak roadmap: "Where This Chapter Fits" storyline, long explanations, every figure explained, fewer exercises; 51,171 words and 66 numbered figures in the four chapters | Pending (QR-221-I01 to QR-225-I01) |
