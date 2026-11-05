# Stage 2 Combined Learning Content

**Babi Guling – AI Overview** | Markdown V2.0 | 2026-11-05

This file combines the four Markdown V2.0 chapters (Chapter 1: Introduction to CS and AI; Chapter 2: Symbolic AI; Chapter 3: Connectionist AI and Big Data; Chapter 4: Behaviorist AI). Place it in `Main/study-guide/v2.0/`, next to the four chapter folders, because its image links point to each chapter's `assets/` folder. The chapter files are the master copies. If a chapter changes, regenerate this file, do not edit it by hand.

---

![Chapter 1 banner: Introduction to CS and AI](chapter-1-introduction-to-cs-and-ai/assets/fig-1-0-banner.png)

# Chapter 1: Introduction to CS and AI

> **Module:** AI Overview  
> **Chapter:** 1 of 4 (course Chapter 1)  
> **Version:** 2.0 (Stage 2; developed from the Stage 1 chapter, version 1.1)  
> **Author:** Jonathan Sugianto (proposed owner)  
> **Reviewer:** Brian Djoni Suzanna (review pending; no signed review exists for this version)  
> **Audience:** Complete beginners with basic computer and internet literacy; no programming needed  
> **Study time:** about 3 hours, including the hands-on activity  
> **Course source:** Lecturer's slides "chap1: Intro to CS and AI": history, definitions, main topics, and a hands-on machine-learning activity.

| Start of the module | [Module overview](../../README.md) | [Chapter 2: Symbolic AI →](chapter-2-symbolic-ai/symbolic-ai.md) |
|:--|:-:|--:|


<details>
<summary><b>Contents</b></summary>

1. [Where This Chapter Fits](#where-this-chapter-fits)
2. [What You Will Learn](#what-you-will-learn)
3. [Topic 1: Computer Science](#topic-1-computer-science)
4. [Topic 2: Artificial Intelligence](#topic-2-artificial-intelligence)
5. [Topic 3: Machine Learning, a First Look](#topic-3-machine-learning-a-first-look)
6. [Topic 4: Hands-On Activity, Machine Learning](#topic-4-hands-on-activity-machine-learning)
7. [Topic 5: Using an AI Assistant for Study](#topic-5-using-an-ai-assistant-for-study)
8. [Common Misconceptions](#common-misconceptions)
9. [Key Takeaways](#key-takeaways)
10. [Practice Questions](#practice-questions)
11. [Answer Key](#answer-key)
12. [What Comes Next: From Words to Rules](#what-comes-next-from-words-to-rules)
13. [Key Terms in Chinese](#key-terms-in-chinese)
14. [Glossary](#glossary)
15. [References](#references)

</details>

---

## Where This Chapter Fits

This is the first of four chapters. Together they answer one question: **how can a machine be made to behave intelligently?** Each chapter gives one answer, and each answer leaves a problem that the next chapter tries to solve.

![Four cards, one per chapter, each with its core idea, what it gives us, and where it struggles. Chapter 1 is highlighted.](chapter-1-introduction-to-cs-and-ai/assets/fig-1-1-how-the-chapters-connect.png)

*Figure 1.1: How the four chapters build on each other.*

**How to read this figure.** Read the cards from left to right. Each card has three parts: the **core idea** of the chapter, **what it gives us**, and **where it struggles**. The last line of one card is the reason the next card exists. For example, Chapter 2 struggles because people cannot write rules for everything, so Chapter 3 lets the machine find the rules itself from data.

| | Before this chapter | In this chapter | In the next chapter |
|---|---|---|---|
| **What you know** | Nothing is assumed. You only need to use a computer and a browser. | You get the shared vocabulary (CS, AI, algorithm, data, model), a short history, a map of both fields, and a first working example of machine learning. | Chapter 2 starts with the oldest approach: people write the knowledge as rules and logic. |
| **Main question** | – | What are CS and AI, and what does it mean for a machine to learn from examples? | What can a machine do when we write the knowledge down for it, and where does that stop working? |

Chapter 1 is the **foundation**. It does not explain how any single AI method works in detail. It gives you the words and the picture so that Chapters 2, 3, and 4 make sense.

## What You Will Learn

After this chapter you should be able to:

1. **Define** Computer Science and Artificial Intelligence in more than one way, and explain why the definitions differ. (Topics 1 and 2)
2. **Describe** the main steps in the history of CS and of AI, using the four columns the lecturer asks for: year, key events, key people, key technologies. (Topics 1 and 2)
3. **Draw** a simple map of CS and a simple map of AI, and say where AI sits inside CS. (Topics 1 and 2)
4. **Explain** the difference between AI, machine learning, and deep learning. (Topic 2)
5. **Explain** how a machine learns from labelled examples, and name the three families of machine learning. (Topic 3)
6. **Train and test** a simple classifier by hand, and say why the examples matter. (Topics 3 and 4)
7. **Use** an AI assistant for study without trusting it blindly. (Topic 5)

---

## Topic 1: Computer Science

Artificial Intelligence is a part of Computer Science, so we start with the larger field. This topic answers four questions in order: **what** CS is, **where it came from**, **what it contains**, and **which two ideas** appear everywhere in it.

### What Computer Science is

**Computer Science (CS)** is the study of computation: what problems a machine can solve, how to solve them efficiently, how to build the software and hardware that does it, and how people use the results.

You will not find one sentence that everybody uses. Textbooks, universities, and professional bodies each put the weight on a different part. That is not a mistake. CS is a large field, and each definition looks at it from one side.

| Viewpoint | What it stresses | A simple way to say it |
|---|---|---|
| **Computation** | Algorithms and what can be computed | "CS is the study of step-by-step procedures and the problems they can solve." |
| **Information** | How information is represented, stored, and moved | "CS is the study of how to handle information with machines." |
| **Engineering** | Building reliable hardware and software | "CS is the discipline of designing, building, and testing computing systems." |
| **Automation** | Which tasks a machine can do instead of a person | "CS is the study of what can be automated." |
| **Human use** | How people use computers and what that does to society | "CS is about computers and the people who use them." |

These are our own summaries in plain words, not quotations. When you meet a definition in a book or from an AI assistant, ask which viewpoint it takes. Two definitions that look different usually describe the same field from two sides.

Every viewpoint uses the same word: **computer**. A computer is a machine that follows instructions to change input into output. The input might be a typed sentence, a photo, or a sensor reading. The output might be a translated sentence, a sorted list, or a signal that turns on a lamp. What happens in between is an **algorithm**, a precise list of steps, and the data it works on. Those two words, *algorithm* and *data*, appear in every chapter of this module.

### Where CS came from: a short history

The lecturer's slides ask for the history of CS as a table with four columns: **Year, Key Events, Key People, Key Technologies**. The table below follows that format.

| Year | Key events | Key people | Key technologies |
|---|---|---|---|
| 1830s–1840s | Design of the [Analytical Engine](https://en.wikipedia.org/wiki/Analytical_Engine), a mechanical general-purpose computer that was never completed; the first published program for it | Charles Babbage, Ada Lovelace | Mechanical computing, punched cards |
| 1936 | The [Turing machine](https://en.wikipedia.org/wiki/Turing_machine), a mathematical model of what can be computed | Alan Turing | Theory of computation |
| 1945 | The [stored-program](https://en.wikipedia.org/wiki/Stored-program_computer) design: instructions and data live in the same memory | John von Neumann and colleagues | Stored-program architecture |
| 1946 | [ENIAC](https://en.wikipedia.org/wiki/ENIAC), an early large electronic computer, is completed | J. Presper Eckert, John Mauchly | Vacuum tubes |
| 1947 | The [transistor](https://en.wikipedia.org/wiki/Transistor) is invented | John Bardeen, Walter Brattain, William Shockley | Transistors |
| 1957 | [FORTRAN](https://en.wikipedia.org/wiki/Fortran), an early high-level programming language | John Backus and team | Compilers |
| 1958–1959 | The [integrated circuit](https://en.wikipedia.org/wiki/Integrated_circuit) | Jack Kilby, Robert Noyce | Integrated circuits |
| 1969 | [ARPANET](https://en.wikipedia.org/wiki/ARPANET) links its first computers; [Unix](https://en.wikipedia.org/wiki/Unix) is started | ARPA researchers; Ken Thompson, Dennis Ritchie | Packet networks, operating systems |
| 1971 | First commercial [microprocessor](https://en.wikipedia.org/wiki/Intel_4004) (Intel 4004) | Intel engineers | Microprocessors |
| 1981 | [IBM Personal Computer](https://en.wikipedia.org/wiki/IBM_Personal_Computer) released | IBM team | Personal computers |
| 1989–1991 | The [World Wide Web](https://en.wikipedia.org/wiki/World_Wide_Web) | Tim Berners-Lee | HTTP, HTML, browsers |
| 2007 | Smartphones become mainstream ([iPhone](https://en.wikipedia.org/wiki/IPhone_(1st_generation))) | Apple team | Touch screens, mobile apps |
| 2010s | Cloud computing and very large data centres become common | Many companies | Cloud, GPUs |

The links lead to encyclopedia pages as a starting point. They are not final sources, so a reviewer should confirm the details in a textbook.

A table of dates is hard to remember, so here is the story behind it. The history of CS has three stages, and each one made the next possible.

**Stage 1: the idea of computation (1830s to 1940s).** Before any useful computer existed, people worked out what a computing machine would be. Babbage designed one in metal and gears. Lovelace saw that such a machine could work on more than numbers. Turing then gave a precise mathematical description of "anything that can be computed". This stage is about **ideas**.

**Stage 2: the machine gets small, cheap, and connected (1940s to 1990s).** The first computers filled rooms and used vacuum tubes. The transistor and then the integrated circuit made the parts smaller and far more reliable, and the microprocessor put a whole processor on one chip. Personal computers followed, and the network that began as ARPANET grew into the Web. This stage is about **hardware and networks**.

**Stage 3: computing everywhere, and data everywhere (1990s to today).** Phones put a computer in every pocket. Cloud services moved the heavy work to large data centres. All these devices produce a huge amount of data, and graphics processors (GPUs) provide the power to process it. This is the stage in which modern AI became practical, and it is the reason this module exists.

![Two lanes of milestone cards: computing on top, AI below, with bands for rule-based AI and learning-based AI](chapter-1-introduction-to-cs-and-ai/assets/fig-1-2-two-histories.png)

*Figure 1.2: Computing and AI side by side. The top lane is the history of CS from the table above. The bottom lane is the history of AI that you will meet in Topic 2.*

**How to read this figure.** Each card is one milestone. The top lane is CS and the bottom lane is AI. Notice that AI starts in the 1940s and 1950s, when the first electronic computers exist, and that the big learning-based results (2012 and later) come after cheap processors, networks, and data (the 1971 to 2010s cards above). AI did not appear on its own. It grew inside computing and used what computing had built.

### What CS contains: a map

The slides show a mind map of CS based on the **ACM classification**, the classification of computing topics by the Association for Computing Machinery. A university programme will usually teach the areas in the figure below, though the names differ between schools. This is a simplified version for freshmen.

![Seven cards: theory of computation, computer hardware, systems and networks, software engineering, data and information, human-computer interaction, and artificial intelligence, the last one highlighted](chapter-1-introduction-to-cs-and-ai/assets/fig-1-3-cs-map.png)

*Figure 1.3: A map of Computer Science. Each card is one area, with its main question and typical topics.*

**How to read this figure.** Each card is a different kind of question. **Theory** asks what can be computed and how fast. **Hardware** and **systems** ask how real machines are built and how they work together. **Software engineering** asks how to build large programs that work. **Data** asks how to store and find information. **Human–computer interaction** asks how people use all of this. **Artificial intelligence** asks how a machine can do tasks that normally need human intelligence, and it is the area highlighted because it is the subject of this module.

Two points to notice. First, the areas overlap. A web search engine uses data, networks, algorithms, and AI at the same time. Second, **AI is a branch of CS, not a separate subject.** An AI system is a program. It runs on hardware, stores its data in databases, and is built with software engineering. What makes AI special is the *kind of task*: recognising a face, understanding a sentence, planning a route. These are tasks that people do with their minds, and that we do not know how to write as a short list of steps.

### Two ideas that appear everywhere: algorithms and data

Before moving on to AI, look closely at the two ideas that every later chapter depends on.

**An algorithm is a recipe that a computer can follow exactly.** "Find the biggest number in a list" sounds easy, but a computer needs every step spelled out:

1. Write down the first number as the "largest so far".
2. Look at the next number. If it is bigger than the largest so far, replace the largest so far with it.
3. Repeat step 2 until no numbers are left.
4. The largest so far is the answer.

Here is the algorithm on the list 7, 3, 9, 4.

| Number looked at | Bigger than the largest so far? | Largest so far |
|--:|---|--:|
| 7 (start) | not applicable | 7 |
| 3 | no | 7 |
| 9 | yes | 9 |
| 4 | no | 9 |

The answer is **9**. Notice what makes this an algorithm: every step is exact, nothing depends on judgement, and it works for any list. A person could follow it with pen and paper, and so can a machine.

**Algorithms differ in how many steps they need.** Suppose a sorted list has 1,000,000 numbers and you want to know whether one number is in it. *Linear search* looks at the items one by one, so in the worst case it needs 1,000,000 checks. *Binary search* uses the fact that the list is sorted: it checks the middle item, throws away the half that cannot contain the target, and repeats. Each check halves the work, so 1,000,000 items need only **20 checks**, and 1,000,000,000 items need only 30.

![Line chart: the number of checks grows steeply for linear search and very slowly for binary search](chapter-1-introduction-to-cs-and-ai/assets/fig-1-4-steps-growth.png)

*Figure 1.4: How the work grows with the size of the list. Both axes are logarithmic, which means each gridline is ten times the one before.*

**How to read this figure.** The horizontal axis is the size of the list and the vertical axis is the number of checks in the worst case. The red line (linear search) climbs as fast as the list grows. The purple line (binary search) hardly rises at all. At 1,000,000 items the lines are 50,000 times apart. The point of the picture: **choosing a clever algorithm can matter more than buying a faster computer.** AI problems are huge, so this matters a great deal, and you will see it again with game trees in Chapter 2.

**Data is information written in a form a computer can store.** A computer cannot store a photo, a word, or a song directly. It stores **bits**, each of which is 0 or 1, and everything is agreed to be a pattern of bits. A binary number uses place values 8, 4, 2, 1 (and so on) instead of 1000, 100, 10, 1. For example, 13 = 8 + 4 + 0 + 1, which is **1101** in binary.

A picture is a grid of squares called pixels. In the simplest black-and-white picture each pixel is one bit, 1 for dark and 0 for white.

![An eight by eight grid of black and white squares forming a face, with each row also written as a decimal and a hexadecimal number](chapter-1-introduction-to-cs-and-ai/assets/fig-1-5-pixel-face.png)

*Figure 1.5: A small picture stored as bits. Each row of eight bits is one number: 129, 195, 126, 219, 255, 102, 126, 60.*

**How to read this figure.** Each row is eight squares, and each square is a bit (dark = 1). The number to the right is the same row read as a binary number. So the whole face is just eight numbers, which is eight bytes of memory. A colour photo works the same way, with three numbers (red, green, blue) per pixel. A Full HD photo of 1920 × 1080 pixels has 1920 × 1080 × 3 = 6,220,800 numbers before compression.

This matters for AI because **a machine-learning model never sees "a cat". It receives a long list of numbers and looks for patterns in them.** Every example in Chapters 3 and 4 starts from numbers like these.

### Check yourself

<details>
<summary>Question 1. Why is "AI is a branch of CS" a more accurate sentence than "AI and CS are two fields"?</summary>

An AI system is a program. It uses the algorithms, data storage, hardware, and engineering methods of CS. AI differs from the rest of CS by the kind of task (tasks that normally need intelligence), not by the tools.

</details>

<details>
<summary>Question 2. Trace the "largest so far" algorithm on the list 5, 12, 8, 12. What changes it, and what is the answer?</summary>

The largest so far is 5, becomes 12 when 12 is looked at (it is bigger than 5), stays 12 at 8, and stays 12 at the second 12 (it is not *bigger*). The answer is **12**.

</details>

<details>
<summary>Question 3. A list doubles from 1,000,000 to 2,000,000 items. How many more checks does binary search need in the worst case?</summary>

2^20 = 1,048,576 is enough for 1,000,000 items. 2^21 = 2,097,152 is enough for 2,000,000 items. So the worst case rises from 20 to **21 checks: one more**. Doubling the data adds one step.

</details>

> [!IMPORTANT]
> **In short**
>
> * Computer Science studies computation, information, and the systems that handle them. There is no single official definition, so check which viewpoint a source takes.
> * CS grew in three stages: the idea of computation, small and connected machines, and computing and data everywhere. Modern AI depends on the third stage.
> * AI is one branch of CS. What marks it out is the kind of task, not the tools.
> * An **algorithm** is an exact list of steps, and **data** is information stored as bits. Everything in the next chapters is built from these two.

---

## Topic 2: Artificial Intelligence

Topic 1 described the large field. This topic narrows down to one branch of it. It follows the same order as Topic 1: **what** AI is, **where it came from**, **what it contains**, and then one picture that clears up three words people often mix up: AI, machine learning, and deep learning.

### What Artificial Intelligence is

**Artificial Intelligence (AI)** is the field of making machines do things that we normally say need intelligence, such as understanding language, recognising pictures, planning, and learning from experience.

That sentence hides a problem: nobody agrees exactly what "intelligence" means. So, as with CS, there are many definitions, each from a different viewpoint. The slides ask you to list as many as you can. Here are four that cover the main ideas.

| Viewpoint | What it says, in simple words | Where it comes from |
|---|---|---|
| **Making intelligent machines** | AI is the science and engineering of making intelligent machines, especially intelligent computer programs. | John McCarthy, who helped name the field in 1955–1956 |
| **Acting rationally** | An AI system is an *agent*: it perceives its environment and chooses the actions that best reach its goals. | The textbook of Russell and Norvig |
| **A machine that infers** | An AI system is a machine-based system that takes input and infers how to produce outputs such as predictions, content, recommendations, or decisions. | The OECD's description of an AI system |
| **Acting like a human** | A machine is intelligent if, in a written conversation, a person cannot tell it from a human. | Alan Turing's "imitation game", 1950 |

These are summaries, not quotations. A reviewer should check the exact wording in the original sources listed in the References before anyone quotes them.

Read the table as four answers to four different questions. McCarthy's definition is about the **goal** (build intelligent machines). Russell and Norvig's is about **behaviour** (do the best thing to reach a goal). The OECD's is about **how the system works** (infer an output from an input), which is why it covers modern chatbots and recommendation systems. Turing's is a **test** you can actually run. None of them is wrong. They are useful for different jobs.

The imitation game deserves one more sentence, because you will hear it called the Turing test. Turing asked: instead of arguing about whether a machine "thinks", could we ask whether it can *behave* so well in a conversation that a judge cannot tell it from a person? The test is clever, but it measures only conversation, and a program can score well by sounding fluent without understanding anything. Keep this in mind in Topic 5, where you will use an AI assistant that writes very fluent text.

Three things to remember about every definition of AI:

1. **There is no single agreed definition.** Always check which one a source is using.
2. **"Intelligence" is a moving target.** A task that once looked like it needed intelligence, such as playing chess, starts to feel like "just a program" once a machine does it. People say, "that is not real AI". The boundary keeps moving.
3. **Today's AI is narrow.** Each system is good at specific tasks. A chess program cannot translate a letter, and a translation system cannot drive a car. A machine with human-like general ability, often called *general AI*, does not exist today.

### Where AI came from: a short history

The slides again ask for a table with **Year, Key Events, Key People, Key Technologies**.

| Year | Key events | Key people | Key technologies |
|---|---|---|---|
| 1943 | First mathematical model of an [artificial neuron](https://en.wikipedia.org/wiki/Artificial_neuron) | Warren McCulloch, Walter Pitts | Neuron models |
| 1950 | "[Computing Machinery and Intelligence](https://en.wikipedia.org/wiki/Computing_Machinery_and_Intelligence)" proposes the imitation game | Alan Turing | The idea of machine intelligence |
| 1956 | The [Dartmouth workshop](https://en.wikipedia.org/wiki/Dartmouth_workshop), where the term "artificial intelligence" was used | John McCarthy, Marvin Minsky, Nathaniel Rochester, Claude Shannon | Symbolic reasoning programs |
| 1958 | The [perceptron](https://en.wikipedia.org/wiki/Perceptron), a neuron model that learns | Frank Rosenblatt | Early neural networks |
| 1966 | [ELIZA](https://en.wikipedia.org/wiki/ELIZA), a chatbot that follows keyword rules | Joseph Weizenbaum | Rule-based language processing |
| 1970s | [MYCIN](https://en.wikipedia.org/wiki/Mycin), an expert system for infections; the first "[AI winter](https://en.wikipedia.org/wiki/AI_winter)" of reduced funding in the mid-1970s | Edward Shortliffe and colleagues | Expert systems |
| 1980s | Companies use expert systems; [backpropagation](https://en.wikipedia.org/wiki/Backpropagation) is popularised in 1986 | David Rumelhart, Geoffrey Hinton, Ronald Williams | Rule engines, multi-layer networks |
| Late 1980s–1990s | Second "AI winter"; reinforcement learning grows; [TD-Gammon](https://en.wikipedia.org/wiki/TD-Gammon) learns backgammon (1992) | Gerald Tesauro; Richard Sutton and others | Reinforcement learning |
| 1997 | [Deep Blue](https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)) beats world chess champion Garry Kasparov | IBM team | Game-tree search, special hardware |
| 2012 | [AlexNet](https://en.wikipedia.org/wiki/AlexNet) wins the ImageNet image contest by a wide margin | Alex Krizhevsky, Ilya Sutskever, Geoffrey Hinton | Deep neural networks, GPUs, big data |
| 2016 | [AlphaGo](https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol) beats Go champion Lee Sedol 4–1 | DeepMind team | Deep learning plus reinforcement learning |
| 2017 | The [Transformer](https://en.wikipedia.org/wiki/Attention_Is_All_You_Need) architecture | Ashish Vaswani and colleagues | Attention-based neural networks |
| 2022 | [ChatGPT](https://en.wikipedia.org/wiki/ChatGPT) is released to the public | OpenAI | Large language models |

As before, the links are starting points, not final sources.

The table is easier to understand as a story of **three competing ideas**. All of them appear in the early rows, and which one led the field changed over time.

**1. Intelligence as rules and logic (1950s to 1980s).** The first generation of AI researchers believed that thinking is manipulating symbols according to rules. They wrote programs that proved theorems, played games by searching, and answered questions with hand-written rules. ELIZA used keyword rules to imitate a therapist. MYCIN held several hundred rules written by doctors and could suggest a treatment for a blood infection. This idea is called **Symbolic AI**, and it is the subject of Chapter 2. It worked well on problems that people can explain step by step, and it struggled when the rules became too many or could not be put into words, as with recognising a face.

**2. Intelligence from many simple connected units (1940s onward, dominant after 2012).** A second idea started even earlier: build a very simple model of a brain cell, connect many of them, and let the connections be learned from examples. McCulloch and Pitts proposed the first neuron model in 1943, and Rosenblatt's perceptron could learn in 1958. Progress was slow for decades, because there was too little data and computers were too slow. The 2012 result of AlexNet showed what happens when you have both: a deep neural network won an image-recognition contest by a large margin. This idea is called **Connectionist AI**, and it is the subject of Chapter 3.

**3. Intelligence from acting and receiving rewards (1990s onward).** A third idea says that an agent can learn what to do by trying actions and noticing which ones pay off, as an animal does. TD-Gammon learned backgammon this way, and AlphaGo combined it with deep networks to beat a Go champion. This idea is called **Behaviorist AI**, and it is the subject of Chapter 4.

| Approach | Core idea | Typical milestones in the table | Chapter |
|---|---|---|---|
| **Symbolic AI** | Intelligence comes from explicit rules, logic, and search. | Dartmouth programs, ELIZA, MYCIN, Deep Blue | 2 |
| **Connectionist AI** | Intelligence comes from many simple connected units that learn from data. | McCulloch–Pitts, perceptron, backpropagation, AlexNet, Transformer | 3 |
| **Behaviorist AI** | Intelligence comes from acting, receiving rewards, and adjusting behaviour. | TD-Gammon, AlphaGo (together with deep learning) | 4 |

The history also shows two cooling-off periods, called **AI winters**, in the 1970s and in the late 1980s. In each, the early promises were bigger than what the technology could deliver, and funding dropped. The lesson for a beginner is to be careful with claims: each wave of AI was real, and each was also over-sold at first.

**One example that shows two eras.** Chess and Go are the two most famous game-playing results. In 1997, Deep Blue beat the world champion Garry Kasparov in a six-game match (3½ to 2½). Deep Blue worked mainly by **searching**: it evaluated hundreds of millions of positions per second, using a scoring function that its designers wrote by hand. That is the Symbolic idea, powered by special hardware. In 2016, AlphaGo beat Lee Sedol 4 to 1 in Go, a game with far too many positions for plain search. AlphaGo used **deep neural networks trained on many games, and then trained further by playing against itself** with a reward for winning. That is the Connectionist and Behaviorist ideas together. Same goal, two very different methods, twenty years apart.

### What AI contains: a map

The slides also ask for a knowledge map of AI. The map below groups AI by the **kind of ability** the machine has, and tags each group with the chapter that explains the idea behind it.

![Six cards: reasoning and planning, knowledge, perception, language, learning, and acting, each with examples and the chapter that covers it](chapter-1-introduction-to-cs-and-ai/assets/fig-1-6-ai-map.png)

*Figure 1.6: A map of AI by capability. The tag at the bottom of each card shows where this module explains the main idea.*

**How to read this figure.** Each card is an **ability**. *Reasoning and planning* and *knowledge* are about drawing conclusions from facts, and are mostly the territory of Symbolic AI (Chapter 2). *Perception* (vision, speech) is where neural networks made the biggest progress (Chapter 3). *Language* needs both ideas, which is why it has two chapters. *Learning* is not a separate task but a way of getting the other abilities, and it appears in Chapters 1, 3, and 4. *Acting*, as in robots and game players, is where reward-based learning is used (Chapter 4).

There is one distinction that clears up many confusions: **tasks versus methods**. "Recognising pictures" is a *task*: it is something we want done. "Symbolic AI", "Connectionist AI", and "Behaviorist AI" are *methods*: they are ways of doing a task. The same task can be done by different methods, and the same method can be used for different tasks. The map is a list of tasks. The three chapters after this one describe methods.

### AI, machine learning, and deep learning

These three terms are used as if they meant the same thing, and they do not. The figure shows how they relate.

![Three nested circles, AI containing machine learning containing deep learning, with an example of each ring on the right](chapter-1-introduction-to-cs-and-ai/assets/fig-1-7-ai-ml-dl.png)

*Figure 1.7: AI contains machine learning, which contains deep learning. Symbolic AI is inside AI but outside machine learning.*

**How to read this figure.** Each circle is a smaller part of the one around it. The **biggest circle, AI**, is any machine doing tasks that need intelligence, including programs that follow rules written by people. **Machine learning** is the part of AI in which the program *learns* from data instead of following only hand-written rules. **Deep learning** is the part of machine learning that uses neural networks with many layers. The boxes on the right give one example for each ring. A chess program that searches and an expert system with IF–THEN rules are AI, but they do not learn, so they sit in the outer ring only.

So when someone says "AI", they might mean any of the three circles. A news story about a chatbot usually means deep learning. A textbook chapter on logic means the outer ring. When you read, ask which circle is meant.

### Check yourself

<details>
<summary>Question 1. Give two definitions of AI from the table and say how they differ.</summary>

For example: McCarthy's definition is about the *goal* (making intelligent machines), while the OECD description is about *how the system works* (it infers outputs from inputs). Any two viewpoints, compared fairly, are a correct answer.

</details>

<details>
<summary>Question 2. "Image recognition" and "Connectionist AI": which is a task and which is a method?</summary>

Image recognition is a **task** (what we want done). Connectionist AI is a **method** (one way of doing it). Other methods could attempt the same task.

</details>

<details>
<summary>Question 3. A program has 300 hand-written IF–THEN rules for diagnosing plant diseases. Is it AI? Is it machine learning?</summary>

It is **AI** (it does a task that needs expertise) but **not machine learning**, because nothing is learned from data. A person wrote the rules. It is Symbolic AI.

</details>

> [!IMPORTANT]
> **In short**
>
> * There is no single definition of AI. The four common viewpoints are: making intelligent machines, acting rationally, inferring outputs from input, and acting like a human.
> * AI's history is a story of three ideas: rules and logic (Symbolic), connected learning units (Connectionist), and learning from reward (Behaviorist). Each wave was real and also over-sold at first.
> * Abilities such as vision and language are **tasks**. The three approaches are **methods**.
> * AI contains machine learning, which contains deep learning. Rule-based AI is inside AI but outside machine learning.

---

## Topic 3: Machine Learning, a First Look

The hands-on activity in this chapter is about machine learning, and Chapters 3 and 4 depend on it. So this topic explains the idea carefully: **what** machine learning is, **how a machine learns** step by step, **how we know it learned well**, and **what can go wrong**.

### What machine learning is

Think about how you would build a spam filter. The obvious way is to write rules.

```
IF the email contains "free money" THEN spam
IF the email contains "meeting at 3pm" THEN not spam
```

This is easy to read, but it fails on every email you did not think of. Spammers change their words faster than you can add rules. This is the weakness of the rule-writing approach, and it is the problem that machine learning solves.

**Machine learning (ML)** means a program improves at a task by learning from data, instead of following only rules written by a person. Compare the two ways of building the filter.

![Two rows of boxes. Traditional programming: data plus rules go into a computer and answers come out. Machine learning: data plus answers go into a computer and rules come out.](chapter-1-introduction-to-cs-and-ai/assets/fig-1-8-rules-vs-learning.png)

*Figure 1.8: In traditional programming a person writes the rules. In machine learning the computer finds the rules from examples.*

**How to read this figure.** The top row is the traditional way (the one in Chapter 2). A person writes the **rules**, the computer applies them to the **data**, and the **answers** come out. The bottom row turns the arrow around. You give the computer the **data** together with the correct **answers** (for example 1,000 emails that people have already marked spam or not spam). The computer works out the **rules** itself. We call what it finds a **model**. Later you use the model on new emails to get new answers.

A model is not magic. It is a set of numbers together with a procedure that turns an input into an output. What the numbers are depends on which learning method is used, and you will see two different kinds of model in this chapter and in Chapter 3.

A few terms you will meet again and again:

* **Training example**: one piece of data used to teach the model, such as one email.
* **Feature**: a measurable property of an example that the model looks at, such as "contains the word *free*" or, for a fruit, its size and its sourness.
* **Label**: the correct answer attached to a training example, such as "spam".
* **Model**: the thing that is learned and then used to make predictions.

### Three families of machine learning

Machine learning is divided into three families, according to what kind of feedback the machine gets. The slides show the same split.

![Three panels. Supervised: coloured dots with labels and one unknown dot. Unsupervised: unlabelled dots grouped in circles. Reinforcement: an agent and a world exchanging actions, states, and a reward.](chapter-1-introduction-to-cs-and-ai/assets/fig-1-9-three-learning-families.png)

*Figure 1.9: The three families of machine learning.*

**How to read this figure.** In **supervised learning** (left) every training example has a label, shown here as a colour. The machine's job is to give the new item "?" the right label. In **unsupervised learning** (middle) nothing has a label. The machine looks for structure, such as groups of similar items. In **reinforcement learning** (right) there are no examples at all. An **agent** acts in a world, the world answers with a new situation and a **reward** (a number that says how good the last action was), and the agent learns which actions pay off.

| Family | What the data looks like | Example | Where it comes back |
|---|---|---|---|
| Supervised, **classification** | Examples with a category label | Emails labelled *spam* or *not spam* | Chapter 3 |
| Supervised, **regression** | Examples with a number label | Past house sizes and prices | Chapter 3 |
| Unsupervised, **clustering** | Examples with no labels | Grouping customers by buying habits | Chapter 3 |
| Unsupervised, **association** | Shopping baskets | "People who buy bread often buy butter" | Chapter 3 |
| **Reinforcement** | An agent that acts and gets rewards | A program learning to play a game | Chapter 4 |

Supervised and unsupervised learning are mostly studied inside Connectionist AI and statistics (Chapter 3). Reinforcement learning is the engine of Behaviorist AI (Chapter 4). Symbolic AI (Chapter 2) is the opposite starting point: the knowledge is written by people, not learned.

### How a model is trained, tested, and used

A learning program goes through three phases. A rule-based program has none of them, because a person writes the rules.

![Three rows: training turns labelled data into a model, testing checks the model on unseen labelled data to give a score, and inference applies the model to a new input to give a prediction](chapter-1-introduction-to-cs-and-ai/assets/fig-1-10-train-test-inference.png)

*Figure 1.10: The three phases in the life of a model.*

**How to read this figure.** Read each row from left to right. In **training** the learning algorithm studies labelled examples and adjusts the model until it matches the labels well. In **testing** you give the model *new* labelled examples that it has never seen, and compare its answers with the true labels. In **inference** the model is used for real, on input that has no label, so nobody can check the answer on the spot.

The most important rule is in the second row: **always test on examples the model has not seen.** If you test on the training examples, you are giving students the exam questions in advance, and a model that has simply memorised its examples will score perfectly. Real projects usually split the labelled data three ways: a **training set** (for example 700 of 1,000 emails) to learn from, a **validation set** (150) to compare settings and versions, and a **test set** (150) used once at the end for the final honest score.

### A complete example: nearest neighbour

To see learning without any mathematics beyond arithmetic, use one of the simplest learning methods. In **nearest neighbour**, to label a new item you find the training example that is most similar to it and copy its label. The "model" is just the stored examples plus the rule "the closest one wins".

Each fruit is described by two numbers from 1 to 10, its **size** and its **sourness**. These two numbers are the features.

| Training example | Size | Sourness | Label |
|---|--:|--:|---|
| 1 | 6 | 2 | apple |
| 2 | 7 | 3 | apple |
| 3 | 3 | 9 | lemon |
| 4 | 2 | 8 | lemon |

A new fruit arrives: **size 5, sourness 5**. Which label should it get? "Most similar" needs a measurement, and the usual one is the straight-line distance between two points: √((size difference)² + (sourness difference)²).

![A scatter plot of four fruits and a new fruit with distance lines. The nearest one, an apple, is highlighted.](chapter-1-introduction-to-cs-and-ai/assets/fig-1-11-nearest-neighbour.png)

*Figure 1.11: The new fruit "?" and its distance to each training fruit.*

**How to read this figure.** Size runs along the bottom and sourness runs up the side, so each fruit is a point. Apples are purple and lemons are gold. The new fruit "?" is at (5, 5). The dashed lines are the distances, and the green line marks the shortest. The calculation behind the numbers is in the table.

| Compared with | Calculation | Distance |
|---|---|--:|
| Example 1 (apple) | √((5−6)² + (5−2)²) = √(1 + 9) = √10 | 3.16 |
| Example 2 (apple) | √((5−7)² + (5−3)²) = √(4 + 4) = √8 | **2.83** |
| Example 3 (lemon) | √((5−3)² + (5−9)²) = √(4 + 16) = √20 | 4.47 |
| Example 4 (lemon) | √((5−2)² + (5−8)²) = √(9 + 9) = √18 | 4.24 |

The closest example is number 2, so the model predicts **apple**.

Notice what happened. Nobody wrote a rule such as "small and not sour means apple". The prediction came entirely from the **examples**. If we had stored different examples, the same method would give a different answer. This is the central point of machine learning: **the examples decide what the model can know.**

<details>
<summary>Your turn: predict the label for a new fruit with size 4 and sourness 7, then check by computing the four distances.</summary>

| Compared with | Distance |
|---|--:|
| Example 1 (apple): √((4−6)² + (7−2)²) = √29 | 5.39 |
| Example 2 (apple): √((4−7)² + (7−3)²) = √25 | 5.00 |
| Example 3 (lemon): √((4−3)² + (7−9)²) = √5 | **2.24** |
| Example 4 (lemon): √((4−2)² + (7−8)²) = √5 | **2.24** |

The two closest examples are both lemons, so the prediction is **lemon**.

</details>

### How we know the model learned well

Training produces a model, but a model can be bad. How do we tell? We test it on examples it has not seen, and count its mistakes.

Suppose a spam filter is tested on 20 new emails that were labelled by hand: 8 are spam and 12 are normal. The filter catches 7 of the 8 spam emails, and wrongly marks 2 of the 12 normal emails as spam. The correct decisions are 7 (spam caught) plus 10 (normal emails left alone), which is 17 out of 20.

**Accuracy = 17 ÷ 20 = 0.85, or 85%.**

Accuracy is the first measure to look at, but it does not tell you **which** mistakes were made. In this test one spam email slipped through (annoying), and two real emails were blocked (possibly worse, for example a message from a teacher). The two kinds of mistake cost different things, so we count them separately in a table called the **confusion matrix**.

![A two by two table: 30 true positives, 10 false negatives, 5 false positives, 55 true negatives, for a spam filter tested on 100 emails](chapter-1-introduction-to-cs-and-ai/assets/fig-1-12-confusion-matrix.png)

*Figure 1.12: A confusion matrix for a spam filter tested on 100 emails, 40 of which are really spam.*

**How to read this figure.** Rows are the **truth** and columns are the filter's **prediction**. The green cells are correct: **30** spam emails were caught (true positives) and **55** normal emails were left alone (true negatives). The red cells are mistakes: **10** spam emails got through (false negatives) and **5** normal emails were blocked (false positives).

| Measure | Question it answers | Calculation | Result |
|---|---|---|--:|
| **Accuracy** | Of all emails, how many were handled correctly? | (30 + 55) ÷ 100 | **0.85** |
| **Precision** | Of the emails called spam, how many really were spam? | 30 ÷ (30 + 5) | **0.857** |
| **Recall** | Of the real spam, how much did the filter catch? | 30 ÷ (30 + 10) | **0.75** |

**Why accuracy alone can fool you.** Suppose only 5 of 100 emails are spam, and a lazy "model" always answers *not spam*. Its accuracy is 95 ÷ 100 = **95%**, which looks excellent. Yet it catches no spam at all, so its recall is 0 ÷ 5 = **0%**. This is why a good report always looks at the *kinds* of errors, not only the percentage.

### What can go wrong

Two problems appear in every machine-learning project, and you will meet both again in Chapter 3.

* **Bad examples give a bad model.** A model only knows what its examples show. If the training photos of "rock" were all taken in a dark room, the model may learn "dark means rock" instead of the shape of a hand. This is a **biased training set**. In the hands-on activity you will test this.
* **Memorising is not learning.** Imagine a model that scores 92% on the examples it trained on, but only 60% on new examples. It has memorised the training examples rather than finding the general pattern. This is called **overfitting**, and the test on unseen data is exactly how you catch it.

There is also a trade-off between the two ways of building the filter. Hand-written rules are easy to explain: you can point at the rule that fired. A learned model handles new wording better, but it is harder to explain why it called one email spam. This trade-off between **explainable rules** and **flexible learning** comes back in every chapter.

### Check yourself

<details>
<summary>Question 1. Which learning family fits each case: (a) grouping songs by sound with no labels; (b) a robot gets +1 for each metre without falling; (c) predicting tomorrow's temperature from past temperatures?</summary>

(a) Unsupervised learning (clustering). (b) Reinforcement learning. (c) Supervised learning (regression: the label is a number).

</details>

<details>
<summary>Question 2. A medical test is run on 200 people, 10 of whom really have the disease. It finds 8 of them and wrongly flags 12 healthy people. The accuracy is 93%. Is the test "great"?</summary>

True positives = 8, false negatives = 2, false positives = 12, true negatives = 178. Accuracy = (8 + 178) ÷ 200 = 0.93, but precision = 8 ÷ 20 = **0.40** and recall = 8 ÷ 10 = **0.80**. Accuracy is high mainly because most people are healthy. Of the 20 people the test flagged, only 8 are really ill, and 2 ill people are missed. You must look at the kinds of mistakes and what each costs.

</details>

<details>
<summary>Question 3. Why must a model be tested on examples it has not seen?</summary>

A model can memorise its training examples and score perfectly on them without being able to handle anything new. Only unseen examples show whether it learned a general pattern.

</details>

> [!IMPORTANT]
> **In short**
>
> * Machine learning means the computer finds the rules from examples, instead of a person writing them. What it finds is called a **model**.
> * The three families are **supervised** (labelled examples), **unsupervised** (no labels, find structure), and **reinforcement** (learn from reward).
> * A model goes through **training**, **testing**, and **inference**. Always test on examples it has not seen.
> * Accuracy can hide which mistakes were made. Look at precision and recall too. Bad or biased examples give a bad or biased model.

---
|

## Topic 4: Hands-On Activity, Machine Learning

So far you have read about machine learning. Now you will do it. The lecturer's slides include two hands-on tasks built with a block-based programming tool: **Rock Paper Scissors** and **Smart Classroom**. If your lecture uses that tool, follow your lecturer's instructions for the tool itself. If the tool is not available, or its link does not work, use the **paper version** given with each activity. The paper version teaches the same idea without software.

Every activity in this module has six parts: **Goal, Preparation, Task, Observation, Reflection, and Feedback**. The Feedback part has hidden answers, so try each task yourself first.

![Four steps: collect labelled photos, train the model, test it on new photos, then use it and improve the data](chapter-1-introduction-to-cs-and-ai/assets/fig-1-13-hands-on-steps.png)

*Figure 1.13: The four steps of the Rock Paper Scissors activity. The same steps apply to any image classifier.*

**How to read this figure.** The four boxes are the order of work. You **collect** labelled examples (many photos of each hand shape, each with its label). You **train** the model. You **test** it on photos it has never seen. Then you **use** it and look at its mistakes, because wrong answers tell you what is missing in the data, and you add more photos and repeat. Notice that nowhere do you write a rule about fingers. The model learns from the examples.

### Activity A: Rock Paper Scissors (image classification)

**Goal.** Train a classifier with labelled examples, and see how the choice of examples changes the result.

**Preparation.**

* Tool version: the lecture's block tool with a camera, a plain background, and your hand.
* Paper version: pen, paper, and the training table below.
* Optional online tools (links in the References): Machine Learning for Kids and Teachable Machine.

**Task.**

*Tool version (as in the slides)*

1. Create three classes (labels): *rock*, *paper*, *scissors*.
2. Take several photos of your hand for each class. These are the **training examples**.
3. Train the model.
4. Run the program. It recognises a new picture, picks the label, and chooses the move that beats it.
5. Test with different lighting and hand positions.

*Paper version.* Each photo is reduced to two numbers (the features): *how many fingers are open* (0–5) and *how spread out they are* (low, medium, high).

| Training example | Fingers open | Spread | Label |
|---|--:|---|---|
| 1 | 0 | low | rock |
| 2 | 0 | low | rock |
| 3 | 5 | high | paper |
| 4 | 4 | high | paper |
| 5 | 2 | medium | scissors |
| 6 | 2 | medium | scissors |

Use this **distance score** between a new picture and a training example: (difference in fingers) + 1 if the spread is different, + 0 if it is the same. The smallest score wins. For each test picture, find the closest training example and write down its label.

**Observation.** Fill in the table. The first row is done as a model.

| Test | Fingers | Spread | Closest example (score) | Predicted label |
|--:|--:|---|---|---|
| 1 | 2 | medium | Example 5 (score 0) | scissors |
| 2 | 3 | medium | | |
| 3 | 3 | high | | |
| 4 | 1 | low | | |

**Reflection.**

1. For test 2, the new picture matches no training example exactly. How does the model decide?
2. What would happen if every training photo of "rock" were taken in a dark room?
3. How many photos per class are enough? Why can nobody give one fixed number?

**Feedback.**

<details>
<summary>Check your answers</summary>

| Test | Scores | Predicted label |
|--:|---|---|
| 2 (3 fingers, medium) | Rock: 3 + 1 = 4. Paper (5, high): 2 + 1 = 3. Paper (4, high): 1 + 1 = 2. Scissors (2, medium): 1 + 0 = **1**. | scissors |
| 3 (3 fingers, high) | Rock: 3 + 1 = 4. Paper (5, high): 2 + 0 = 2. Paper (4, high): 1 + 0 = **1**. Scissors: 1 + 1 = 2. | paper |
| 4 (1 finger, low) | Rock (0, low): 1 + 0 = **1**. Scissors (2, medium): 1 + 1 = 2. Paper (4, high): 3 + 1 = 4. | rock |

1. It picks the closest example, so it can be wrong. Test 2 is a guess between scissors and paper.
2. The model may learn "dark means rock" instead of the shape of the hand. This is a **biased training set**.
3. There is no fixed number. More *varied* examples (different light, angles, backgrounds) usually help. If you used the tool, write down your own results. Do not assume a number that you did not test.

</details>

### Activity B: Smart Classroom (text and command recognition)

**Goal.** Predict how a program that matches exact text treats different wording. You will test the prediction in Chapter 2 and compare it with a learned model in Chapter 3.

**Preparation.** Pen and paper, and the table below. The program has four exact-match rules: the text *Fan on* switches the fan on, *Fan off* switches it off, *Lamp on* switches the lamp on, and *Lamp off* switches it off. The lecture's block tool is not needed yet.

**Task.** For each typed sentence, predict whether the program does what the person meant: **yes**, **no**, or **depends**. Write the prediction in the table. Then add one sentence of your own.

| # | Typed sentence | Your prediction |
|--:|---|---|
| 1 | Fan on | |
| 2 | fan on | |
| 3 | Fan on please | |
| 4 | Please turn the fan on | |
| 5 | Turn the fan on | |
| 6 | Lamp off | |
| 7 | Switch the lamp off | |
| 8 | (your own sentence) | |

**Observation.** Count how many of the first seven you expect the program to understand.

**Reflection.**

1. What would a person have to do to make the program understand sentence 5?
2. What would a learning program need in order to understand sentence 5?

**Feedback.**

<details>
<summary>Check your answers</summary>

| # | Expected | Reason |
|--:|---|---|
| 1 | yes | Exactly the text of a rule. |
| 2 | depends | A strict comparison treats "fan" and "Fan" as different. Some tools ignore capital letters. Chapter 2 tests this in your tool. |
| 3 | no | Extra word "please". |
| 4 | no | No rule contains this wording. |
| 5 | no | No rule contains this wording. |
| 6 | yes | Exactly the text of a rule. |
| 7 | no | No rule contains this wording. |

Only 2 of the 7 are certain, and 1 depends on the tool.

1. Write more rules, one for each way of saying it.
2. Example sentences with their labels, so that it can learn the pattern. Chapter 3 shows this version.

</details>

### Activity C (optional): Nearest neighbour with more examples

**Goal.** See how adding examples, and how many neighbours you ask, can change a prediction.

**Preparation.** Paper, a pen, and a calculator. The four fruits from Topic 3: apple (6, 2), apple (7, 3), lemon (3, 9), lemon (2, 8), written as (size, sourness).

**Task.**

1. A new fruit has size 4 and sourness 7. Compute its distance to each of the four fruits and name the nearest.
2. Now add three more examples, all labelled lemon: (8, 2), (8, 3), and (9, 2). Take the fruit (5, 2). Find its prediction with **k = 1** (the single nearest example), then with **k = 5** (the five nearest examples vote).

**Observation.** Write the distances you computed and the prediction for each test.

**Reflection.** (1) Why can adding examples change a prediction even though the model has no rules? (2) The three added lemons have very low sourness, so they were probably labelled wrongly. What happened to the prediction for (5, 2)? (3) What does this show about **data quality**?

**Feedback.**

<details>
<summary>Check your answers</summary>

1. Distances from (4, 7): apple (6, 2) = √29 ≈ 5.39; apple (7, 3) = 5; lemon (3, 9) = √5 ≈ 2.24; lemon (2, 8) = √5 ≈ 2.24. The nearest are the two lemons, so the prediction is **lemon**.
2. Distances from (5, 2): apple (6, 2) = 1; apple (7, 3) ≈ 2.24; lemon (8, 2) = 3; lemon (8, 3) ≈ 3.16; lemon (9, 2) = 4; the two original lemons are farther than 6. With **k = 1** the nearest example is the apple (6, 2), so the prediction is **apple**. With **k = 5** the five nearest are 2 apples and 3 lemons, so the vote gives **lemon**.

*Reflection:* (1) The model *is* its examples, so adding examples changes which one is nearest. (2) The wrongly labelled lemons are copied into the prediction: the answer flips from apple to lemon as soon as k is large enough to include them. (3) A model is only as good as its data, a point that returns in Chapter 3.

</details>

> [!IMPORTANT]
> **In short**
>
> * In Rock Paper Scissors you gave the machine labelled examples and it found the pattern. Nobody wrote a rule about fingers.
> * The choice of examples decides the result. Too few, too similar, or wrongly labelled examples give a weak or biased model.
> * In Smart Classroom you saw the limit of exact-match rules. You will test it in Chapter 2 and try the learning version in Chapter 3.

---

## Topic 5: Using an AI Assistant for Study

The lecturer's slides list questions to ask an AI assistant, such as "list as many definitions of Computer Science as possible" or "generate an AI knowledge map for freshmen". This is a good way to study, with one rule: **never copy an answer without checking it.** An assistant writes fluent text even when it is wrong. Fluent does not mean true.

![Four steps in a row: ask, read, verify, use or fix](chapter-1-introduction-to-cs-and-ai/assets/fig-1-14-ask-then-verify.png)

*Figure 1.14: Ask, then verify.*

**How to read this figure.** The first two steps are what everybody does: write a clear question and read the answer. The two steps that follow are what turns an answer into something you can trust: **verify** each claim in a textbook, an official site, or the slides, and then **use** what is confirmed and correct or drop the rest.

Use the slide questions like this.

| Slide question | What to do with the answer |
|---|---|
| "Give me a list of buzzwords of the past 50 years regarding computer technology." | Check three of them in a textbook or encyclopedia. |
| "List as many definitions of Computer Science as possible." | Group the definitions into the five viewpoints in Topic 1. |
| "Use a table to list the history of CS, with columns of Year, Key Events, Key People, and Key Technologies." | Compare with the table in Topic 1. Mark every row that differs, and find out which is right. |
| "Generate a CS knowledge map for freshmen." | Compare with the map in Topic 1. What is missing? |
| "List as many definitions of Artificial Intelligence as possible." | Compare with the four viewpoints in Topic 2. |
| "Use a table to list the history of AI, with the same four columns." | Compare with the table in Topic 2. Check at least three dates. |
| "Generate an AI knowledge map for freshmen." | Compare with the map in Topic 2. |

**Record your work.** Use a table like this one for every question, filled in with what you really did. The team's AI-use log needs this information.

| Date | Tool | What I asked | One claim I checked | Source I opened to check it | Right, partly right, or wrong | What I corrected |
|---|---|---|---|---|---|---|
| (date) | (tool) | (question) | (claim) | (source) | (result) | (correction) |

The row above only shows the format. It is not a record of a real check.

> [!IMPORTANT]
> **In short**
>
> * Treat an AI assistant's answer as a claim to check, not as a fact. Verify it in a second source and record what you did.

---

## Common Misconceptions

> [!WARNING]
> Beginners often believe the statements in the left column. Read each one, decide whether it is true, and then check the right column.

| Misconception | What is true | Where to check |
|---|---|---|
| "AI means robots." | Robotics is one area. Most AI is software, such as spam filters, translation, and recommendations. | Topic 2, AI map |
| "AI thinks the way a human brain does." | Neural networks are only loosely inspired by the brain, and Symbolic AI is not brain-like at all. | Chapters 2 and 3 |
| "Machine learning and AI are the same." | Machine learning is a part of AI. Rule-based AI is not machine learning. | Topic 2, nested circles |
| "More data always gives a better model." | Biased or poor data gives a biased or poor model, however much there is. | Activity A |
| "If an AI assistant sounds sure, it is right." | Assistants can be confident and wrong. Check with a reliable source. | Topic 5 |
| "There is one correct definition of AI." | Definitions differ by viewpoint. Check which one a source uses. | Topic 2 |

---

## Key Takeaways

> [!IMPORTANT]
> **If you remember only ten things**
>
> * **CS** is the study of computation, information, and the systems that process them. **AI is one branch of CS.**
> * There is **no single definition** of CS or AI. Read which viewpoint a source uses.
> * AI history moves through three big ideas: **rules and logic** (Symbolic), **connected learning units** (Connectionist), and **learning from reward** (Behaviorist).
> * AI areas (vision, language, speech, planning, robotics) are **tasks**. The three approaches are **methods**.
> * Machine learning has three families: **supervised**, **unsupervised**, and **reinforcement**.
> * A model learns from **examples**. Poor or biased examples lead to poor or biased results.
> * **AI contains machine learning, which contains deep learning.** Symbolic AI is inside AI but outside machine learning.
> * A learning program goes through **training**, **testing**, and **inference**. Test on examples the model has not seen.
> * **Accuracy** can hide which mistakes were made. Look at the kinds of errors.
> * Always **verify** what an AI assistant tells you.

---

## Practice Questions

### Part A: Multiple Choice

**Q1.** Which statement about AI and CS is correct?  
A. AI and CS are unrelated fields.  
B. AI is a branch of CS.  
C. CS is a branch of AI.  
D. AI only studies robots.

**Q2.** In which decade did the Dartmouth workshop use the term "artificial intelligence"?  
A. 1930s  
B. 1940s  
C. 1950s  
D. 1990s

**Q3.** Which task is an example of *supervised classification*?  
A. Grouping customers with no labels  
B. Labelling emails as spam or not spam using labelled examples  
C. A robot learning to walk from rewards  
D. Compressing a file

**Q4.** Which family of machine learning learns from rewards?  
A. Supervised  
B. Unsupervised  
C. Reinforcement  
D. Association

**Q5.** Which pair matches an approach with its core idea?  
A. Symbolic AI: learning from rewards  
B. Connectionist AI: explicit rules and logic  
C. Behaviorist AI: acting and receiving rewards  
D. Symbolic AI: neurons and weights

**Q6.** Why can a Rock Paper Scissors model fail if all "rock" photos were taken in a dark room?  
A. The model may learn lighting instead of hand shape.  
B. The camera breaks.  
C. Rock is a hard word.  
D. It cannot fail.

**Q7.** Which is a *task* (not a method)?  
A. Symbolic AI  
B. Image recognition  
C. Connectionist AI  
D. Behaviorist AI

**Q8.** What should you do with an answer from an AI assistant?  
A. Copy it as it is.  
B. Verify key facts with a reliable source.  
C. Ignore it completely.  
D. Assume it is always correct.

### Part B: Short Answer

**Q9.** Give two different definitions of AI and say how they differ.

**Q10.** Explain the difference between supervised and unsupervised learning in two sentences, with one example each.

**Q11.** In the Smart Classroom activity, why might a rule-based program fail on "Please turn the fan on"?

### Part C: Apply It

**Q12.** A school wants a system that sorts student questions into the categories *homework*, *exam*, and *other*. Would you start with hand-written rules or with machine learning? List one advantage and one disadvantage of your choice.

### Part D: Find the Mistake and Compute

**Q13.** A student writes: "Symbolic AI is a kind of machine learning, because it is also AI." What is wrong with this statement?

**Q14.** Use the "largest so far" algorithm on the list 4, 11, 6, 11. Give the answer and say at which numbers the "largest so far" changes.

**Q15.** Convert 9 to binary, and convert 1101 to decimal.

**Q16.** Use the training fruits of Topic 3 (apple: size 6, sourness 2; apple: 7, 3; lemon: 3, 9; lemon: 2, 8). Predict the label of a new fruit with size 6 and sourness 4. Show the distance to the closest example.

**Q17.** A model scores 92% on the examples it was trained on, but only 60% on new examples. What does this suggest, and what should the team do?

---

## Answer Key

| Q | Answer | Explanation |
|---|---|---|
| Q1 | B | AI is a branch of CS (Topic 1, the map of CS). |
| Q2 | C | The Dartmouth workshop took place in 1956. |
| Q3 | B | Classification with labelled examples is supervised learning. |
| Q4 | C | Reinforcement learning learns from rewards. |
| Q5 | C | Behaviorist AI is about acting and receiving rewards. Symbolic = rules; Connectionist = neurons and weights. |
| Q6 | A | The model can pick up an accidental pattern (lighting). This is a biased training set. |
| Q7 | B | Image recognition is something we want done. The others are ways to do it. |
| Q8 | B | Verify with a reliable source (Topic 5). |
| Q9 | Sample | For example: McCarthy's view (making intelligent machines) is about the goal; the OECD view (a machine that infers outputs from input) describes what the system does. Any two viewpoints from Topic 2 compared fairly is correct. |
| Q10 | Sample | Supervised learning uses labelled examples, such as emails marked spam or not spam. Unsupervised learning uses unlabelled data to find structure, such as grouping customers by buying habits. |
| Q11 | Sample | The rule checks for the exact text, so different wording does not match. A learned model may handle the new wording because it has seen many example sentences. |
| Q12 | Sample | Rules: easy to explain and no training data needed, but each new wording needs a new rule. Machine learning: handles varied wording, but needs many labelled questions and is harder to explain. Either choice is correct with a fair advantage and disadvantage. |
| Q13 | Sample | Machine learning is only a part of AI (Topic 2, nested circles). Symbolic AI uses rules that people write, so it is AI but not machine learning. |
| Q14 | 11 | The largest so far starts at 4, changes at 11 (the first one), and stays 11 afterwards. The second 11 is not bigger than 11. |
| Q15 | 1001; 13 | 9 = 8 + 1, so 1001. 1101 = 8 + 4 + 0 + 1 = 13. |
| Q16 | apple | Distances: apple (6, 2): √(0 + 4) = 2.00; apple (7, 3): √(1 + 1) ≈ 1.41; lemon (3, 9): √(9 + 25) ≈ 5.83; lemon (2, 8): √(16 + 16) ≈ 5.66. The closest is the apple with size 7 and sourness 3. |
| Q17 | Sample | The model may have memorised its training examples and does not work well on new ones (this is called overfitting, Chapter 3). The team should test on unseen data, add more varied examples, and check whether the training set is biased. |

---

## What Comes Next: From Words to Rules

**What you have now.** The vocabulary and the map of the field, a short history of CS and AI, the difference between AI, machine learning, and deep learning, and a first working example of a model that learns from examples.

**What is still missing.** You have seen two ways to build the same spam filter: a person writes rules, or the machine learns them. You have only studied the second way closely. The first way is much older, and a lot of useful AI is built with it.

**Chapter 2 starts there.** It studies **Symbolic AI**, where people write the knowledge down as symbols, rules, and logic, and the machine reasons with it and searches for a plan. You have already met the idea twice: the spam rules in Topic 3 and the exact-match rules of Activity B. In Chapter 2 you will see how far such rules can go, and where they stop working. That stopping point is what opens the door to Chapter 3.

**Keep your prediction table from Activity B.** In Chapter 2 you will test it against real rules and find out which predictions were right. Question to carry into the next chapter: *What does a rule-based program do with a sentence that no rule mentions?*

---

## Key Terms in Chinese

Many of you will meet these terms in Chinese textbooks. The English term is the one this module uses. *Check the Chinese terms against your course textbook or a Chinese-speaking teammate; wording can vary between books.*

| English | 中文 |
|---|---|
| Computer Science | 计算机科学 |
| Artificial Intelligence (AI) | 人工智能 |
| algorithm | 算法 |
| data | 数据 |
| model | 模型 |
| training | 训练 |
| label | 标签 |
| machine learning | 机器学习 |
| deep learning | 深度学习 |
| supervised learning | 监督学习 |
| unsupervised learning | 无监督学习 |
| reinforcement learning | 强化学习 |
| Symbolic AI | 符号主义（符号人工智能） |
| Connectionist AI | 连接主义 |
| Behaviorist AI | 行为主义 |

## Glossary

| Term | Meaning |
|---|---|
| **Accuracy** | The share of decisions that a model gets right on test examples. |
| **Agent** | Something that perceives its environment and acts on it to reach a goal. |
| **Algorithm** | A step-by-step procedure for solving a problem. |
| **Artificial Intelligence (AI)** | The field of making machines perform tasks that normally need intelligence. |
| **Binary** | A number system that uses only 0 and 1. |
| **Binary search** | A search on a sorted list that checks the middle item and discards half of the remaining items each time. |
| **Bit** | One binary digit, 0 or 1. |
| **Classification** | Predicting a category for an item. |
| **Clustering** | Grouping similar items without labels. |
| **Computer Science (CS)** | The study of computation, information, and computing systems. |
| **Confusion matrix** | A table that counts true positives, false negatives, false positives, and true negatives. |
| **Data** | Facts recorded in a form a computer can use. |
| **Encoding** | An agreement about which numbers stand for which letters, pictures, or sounds. |
| **F1 score** | A single number that combines precision and recall. |
| **Feature** | A measurable property of an example that a model looks at, such as size or sourness. |
| **Inference** | Using a trained model on new input to get an output. |
| **Knowledge base** | The facts and rules that a symbolic system reasons with. |
| **Label** | The correct answer attached to a training example. |
| **Linear search** | A search that checks the items one by one. |
| **Machine learning (ML)** | A way for programs to improve at a task by learning from data. |
| **Model** | What a machine-learning method produces by learning: numbers plus the procedure that turns an input into an output. |
| **Narrow AI** | An AI system that is good at specific tasks only. |
| **Nearest neighbour** | A simple learning method that gives a new item the label of the most similar training example. |
| **Overfitting** | When a model has memorised its training examples and does not work well on new ones. |
| **Pixel** | One tiny square of a picture. |
| **Precision** | Of the items a model called positive, the share that really were positive. |
| **Recall** | Of the items that really were positive, the share that the model found. |
| **Regression** | Predicting a number. |
| **Reinforcement learning** | Learning to act by receiving rewards. |
| **Reward** | A number that tells an agent how good the result of its last action was. |
| **Rule** | An IF–THEN statement written by a person. |
| **Supervised learning** | Learning from labelled examples. |
| **Test data** | Examples kept apart from training, used to check a model. |
| **Training** | Adjusting a model, using examples or rewards, so that it does a task better. |
| **Training example** | One piece of data used to teach a model. |
| **Unsupervised learning** | Finding structure in data that has no labels. |

---

## References

1. Course slides, "chap1: Intro to CS and AI". Lecturer's course materials (no public link). Primary source for the outline, the CS and AI maps, and the hands-on activities.
2. McCarthy, J. (2007). *What is Artificial Intelligence?* Stanford University. [http://jmc.stanford.edu/artificial-intelligence/what-is-ai/](http://jmc.stanford.edu/artificial-intelligence/what-is-ai/) *(not opened; definition summarised in Topic 2)*
3. OECD. *AI Principles* and the OECD description of an AI system. [https://www.oecd.org/en/topics/ai-principles.html](https://www.oecd.org/en/topics/ai-principles.html) *(not opened; check the current wording)*
4. Russell, S., and Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson. [https://aima.cs.berkeley.edu/](https://aima.cs.berkeley.edu/) *(not opened)*
5. Turing, A. M. (1950). Computing Machinery and Intelligence. *Mind*, 59(236), 433–460. [https://doi.org/10.1093/mind/LIX.236.433](https://doi.org/10.1093/mind/LIX.236.433) *(not opened)*
6. Association for Computing Machinery. *ACM Computing Classification System.* [https://dl.acm.org/ccs](https://dl.acm.org/ccs) *(not opened; basis of the CS map)*
7. Encyclopedia pages linked in the history tables of Topics 1 and 2, for example [ENIAC](https://en.wikipedia.org/wiki/ENIAC) and [Dartmouth workshop](https://en.wikipedia.org/wiki/Dartmouth_workshop). *(starting points only; not opened; confirm each row in a second source)*
8. Machine Learning for Kids (Dale Lane). [https://machinelearningforkids.co.uk/](https://machinelearningforkids.co.uk/) *(optional tool for Activity A; not opened)*
9. Teachable Machine (Google). [https://teachablemachine.withgoogle.com/](https://teachablemachine.withgoogle.com/) *(optional tool for Activity A; not opened)*
10. Britannica. "Deep Blue." [https://www.britannica.com/print/article/155485](https://www.britannica.com/print/article/155485) *(match result 3½–2½; read with a fetch tool on 5 November 2026; a person should open it again)*
11. Wikipedia. "AlphaGo versus Lee Sedol." [https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol](https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol) *(dates, venue, and score 4–1; read with a fetch tool on 5 November 2026)*
12. Silver, D., Huang, A., et al. (2016). "Mastering the game of Go with deep neural networks and tree search." *Nature*, 529(7587), 484–489. [https://doi.org/10.1038/nature16961](https://doi.org/10.1038/nature16961) *(citation taken from the Wikipedia page above; the paper itself was not opened)*

> **Link status.** Links marked **not opened** could not be opened while this chapter was written. The author or reviewer must click every link, confirm that it opens the right work and supports the claim it is cited for, and then change the label to "opened" with the date.

---

| Start of the module | [Module overview](../../README.md) | [Chapter 2: Symbolic AI →](chapter-2-symbolic-ai/symbolic-ai.md) |
|:--|:-:|--:|

---

![Chapter 2 banner: Symbolic AI](chapter-2-symbolic-ai/assets/fig-2-0-banner.png)

# Chapter 2: Symbolic AI

> **Module:** AI Overview  
> **Chapter:** 2 of 4 (course Chapter 4)  
> **Version:** 2.0 (Stage 2; developed from the Stage 1 chapter, version 1.1)  
> **Author:** Gandhi Bestin Dhammananda (proposed owner)  
> **Reviewer:** Brian Djoni Suzanna (review pending; no signed review exists for this version)  
> **Audience:** Complete beginners with basic computer and internet literacy; no programming needed  
> **Study time:** about 4.5 hours, including the hands-on activity  
> **Course source:** Lecturer's slides "chap4: Symbolic AI". The chapter follows the slides' six topics: Introduction, Logic and Reasoning, Knowledge Representation, Rule-Based Systems and Expert Systems, Planning and Problem Solving, and Natural Language Processing in Symbolic AI.

| [← Chapter 1: Introduction to CS and AI](chapter-1-introduction-to-cs-and-ai/introduction-to-cs-and-ai.md) | [Module overview](../../README.md) | [Chapter 3: Connectionist AI and Big Data →](chapter-3-connectionist-ai-and-big-data/connectionist-ai-and-big-data.md) |
|:--|:-:|--:|


<details>
<summary><b>Contents</b></summary>

1. [Where This Chapter Fits](#where-this-chapter-fits-1)
2. [What You Will Learn](#what-you-will-learn-1)
3. [Topic 1: Introduction to Symbolic AI](#topic-1-introduction-to-symbolic-ai)
4. [Topic 2: Logic and Reasoning](#topic-2-logic-and-reasoning)
5. [Topic 3: Knowledge Representation](#topic-3-knowledge-representation)
6. [Topic 4: Rule-Based Systems and Expert Systems](#topic-4-rule-based-systems-and-expert-systems)
7. [Topic 5: Planning and Problem Solving](#topic-5-planning-and-problem-solving)
8. [Topic 6: Natural Language Processing in Symbolic AI](#topic-6-natural-language-processing-in-symbolic-ai)
9. [Hands-On Activity: A Rule-Based Smart Classroom](#hands-on-activity-a-rule-based-smart-classroom)
10. [Common Misconceptions](#common-misconceptions-1)
11. [Key Takeaways](#key-takeaways-1)
12. [Practice Questions](#practice-questions-1)
13. [Answer Key](#answer-key-1)
14. [What Comes Next: From Written Rules to Learned Weights](#what-comes-next-from-written-rules-to-learned-weights)
15. [Key Terms in Chinese](#key-terms-in-chinese-1)
16. [Glossary](#glossary-1)
17. [References](#references-1)

</details>

---

## Where This Chapter Fits

Chapter 1 ended with a question: you saw two ways to build the same spam filter, one with rules written by a person and one learned from examples, but you studied only the second one closely. Chapter 2 goes back to the first way. It is the oldest approach to AI, and it is still used today.

![Four cards, one per chapter, with Chapter 2 highlighted](chapter-2-symbolic-ai/assets/fig-2-1-how-the-chapters-connect.png)

*Figure 2.1: How the four chapters build on each other. You are in Chapter 2.*

**How to read this figure.** Find the highlighted card, Chapter 2. Its **core idea** is that people write the knowledge down as rules and logic. Its **strength** is that the system is clear and explainable. Its **weak point**, in the red part, is the reason Chapter 3 exists: rules are very hard to write for pictures, speech, and open-ended language.

| | Before this chapter | In this chapter | In the next chapter |
|---|---|---|---|
| **What you know** | AI, machine learning, and the idea of a model. You have seen that a machine can follow rules or learn them. You made predictions about the Smart Classroom. | How a machine can **reason** with knowledge that people write down: logic, knowledge representation, rule-based and expert systems, search, and language rules. | A machine that **learns its own rules** from examples, stored as numbers in a neural network. |
| **Main question** | What does it mean for a machine to learn? | What can a machine do when we write the knowledge for it, and where does that stop working? | What if the knowledge is too big or too hard to write by hand? |

## What You Will Learn

After this chapter you should be able to:

1. **Explain** what Symbolic AI is and name its strengths and limits. (Topic 1)
2. **Use** propositional and predicate logic to write statements and to tell valid reasoning from invalid reasoning. (Topic 2)
3. **Describe** five ways to represent knowledge and say when each one fits. (Topic 3)
4. **Trace** a rule-based system with forward chaining, and describe the parts of an expert system. (Topic 4)
5. **Describe** how a machine plans and solves problems by search, and compare breadth-first, depth-first, A\*, minimax, and local search. (Topic 5)
6. **Explain** how rule-based language processing works and why it breaks. (Topic 6)
7. **Build** a rule-based program, test it, and find where it fails. (Hands-on activity)

---

## Topic 1: Introduction to Symbolic AI

This topic answers three questions: **what** Symbolic AI is and how it works, **where** it is used, and **what it does well and badly**. The other five topics each go deeper into one part of the picture.

### What Symbolic AI is

**Symbolic AI**, also called **Good Old-Fashioned AI (GOFAI)**, builds intelligence by working with **symbols** (words, labels, logical statements) according to **explicit rules and logic**. A person writes the knowledge down in a form the computer can reason with, and the computer applies it.

Here is the lecturer's example, a rule for medical diagnosis:

```
IF   patient has a fever
AND  patient has a cough
AND  patient has difficulty breathing
THEN patient may have pneumonia
```

The system checks each condition against what it knows about the patient. If all three are true, it concludes "may have pneumonia". Notice two things. First, **you can point at the exact rule that produced the answer**, so the system can explain itself. Second, **a person can edit the rule** when medical knowledge changes, and nothing else in the system has to be rebuilt. Also notice the wording: the rule says *may have*, not *has*. A real medical system is a decision-support tool for doctors. It does not replace them.

The figure shows the three parts that every symbolic system has.

![Knowledge written by people flows into an inference engine, which produces a conclusion and an explanation](chapter-2-symbolic-ai/assets/fig-2-2-symbolic-system.png)

*Figure 2.2: How a symbolic AI system works, using the pneumonia rule.*

**How to read this figure.** Read from left to right. In the first box a person has written the **knowledge**: the facts about this patient and a rule. The second box is the **inference engine**, a general-purpose program that compares the rule's conditions with the facts. It does not know anything about medicine. All three conditions are true, so the rule fires. The third box shows the **output**: a conclusion, and the reason for it. The key idea is the **separation** between knowledge and engine. To give the system new knowledge, you change the first box. To use the same engine for a different job, such as checking loan applications, you give it a different set of rules.

### Where Symbolic AI is used

The slides list four application areas. In each one the symbolic part is the part that follows known rules.

| Application | Symbolic part | Note |
|---|---|---|
| **Digital assistants** (for example Siri) | Rules and grammars that interpret a command, and dialogue rules | Modern assistants combine such parts with machine-learning models (Chapter 3). |
| **Medical diagnosis** | Rules and knowledge bases that suggest a condition from symptoms | Classic expert systems such as MYCIN worked this way. |
| **Autonomous cars** | Traffic rules such as "if the light is red, stop", and route planning by search | Recognising a stop sign from a camera picture is mostly done with neural networks. |
| **Computer vision** | Rules that reason about what was detected (for example, "a pedestrian near a crossing means slow down") | Detecting objects in pixels is mostly done with neural networks. |

The pattern in the last two rows matters. **Most real systems are hybrids.** The symbolic part handles *reasoning with known rules*. The learning part (Chapter 3) handles *messy sensor data* such as pictures and sound. So Symbolic AI is not obsolete. It is one half of many modern systems.

### What it does well and what it does badly

| Strength | What it means in practice |
|---|---|
| **Interpretability** | You can trace the reasoning from the conclusion back to the rules. This matters in medicine, law, and finance, where someone must be able to ask "why?". |
| **Structured knowledge** | Complex knowledge can be stored in a formal, organised way, so it can be checked and reused. |
| **Flexibility of the knowledge** | Change the rules or the knowledge base and the system adapts to a new domain, without redesigning the engine. |

| Limitation | What it means in practice |
|---|---|
| **Incomplete knowledge** | The system works only if the knowledge is complete. For a situation no rule covers, it does nothing, or does the wrong thing. This is called **brittleness**. |
| **Scalability** | The more symbols and rules there are, the more computing work is needed, and the harder it is to keep the rules consistent. |
| **Uncertain or ambiguous information** | Rules need precise statements. "Fairly warm" or "maybe" is hard to write as a rule. |
| **Limited ability to learn** | A person must write and update every rule by hand. |

The two lists are two sides of one fact: **the knowledge is written by people**. That makes the system clear and editable, and it also makes it limited by what people can write down. The rest of the chapter shows this trade-off again and again.

### Check yourself

<details>
<summary>Question 1. A school library lets a student borrow a book only if the student has a valid card, has fewer than 5 books on loan, and has no overdue book. Write one IF–THEN rule, then say what happens for a student with a valid card, 5 books on loan, and no overdue book.</summary>

```
IF   student has a valid card
AND  books on loan < 5
AND  student has no overdue book
THEN allow borrowing
```

The student is **refused**, because 5 is not fewer than 5. The system can name the exact condition that refused the request, which is the explainability of Symbolic AI. If the library later allows 6 books, only one number in the rule changes.

</details>

<details>
<summary>Question 2. Why is Symbolic AI called "brittle"?</summary>

Because it handles only the cases that its rules cover. For a situation that nobody wrote a rule for, it fails instead of adapting, like a brittle object that breaks instead of bending.

</details>

> [!IMPORTANT]
> **In short**
>
> * Symbolic AI represents knowledge as symbols and rules that people write. An inference engine applies them to facts.
> * Its strengths are exactness and explanation: you can point to the rule that produced an answer.
> * Its limits are brittleness (it fails on cases no rule covers), the effort of writing rules, and difficulty with messy sensor data.
> * Most real systems are hybrids: symbolic reasoning for known rules, learning for messy data.

---

## Topic 2: Logic and Reasoning

Rules such as "IF fever AND cough THEN…" are a small piece of something bigger: **logic**. Logic is the precise language in which a machine can state facts and the exact method by which it can derive new facts from old ones. This topic builds it in two layers: **propositional logic** (whole statements) and **predicate logic** (statements about things and their properties).

Why does a machine need logic, when people reason without it? Because people use common sense to fill gaps, and a machine has none. Consider the sentence "If it rains, the ground is wet." Does it follow that "if the ground is wet, it rained"? A person knows at once that it does not (someone may have watered the garden). A computer can only know this if its reasoning rules are exact.

### Propositional logic

A **proposition** is a declarative sentence that is either **true or false, but not both**.

* "The sky is blue." is a proposition.
* "2 + 2 = 4." is a proposition (true).
* "Close the door!" is **not** a proposition. It is a command, so it is neither true nor false.

Take two propositions: **p** = "It is raining" and **q** = "It is windy". We build bigger statements with **Boolean operators**.

| Operator | Symbol | Reads as | True when |
|---|:-:|---|---|
| AND | ∧ | p ∧ q: "raining and windy" | both p and q are true |
| OR | ∨ | p ∨ q: "raining or windy (or both)" | at least one is true |
| NOT | ¬ | ¬p: "not raining" | p is false |

A **truth table** lists every possible combination of true (T) and false (F) and the result.

| p | q | p ∧ q | p ∨ q | ¬p |
|:-:|:-:|:-:|:-:|:-:|
| T | T | T | T | F |
| T | F | F | T | F |
| F | T | F | T | T |
| F | F | F | F | T |

Two statements are **logically equivalent** when they have the same truth value in every row. Two useful equivalences are **De Morgan's laws**, ¬(p ∧ q) ≡ ¬p ∨ ¬q and ¬(p ∨ q) ≡ ¬p ∧ ¬q, and **double negation**, ¬(¬p) ≡ p. To check the first law in one case, let p = T and q = F. Then p ∧ q = F, so ¬(p ∧ q) = T. On the other side ¬p = F and ¬q = T, so ¬p ∨ ¬q = T. Both sides agree. In words, "it is not true that I have both a pen and a pencil" means the same as "I lack a pen or I lack a pencil".

The most important operator for AI is the **implication**, because every rule is one. The statement **p → q** reads "if p, then q". Here p is the **antecedent** (the condition) and q is the **consequent** (the conclusion). A related statement, **p ↔ q**, reads "p if and only if q" and means that p and q always have the same truth value.

| p | q | p → q | p ↔ q |
|:-:|:-:|:-:|:-:|
| T | T | T | T |
| T | F | **F** | F |
| F | T | T | F |
| F | F | T | T |

Look at the implication column. "If it is raining, then the ground is wet" is false in only **one** situation: it is raining and the ground is *not* wet. If it is not raining, the statement does not claim anything, so it counts as true. This surprises many beginners, but it is the right definition for rules: a rule is broken only when its condition holds and its conclusion does not.

### Rules of inference

**Inference** means deriving a new statement from statements we already accept. An inference rule is valid if it can never lead from true statements to a false one. Two valid rules matter most.

![Three cards: modus ponens and modus tollens are valid, affirming the result is invalid](chapter-2-symbolic-ai/assets/fig-2-3-valid-invalid.png)

*Figure 2.3: Two valid rules and one common mistake, all starting from "If it rains, the ground is wet."*

**How to read this figure.** Each card starts from the same rule and adds a different fact. In the left card the fact is "it rains", and the conclusion "the ground is wet" must be true: this is **modus ponens** ("the mode that affirms"). In the middle card the fact is "the ground is *not* wet", and the conclusion "it is not raining" must be true, because if it were raining the ground would be wet: this is **modus tollens** ("the mode that denies"). In the red card the fact is "the ground is wet", and the conclusion "so it rained" does **not** follow, because the ground could be wet for another reason. This mistake is called *affirming the consequent*, and it is the most common error in everyday reasoning.

An AI system that reasons with rules must avoid the red card. This is the reason for formal logic: it makes the check mechanical.

### Predicate logic

Propositional logic treats "Socrates is a man" as one indivisible block. It cannot say "**all** men are mortal" in a way that applies to Socrates. **Predicate logic** (also called first-order logic) looks inside the sentence.

* A **predicate** is a statement with a variable that is true or false depending on the value. **Even(x)** is true for x = 4 and false for x = 5.
* The **universal quantifier ∀** means "for all". ∀x (Cat(x) → Mammal(x)) reads "every cat is a mammal".
* The **existential quantifier ∃** means "there exists at least one". ∃x (Prime(x) ∧ x < 10) reads "some prime number is less than 10" (true: 2, 3, 5, 7).

To turn an English sentence into logic, follow four steps. Take "Some birds can fly."

| Step | Action | Result |
|---|---|---|
| a | Identify the predicates | Bird(·), CanFly(·) |
| b | Introduce a variable | y |
| c | Apply the quantifier | "Some" means ∃ |
| d | Write the expression | ∃y (Bird(y) ∧ CanFly(y)) |

A habit worth learning: **∀ goes with →, and ∃ goes with ∧.** "Every cat is a mammal" is ∀x (Cat(x) → Mammal(x)). If you wrote ∀x (Cat(x) ∧ Mammal(x)) it would say that *everything* is a cat and a mammal.

The connectives work as before. For example, Adult(x) → CanVote(x) says "if x is an adult, x can vote (in a given rule set)", and ¬Married(x) says "x is not married". One more example needs care: ∀x (Even(x) → Positive(x)) is **false** if x ranges over all integers, because −2 is even but not positive. It is true only if x ranges over positive numbers. A logic statement is true or false **relative to a domain**, so a knowledge base must say what its variables range over.

The slides give four more inference rules for quantifiers.

| Rule | In words | Form |
|---|---|---|
| **Universal instantiation** | If it is true for all x, it is true for a particular a | from ∀x (P(x) → Q(x)) to P(a) → Q(a) |
| **Existential instantiation** | If something has the property, give it a *new* name c | from ∃x (P(x) ∧ Q(x)) to P(c) ∧ Q(c) |
| **Universal generalization** | If it holds for an *arbitrary* a, it holds for all | from P(a) → Q(a) to ∀x (P(x) → Q(x)) |
| **Existential generalization** | If it holds for a particular c, then something exists | from P(c) ∧ Q(c) to ∃x (P(x) ∧ Q(x)) |

The slides ask: "Do you see anything strange about these four rules?" Yes, and the answer is the point of the table.

* **Existential generalization** is always safe. If c has the property, then *something* has it.
* **Universal instantiation** is always safe. What holds for everything holds for a.
* **Existential instantiation** is safe only if the name c is **new**. We know that *some* x has the property but not which one. If c is already the name of something else, the step is wrong.
* **Universal generalization** is the strange one. Going from **one** example to **all** is **not valid** in general. "My cat is black" does not prove "all cats are black". The rule is valid only when a is **arbitrary**, meaning we assumed nothing special about it.

The classic use is the one you know from school logic. Premises: ∀x (Human(x) → Mortal(x)) and Human(Socrates). **Universal modus ponens** gives **Mortal(Socrates)**. Together with its mirror image, universal modus tollens (from ∀x (P(x) → Q(x)) and ¬Q(a), conclude ¬P(a)), this is how a rule-based system applies a general rule to a particular case.

### Check yourself

<details>
<summary>Question 1. For p = true and q = false, what is p → q? Why?</summary>

It is **false**. An implication is false only when the condition is true and the conclusion is false.

</details>

<details>
<summary>Question 2. "If it rains, the ground is wet. The ground is not wet." Which conclusion is valid?</summary>

"It is not raining." This is modus tollens. The conclusion "it is raining" would be wrong.

</details>

<details>
<summary>Question 3. Write "Every student is tired" and "Some students are not tired" in predicate logic, using Student(x) and Tired(x).</summary>

"Every student is tired": ∀x (Student(x) → Tired(x)).  
"Some students are not tired": ∃x (Student(x) ∧ ¬Tired(x)).

</details>

> [!IMPORTANT]
> **In short**
>
> * Logic gives a machine an exact language for facts (propositions, predicates) and exact rules for deriving new facts (inference).
> * An implication p → q is false only when p is true and q is false.
> * Modus ponens and modus tollens are valid. Affirming the consequent ("q is true, so p is true") is not.
> * ∀ goes with →, and ∃ goes with ∧. A statement is true or false relative to a domain.

---

## Topic 3: Knowledge Representation

Logic tells a machine *how to reason*. Before it can reason, it needs something to reason **about**: facts about the world, written in a form it can use. **Knowledge representation (KR)** is the work of structuring information so that a program can use it to reason, solve problems, and make decisions.

The slides give three reasons why this matters. First, **reasoning**: well-structured knowledge allows logical inference. Second, **problem solving**: well-organised information makes hard problems easier. Third, **learning**: structured knowledge can be extended and generalised. In short, a machine cannot be smarter than the way its knowledge is written. A fact that is stored in a form the machine cannot use might as well not be stored.

### Five ways to write the same knowledge

There is no single best way to write knowledge. The figure takes one small piece of knowledge, "Birds can fly. A penguin is a bird. A penguin cannot fly", and writes it five ways.

![Five cards showing the same penguin knowledge as logic, a semantic network, a frame, a rule, and an ontology](chapter-2-symbolic-ai/assets/fig-2-4-five-representations.png)

*Figure 2.4: One piece of knowledge in five forms. Each form suits a different job.*

**How to read this figure.** Each card is one representation, and the bottom line says what it is good for. Compare the cards, not the details. The **logic** card is exact and supports formal proofs. The **semantic network** card shows relationships as links. The **frame** card describes a typical object with named slots. The **rule** card is an IF–THEN statement that can be applied to decide something. The **ontology** card defines classes and properties so that different systems can share one vocabulary. Notice that every card needs a way to say "except penguins". Exceptions are the hardest part of knowledge.

Here is each form in more detail.

**1. Logic-based representation.** Facts are statements in propositional or predicate logic: P = "It is raining", or ∀x (Human(x) → Mortal(x)). Logic is exact and supports proofs, but it is hard to write everyday knowledge in it.

**2. Semantic networks.** Knowledge is a graph. The **nodes** are concepts and the **links** are relationships. The next figure shows a small network and how it handles an exception.

![A network with Animal at the top, Bird and Mammal below, then Penguin, Sparrow and Whale, with properties such as can fly and cannot fly](chapter-2-symbolic-ai/assets/fig-2-5-semantic-network.png)

*Figure 2.5: A semantic network. Properties are passed down along "is a" links, and a more specific property overrides the inherited one.*

**How to read this figure.** Arrows labelled "is a" go from a specific concept to a more general one: a sparrow *is a* bird, a bird *is an* animal. The green bubbles are properties. A concept **inherits** the properties of everything above it, so a sparrow can fly (from Bird) and has skin (from Animal) although nobody wrote those facts on the Sparrow node. The red bubble shows an **exception**: a penguin is a bird, but its own "cannot fly" overrides the inherited "can fly". This saves a great deal of writing, because facts are stored once at the most general level. It also needs a rule for handling exceptions, and a network that is not careful about this will wrongly conclude that penguins fly.

**3. Frames and scripts.** A **frame** is a data structure for a typical object or situation, with named **slots**. A "car" frame has the slots make, model, year, and colour; one particular car fills them in (Toyota, Corolla, 2019, white). A **script** is a sequence of frames for a typical event. "Going to a restaurant" is a script made of the frames *reservation*, *ordering*, and *paying the bill*, which lets a program fill in what usually happens even when a story does not mention it.

**4. Rule-based representation.** Knowledge is a set of **IF–THEN** production rules: "If the patient has a fever and a cough, then consider a respiratory infection." This is the form used by the expert systems in the next topic.

**5. Ontologies.** An ontology is a formal description of the **concepts in a domain and the relationships between them**, which gives everyone a shared vocabulary. A medical ontology defines *disease*, *symptom*, and *treatment*, and how they relate: a disease *has symptom* a symptom, and a treatment *treats* a disease. Its main value is agreement: two hospital systems that use the same ontology can exchange information without misunderstanding each other.

| Method | Best for | Weakness |
|---|---|---|
| Logic | Precise reasoning and proof | Hard to write for everyday knowledge |
| Semantic network | Showing relationships and "is a" inheritance | Can be vague about the exact meaning of a link |
| Frames and scripts | Typical objects and routines | Struggles with exceptions |
| Rules | Decisions and advice | Many rules are hard to keep consistent |
| Ontology | A shared vocabulary across systems | Costly to build, and people must agree on it |

### Where knowledge representation is used

* **Medical diagnosis.** Symptoms, diseases, and medical expertise are stored so that a system can match them.
* **Natural language understanding.** Linguistic knowledge is represented so that a program can understand and produce language (Topic 6).
* **Robotics.** Spatial relations, objects, and task plans are represented so that a robot can reason about its surroundings.
* **Expert systems.** Domain knowledge is stored as rules so that the system can give expert-level advice (Topic 4).

### Check yourself

<details>
<summary>Question 1. In Figure 2.5, a whale "is a" mammal and a mammal "has fur". What does the network wrongly conclude about whales, and what does that show?</summary>

It concludes that whales have fur, which is wrong (whales are almost hairless). It shows that inheritance is only as good as its general facts, and that a careful network must record exceptions. Real knowledge has many exceptions, which is why "All birds can fly" is a poor rule.

</details>

<details>
<summary>Question 2. Which representation would you choose to say that a school's "lesson" has a teacher, a room, and a time slot? Why?</summary>

A **frame**: it describes a typical object with named slots (teacher, room, time slot), and each real lesson fills in the slots.

</details>

> [!IMPORTANT]
> **In short**
>
> * Knowledge representation structures information so that a machine can reason with it. A machine cannot be smarter than its representation.
> * Five common forms are logic, semantic networks, frames and scripts, rules, and ontologies. Each has a best use and a weakness.
> * Inheritance saves writing but needs a way to handle exceptions.

---

## Topic 4: Rule-Based Systems and Expert Systems

Topic 3 listed rules as one way to write knowledge. This topic shows what a machine can **do** with rules. It answers three questions: how a rule-based system is built, how rules trigger one another to reach a conclusion nobody typed in, and how all this is packaged into an expert system.

### Rule-based systems

A **rule-based system** (also called a **production system**) works with a collection of **condition–action rules**. Each rule has a condition (the IF part) and an action (the THEN part). Examples: "If the temperature is greater than 30 °C, then turn on the air conditioning." "If the customer has purchased more than $100 of goods, then offer a 10% discount."

Every rule-based system has three parts.

| Part | Role |
|---|---|
| **Condition–action rules** | The knowledge: what to do in which situation |
| **Knowledge base** (working memory) | The facts the system currently knows |
| **Inference engine** | The program that checks the conditions and triggers the actions |

The simplest example is a thermostat with two rules: **R1:** if the temperature is above 25 °C, turn on the air conditioning. **R2:** if the temperature is below 20 °C, turn on the heating.

| Current temperature | R1 fires? | R2 fires? | Action |
|--:|:-:|:-:|---|
| 28 °C | yes | no | Air conditioning on |
| 22 °C | no | no | Nothing |
| 15 °C | no | yes | Heating on |

A thermostat looks too simple to be AI, and that is the point: the same three parts, scaled up to thousands of rules, are what the first commercial AI systems were made of.

### Forward chaining: rules triggering rules

The interesting thing happens when the result of one rule becomes the condition of another. In **forward chaining**, the engine starts from the known facts and keeps applying rules until no new fact appears. Take the facts "it is raining" and "I am going outside", and two rules. **R1:** if it is raining, then the ground is wet. **R2:** if the ground is wet and I am going outside, then take an umbrella and wear waterproof shoes.

![A chain: known facts, rule R1 fires, new fact the ground is wet, rule R2 fires, new fact take an umbrella](chapter-2-symbolic-ai/assets/fig-2-6-forward-chaining.png)

*Figure 2.6: Forward chaining on the umbrella example.*

**How to read this figure.** Follow the arrows. The known facts make R1's condition true, so R1 **fires** and adds a new fact, "the ground is wet". That new fact makes R2's condition true, so R2 fires and adds the final fact, the advice. The engine then checks again, finds no rule with a new result, and stops. Nobody typed "take an umbrella" as a conclusion. The system **derived** it by chaining two rules. The box at the bottom shows a major benefit: the trace of rules that fired *is* the explanation.

| Step | Facts known | Rule that fires | Result |
|--:|---|---|---|
| 0 | raining; going outside | none | start |
| 1 | raining; going outside | R1 | adds "ground is wet" |
| 2 | raining; going outside; ground wet | R2 | adds "take umbrella and waterproof shoes" |
| 3 | all facts | none | stop |

There is a mirror-image method called **backward chaining**. Instead of starting from the facts, the engine starts from a **goal** ("should I take an umbrella?") and works backward: which rule would conclude this, and are its conditions true? If a condition is not known, that condition becomes a new goal. Forward chaining suits problems where you collect data and want to know what follows. Backward chaining suits problems where you have one question to answer. Prolog, a programming language built around this idea, is used in AI courses.

Two problems appear when rules interact. The first is **incomplete knowledge**: if no rule matches, the system does nothing, even when something should be done. The second is **conflicting rules**: two rules can fire at once and give opposite advice. The engine then needs a **conflict resolution** strategy, such as a fixed priority order (rule R5 before R4), the most specific rule first, or the most recently added rule first. You will meet both problems in the hands-on activity.

### Expert systems

An **expert system** is a rule-based system built to copy the decision-making of a **human expert in a narrow domain**, such as medicine, finance, or engineering. In addition to the knowledge base and inference engine, it has a **user interface**, through which a non-expert enters data and reads the advice.

![A human expert talks to a knowledge engineer, who writes the knowledge base; a user talks to the system through the interface and gets advice with an explanation](chapter-2-symbolic-ai/assets/fig-2-7-expert-system.png)

*Figure 2.7: The parts of an expert system and the people around it.*

**How to read this figure.** The top row shows how the knowledge gets into the system: a **knowledge engineer** interviews a human expert (a doctor, for example) and writes what the expert knows as rules and rules of thumb, called **heuristics**. These go into the **knowledge base**. The bottom row shows how the system is used: a user enters facts about a case, the **inference engine** applies the rules, and the user receives **advice together with an explanation** of which rules led to it.

| | Rule-based system | Expert system |
|---|---|---|
| Focus | Conditional rules for decisions or tasks | Copy the reasoning of a human expert |
| Scope | General-purpose | Specialised in one domain |
| Example | A thermostat | A MYCIN-style infection advisor |

The best-known early expert system is **MYCIN**, built at Stanford in the 1970s. It suggested diagnoses and treatments for blood infections using rules written with doctors. Expert systems were widely used in business in the 1980s. Their main weakness is the **knowledge acquisition bottleneck**: it takes a very long time to get an expert's knowledge out of their head and into rules, and the rules go out of date. This is a large part of why the field moved toward learning from data (Chapter 3).

### Check yourself

<details>
<summary>Question 1. A garden system has three rules. R1: IF the soil is dry AND it is sunny THEN the plant needs water. R2: IF the plant needs water AND the tank is empty THEN refill the tank. R3: IF the plant needs water AND the tank has water THEN water the plant. The facts are: soil is dry; it is cloudy; tank has water. What happens, and what does it show?</summary>

R1 does not fire, because it is not sunny, so no rule fires at all and nothing happens. Yet the soil is dry, so the plant should still be watered. The rules never said what to do on a cloudy day. The program is correct about its rules, but the **knowledge is incomplete**, which is the main limit of Symbolic AI.

</details>

<details>
<summary>Question 2. Rules: R1: if A and B then C. R2: if C then D. R3: if D and E then F. The known facts are A, B, and E. Which facts are known after forward chaining?</summary>

R1 fires (A and B), adding C. R2 fires (C), adding D. R3 fires (D and E), adding F. No rule is left. The facts are **A, B, E, C, D, F**.

</details>

<details>
<summary>Question 3. Rule R4: IF the plant needs water THEN water the plant. Rule R5: IF rain is expected THEN do not water. Both conditions are true. What is the problem and one way to solve it?</summary>

The two rules give opposite advice, which is a **conflict**. One solution is a priority order, for example "R5 before R4", so that the system does not water when rain is expected.

</details>

> [!IMPORTANT]
> **In short**
>
> * A rule-based system has condition–action rules, a knowledge base of facts, and an inference engine.
> * In forward chaining, rules fire and add new facts, which can trigger more rules. The trace of fired rules is the explanation. Backward chaining starts from a goal instead.
> * An expert system copies a human expert in one narrow domain. Its weak point is the effort of getting knowledge into rules (the knowledge acquisition bottleneck).
> * Incomplete knowledge and conflicting rules are the two main problems.

---

## Topic 5: Planning and Problem Solving

Rules and logic tell a machine what is true and what follows. Many problems ask something different: **what should I do?** How do I get a delivery robot to room 305? How do I move a farmer, a wolf, a goat, and a cabbage across a river? How do I choose a good chess move? These are problems of **planning and problem solving**, and the symbolic answer is **search**: describe every situation the machine could be in, and look through them systematically.

### What a problem looks like to a machine

* **Planning** finds a **sequence of actions** that changes an **initial state** into a **goal state**.
* **Problem solving** finds solutions to hard problems by searching, by reasoning about possible actions, and by evaluating the results.

Every such problem is described with four building blocks.

| Block | Meaning | Example: a delivery robot in a building |
|---|---|---|
| **State space** | All states the system can be in | Every position of the robot |
| **Actions** | Steps that move from one state to another, with **preconditions** and **effects** | "Move through door" needs the door open |
| **Goal state** | The desired end state | The robot is at room 305 |
| **Search** | Systematically exploring the state space to find the action sequence | Try routes until room 305 is reached |

A small puzzle makes this concrete. A farmer must take a wolf, a goat, and a cabbage from the left bank of a river to the right bank. The boat carries the farmer and **at most one** item. If the farmer is away, the wolf eats the goat, and the goat eats the cabbage. So the wolf and the goat must never be left alone together, and neither must the goat and the cabbage.

A **state** says which bank each of the four (farmer, wolf, goat, cabbage) is on. A **move** is one crossing. The **goal state** has all four on the right bank. The figure shows the shortest path through the states.

![Eight boxes, each showing the left bank and right bank after a crossing, from the start FWGC | nothing to the goal nothing | FWGC](chapter-2-symbolic-ai/assets/fig-2-8-farmer-states.png)

*Figure 2.8: The farmer puzzle as a path through states. F = farmer, W = wolf, G = goat, C = cabbage.*

**How to read this figure.** Each box is one state, written *left bank | right bank*. The first box is the start: everyone is on the left. Each arrow is one legal crossing, described at the top of the next box. For example, in move 1 the farmer takes the goat over, leaving the wolf and the cabbage alone on the left, which is safe because wolves do not eat cabbages. The last box is the goal. The surprising step is **move 4**, where the farmer brings the goat **back**. It looks like going backwards, but without it the puzzle cannot be solved. A search program finds such moves automatically, because it tries every legal move instead of only the ones that look like progress. (The puzzle has a second solution of the same length, where the cabbage and the wolf swap roles in moves 3 and 5.)

Why not just take the wolf first? Then the goat and the cabbage would be left alone on the left bank and the goat would eat the cabbage. A program knows this only because the rule is written into the **actions**: a move is legal only if it does not leave a forbidden pair alone.

### Uninformed (blind) search

The first family of search methods knows nothing about where the goal is. They only know the structure of the problem.

* **Breadth-first search (BFS)** explores all neighbours at the current depth before going deeper.
* **Depth-first search (DFS)** goes as deep as possible along one branch, then backtracks.
* **Uniform-cost search** always expands the node with the lowest path cost so far.

The figure shows BFS and DFS on the same small tree. The goal is node B, and children are taken left to right.

![Two copies of a six-node tree with visiting order numbers: breadth-first reaches B third, depth-first reaches B fifth](chapter-2-symbolic-ai/assets/fig-2-9-bfs-dfs.png)

*Figure 2.9: BFS and DFS on the same tree, goal B. The numbers give the order of visiting.*

**How to read this figure.** The yellow numbers are the order in which each search visits a node. **BFS** (left) visits S, then both of S's children, A and B, and stops: three nodes. **DFS** (right) goes from S down to A, then down to A's first child C (a dead end), then D (another dead end), backs up, and only then reaches B: five nodes. For this goal BFS is faster, but the result depends on where the goal is. If the goal were E, both would visit six nodes.

What to remember: BFS finds the **shallowest** goal, which means the path with the fewest steps, but it must remember many nodes at once. DFS needs little memory but can wander down a long wrong branch and does not guarantee the shortest path.

### Informed search

Blind search wastes time on directions that obviously lead away from the goal. **Informed search** uses a **heuristic**, an estimate of how close a state is to the goal. A good heuristic is a rule of thumb, for example "straight-line distance to the destination".

* **Greedy best-first search** expands the node that *looks* closest to the goal.
* **A\* search** combines two quantities, **f(n) = g(n) + h(n)**, where **g** is the cost already paid to reach the node and **h** is the estimated cost still to go. It always expands the node with the lowest f.

Here is a small example. The start is S and the goal is G. The roads cost S→A = 1, S→B = 2, A→G = 6, and B→G = 3. The estimates are h(A) = 5 and h(B) = 3.

![A graph with four nodes and road costs, and a box showing f for nodes A and B](chapter-2-symbolic-ai/assets/fig-2-10-astar.png)

*Figure 2.10: A\* decides between two roads using f = g + h.*

**How to read this figure.** The numbers on the lines are road costs. The estimate h is written next to each middle node. For node A, g = 1 and h = 5, so f = 6. For node B, g = 2 and h = 3, so f = 5. B has the lower f, so A\* expands B first, reaches G with total cost 2 + 3 = **5**, and does not need to try the other road, which would cost 1 + 6 = 7.

A\* is both efficient and **optimal** (it finds a cheapest path) **as long as the heuristic never overestimates** the true remaining cost. This condition is easy to forget and important. If a heuristic were too pessimistic, say h(B) = 10 when the true cost is 3, A\* would wrongly think B is a bad road and might return a worse route. An honest estimate, one that is never larger than the truth, keeps A\* safe. A weak but honest estimate (such as h = 0 everywhere) never breaks the answer. It only makes the search do extra work.

### Adversarial search: games

In a two-player game, one player's gain is the other player's loss. The machine must plan against an opponent who also plans.

* **Minimax** assumes that the opponent always plays the best reply. The machine picks the move whose result is best in the worst case.
* **Alpha-beta pruning** skips branches that cannot change the final decision. It gives exactly the same answer as minimax with less work.

The next figure shows a tiny game tree. **Max** (the machine) moves first, then **Min** (the opponent). The numbers in the squares are the final scores, where a high score is good for Max.

![A game tree: Max at the top, two Min nodes, four leaves, with one leaf marked never looked at](chapter-2-symbolic-ai/assets/fig-2-11-minimax.png)

*Figure 2.11: Minimax on a small tree, with alpha-beta pruning.*

**How to read this figure.** Work from the bottom up. In the left branch Min can choose between 3 and 5, and Min picks the smaller, so that branch is worth **3** to Max. Max is now sure of at least 3. In the right branch the first leaf is 2. Min can already force a score of 2 or less there, which is worse for Max than 3, so **it does not matter what the next leaf is**. The leaf with 9 is never examined. That is pruning: the same answer (Max picks the left move) with one leaf fewer to look at. In a real game tree, pruning can remove most of the tree.

### Local search

All the methods above build a solution step by step. **Local search** does the opposite: it starts with a **complete** solution and keeps moving to a neighbouring better one.

* **Hill climbing** always moves uphill. It is simple, but it can get stuck on a small hill (a *local maximum*) while a higher mountain exists elsewhere.
* **Simulated annealing** sometimes accepts a worse move, with a probability that decreases over time, to escape local maxima.

| Family | Looks at | Example use |
|---|---|---|
| Uninformed | Only the structure of the problem | Finding any route in a maze |
| Informed | Structure plus a heuristic | The shortest road route |
| Adversarial | A game with an opponent | Chess, checkers |
| Local | Neighbouring complete solutions | Timetables, circuit layout |

### Why search is hard: combinatorial explosion

Search sounds easy: just try everything. How big is "everything"? Take tic-tac-toe, a game that children play. A **game tree** has a node for every position that can appear and a branch for every legal move.

![Bar chart of positions in the tic-tac-toe game tree after each number of moves, rising to 200,448 after eight moves](chapter-2-symbolic-ai/assets/fig-2-12-tictactoe-explosion.png)

*Figure 2.12: The number of positions in the tic-tac-toe game tree after each number of moves. The total is 549,946.*

**How to read this figure.** The horizontal axis is the number of moves already played, and the bar is how many positions exist at that depth. After 1 move there are 9 positions. After 2 moves there are 72 (9 × 8). After 3 there are 504 (9 × 8 × 7). The counts grow quickly until about move 8, where there are 200,448. They drop at move 9 (127,872) because many games **end early** when someone completes a line. The total is **549,946** positions, and there are **255,168** different complete games, although only 5,478 different boards can occur, because many move orders reach the same board.

For chess, Shannon's rough estimate of the number of possible games is about 10^120, which no computer can search. Real programs therefore use three tricks that you have now met: a **heuristic** (estimate how good a position is), **pruning** (skip useless branches), and **memory** (remember positions already seen). This pressure, the **combinatorial explosion**, is one reason why symbolic search alone was not enough for games such as Go, where Chapters 3 and 4 take over.

### Check yourself

<details>
<summary>Question 1. On the tree in Figure 2.9, the goal is E. In which order does BFS visit nodes and in which order does DFS? Which visits fewer?</summary>

BFS: S, A, B, C, D, E. DFS: S, A, C, D, B, E. Both visit **6** nodes, so neither is faster for this goal.

</details>

<details>
<summary>Question 2. In the A* example, suppose the heuristic is changed to h(A) = 1. Which node is expanded first, and does the final answer change?</summary>

f(A) = 1 + 1 = 2 and f(B) = 2 + 3 = 5, so A is expanded first. Through A the goal is reached with cost 1 + 6 = 7. B (f = 5) is then expanded, and through B the goal costs 5, which is better, so A\* still returns the optimal cost **5**. The answer does not change, because h(A) = 1 never overestimates the true remaining cost (6). The weaker estimate only makes A\* do extra work.

</details>

<details>
<summary>Question 3. Why can alpha-beta pruning skip a branch without changing the result?</summary>

Because once Max already has a guaranteed score from another branch, a branch where Min can force something worse cannot be chosen. Whatever its remaining leaves are, they cannot change Max's decision.

</details>

> [!IMPORTANT]
> **In short**
>
> * Planning finds a sequence of actions from an initial state to a goal state by searching a **state space**.
> * Blind search (BFS, DFS) uses only the structure of the problem. Informed search (A\*) adds a heuristic. A\* is optimal if the heuristic never overestimates.
> * Games use minimax, and alpha-beta pruning gives the same answer with less work.
> * The number of possibilities grows explosively, so real programs need heuristics, pruning, and memory.

---

## Topic 6: Natural Language Processing in Symbolic AI

Human language is the hardest test for rules. **Natural Language Processing (NLP)** is the part of AI that lets computers **understand, interpret, and generate human language**. In symbolic NLP, this work is done with **formal rules, logic, and symbolic representations**. This topic shows how, and then shows why it breaks.

### Syntax and semantics

Two ideas organise the work. **Syntax** is the *structure* of a sentence: word order, phrases, and clauses. **Semantics** is its *meaning*.

For syntax, linguists write **grammar rules**. A small set is enough to describe a simple sentence. Take *The cat chased the mouse.*

| Rule | Meaning |
|---|---|
| S → NP VP | A sentence is a noun phrase plus a verb phrase |
| NP → Det N | A noun phrase is a determiner plus a noun |
| VP → V NP | A verb phrase is a verb plus a noun phrase |

![A parse tree for the sentence, with S at the top, NP and VP below, and the words at the bottom, plus the logic form chased(cat, mouse)](chapter-2-symbolic-ai/assets/fig-2-13-parse-tree.png)

*Figure 2.13: The grammar structure and the meaning of one sentence.*

**How to read this figure.** The tree shows how the rules break the sentence into parts. The sentence **S** splits into a noun phrase **NP** (*the cat*) and a verb phrase **VP** (*chased the mouse*). The VP splits again into a verb and another NP. From the tree the program knows that *cat* is the subject, *chased* is the verb, and *mouse* is the object. The box at the left shows the **meaning** written in logic: **chased(cat, mouse)**. Now the system "knows" who did what to whom, and a different sentence, *The mouse was chased by the cat*, can be mapped to the same logic form.

### What rule-based language processing can do

| Task | How a rule-based system does it | Example |
|---|---|---|
| **Part-of-speech tagging** | Pattern rules for each word | "the" is a determiner; "quick" and "brown" are adjectives; "fox" is a noun |
| **Syntactic parsing** | Grammar rules | Find the subject, verb, and object |
| **Information extraction** | Patterns for names, dates, organisations | Capitalised words after "Mr." may be a person's name |
| **Sentiment analysis** | Lists of positive and negative words | "good", "excellent", "happy" mean positive; "bad", "poor", "disappointed" mean negative |
| **Question answering** | A knowledge graph plus logical inference | "Which symptoms go with disease X?" follows links in a medical knowledge graph |
| **Information retrieval** | Formal representations of documents | Match a legal question to relevant statutes |

Logic helps here too. A knowledge base can store parent(Ann, Ben) and parent(Ann, Carla). A rule says: **sibling(x, y) if x and y have the same parent and x ≠ y**. The system then infers sibling(Ben, Carla) without being told.

### Why rules break

Rule-based NLP is transparent, but it is **brittle**. Language is full of exceptions and ambiguity.

| Rule | Where it fails |
|---|---|
| "A word ending in *-ing* is a verb." | *Thing* and *king* end in -ing and are nouns. |
| "Words in the positive list make the review positive." | "This is **not good**" contains *good* but is negative. |
| "The sentence has the form NP VP NP." | "Time flies like an arrow" can be parsed in more than one way. |

Every rule works on most cases and fails on some, and each patch creates new failures. This is one reason that modern NLP mostly uses learning (Chapter 3), often combined with symbolic parts.

### A famous example: ELIZA

The first chatbot, **ELIZA**, was written by Joseph Weizenbaum at MIT in the mid-1960s (1966 is the usual release date) and is described in a 1966 article in *Communications of the ACM*. Its best-known script, **DOCTOR**, imitated a therapist who reflects the speaker's words back as questions. It used scripted keyword rules, like the three below. This small version checks the rules **in order**, uses the **first** rule that matches, and ignores capital letters.

* **R1:** If the text starts with "I feel ", answer "Why do you feel " + the rest of the text + "?"
* **R2:** If the text contains "mother" or "father", answer "Tell me more about your family."
* **R3:** Otherwise, answer "Please go on."

| # | Input | Rule that fires | Answer |
|--:|---|---|---|
| a | I feel tired | R1 | Why do you feel tired? |
| b | My mother called me | R2 | Tell me more about your family. |
| c | I don't feel well | R3 | Please go on. |
| d | I feel that my mother is angry | R1 | Why do you feel that my mother is angry? |

Inputs a and b work well. Input c shows **brittleness**: the sentence is about feeling unwell, but "I don't feel" does not match "I feel ", so the chatbot says nothing useful. Input d shows two weaknesses at once: R1 comes first, so the family rule is never reached, and the chatbot repeats "my mother" instead of changing it to "your mother". The rules do not understand the sentence. They only match text.

The lesson is older than modern chatbots: **a program can produce replies that *seem* attentive using only pattern matching, and people are quick to read understanding into fluent text.** When you evaluate any chatbot, ask how it produces its answers, not only how they sound.

### Check yourself

<details>
<summary>Question 1. Give one example where a rule-based sentiment analyser fails, and say why.</summary>

"The film was not good" contains the positive word *good*, so a word-list rule marks it positive, although the sentence is negative. The rule cannot see negation.

</details>

<details>
<summary>Question 2. With the ELIZA-style rules above, what does the chatbot answer to "My father and I feel tired"? Why does R1 not fire?</summary>

R2 fires, so the answer is "Tell me more about your family." R1 needs the text to *start with* "I feel ", but this text starts with "My father".

</details>

> [!IMPORTANT]
> **In short**
>
> * Symbolic NLP uses grammars (for structure) and logic (for meaning). It does well in narrow, controlled settings.
> * It breaks on ambiguity, negation, words hidden inside other words, and context.
> * ELIZA shows that matching text can look like understanding. Modern NLP mostly learns from data (Chapter 3), often together with symbolic parts.

---

## Hands-On Activity: A Rule-Based Smart Classroom

In Chapter 1 you predicted how a program that matches exact text would treat different wording. Now you build that program and test your predictions. Finding where the rules break is the main lesson, because it shows what Symbolic AI cannot do alone.

The lecturer's hands-on slide shows a block program for a virtual classroom with a **fan** and a **lamp**. The program *asks* for a command, then uses IF–THEN blocks to react.

### Activity A: Exact-Match Rules, Then "Contains" Rules

**Goal.** Build a rule-based program, test it with the sentences from your Chapter 1 prediction table, and find out where rules fail and what each fix costs.

**Preparation.**

* Your completed prediction table from Chapter 1, Activity B.
* Tool version: the lecture's block tool with a fan and a lamp. Paper version: pen and paper, and the test table below. If the tool is unavailable, use the paper version. It gives the same result.

**Task.**

*Part 1: exact-match rules (the same four rules as in Chapter 1)*

```
ASK "Enter your command"
IF answer = "Fan on"    THEN broadcast  fan-on
IF answer = "Fan off"   THEN broadcast  fan-off
IF answer = "Lamp on"   THEN broadcast  lamp-on
IF answer = "Lamp off"  THEN broadcast  lamp-off
```

Test each sentence and write what happens in the last column. In the tool, type it in. On paper, apply the rules by hand.

| # | Typed sentence | Your Chapter 1 prediction | What happens |
|--:|---|---|---|
| 1 | Fan on | | |
| 2 | fan on | | |
| 3 | Fan on please | | |
| 4 | Please turn the fan on | | |
| 5 | Turn the fan on | | |
| 6 | Lamp off | | |
| 7 | Switch the lamp off | | |

*Part 2: fix it with "contains" rules*

Add these four rules and test again.

```
IF answer CONTAINS "fan"  AND answer CONTAINS "on"   THEN broadcast  fan-on
IF answer CONTAINS "fan"  AND answer CONTAINS "off"  THEN broadcast  fan-off
IF answer CONTAINS "lamp" AND answer CONTAINS "on"   THEN broadcast  lamp-on
IF answer CONTAINS "lamp" AND answer CONTAINS "off"  THEN broadcast  lamp-off
```

Test: "Turn the fan on", "Switch the lamp off", "Turn the fan off soon", and "Don't turn the fan on".

**Observation.**

* How many of the 7 sentences in Part 1 did the program handle correctly? How many of your predictions were right?
* In Part 2, which of the four test sentences are handled correctly, and which are not?

**Reflection.**

1. How many exact-match rules would you need to cover ten different ways of saying "turn on the fan"?
2. In Part 2, what went wrong with "Turn the fan off soon"? (Hint: look at the letters of the word "soon".)
3. Is the program **explainable**? Is it **flexible** with new wording?

**Feedback.**

<details>
<summary>Check your answers</summary>

**Part 1** (strict, case-sensitive comparison)

| # | What happens |
|--:|---|
| 1 | The fan turns on. |
| 2 | Depends on the tool. A strict comparison treats "fan" and "Fan" as different, so nothing happens. Some tools ignore capital letters. Record what your tool does. |
| 3 | Nothing happens (the text is not exactly "Fan on"). |
| 4 | Nothing happens. |
| 5 | Nothing happens. |
| 6 | The lamp turns off. |
| 7 | Nothing happens. |

Only sentences 1 and 6 are certain to work. Compare with your predictions from Chapter 1.

**Part 2**

| Sentence | Result |
|---|---|
| Turn the fan on | The fan turns on (fan-on rule). Correct. |
| Switch the lamp off | The lamp turns off (lamp-off rule). Correct. |
| Turn the fan off soon | The word "soon" contains the letters "on", so the fan-on rule **and** the fan-off rule both fire. The program receives two opposite commands. This is a **rule conflict**. |
| Don't turn the fan on | The fan turns on. The rules do not understand "don't". |

1. About ten, one for each wording, unless you use "contains" rules. The "contains" rules reduce the count but create new mistakes.
2. A "contains" test matches letters inside other words. A fix is to match whole words, and to give "off" a higher priority than "on". Each fix adds more rules.
3. **Explainable: yes.** Every action comes from a visible rule, and you can say which one fired. **Flexible: no.** A person must write each new rule and also check how it interacts with the old ones.

</details>

### Activity B: Repair the Rules, Then Break Them Again

**Goal.** See that each repair to a rule-based program removes one failure and leaves others.

**Preparation.** Your results for Part 2 ("contains" rules) of Activity A.

**Task.**

1. In Part 2, the sentence "Turn the fan off soon" fired two opposite rules. Change the rules so that a word counts only when it appears as a **whole word**. Test the sentence again.
2. Test "Don't turn the fan on" with the whole-word rules. What happens?
3. Add a rule to handle "don't". Write one sentence that this new rule would handle wrongly.

**Observation.** Record what each repair fixed and what it left broken.

**Reflection.** (1) Why does every fix leave some failure behind? (2) What does this say about the cost of maintaining a large rule base?

**Feedback.**

<details>
<summary>Check your answers</summary>

1. With whole-word matching, "soon" no longer contains "on", so only the fan-off rule fires. The conflict is repaired.
2. The fan still turns **on**: the rules ignore the word "don't".
3. One possible rule: "if the sentence contains *don't*, do nothing." It fails on "Don't worry, turn the fan on", which should turn the fan on. Your own example may differ; any sentence where "don't" does not negate the command works.

*Reflection:* (1) Language has many more cases than any one rule covers, so each rule handles some cases and breaks others. (2) Every new rule must be checked against all the old ones, which is why large rule bases are expensive to maintain.

In Chapter 3 you will see the **machine-learning version** of the same classroom. It recognises new wording because it has learned from example sentences.

</details>

> [!IMPORTANT]
> **In short**
>
> * Exact-match rules work only for the exact wording. "Contains" rules cover more wording but can fire by accident and can conflict.
> * Every repair removes one failure and creates another, so a large rule base becomes expensive to maintain.
> * The program is **explainable** (you can name the rule that fired) but not **flexible** (a person must write each new case).

---

## Common Misconceptions

> [!WARNING]
> Read the left column, decide whether it is true, and then check the right column.

| Misconception | What is true | Where to check |
|---|---|---|
| "Symbolic AI is obsolete." | Rule engines, planners, and game search are still used, and many modern systems mix symbolic and learning parts. | Topic 1 |
| "A rule that passes my tests works for every input." | It works for the inputs that the author thought of. New wording can fall outside every rule. | Hands-on activity |
| "If p → q and q is true, then p is true." | That is affirming the consequent. The conclusion can have another cause. | Topic 2 |
| "'All birds can fly' is a good rule." | Real knowledge has exceptions, such as penguins. | Topic 3 |
| "A\* always finds the best path." | It finds a cheapest path when the heuristic never overestimates the real remaining cost. | Topic 5 |
| "An expert system understands the subject." | It applies the rules that people wrote. It knows nothing beyond them. | Topic 4 |

---

## Key Takeaways

> [!IMPORTANT]
> **If you remember only eight things**
>
> * **Symbolic AI** works with symbols, explicit rules, and logic that people write.
> * Its great strength is **explanation**. Its great weakness is **brittleness**: it fails where no rule applies.
> * **Logic** makes reasoning exact. An implication is false only when the condition is true and the conclusion false. Modus ponens and modus tollens are valid; affirming the consequent is not.
> * **Knowledge representation** decides what a machine can conclude. Logic, semantic networks, frames, rules, and ontologies each suit a different job.
> * **Rule-based and expert systems** chain rules by forward chaining. The knowledge acquisition bottleneck is their main weakness.
> * **Planning** is search through a state space. A\* is optimal when its heuristic never overestimates; alpha-beta pruning saves work without changing the answer.
> * **Combinatorial explosion** limits search, even for simple games.
> * **Symbolic NLP** gives structure and meaning but breaks on ambiguity and negation. That opens the door to learning from data, which is Chapter 3.

---

## Practice Questions

### Part A: Multiple Choice

**Q1.** Which description fits Symbolic AI best?  
A. Learning weights from millions of images  
B. Reasoning with explicit rules and logic  
C. Learning from rewards by trial and error  
D. Grouping data without any rules

**Q2.** For p = true and q = false, what is p → q?  
A. true  
B. false  
C. unknown  
D. both

**Q3.** "If it rains, the ground is wet. The ground is not wet." Which conclusion is valid?  
A. It is raining.  
B. It is not raining.  
C. The ground is dry because of the sun.  
D. No conclusion is possible.

**Q4.** Which statement is written correctly in predicate logic: "Every cat is a mammal"?  
A. ∃x (Cat(x) ∧ Mammal(x))  
B. ∀x (Cat(x) → Mammal(x))  
C. ∀x (Cat(x) ∧ Mammal(x))  
D. ¬Cat(x)

**Q5.** Which is *not* part of an expert system?  
A. Knowledge base  
B. Inference engine  
C. User interface  
D. Neural network weights

**Q6.** In BFS on the tree in Figure 2.9, which node is visited right after A?  
A. D  
B. B  
C. C  
D. E

**Q7.** In alpha-beta pruning, what is the main benefit?  
A. It changes the answer of minimax.  
B. It gives the same answer while examining fewer nodes.  
C. It removes the need for a heuristic.  
D. It makes the opponent play worse.

**Q8.** Which problem is a typical limit of Symbolic AI?  
A. It cannot be explained.  
B. It copes poorly with uncertain or ambiguous information.  
C. It cannot use logic.  
D. It cannot be edited.

### Part B: Short Answer

**Q9.** Write "Some students are not tired" in predicate logic, using Student(x) and Tired(x).

**Q10.** Explain why "From p → q and q, conclude p" is invalid. Give an example.

**Q11.** Explain the difference between a frame and a script, with one example of each.

**Q12.** Show one step of forward chaining on these rules. R1: if it is raining, then the ground is wet. R2: if the ground is wet, then the road is slippery. The fact: it is raining.

### Part C: Apply It

**Q13.** Give one example where a rule-based sentiment analyser fails, and say why.

**Q14.** "All birds can fly. Penguins are birds. So penguins can fly." Which statement is wrong, and what does this show about knowledge written as rules?

### Part D: Trace It

**Q15.** Rules: R1: if A and B then C. R2: if C then D. R3: if D and E then F. The known facts are A, B, and E. Use forward chaining. Which facts are known at the end?

**Q16.** On the tree in Figure 2.9 the goal is node E. In which order does BFS visit the nodes, and in which order does DFS? Which one visits fewer nodes?

**Q17.** Use the ELIZA-style rules of Topic 6. What does the chatbot answer to "My father and I feel tired"? Why does R1 not fire?

---

## Answer Key

| Q | Answer | Explanation |
|---|---|---|
| Q1 | B | Symbolic AI reasons with explicit rules and logic. |
| Q2 | B | An implication is false only when the premise is true and the conclusion is false. |
| Q3 | B | Modus tollens: from p → q and ¬q, conclude ¬p. |
| Q4 | B | "For all x, if x is a cat then x is a mammal." Option C would say everything is a cat and a mammal. |
| Q5 | D | Neural network weights belong to Connectionist AI (Chapter 3). |
| Q6 | B | BFS visits all neighbours of S (A, B) before going deeper, so B comes right after A. |
| Q7 | B | Pruning skips branches that cannot affect the final choice. |
| Q8 | B | Rules need precise statements; uncertainty is hard. |
| Q9 | ∃x (Student(x) ∧ ¬Tired(x)) | "Some" means ∃. Use ∧ with ∃. |
| Q10 | Sample | The conclusion may come from another cause. "If it rains, the ground is wet. The ground is wet." The ground might be wet because of a sprinkler, so we cannot conclude it rained. |
| Q11 | Sample | A frame describes one typical object with slots (a car: make, model, year, colour). A script is a sequence of frames for a typical event (a restaurant visit: reservation, ordering, paying). |
| Q12 | Sample | R1 fires because it is raining, so we add "the ground is wet". Next, R2 can fire because the ground is wet, so we add "the road is slippery". |
| Q13 | Sample | "The film was not good" contains the positive word *good*, so a word-list rule marks it positive, although the sentence is negative. The rule cannot see negation. |
| Q14 | Sample | The first statement is wrong, because penguins cannot fly. It shows that rules need **exceptions**, and that incomplete knowledge leads to wrong conclusions. |
| Q15 | A, B, E, C, D, F | R1 fires (A and B), adding C. R2 fires (C), adding D. R3 fires (D and E), adding F. No rule is left. |
| Q16 | Sample | BFS: S, A, B, C, D, E. DFS: S, A, C, D, B, E. Both visit 6 nodes for this goal, so neither is faster here. |
| Q17 | Sample | R2 fires, so the answer is "Tell me more about your family." R1 needs the text to *start with* "I feel ", but this text starts with "My father". |

---

## What Comes Next: From Written Rules to Learned Weights

**What you have now.** You saw what a machine can do when people write the knowledge: it can reason exactly with logic, chain rules to reach new conclusions, explain every step, and search for a plan. You also saw the limits: incomplete knowledge, rule conflicts, new wording, the effort of writing rules, and an explosion of possibilities.

**What is still missing.** Everything above depended on people writing the knowledge. Nobody can write rules for recognising a face, understanding any sentence, or spotting a tumour in a scan. People cannot put such knowledge into words, even though they can do the tasks.

**Chapter 3 starts there.** It asks: *what if the program could find the rules itself, from examples?* That is **Connectionist AI**. You will replace IF–THEN rules with **neurons and weights**, see how a network learns from data, and learn why very large amounts of data (Big Data) changed what is possible. **Keep your test table from the hands-on activity.** In Chapter 3 you will build the machine-learning version of the same Smart Classroom and compare how many rules you needed here with how many examples you need there.

---

## Key Terms in Chinese

*Check these against your course textbook or a Chinese-speaking teammate; wording varies between books.*

| English | 中文 |
|---|---|
| Symbolic AI | 符号主义（符号人工智能） |
| logic | 逻辑 |
| propositional logic | 命题逻辑 |
| predicate logic | 谓词逻辑 |
| knowledge representation | 知识表示 |
| semantic network | 语义网络 |
| ontology | 本体 |
| rule-based system | 基于规则的系统 |
| expert system | 专家系统 |
| inference engine | 推理机 |
| forward chaining | 正向推理（前向链接） |
| backward chaining | 反向推理（后向链接） |
| search | 搜索 |
| breadth-first search (BFS) | 广度优先搜索 |
| depth-first search (DFS) | 深度优先搜索 |
| heuristic | 启发式 |
| minimax | 极小极大算法 |
| alpha-beta pruning | α-β 剪枝 |
| natural language processing | 自然语言处理 |

## Glossary

| Term | Meaning |
|---|---|
| **A\* search** | An informed search that uses cost so far plus an estimate of the remaining cost. |
| **Admissible heuristic** | An estimate of the remaining cost that never exceeds the true cost. |
| **Alpha-beta pruning** | A way to speed up minimax by skipping branches that cannot change the result. |
| **Backward chaining** | Reasoning that starts from a goal and looks for rules and facts that prove it. |
| **Breadth-first search** | Search that explores all nodes at one depth before the next. |
| **Conflict resolution** | A strategy for choosing which rule to use when two rules give different advice, such as priority, specificity, or recency. |
| **Contrapositive** | The statement “if not q then not p”, which is equivalent to “if p then q”. |
| **Converse** | The statement “if q then p”, which is **not** equivalent to “if p then q”. |
| **Default knowledge** | A fact assumed true unless an exception is known, such as "birds can fly". |
| **Depth-first search** | Search that follows one branch as deep as possible before backtracking. |
| **Equivalent statements** | Statements that have the same truth value in every row of the truth table. |
| **Exception** | A case in which a general rule does not hold, such as a penguin among birds. |
| **Expert system** | A system that copies the decision-making of a human expert in a narrow domain. |
| **Forward chaining** | Reasoning from known facts, applying rules until no new fact appears. |
| **Frame** | A data structure with slots describing a typical object or situation. |
| **Game tree** | A tree of the positions that can occur in a game, with a branch for each legal move. |
| **Goal state** | The state a search is trying to reach. |
| **GOFAI** | Good Old-Fashioned AI, another name for Symbolic AI. |
| **Heuristic** | A rule of thumb that estimates how good a state or choice is. |
| **Inference engine** | The part of a system that applies rules to knowledge to reach conclusions. |
| **Inheritance** | In a semantic network, passing a property from a general concept to a more specific one. |
| **Knowledge base** | The facts and rules that a symbolic system reasons with. |
| **Modus ponens / tollens** | Valid inference rules: from p → q and p conclude q; from p → q and ¬q conclude ¬p. |
| **Ontology** | A formal description of the concepts in a domain and how they relate. |
| **Pattern matching** | Comparing text with a template to decide which rule applies. |
| **Predicate** | A statement with variables that is true or false depending on their values. |
| **Proposition** | A sentence that is either true or false. |
| **Quantifier** | ∀ ("for all") or ∃ ("there exists"). |
| **Rule-based system** | A system whose knowledge is a set of IF–THEN rules that an inference engine applies. |
| **Script** | A sequence of frames describing a typical event. |
| **Semantic network** | A graph of concepts (nodes) and relationships (links). |
| **State** | A complete description of the situation at one moment, for example in a search problem (Chapter 2) or a reinforcement learning problem (Chapter 4). |
| **State space** | The set of all states a system can be in. |

---

## References

1. Course slides, "chap4: Symbolic AI". Lecturer's course materials (no public link). Primary source for the structure, examples, and hands-on activity.
2. Russell, S., and Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson. [https://aima.cs.berkeley.edu/](https://aima.cs.berkeley.edu/) *(not opened; logic, knowledge representation, search)*
3. Haugeland, J. (1985). *Artificial Intelligence: The Very Idea*. MIT Press. Overview of the term GOFAI: [https://en.wikipedia.org/wiki/GOFAI](https://en.wikipedia.org/wiki/GOFAI) *(the link is a secondary overview and was not opened; the book itself was not opened)*
4. Shortliffe, E. H. (1976). *Computer-Based Medical Consultations: MYCIN*. Elsevier. Overview: [https://en.wikipedia.org/wiki/Mycin](https://en.wikipedia.org/wiki/Mycin) *(the link is a secondary overview and was not opened; the book itself was not opened)*
5. Weizenbaum, J. (1966). ELIZA: a computer program for the study of natural language communication between man and machine. *Communications of the ACM*, 9(1), 36–45. [https://doi.org/10.1145/365153.365168](https://doi.org/10.1145/365153.365168) *(not opened; basis of the ELIZA example in Topic 6)*
6. Wolf, goat and cabbage problem. [https://en.wikipedia.org/wiki/Wolf,_goat_and_cabbage_problem](https://en.wikipedia.org/wiki/Wolf,_goat_and_cabbage_problem) *(secondary overview of the puzzle in Topic 5; not opened; the 7-move solutions were checked by a short breadth-first search script on 5 November 2026)*
7. Stanford Encyclopedia of Philosophy. *Classical Logic.* [https://plato.stanford.edu/entries/logic-classical/](https://plato.stanford.edu/entries/logic-classical/) *(optional reading on propositional and predicate logic; not opened)*
8. Wikipedia. "A* search algorithm." [https://en.wikipedia.org/wiki/A*_search_algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm) *(admissible heuristic and optimality; read with a fetch tool on 5 November 2026)*
9. Wikipedia. "ELIZA." [https://en.wikipedia.org/wiki/ELIZA](https://en.wikipedia.org/wiki/ELIZA) *(creator, year, DOCTOR script, 1966 Communications of the ACM article; read with a fetch tool on 5 November 2026)*
10. Wikipedia. "Game complexity." [https://en.wikipedia.org/wiki/Game_complexity](https://en.wikipedia.org/wiki/Game_complexity) *(tic-tac-toe: 5,478 legal positions and 255,168 possible games; read with a fetch tool on 5 November 2026. We also recomputed these numbers with a program)*
11. ChessWorld. "What Is the Shannon Number in Chess?" [https://www.chessworld.net/what-is-the-shannon-number-in-chess.asp](https://www.chessworld.net/what-is-the-shannon-number-in-chess.asp) *(about 10^120, a rough estimate; read with a fetch tool on 5 November 2026)*

> **Link status.** Links marked **not opened** could not be opened while this chapter was written. The author or reviewer must click every link, confirm that it opens the right work and supports the claim it is cited for, and then change the label to "opened" with the date.

---

| [← Chapter 1: Introduction to CS and AI](chapter-1-introduction-to-cs-and-ai/introduction-to-cs-and-ai.md) | [Module overview](../../README.md) | [Chapter 3: Connectionist AI and Big Data →](chapter-3-connectionist-ai-and-big-data/connectionist-ai-and-big-data.md) |
|:--|:-:|--:|

---

![Chapter 3 banner: Connectionist AI and Big Data](chapter-3-connectionist-ai-and-big-data/assets/fig-3-0-banner.png)

# Chapter 3: Connectionist AI and Big Data

> **Module:** AI Overview  
> **Chapter:** 3 of 4 (course Chapter 5)  
> **Version:** 2.0 (Stage 2; developed from the Stage 1 chapter, version 1.1)  
> **Author:** Benedict Subhata (proposed owner)  
> **Reviewer:** Brian Djoni Suzanna (review pending; no signed review exists for this version)  
> **Audience:** Complete beginners with basic computer and internet literacy; no programming needed  
> **Study time:** about 6 hours, including the hands-on activity  
> **Course source:** Lecturer's slides "chap5: Connectionist AI and Big Data Overview". The slides have two groups of topics, and this chapter follows both in the same order: **Part A** (Connectionist AI: introduction, neural-network basics, architectures, deep learning, applications, ethics) and **Part B** (Big Data: introduction, technologies, processing and analytics, visualization, use cases, ethics and privacy).

| [← Chapter 2: Symbolic AI](chapter-2-symbolic-ai/symbolic-ai.md) | [Module overview](../../README.md) | [Chapter 4: Behaviorist AI →](chapter-4-behaviorist-ai/behaviorist-ai.md) |
|:--|:-:|--:|


<details>
<summary><b>Contents</b></summary>

1. [Where This Chapter Fits](#where-this-chapter-fits-2)
2. [What You Will Learn](#what-you-will-learn-2)
3. [Part A, Topic 1: Introduction to Connectionist AI](#part-a-topic-1-introduction-to-connectionist-ai)
4. [Part A, Topic 2: Basics of Neural Networks](#part-a-topic-2-basics-of-neural-networks)
5. [Part A, Topic 3: Architectures of Neural Networks](#part-a-topic-3-architectures-of-neural-networks)
6. [Part A, Topic 4: Deep Learning and Advanced Concepts](#part-a-topic-4-deep-learning-and-advanced-concepts)
7. [Part A, Topic 5: Key Applications of Connectionist AI](#part-a-topic-5-key-applications-of-connectionist-ai)
8. [Part A, Topic 6: Ethical Considerations and Challenges](#part-a-topic-6-ethical-considerations-and-challenges)
9. [Part B, Topic 1: Introduction to Big Data](#part-b-topic-1-introduction-to-big-data)
10. [Part B, Topic 2: Big Data Technologies](#part-b-topic-2-big-data-technologies)
11. [Part B, Topic 3: Data Processing and Analytics](#part-b-topic-3-data-processing-and-analytics)
12. [Part B, Topic 4: Data Analysis and Visualization](#part-b-topic-4-data-analysis-and-visualization)
13. [Part B, Topic 5: Big Data Use Cases](#part-b-topic-5-big-data-use-cases)
14. [Part B, Topic 6: Big Data Ethics and Privacy](#part-b-topic-6-big-data-ethics-and-privacy)
15. [Hands-On Activity: A Learner You Train and Then Break](#hands-on-activity-a-learner-you-train-and-then-break)
16. [Common Misconceptions](#common-misconceptions-2)
17. [Key Takeaways](#key-takeaways-2)
18. [Practice Questions](#practice-questions-2)
19. [Answer Key](#answer-key-2)
20. [What Comes Next: From Labelled Examples to Rewards](#what-comes-next-from-labelled-examples-to-rewards)
21. [Key Terms in Chinese](#key-terms-in-chinese-2)
22. [Glossary](#glossary-2)
23. [References](#references-2)

</details>

---

## Where This Chapter Fits

Chapter 2 ended with a problem. In Symbolic AI a person has to write the knowledge as rules. That works for a library card or a medical checklist, but nobody can write rules that recognise a face, understand any spoken sentence, or spot a tumour in a scan. People can do those tasks, yet they cannot put *how* they do them into words.

![Four cards, one per chapter, with Chapter 3 highlighted](chapter-3-connectionist-ai-and-big-data/assets/fig-3-1-how-the-chapters-connect.png)

*Figure 3.1: How the four chapters build on each other. You are in Chapter 3.*

**How to read this figure.** Find the highlighted card, Chapter 3. Its **core idea** is that the machine learns the rules itself, and stores them as numbers in a neural network. Its **strength** is that it can handle images, speech, and language, if there is enough data. Its **weak point**, in the red part, leads to Chapter 4: it needs many *labelled* examples, and sometimes nobody can say what the right answer for each example is.

| | Before this chapter | In this chapter | In the next chapter |
|---|---|---|---|
| **What you know** | Symbolic AI: a machine reasons exactly with rules and logic that people write, and it can explain every step. | A machine **learns the rules from examples**. The knowledge sits in numbers called weights, inside a neural network. You also see where the examples come from: **Big Data**. | A machine that learns **by trying actions and receiving rewards**, with no example of the right answer. |
| **Main question** | What can a machine do when we write the knowledge for it, and where does that stop working? | What if the knowledge is too big or too hard to write, but we have lots of examples? | What if there are no examples of the right answer, only consequences? |

This chapter has two parts because the two ideas belong together.

![Part B (Big Data) prepares a good data set that Part A (neural networks) learns from](chapter-3-connectionist-ai-and-big-data/assets/fig-3-2-parts-connect.png)

*Figure 3.2: The two parts of this chapter. Part B prepares the data. Part A learns from it.*

**How to read this figure.** Start at the top left. Data is **collected**, **stored**, **cleaned**, and **processed** (Part B). The result is a good data set: many examples, labelled and varied. That data set flows down into the neural network (Part A), which learns from it and becomes a trained model that makes predictions. Part A is the learner. Part B is where the learner's food comes from, and it also covers what must be handled with care, such as privacy.

## What You Will Learn

After this chapter you should be able to:

1. **Explain** what Connectionist AI is and how it differs from Symbolic AI. (Part A, Topic 1)
2. **Calculate** the output of a single neuron, and **describe** how a network learns by gradient descent. (Part A, Topic 2)
3. **Match** four neural-network architectures to the data they suit. (Part A, Topic 3)
4. **Explain** what makes learning "deep", why it took off around 2012, and what overfitting is. (Part A, Topic 4)
5. **Name** key applications and the ethical problems they raise, including bias. (Part A, Topics 5 and 6)
6. **Describe** Big Data with its five Vs, and the technologies, pipeline, and levels of analysis used with it. (Part B, Topics 1 to 3)
7. **Choose** an honest chart, **list** real use cases, and **explain** why removing names does not make data anonymous. (Part B, Topics 4 to 6)
8. **Train** a very small learner on paper and compare it with the rule-based program of Chapter 2. (Hands-on activity)

---

## Part A, Topic 1: Introduction to Connectionist AI

This topic answers three questions: **what** Connectionist AI is, **where** the idea came from, and **how** it differs from the Symbolic AI of Chapter 2.

### What Connectionist AI is

**Connectionist AI** builds intelligence from a large number of very simple units, called **artificial neurons**, that are connected to each other. Each connection has a number on it, called a **weight**. A group of connected neurons is a **neural network**.

There is no IF–THEN rule anywhere in the system. Instead, **the knowledge is stored in the weights**. When the weights are good, the network gives good answers. When they are bad, it gives bad answers. And nobody types the weights in. The network **learns** them by looking at many examples.

Here is the difference in one picture. Suppose you want a system that decides whether a photo shows a cat.

* **Symbolic way.** You write rules: "IF it has pointed ears AND whiskers AND fur THEN cat." You immediately meet a problem: how does a computer find "pointed ears" in a grid of coloured dots? You cannot write that rule.
* **Connectionist way.** You collect 100,000 photos, each labelled "cat" or "not cat". You let a neural network look at them one by one. Each time it guesses wrong, its weights are adjusted a little. After many rounds, it recognises cats, and nobody ever wrote a rule about ears.

The name comes from the idea that intelligence is in the **connections**. It is inspired, loosely, by the brain, which is made of billions of simple cells (neurons) joined by connections that get stronger or weaker with experience. An artificial neuron is **far simpler** than a real one. The brain is only the inspiration, not a blueprint.

### A short history

![A timeline with four dates: 1943, 1958, 1986, and 2012](chapter-3-connectionist-ai-and-big-data/assets/fig-3-3-timeline.png)

*Figure 3.3: Four dates in the history of the connectionist idea.*

**How to read this figure.** Follow the line from left to right. In **1943**, Warren McCulloch and Walter Pitts described a simple mathematical model of a neuron. In **1958**, Frank Rosenblatt built the **perceptron**, a neuron that can *learn* its weights from examples. In **1986**, David Rumelhart, Geoffrey Hinton, and Ronald Williams popularised **backpropagation**, a method that can train networks with hidden layers (you will see how in Topic 2). In **2012**, a deep network called AlexNet won an image-recognition contest by a wide margin.

Notice the long gap between the ideas (1943 to 1986) and the breakthrough (2012). The ideas were there early. What was missing were **large labelled data sets** and **fast hardware**. This is why Big Data (Part B) belongs in the same chapter: without the data, the method does not work.

### Symbolic AI and Connectionist AI side by side

| | Symbolic AI (Chapter 2) | Connectionist AI (this chapter) |
|---|---|---|
| **Where does the knowledge come from?** | People write it. | The machine learns it from examples. |
| **How is it stored?** | As rules, logic, and networks of symbols that people can read. | As numbers (weights) that look meaningless one by one. |
| **Explanation** | Easy. You can point at the rule that fired. | Hard. The answer comes from millions of numbers working together. |
| **Strong at** | Exact reasoning, planning, clearly defined tasks. | Messy data: images, sound, text. |
| **Weak at** | Anything nobody can write rules for. | Needs a lot of data. Can be wrong without a visible reason. |
| **Example** | A rule: "IF fever AND cough AND difficulty breathing THEN may have pneumonia". | A network that reads a chest X-ray and marks a suspicious area. |

Neither approach is "the winner". The two are **complementary**. A self-driving system, for example, uses a neural network to see (is that a pedestrian?), and then an explicit rule to act (if a pedestrian is within 10 metres, brake). The second half of Part A shows more of this.

### Check yourself

<details>
<summary>Question 1. Where is the knowledge stored in a neural network, and who puts it there?</summary>

The knowledge is stored in the **weights** of the connections between neurons. Nobody types the weights in. They are set by **training**: the network sees many examples and its weights are adjusted whenever it makes a mistake.

</details>

<details>
<summary>Question 2. A bank must tell a customer exactly why a loan was refused. Which approach is easier to use, and why?</summary>

**Symbolic AI** is easier, because the decision comes from rules that can be read out ("refused because income is below the limit"). A neural network may be more accurate on messy data, but it cannot easily say *why*, which is a problem when someone has the right to an explanation.

</details>

> [!IMPORTANT]
> **In short**
>
> * Connectionist AI uses many simple, connected neurons. The knowledge is in the **weights**, and the network **learns** them from examples.
> * The ideas are old (1943 to 1986). They took off in 2012 when large data sets and fast hardware arrived.
> * Symbolic AI is explainable but needs written rules. Connectionist AI handles messy data but is hard to explain. Real systems often combine both.

---

## Part A, Topic 2: Basics of Neural Networks

A neural network can look mysterious, but it is built from one very small piece repeated many times. This topic builds it up in order: **one neuron**, then **layers**, then the question of **how the weights are learned**.

### The artificial neuron

An artificial neuron does four things:

1. It receives some numbers, its **inputs** (written x1, x2, and so on).
2. It multiplies each input by its own **weight** (w1, w2, and so on). The weight says **how much that input matters**. A large positive weight means "this input pushes me to fire". A negative weight means "this input holds me back".
3. It adds all the results together with one extra number, the **bias** (b). The bias sets **how easily the neuron fires**, even when all inputs are zero.
4. It passes the total, called **z**, through an **activation function** that decides the final output.

![One neuron with two inputs, two weights, a bias, and an activation function](chapter-3-connectionist-ai-and-big-data/assets/fig-3-4-neuron-anatomy.png)

*Figure 3.4: One artificial neuron with real numbers.*

**How to read this figure.** Read from left to right. Two inputs enter on the left: x1 has the value 1 and x2 has the value 0.5. Each travels along an arrow that carries a weight: 0.4 for x1 and −0.2 for x2. In the circle, the neuron adds the weighted inputs and the bias of 0.1, giving **z = 0.4**. The yellow box applies the activation function, and the green box is the final output. The calculation at the bottom of the figure is the same thing written out:

**z = w1 × x1 + w2 × x2 + b = 0.4 × 1 + (−0.2) × 0.5 + 0.1 = 0.4 − 0.1 + 0.1 = 0.4**

That is all a neuron does. Everything else in this chapter is made of this piece.

### Activation functions

If a neuron only added numbers, a stack of neurons would be no more powerful than one neuron. The activation function makes the difference: it adds a **bend** to the calculation, so that layers can build on each other.

![Three small graphs: a step, a smooth S-curve, and a bent line](chapter-3-connectionist-ai-and-big-data/assets/fig-3-5-activations.png)

*Figure 3.5: Three common activation functions. Each graph shows the output (up) for each value of z (across).*

**How to read this figure.** In each graph, the horizontal axis is z, the number coming out of the neuron's addition, and the vertical line is the output. The **step** function gives 0 for any negative z and 1 for any positive z, a hard yes or no. The **sigmoid** function is a smooth S-curve that gives values between 0 and 1, which is handy for probabilities. **ReLU** (rectified linear unit) gives 0 for negative z and z itself for positive z, and it is the most common choice in the hidden layers of modern networks.

For our neuron, z = 0.4. With **ReLU** the output is **0.4**. With **sigmoid** the output is about **0.60**. With the **step** function it would be 1, because 0.4 is above zero.

### A neuron that decides: the AND neuron

A single neuron can already make a simple decision. Take two inputs that are each 0 or 1, the weights w1 = 1 and w2 = 1, the bias b = −1.5, and the step function (output 1 if z > 0).

| x1 | x2 | z = x1 + x2 − 1.5 | Output |
|:-:|:-:|--:|:-:|
| 0 | 0 | −1.5 | 0 |
| 0 | 1 | −0.5 | 0 |
| 1 | 0 | −0.5 | 0 |
| 1 | 1 | 0.5 | 1 |

The neuron fires only when **both** inputs are 1. It computes **AND**. Here, a person chose the weights by hand. The whole point of a neural network is that **training finds good weights automatically**.

### Layers

One neuron is limited, so we connect many. Neurons are arranged in **layers**:

* The **input layer** receives the data. It does no calculation. For a small picture, there is one input per pixel.
* One or more **hidden layers** do the calculation. They are "hidden" because we do not see their values from outside.
* The **output layer** gives the answer. For reading digits, there is one output neuron per digit, and the neuron with the highest value is the answer.

![A network with an input layer, two hidden layers, and an output layer, with every neuron joined to every neuron in the next layer](chapter-3-connectionist-ai-and-big-data/assets/fig-3-6-layers.png)

*Figure 3.6: Layers, from pixels to an answer. Every line is a connection with its own weight.*

**How to read this figure.** Information moves from left to right. The input layer holds the pixels of a handwritten digit. The first hidden layer combines pixels into simple patterns such as short strokes. The second hidden layer combines those patterns into larger ones such as loops and lines. The output layer has one neuron per digit, and the digit with the strongest output is the network's answer. Every line is a **weight**, so even this small drawing has dozens of weights, and real networks have millions. The calculation that moves the data from left to right is called the **forward pass**. A network with *many* hidden layers is called **deep**, which is where "deep learning" gets its name.

### Why one neuron is not enough: the XOR problem

Some problems cannot be solved by a single neuron, however well its weights are chosen. The standard example is **XOR** ("exclusive or"), which is 1 when **exactly one** of the two inputs is 1.

| x1 | x2 | XOR |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

![Left: four points that no straight line can separate. Right: a two-layer network that solves the problem](chapter-3-connectionist-ai-and-big-data/assets/fig-3-7-xor.png)

*Figure 3.7: Why one neuron fails at XOR, and how a hidden layer fixes it.*

**How to read this figure.** On the left, the four possible inputs are drawn as points on a square. Green points should give 1 and red points should give 0. A single neuron can only separate points with **one straight line**. Try to draw one line with the two greens on one side and the two reds on the other: it is impossible, and the two dashed lines show two failed attempts. On the right, a network with a **hidden layer** solves it. Hidden neuron h1 computes OR ("at least one input is 1") and hidden neuron h2 computes AND ("both are 1"). The output neuron says "h1 is on **and** h2 is off", which is exactly XOR.

| x1 | x2 | h1 (OR) | h2 (AND) | Output z = h1 − h2 − 0.5 | Output |
|:-:|:-:|:-:|:-:|--:|:-:|
| 0 | 0 | 0 | 0 | −0.5 | 0 |
| 0 | 1 | 1 | 0 | 0.5 | 1 |
| 1 | 0 | 1 | 0 | 0.5 | 1 |
| 1 | 1 | 1 | 1 | −0.5 | 0 |

<details>
<summary>Why can no single neuron do XOR? (a short proof, optional)</summary>

A step neuron gives 1 when w1 × x1 + w2 × x2 + b > 0. For XOR the four rows demand:

* (0, 0) must give 0, so b ≤ 0.
* (0, 1) must give 1, so w2 + b > 0.
* (1, 0) must give 1, so w1 + b > 0.
* (1, 1) must give 0, so w1 + w2 + b ≤ 0.

From the middle two, w1 > −b and w2 > −b, so w1 + w2 > −2b, and therefore w1 + w2 + b > −b. Because b ≤ 0, −b ≥ 0, so w1 + w2 + b > 0. That contradicts the last condition. No weights satisfy all four.

</details>

The lesson is that **hidden layers let a network build new features** ("at least one", "both") out of the raw inputs, and then combine them. This is why networks have layers.

### How a network learns

So far the weights were chosen by hand. Learning means finding them automatically. The method is a loop of five steps.

![Five boxes in a loop: forward pass, loss, backpropagation, gradient descent, repeat](chapter-3-connectionist-ai-and-big-data/assets/fig-3-8-learning-loop.png)

*Figure 3.8: The learning loop.*

**How to read this figure.** Start at box 1 and follow the arrows. **(1) Forward pass:** give the network one example and let it guess. **(2) Loss:** compare the guess with the true answer and turn the difference into one number that says how wrong it was. For a house price, the loss could be the squared difference between the predicted and the true price. **(3) Backpropagation:** work out how much each weight contributed to the error, from the output layer back toward the input layer. **(4) Gradient descent:** change every weight a small step in the direction that reduces the loss. **(5) Repeat** with the next example. One full pass through all the examples is an **epoch**. The dashed arrow shows that the loop runs over and over, with the weights a little better each time.

A good everyday picture is a student practising with a past exam. Answer a question (forward pass). Check the answer (loss). Ask "what did I misunderstand?" (backpropagation). Study a little to fix it (gradient descent). Do the next question (repeat).

### Gradient descent

The key step is gradient descent. Imagine you are standing on a hillside in thick fog and want to reach the valley. You cannot see the valley, but you can feel the **slope** under your feet. So you take a small step **downhill**, feel the slope again, and repeat.

In a network, the "height" is the **loss**, and the "position" is the set of weights. The **slope** (called the **gradient**) says which way is uphill, so we move the other way. The size of each step is the **learning rate**.

Here is the smallest possible example. There is one weight w, the loss is (w − 3)², so the best weight is 3, and the slope of the loss is 2 × (w − 3). We start at w = 0 with a learning rate of 0.1. Each step is: **new w = old w − learning rate × slope**.

| Step | w before | Slope 2(w − 3) | w after |
|--:|--:|--:|--:|
| 1 | 0 | −6 | 0 − 0.1 × (−6) = 0.6 |
| 2 | 0.6 | −4.8 | 1.08 |
| 3 | 1.08 | −3.84 | 1.464 |
| 4 | 1.464 | −3.072 | 1.7712 |
| 5 | 1.7712 | −2.4576 | 2.01696 |

![Two loss curves. With learning rate 0.1 the points walk down to the minimum. With learning rate 1.1 they jump from side to side and climb](chapter-3-connectionist-ai-and-big-data/assets/fig-3-9-gradient-descent.png)

*Figure 3.9: The same loss with two learning rates.*

**How to read this figure.** Each picture shows the loss curve (the grey bowl) and the weight on the horizontal axis. The best weight is at the bottom, w = 3. **Left:** with a learning rate of 0.1, the weight starts at 0 and walks down the bowl in steady steps that get smaller as the slope flattens. After five steps it is at 2.02, close to 3. **Right:** with a learning rate of 1.1, the first step jumps from 0 to 6.6, which is past the bottom and up the other side. The next step jumps to −1.32, then to 8.18. The weight lands **farther from the best value each time**, and the loss grows: 9, 12.96, 18.6, 26.9.

The lesson: **a learning rate that is too large makes training fail, and one that is too small trains very slowly.** Choosing it well is part of the craft. A real network does this same step for millions of weights at once.

### A neuron that learns by itself

To see "learning from examples" with nothing hidden, let a single neuron teach itself **OR** (the output is 1 when at least one input is 1). Start with w1 = 0, w2 = 0, b = 0. Show the examples in the order (0,0), (0,1), (1,0), (1,1). After each example, use the **perceptron rule**: if the neuron is wrong, change each weight by (target − output) × its input, and change the bias by (target − output). If it is right, change nothing.

| Epoch | Example (x1, x2) | z before | Output | Target | Change | Weights after (w1, w2, b) |
|--:|:-:|--:|:-:|:-:|---|:-:|
| 1 | (0, 0) | 0 | 0 | 0 | none | (0, 0, 0) |
| 1 | (0, 1) | 0 | 0 | 1 | wrong: +1 | **(0, 1, 1)** |
| 1 | (1, 0) | 1 | 1 | 1 | none | (0, 1, 1) |
| 1 | (1, 1) | 2 | 1 | 1 | none | (0, 1, 1) |
| 2 | (0, 0) | 1 | 1 | 0 | wrong: −1 | (0, 1, 0) |
| 2 | (0, 1) | 1 | 1 | 1 | none | (0, 1, 0) |
| 2 | (1, 0) | 0 | 0 | 1 | wrong: +1 | **(1, 1, 1)** |
| 2 | (1, 1) | 3 | 1 | 1 | none | (1, 1, 1) |
| 3 | (0, 0) | 1 | 1 | 0 | wrong: −1 | **(1, 1, 0)** |
| 3 | (0, 1) | 1 | 1 | 1 | none | (1, 1, 0) |
| 3 | (1, 0) | 1 | 1 | 1 | none | (1, 1, 0) |
| 3 | (1, 1) | 2 | 1 | 1 | none | (1, 1, 0) |

In epoch 4 there are no mistakes, so training **stops**. The neuron now computes z = x1 + x2, and it fires when z > 0, which is exactly OR. Nobody typed those weights: **the examples shaped them**. (This rule works only when a straight line *can* solve the problem. On XOR it never settles.)

<details>
<summary>Optional: backpropagation with real numbers on the smallest network</summary>

"Backpropagation" sounds mysterious, so here it is on the smallest possible network, with every number visible. One input x = 1. One hidden neuron: h = sigmoid(w1 × x). One output neuron: ŷ = sigmoid(w2 × h). The target is y = 1, the loss is L = (ŷ − y)², and the starting weights are w1 = 0.6 and w2 = 0.4. The sigmoid is σ(z) = 1 / (1 + e^(−z)), and its slope is σ(z) × (1 − σ(z)).

| Direction | Calculation | Value |
|---|---|--:|
| Forward | h = σ(0.6 × 1) | 0.6457 |
| Forward | ŷ = σ(0.4 × 0.6457) | 0.5642 |
| Forward | L = (0.5642 − 1)² | 0.1899 |
| Backward | dL/dŷ = 2(ŷ − 1) | −0.8716 |
| Backward | slope of the output sigmoid = ŷ(1 − ŷ) | 0.2459 |
| Backward | **dL/dw2** = −0.8716 × 0.2459 × h (0.6457) | **−0.1384** |
| Backward | slope of the hidden sigmoid = h(1 − h) | 0.2288 |
| Backward | **dL/dw1** = −0.8716 × 0.2459 × w2 (0.4) × 0.2288 × x (1) | **−0.01961** |

With a learning rate of 1.0, w2 becomes 0.4 − (−0.1384) = **0.5384** and w1 becomes 0.6 − (−0.01961) = **0.6196**. Running the forward pass again gives a loss of **0.1709**, down from 0.1899. One step, and the network is a little less wrong.

The backward calculation is simply the **chain rule**: multiply the slopes of each step from the output back to the weight. Notice that dL/dw1 is much smaller than dL/dw2. A sigmoid's slope is at most 0.25, so every sigmoid layer the signal passes on the way back shrinks it. In a network with many sigmoid layers, the early layers learn very slowly. This is the **vanishing gradient** problem, and it is one reason ReLU is popular.

</details>

### Check yourself

<details>
<summary>Question 1. A neuron has x1 = 2, x2 = 1, weights w1 = 0.5 and w2 = −1, and bias b = 0.5. What are z, the ReLU output, and the step output?</summary>

z = 0.5 × 2 + (−1) × 1 + 0.5 = 1 − 1 + 0.5 = **0.5**. The ReLU output is **0.5** (a positive z passes through). The step output is **1**, because 0.5 > 0.

</details>

<details>
<summary>Question 2. Continue the gradient-descent table with learning rate 0.1: what is w after step 6? Then say what happens if the learning rate is 1.1.</summary>

The slope at w = 2.01696 is 2 × (2.01696 − 3) = −1.96608, so w after step 6 = 2.01696 + 0.196608 = **2.213568**. With a learning rate of 1.1, the weight overshoots the best value 3 and lands farther away each step, so training **diverges**.

</details>

<details>
<summary>Question 3. Why do networks have hidden layers?</summary>

One neuron can only separate things with one straight line, so it cannot solve problems such as XOR. A hidden layer lets the network build **new features** from the inputs (such as "at least one" and "both") and combine them in the next layer.

</details>

> [!IMPORTANT]
> **In short**
>
> * A neuron computes a weighted sum plus a bias (z) and passes it through an activation function. Neurons are arranged in input, hidden, and output layers.
> * Learning means adjusting the weights to reduce a **loss**. Backpropagation finds how much each weight caused the error, and **gradient descent** moves each weight a small step downhill. The **learning rate** is the step size.
> * One neuron cannot solve XOR. Hidden layers can.

---

## Part A, Topic 3: Architectures of Neural Networks

In Topic 2 every neuron was joined to every neuron in the next layer. That is only one way to connect them. An **architecture** is the pattern of connections, and different kinds of data call for different patterns. Think of it as choosing the right tool: the shape of the data decides the shape of the network.

![Four cards: feedforward, convolutional, recurrent, and transformer, each with a small diagram, an idea, what it is good for, and an example](chapter-3-connectionist-ai-and-big-data/assets/fig-3-10-architectures.png)

*Figure 3.10: Four architectures and the data each one fits.*

**How to read this figure.** Each card shows one architecture. The small drawing at the top shows how the neurons or data are connected. Under it, **Idea** says how it works, **Good for** names the kind of data, and **Example** gives a real use. Read the four cards in turn:

* **Feedforward network (also called MLP, multilayer perceptron).** This is the network of Topic 2: layers connected in one direction. It suits **tables of numbers**, such as predicting a house price from its size, age, and location.
* **Convolutional neural network (CNN).** A small **filter** (here 3 × 3 squares) slides across the picture, and at each position it checks for a local pattern such as an edge. The same filter is reused everywhere, which makes the network efficient for images. It suits **images and video**, for example finding a tumour in a scan.
* **Recurrent neural network (RNN, LSTM).** It processes a sequence one item at a time, and passes a **memory** (h1, h2, h3, ...) from each step to the next. It was long the standard choice for **sequences** such as speech, but today it is mostly replaced by transformers.
* **Transformer.** Instead of passing memory step by step, it uses **attention**: every word looks at every other word and decides how much it matters. In the drawing, thicker arcs mean more attention. It suits **language**, and is now also used for images and audio. It is the basis of today's large language models and chatbots.

Other architectures exist, such as **autoencoders** (they compress the input and rebuild it, useful for spotting unusual machine readings) and **generative adversarial networks** (two networks compete so that one learns to create realistic images). You do not need to memorise every architecture. Remember the pairing: **CNN for images, transformer for language, feedforward for tables.**

### Check yourself

<details>
<summary>Question 1. Which architecture would you pick for (a) predicting a customer's monthly spending from five numbers, (b) detecting cracks in photos of bridges, (c) translating a sentence? Why?</summary>

(a) A **feedforward network**, because the data is a small table of numbers. (b) A **CNN**, because the data is an image and cracks are local patterns. (c) A **transformer**, because the data is language, where each word depends on other words in the sentence.

</details>

> [!IMPORTANT]
> **In short**
>
> * An architecture is the way the neurons are connected. The data decides which one is a good fit.
> * Feedforward fits tables. CNNs fit images. RNNs were used for sequences. Transformers use attention and fit language.

---

## Part A, Topic 4: Deep Learning and Advanced Concepts

**Deep learning** means neural networks with **many hidden layers**. The word "deep" refers to the number of layers, nothing more mysterious.

![Three stages of an image network, then three ingredients that came together in 2012](chapter-3-connectionist-ai-and-big-data/assets/fig-3-11-deep-and-2012.png)

*Figure 3.11: What each layer learns, and why deep learning took off around 2012.*

**How to read this figure.** The top row follows a picture through a deep image network. **Early layers** pick out simple edges and colours. **Middle layers** combine them into parts, such as an eye, a wheel, or a window. **Late layers** combine parts into whole objects, such as a face or a car. Nobody told the network to do this: the stages appear because each layer builds on the one before. The bottom row answers the question "why now?" Deep learning took off when three ingredients arrived together: **big data** (large labelled sets such as ImageNet), **GPUs** (graphics chips that make training much faster), and **better methods** (improved activation functions and training tricks). The yellow box shows the event that made this famous: in the 2012 ImageNet contest the network called AlexNet reached an error rate of 15.3%, against 26.2% for the runner-up. (These two numbers come from a secondary summary and should be checked against the original paper; see the References.)

### Overfitting: the main enemy of learning

A student who memorises last year's exam answers scores 100% on those exact questions, and only 40% on this year's different ones. A network can do the same: it **memorises** its training examples, including their noise, and then does badly on new data. This is **overfitting**.

The following small experiment shows it. A wave (a sine curve, the dashed grey line) is the truth. We get only **10 noisy points** from it (the gold dots) and fit three curves of different flexibility.

![Three panels showing a straight line, a smooth curve, and a very wiggly curve fitted to the same ten points](chapter-3-connectionist-ai-and-big-data/assets/fig-3-12-overfitting.png)

*Figure 3.12: Underfitting, a good fit, and overfitting, on the same ten points.*

**How to read this figure.** In each panel, the coloured line is the model, the gold dots are the training data, and the dashed grey line is the true wave. **Left:** a straight line is too simple to follow the wave, so it **underfits**. **Middle:** a smooth curve follows the wave and ignores the noise. **Right:** a very flexible curve passes through **every** training point, but it swings wildly between them, so it **overfits**. The numbers under each panel are the average squared error on the 10 training points and on 50 new positions along the true wave that the model never saw (the **test** error).

| Curve | Training error | Test error | What happened |
|---|--:|--:|---|
| Straight line (degree 1) | 0.3047 | 0.2103 | **Underfitting**: too simple |
| Smooth curve (degree 3) | 0.0453 | **0.0085** | About right |
| Very flexible (degree 9) | **0.0000** | 0.1050 | **Overfitting**: memorised the noise |

Look at the last row: the best score on the *training* data and a test error more than twelve times worse than the smooth curve. A model that is perfect on its own training data can be bad on new data. That is why we always keep a **test set** that the model has never seen. (These numbers come from a short program with only 10 points, so read them as an illustration of the pattern, not as a law.)

### Other terms you will meet

| Term | Plain meaning | Why it matters |
|---|---|---|
| **Training, validation, and test sets** | Three separate piles of data: one to learn from, one to tune settings on, one for a final fair check. | Gives an honest estimate of how the model will behave in real use. |
| **Regularisation and dropout** | Tricks that make overfitting less likely, for example randomly switching off some neurons during training. | Better results on new data. |
| **Transfer learning** | Start from a model trained on a big task and adjust it to a smaller one. | Saves data and time. |
| **Foundation model, large language model** | A very large model trained on huge amounts of data that can be adapted to many tasks. | The basis of modern chatbots. |
| **Embedding** | Turning words or images into lists of numbers so that similar items end up close together. | How networks "understand" meaning mathematically. |
| **Parameters** | All the weights and biases a network has to learn. | Counting them shows why deep learning needs so much data and computing. |

**Counting parameters.** A 28 × 28 picture has 784 pixels. A network with 784 inputs, one hidden layer of 128 neurons, and 10 outputs has 784 × 128 + 128 = 100,480 numbers in the first layer and 128 × 10 + 10 = 1,290 in the second: **101,770 parameters** for a tiny network that reads a postage-stamp image. Modern language and image models have far more, which is why they need huge data sets, many GPUs, and a lot of electricity.

### Check yourself

<details>
<summary>Question 1. A model scores 99% on its training data and 60% on new data. What is the problem, and what would you do?</summary>

It is **overfitting**: it has memorised the training examples. Options: collect more varied training data, use a simpler model, use regularisation or dropout, and always judge the model by its **test** score, not its training score.

</details>

<details>
<summary>Question 2. How many parameters does a network with 10 inputs, one hidden layer of 5 neurons, and 1 output have?</summary>

Input to hidden: 10 × 5 + 5 = 55. Hidden to output: 5 × 1 + 1 = 6. Total **61**.

</details>

> [!IMPORTANT]
> **In short**
>
> * Deep learning means many hidden layers. Early layers find simple patterns, later layers combine them.
> * It took off around 2012 because big data, GPUs, and better methods arrived together.
> * **Overfitting** means doing well on training data and badly on new data. Always test on data the model has never seen.

---

## Part A, Topic 5: Key Applications of Connectionist AI

Connectionist AI is everywhere you look at a screen. The slides list the main areas, and the figure shows what goes in and what comes out in each.

![Six cards showing input, output, and an example for images, speech, language, recommendation, driving perception, and generation](chapter-3-connectionist-ai-and-big-data/assets/fig-3-13-applications.png)

*Figure 3.13: Where you meet connectionist AI.*

**How to read this figure.** Each card has the same layout: **IN** is what the network receives, the arrow means "the network turns it into", **OUT** is what it produces, and **Example** is a real use. For instance, in *Images* the network receives pixels and produces labels or boxes, which is how face unlock works. In *Speech* it receives a sound wave and produces text, which is how subtitles are made. In *Generation* it receives a prompt and produces a new image, text, or audio clip.

**Back to the Smart Classroom.** In Chapter 2, the rule-based classroom failed on "Turn on the fan" because no rule covered that wording. A connectionist version is trained with many example sentences labelled *fan on*, *fan off*, *lamp on*, and *lamp off*. It learns which words go with which label, so it can handle new wording. The price is that it can still be wrong on unusual sentences, and nobody can easily point to "the rule" that decided. You will try a paper version of this in the hands-on activity.

**Hybrid systems.** Real products mix the approaches. A driver-assistance system might use a neural network to recognise a pedestrian in the camera picture (**connectionist**: recognising objects in pixels is learned from data), then the rule "IF a pedestrian is within 10 metres THEN brake" (**symbolic**: an explicit rule that people can read and check), and a route planner that searches for a path (**symbolic search**). The learning part handles messy sensor data, and the rule part handles known rules that must be explainable.

### Check yourself

<details>
<summary>Question 1. A shopping app suggests videos using your watch history, and then applies the rule "never show videos marked for adults to an account of a child". Which part is connectionist and which is symbolic?</summary>

The **suggestion** is connectionist: a network learns from many users' histories what you may like. The **age rule** is symbolic: an explicit rule that must always hold and that can be read and audited.

</details>

> [!IMPORTANT]
> **In short**
>
> * Connectionist methods power vision, speech, language, recommendation, driving perception, and generation.
> * Real systems are often hybrids: a learned part for messy data and a rule part for what must be explainable.

---

## Part A, Topic 6: Ethical Considerations and Challenges

A model can be right 95% of the time overall and still treat one group badly. How is that possible? Because a network learns whatever patterns are in its data, including unfair ones, and an overall score can hide who the errors fall on.

| Challenge | What can go wrong | Example |
|---|---|---|
| **Bias** | The model learns unfair patterns from unrepresentative data. | A 2018 study of commercial face-analysis systems found much higher error rates for darker-skinned women than for lighter-skinned men (Buolamwini and Gebru, 2018). |
| **Lack of explanation** | We cannot easily say why the network gave an answer. | A loan is refused and nobody can say why. |
| **Privacy** | Training data may contain personal data that the model can leak. | A model repeating private text it saw in training. |
| **Reliability** | Networks can be fooled by small changes, or be wrong with high confidence. | A sticker on a sign changes how a vision system reads it. |
| **Energy and cost** | Training large models uses a lot of electricity and hardware. | Large data-centre training runs. |
| **Misuse** | Synthetic images, voices, and text can mislead people. | Fake videos. |

### How an average hides a problem

The *Gender Shades* study, by Joy Buolamwini and Timnit Gebru, did not report one overall score. They split the photos by skin tone and gender. The abstract of their paper reports error rates of **up to 34.7% for darker-skinned women**, while the maximum error rate for **lighter-skinned men was 0.8%**.

To see why a single average can hide such a gap, look at a **made-up** example (not from the study). A test set has 100 people: 90 from Group A and 10 from Group B. The model makes 2 mistakes on Group A and 4 on Group B.

![Left: two bars from the Gender Shades study. Right: a made-up example where the overall accuracy of 94% hides 60% for a small group](chapter-3-connectionist-ai-and-big-data/assets/fig-3-14-average-hides.png)

*Figure 3.14: An average can hide who is being failed.*

**How to read this figure.** The left panel shows the real study: the highest error rate was 34.7% for darker-skinned women and 0.8% for lighter-skinned men. The right panel is our own illustration. Group A (90 people) has 97.8% accuracy and Group B (10 people) has only 60%, yet the blue bar for **everyone** is 94%. The small group barely moves the overall average. "94% accurate" sounds excellent, but for Group B it is wrong four times out of ten.

That is why reports should show results **for each group**, and why the first questions to ask about any connectionist system are these:

1. What data was it trained on, and who is missing from that data?
2. How was it tested, and on whom?
3. Can its decisions be explained well enough for the situation?
4. Who is responsible when it is wrong?
5. Can a human check or overrule the result?

### Check yourself

<details>
<summary>Question 1. A company trains a network to screen CVs, using the last ten years of hiring decisions. In those years most people hired were men. What could go wrong, and which of the five questions apply?</summary>

The model may learn the **past pattern** rather than the quality of candidates, and rank women lower: it copies the unfairness in its data. The questions that apply most directly are 1 (what data, and who is missing), 2 (how was it tested, and on whom), and 5 (can a human check or overrule it). A good check before use is to compare selection and error rates between groups on test data, and to keep a human in the decision.

</details>

<details>
<summary>Question 2. A company says "our face system is 94% accurate". Which two questions would you ask before trusting it?</summary>

(1) Accurate for **whom**? Ask for the results for each group (skin tone, gender, age). (2) How many people were in the test set, and how were they chosen?

</details>

> [!IMPORTANT]
> **In short**
>
> * Models inherit the biases of their data, and they are hard to explain.
> * A high overall accuracy can hide poor results for one group, so check results group by group.
> * Ask who is affected, how the data was collected, and who is accountable.

---

## Part B, Topic 1: Introduction to Big Data

In Part A you saw that a neural network has millions of weights, and that it needs many varied examples to set them well. **Part B asks where those examples come from, and what it takes to store, process, and use them responsibly.**

**Big Data** means data that is so **large, fast, or varied** that ordinary tools cannot store or process it well. It does not mean "any big file". It is a set of *challenges*, and the classic way to describe them is with Vs.

![Five cards for volume, velocity, variety, veracity, and value, and three cards for structured, semi-structured, and unstructured data](chapter-3-connectionist-ai-and-big-data/assets/fig-3-15-five-vs.png)

*Figure 3.15: The five Vs of Big Data and the three kinds of data.*

**How to read this figure.** The top row has one card per V. Each card has the V, the question it asks, and an example. **Volume** asks "how much?" (billions of photos). **Velocity** asks "how fast?" (live payments and sensor readings that arrive and change quickly). **Variety** asks "how different?" (posts, photos, and clicks together). **Veracity** asks "how trustworthy?" (missing, wrong, or fake records). **Value** asks "how useful?" (data matters only if it helps a decision). The first three are the **classic three**. Veracity and value are often added. The bottom row shows the three kinds of data: **structured** (rows and columns, such as a bank table), **semi-structured** (tags or keys but no fixed table, such as JSON or XML files), and **unstructured** (no fixed format, such as photos, audio, and free text).

**Why Big Data matters for AI.** Most of the data that deep networks learn from is unstructured, and a network with millions of weights needs a very large number of examples. This is why deep learning grew together with Big Data.

### Check yourself

<details>
<summary>Question 1. Name the main V in each case: (a) a payment company receives millions of card payments every minute, (b) a hospital wants to combine X-ray images, doctors' notes, and heart-rate streams, (c) 20% of the ages in a customer data set are missing and some are 250.</summary>

(a) **Velocity** (and volume). (b) **Variety**. (c) **Veracity**: the data cannot be trusted as it is.

</details>

> [!IMPORTANT]
> **In short**
>
> * Big Data is a set of challenges: volume, velocity, and variety, plus veracity and value.
> * Data can be structured, semi-structured, or unstructured, and most data for deep learning is unstructured.

---

## Part B, Topic 2: Big Data Technologies

One computer cannot read a huge library in a lifetime. What if a thousand computers each read one shelf? That question is the idea behind most Big Data technology: **spread the storage and the work over many machines**.

### Storing very large data

![Top: a file cut into blocks and copied over four computers. Bottom: a data lake of raw items and a data warehouse of tidy tables](chapter-3-connectionist-ai-and-big-data/assets/fig-3-16-storing-big-data.png)

*Figure 3.16: Storing very large data.*

**How to read this figure.** In the top panel, a single computer fails because its disk is too small, reading everything takes too long, and a failure loses the data. On the right, the file is cut into blocks A to D and spread over four computers. Each block is stored on **two** computers, so if one computer breaks, no block is lost. This is a **distributed file system** (HDFS is a well-known example). In the bottom panel, a **data lake** keeps raw data of every kind exactly as it arrived (photos, audio, logs, video, text, sensor data), which suits future uses nobody has planned yet. A **data warehouse** keeps data that has already been cleaned and organised into tables, which suits regular reports and dashboards.

| Need | Technology idea | Examples |
|---|---|---|
| **Store very large data** | Distributed file systems: split files over many computers and keep copies. | HDFS |
| **Store flexible data** | **NoSQL** databases: key-value, document, column, or graph stores instead of fixed tables. | MongoDB, Cassandra, Neo4j |
| **Store for analysis** | A data warehouse (organised, ready for reports) or a data lake (raw data of all kinds). | Cloud warehouses and lakes |
| **Process in parallel** | Split the work across many machines. | MapReduce, Apache Spark |
| **Process live streams** | Handle events as they arrive. | Apache Kafka, stream processors |
| **Rent computing** | Cloud platforms that provide storage and computing on demand. | Public cloud services |

### Processing in parallel: MapReduce

**MapReduce** (described by Jeffrey Dean and Sanjay Ghemawat of Google in 2004) is the classic way to process data on many computers. You write two small functions, **map** and **reduce**, and the system runs them on many machines. The standard example is counting words.

![Three lines of text go through map, shuffle, and reduce to give word counts](chapter-3-connectionist-ai-and-big-data/assets/fig-3-17-mapreduce.png)

*Figure 3.17: Word count with MapReduce.*

**How to read this figure.** Read the four columns from left to right. **Input:** three lines of text. **1 Map:** each line goes to its own machine, which emits a pair (word, 1) for every word it sees. For line 1 that gives (big,1) (data,1) (needs,1) (big,1) (storage,1). **2 Shuffle:** the system gathers all pairs with the same word in one place, giving, for example, big → [1,1,1]. **3 Reduce:** each group is added up, giving **big = 3, data = 2, needs = 2, analysis = 2, storage = 1**.

Why does the middle step exist? A reducer must see **every** pair for its word. Without the shuffle, two reducers might each see part of the pairs for "big" and report two wrong partial counts (such as 2 and 1) instead of one right total (3). And because the map step handles each line separately, it can run on thousands of machines at the same time. A real system also copes with machines that break in the middle of a job.

### Check yourself

<details>
<summary>Question 1. Use the map, shuffle, and reduce recipe to count the words in these three lines: "ai learns from data", "data helps ai learn", "big data big ai". (Treat "learn" and "learns" as different words.)</summary>

* Map: (ai,1) (learns,1) (from,1) (data,1) | (data,1) (helps,1) (ai,1) (learn,1) | (big,1) (data,1) (big,1) (ai,1)
* Shuffle: ai → [1,1,1]; data → [1,1,1]; big → [1,1]; learns → [1]; from → [1]; helps → [1]; learn → [1]
* Reduce: **ai = 3, data = 3, big = 2, learns = 1, from = 1, helps = 1, learn = 1**

"learn" and "learns" are counted separately because the recipe only matches identical text.

</details>

<details>
<summary>Question 2. Choose a data lake or a data warehouse: (a) raw camera footage and sensor logs kept for future use, (b) cleaned monthly finance tables used for reports.</summary>

(a) **Data lake**: raw data of all kinds. (b) **Data warehouse**: organised data ready for reports.

</details>

> [!IMPORTANT]
> **In short**
>
> * Big Data technologies spread storage and computing across many machines, and keep copies so that a failure loses nothing.
> * **MapReduce** splits a job into a map step, a shuffle step, and a reduce step. A data lake keeps raw data; a data warehouse keeps cleaned, structured data.

---

## Part B, Topic 3: Data Processing and Analytics

Real data arrives messy. Between the moment a sensor records a number and the moment a chart appears, the data passes through a series of steps called a **pipeline**.

![Five steps from collect to analyse, then two ways to run the processing step: batch and stream](chapter-3-connectionist-ai-and-big-data/assets/fig-3-18-data-pipeline.png)

*Figure 3.18: A data pipeline, and two ways to run step 4.*

**How to read this figure.** The top row shows the five steps. **Collect** gathers data from sensors, apps, forms, and logs. **Clean** removes duplicates, fixes wrong values, and fills gaps. **Store** puts the data in files, databases, a lake, or a warehouse. **Process** combines, filters, and counts at scale. **Analyse** produces charts, statistics, and machine-learning models. The bracket at the top shows **ETL** (extract, transform, load), the common name for the first three steps. The red label is a warning: **cleaning is usually the biggest job.** The bottom row shows two ways to run the processing step. In **batch** processing, a large group of data is collected and processed at once, so the result comes after minutes or hours (a monthly sales report or an electricity bill). In **stream** processing, each event is processed as it arrives, so the result comes in seconds or less (flagging a suspicious card payment while the customer is still at the till).

### Four levels of analytics

Once the data is ready, the questions you ask about it fall into four levels, each more valuable and more difficult than the one before. The figure uses a university looking at student results.

![Four rising steps: descriptive, diagnostic, predictive, and prescriptive analytics, each with its question and an example](chapter-3-connectionist-ai-and-big-data/assets/fig-3-19-four-levels.png)

*Figure 3.19: The four levels of analytics.*

**How to read this figure.** Climb the steps from left to right. **Descriptive** asks *what happened?* (How many students passed last term?) **Diagnostic** asks *why did it happen?* (Why did the pass rate fall?) **Predictive** asks *what will probably happen?* (Which students are likely to fail next term?) This is where **machine learning from Part A** is used. **Prescriptive** asks *what should we do?* (Which extra classes should we offer?)

### Check yourself

<details>
<summary>Question 1. Choose batch or stream for each: (a) a monthly electricity bill, (b) an alarm when a heart-rate sensor shows danger, (c) a weekly sales report, (d) flagging a suspicious payment at the till. Then name the level of analytics for: "Which students are likely to fail next term?"</summary>

(a) Batch. (b) Stream. (c) Batch. (d) Stream. The last question is **predictive** analytics.

</details>

> [!IMPORTANT]
> **In short**
>
> * Data passes through a pipeline: collect, clean, store, process, analyse. Most of the effort goes into cleaning.
> * Batch processing handles data in large groups. Stream processing handles each event as it arrives.
> * Analytics has four levels: descriptive, diagnostic, predictive, and prescriptive.

---

## Part B, Topic 4: Data Analysis and Visualization

The same numbers can tell two opposite stories depending on the chart. **Visualization** shows data as pictures so that people see patterns quickly, and the right chart depends on the question you are asking.

![Five chart types, each under the question it answers](chapter-3-connectionist-ai-and-big-data/assets/fig-3-20-chart-chooser.png)

*Figure 3.20: Choose the chart that fits the question.*

**How to read this figure.** Each card starts with a question and ends with the chart that answers it. To see how something **changes over time**, use a **line chart**. To **compare categories**, use a **bar chart**, because lengths are easy to compare. To show the **share of a whole**, use a **pie chart** (only with a few parts) or a stacked bar. To check whether **two numbers are related**, use a **scatter plot**, which shows patterns and outliers. To see **how one number is spread out**, use a **histogram**, which shows the shape of the data.

**A small worked example.** Monthly app downloads, in thousands: January 12, February 15, March 21, April 18. The highest month is March (21 thousand). From January to March the change is 21 − 12 = 9 thousand, which is 9 ÷ 12 = 75% more. From March to April the change is 18 − 21 = −3 thousand, which is −3 ÷ 21 ≈ −14%.

### Charts can mislead

A chart can mislead through its axis, its scale, or the data selected. The most common trick is a bar chart whose axis does not start at zero. Two versions of a program scored 92% and 95% on a test. The figure draws the same two numbers twice.

![Two bar charts of the same data; the left axis starts at 0 and the right axis starts at 90](chapter-3-connectionist-ai-and-big-data/assets/fig-3-21-misleading-axis.png)

*Figure 3.21: The same two numbers, drawn with an axis that starts at 0 (left) and at 90 (right).*

**How to read this figure.** Check the number at the bottom of each vertical axis. On the left it is 0, and the bars look almost equal, which matches the truth: (95 − 92) ÷ 92 ≈ **3.3%** more. On the right it is 90, so the bars are only 2 and 5 units tall, and Version B looks 5 ÷ 2 = **2.5 times** as tall as Version A. The data did not change. Only the axis did.

**Four rules for honest charts.** (1) Start bar charts at zero. (2) Label the axes and units. (3) Do not use too many colours or 3-D effects. (4) Show where the data comes from.

### Check yourself

<details>
<summary>Question 1. A bar chart shows two products, with sales of 480 and 500, on an axis that starts at 460. How tall does the second bar look compared with the first, and what is the real difference?</summary>

The bars are 20 and 40 units tall, so the second looks **twice** as tall. The real difference is (500 − 480) ÷ 480 ≈ **4.2%**. The chart breaks the rule "start bar charts at zero".

</details>

> [!IMPORTANT]
> **In short**
>
> * Choose the chart that fits the question: line for time, bar for categories, scatter for relationships, histogram for spread.
> * A chart can mislead through its axis, scale, or choice of data. Check the axes before trusting a picture.

---

## Part B, Topic 5: Big Data Use Cases

Online shopping, road traffic, hospital records: what do they have in common? Each produces a stream of data about many people, and each can be used to improve a service or to harm a person. The table pairs the benefit with the concern.

| Field | Use | Data used | Possible concern |
|---|---|---|---|
| **Retail and media** | Recommend products and videos | Purchase and viewing history | Profiling and manipulation |
| **Healthcare** | Spot disease patterns; support diagnosis | Records, scans, wearable data | Very sensitive personal data |
| **Transport** | Predict traffic; plan routes | GPS and sensor data | Location tracking |
| **Finance** | Detect fraud in real time | Transaction streams | Customers wrongly blocked |
| **Smart cities** | Manage energy, waste, and public transport | Sensor networks | Surveillance |
| **Education** | Find students who need extra help | Quiz and attendance data | Labelling students unfairly |

**Link to the three approaches.** Take fraud detection. A *symbolic* system flags "any payment above a limit". A *connectionist* system learns what fraudulent payments look like from millions of past cases. A real bank often uses **both**: rules for what must always be caught, and a learned model for subtle patterns. Because the data arrives continuously, it is also a typical case for **stream** processing (Topic 3).

> [!IMPORTANT]
> **In short**
>
> * Big Data use cases such as fraud detection, traffic, health, retail, and education can use rules, learned models, or both.
> * Every use case comes with a concern about people. That is the subject of the next topic.

---

## Part B, Topic 6: Big Data Ethics and Privacy

If a table has no names in it, is anyone in it safe? Not necessarily. This topic shows why, and then lists the ethical issues that come with Big Data.

### Why removing names is not enough

![Two tables, one without names and one with names, joined on shared facts to reveal who has which diagnosis](chapter-3-connectionist-ai-and-big-data/assets/fig-3-22-reidentification.png)

*Figure 3.22: How a table without names can still identify a person.*

**How to read this figure.** On the left is a hospital table with **no names**: it lists a ZIP code, a birth year, a sex, and a diagnosis. On the right is a public list (for example a voter list) that holds **names** with the same three facts. The yellow box in the middle is the attack: **join** the two tables wherever ZIP code, birth year, and sex match. Only one row in each table matches Mia, so the join links her name to the diagnosis diabetes, although neither table contained both. The table is made up for practice, but the effect is real: Latanya Sweeney (2000) showed that, using 1990 US census data, **87%** of the US population could be uniquely identified by just three facts, a five-digit ZIP code, gender, and date of birth.

### Measuring the risk: k-anonymity

A table has **k-anonymity** if every combination of "identifying-looking" columns (called **quasi-identifiers**) is shared by at least **k** people. If k = 1, someone is unique and can be found by anyone who knows those facts about them. Our practice table has 8 people.

| ZIP | Birth year | Sex | People sharing this combination |
|---|:-:|:-:|:-:|
| 510 | 1990 | F | 2 |
| 510 | 1991 | M | **1** (unique) |
| 511 | 1990 | F | **1** (unique) |
| 511 | 1992 | M | 2 |
| 512 | 1991 | F | **1** (unique) |
| 512 | 1993 | M | **1** (unique) |

The smallest group has 1 person, so **k = 1**, and four of the eight people are unique. Now **generalise**: keep only the first two digits of the ZIP code and the decade of birth.

| ZIP prefix | Decade | Sex | People sharing this combination |
|---|:-:|:-:|:-:|
| 51 | 1990s | F | 4 |
| 51 | 1990s | M | 4 |

Now **k = 4**: nobody is unique. The price is **less detail**, because analysts can no longer see small differences between neighbourhoods or birth years. Privacy and usefulness pull in opposite directions, and someone must decide the balance. (k-anonymity is not complete protection: if everyone in a group has the same illness, an outsider learns it anyway.)

**A real case.** A biography of Sweeney reports that in **1997** she re-identified the then Governor of Massachusetts, William Weld, by matching medical records with the names removed to a public list of people. The lesson: "we removed the names" is not a guarantee. Ordinary facts, **combined**, can act like a name.

### Ethical issues and good practice

| Issue | Meaning | Example |
|---|---|---|
| **Consent** | People should know what is collected and agree to it. | An app that collects location without telling users. |
| **Purpose limitation** | Use data only for the stated purpose. | Health data reused for advertising. |
| **Anonymisation is hard** | Removing names does not always make people unidentifiable. | The example above. |
| **Security** | Large collections are attractive targets. | Data breaches. |
| **Bias and fairness** | Data reflects past unfairness, and models copy it. | A hiring model trained on past decisions. |
| **Transparency and control** | People should be able to see, correct, or delete their data. | Rights under privacy laws such as the EU GDPR. |

**A good-practice checklist.** (1) Collect only the data you need. (2) Explain what you collect and why. (3) Remove or mask direct identifiers, and be careful with combinations of fields. (4) Protect the data with access control and encryption. (5) Delete it when it is no longer needed. (6) Check the results for unfair outcomes.

### Check yourself

<details>
<summary>Question 1. A hospital publishes a table without names (ZIP code, birth year, gender, diagnosis). A neighbour knows that Mia lives in ZIP 10003, was born in 1992, and is female. Only one row matches. What does the neighbour learn, and what could the hospital do?</summary>

The neighbour learns Mia's **diagnosis**. The hospital could **generalise** the quasi-identifiers (for example, keep a ZIP prefix and a birth decade) until every combination is shared by several people, and could remove rows that stay unique. Generalising loses some detail, so the hospital must balance privacy and usefulness.

</details>

<details>
<summary>Question 2. In the first k-anonymity table, what would k be if you kept the full ZIP code but generalised the birth year to the decade?</summary>

Groups by (ZIP, decade, sex): (510, 1990s, F) has 2, (510, 1990s, M) has 1, (511, 1990s, F) has 1, (511, 1990s, M) has 2, (512, 1990s, F) has 1, (512, 1990s, M) has 1. The smallest is 1, so **k is still 1**. Generalising only one column was not enough.

</details>

> [!IMPORTANT]
> **In short**
>
> * Removing names does not make data anonymous. A few ordinary facts together can identify a person.
> * k-anonymity measures how many people share the same combination of facts. Generalising raises k but costs detail.
> * Ethical use means collecting only what is needed, protecting it, being open about how it is used, and checking for unfair results.

---

## Hands-On Activity: A Learner You Train and Then Break

In Chapter 2 you built a rule-based Smart Classroom and found where the rules failed. Here you build the **learned** version on paper, with a very small model that counts words. It is not a neural network, but it shows the same idea: **the knowledge comes from labelled examples, not from rules that someone wrote.** The lecturer's block tool has a *recognise text* block that does the same job with a real model; use it if it is available, and use the paper version if it is not.

**Goal.** Train a small model from example sentences, test it on sentences it has not seen, and discover what a learner gains and loses compared with rules.

### Step 1: Train

The model sees eight labelled sentences.

| # | Sentence | Label |
|--:|---|---|
| 1 | turn on the fan | fan on |
| 2 | fan on please | fan on |
| 3 | switch the fan off | fan off |
| 4 | fan off now | fan off |
| 5 | turn on the lamp | lamp on |
| 6 | lamp on please | lamp on |
| 7 | switch the lamp off | lamp off |
| 8 | lamp off now | lamp off |

For each label, count in how many of its two sentences each word appears. For *fan on* the counts are: turn 1, on 2, the 1, fan 2, please 1. Do the same for the other three labels. These counts are the model's "weights".

### Step 2: Classify new sentences

To classify a sentence, add up the counts of its words for each label. The label with the highest total wins. Words that were never seen add nothing. Classify:

* (a) please turn the fan on
* (b) switch the fan off soon
* (c) don't turn the fan on
* (d) make it bright

Write the four totals for each sentence and the winner.

### Step 3: Fix it with more examples, and look again

Add two more training sentences: **9. turn the fan off please** (label *fan off*) and **10. please switch the lamp on** (label *lamp on*). Update the counts. Then classify two sentences again: **(e) turn the fan off please** and **(f) turn off the lamp**. Compare each with the result you got before adding the two sentences.

### Reflect

1. Compare (b) with the rule-based program of Chapter 2. What changed?
2. Which sentence did the model get wrong in Step 2, and why?
3. What happened to (f) after Step 3, and what does it tell you about learning from examples?
4. Count what you gained and lost compared with rules: how many examples did you need, and could the model explain a wrong answer?

<details>
<summary>Check your answers</summary>

**Step 1: counts**

| Label | Word counts |
|---|---|
| fan on | turn 1, on 2, the 1, fan 2, please 1 |
| fan off | switch 1, the 1, fan 2, off 2, now 1 |
| lamp on | turn 1, on 2, the 1, lamp 2, please 1 |
| lamp off | switch 1, the 1, lamp 2, off 2, now 1 |

**Step 2: totals**

| Sentence | fan on | fan off | lamp on | lamp off | Winner |
|---|--:|--:|--:|--:|---|
| (a) please turn the fan on | 7 | 3 | 5 | 1 | fan on (right) |
| (b) switch the fan off soon | 3 | 6 | 1 | 4 | fan off (right) |
| (c) don't turn the fan on | 6 | 3 | 4 | 1 | fan on (**wrong**) |
| (d) make it bright | 0 | 0 | 0 | 0 | no winner |

**Step 3.** After adding the two sentences, (e) improves: before, "turn the fan off please" was a **tie** (fan on 5, fan off 5), and afterwards it is fan off 10 against fan on 5, which is right. But (f) "turn off the lamp" was right before (lamp off 5, against fan off 3 and lamp on 4) and is **wrong afterwards**: fan off 6, lamp on 6, lamp off 5. The new sentences added "please", "turn", and "off" to other labels, and that pulled the total of the wrong labels above the right one.

**Reflections**

1. The rule-based program with "contains" rules was confused by "soon" (Chapter 2). The learned model picks *fan off*, because "switch", "the", "fan", and "off" are all evidence for it, and "soon" adds nothing. It handles wording that no rule listed.
2. (c) is wrong. The model counts words and ignores order and meaning, so "don't" means nothing to it. A bigger model with many more examples, including negative ones, could learn it, but it would still be a guess.
3. **Fixing one sentence broke another.** The model's behaviour is the combined effect of all the examples, so changing the data changes everything a little. This is why learned systems must be **tested again on all old cases** after every change, and why a *test set* matters.
4. Eight to ten examples replaced a list of rules, and new wording works without writing a new rule. But we **lose explanation**: for (c) and (f) the model cannot say why it was wrong. Real systems use neural networks instead of word counts, but the idea is the same.

</details>

---

## Common Misconceptions

> [!WARNING]
> Read the left column, decide whether it is true, and then check the right column.

| Misconception | What is true | Where to check |
|---|---|---|
| "A neural network works like a human brain." | It is only loosely inspired by the brain. An artificial neuron is a weighted sum and a simple function. | Part A, Topic 1 |
| "Someone programs the weights." | The weights are found by training on examples. People choose the architecture and the data. | Part A, Topic 2 |
| "A model that scores 99% on its training data is excellent." | It may have memorised the data. What counts is the score on data it has never seen. | Part A, Topic 4 |
| "94% accurate means it works well for everyone." | An average can hide a group with a much worse result. | Part A, Topic 6 |
| "Big Data just means a big file." | It means data that is large, fast, or varied enough that ordinary tools fail, and that may be untrustworthy. | Part B, Topic 1 |
| "If the names are removed, the data is anonymous." | A few ordinary facts, combined, can identify a person. | Part B, Topic 6 |

---

## Key Takeaways

> [!IMPORTANT]
> **If you remember only eight things**
>
> * **Connectionist AI** stores knowledge as **weights** in a network of simple neurons, and the network **learns** them from examples.
> * A neuron computes a weighted sum plus a bias, then applies an activation function. Layers of neurons build new features out of old ones, which is why one neuron cannot solve XOR and a network can.
> * Learning is a loop: forward pass, loss, backpropagation, gradient descent. A learning rate that is too large makes training diverge.
> * Choose the **architecture** to fit the data: CNN for images, transformer for language, feedforward for tables.
> * **Deep learning** took off around 2012 because big data, GPUs, and better methods arrived together. Its enemy is **overfitting**, so always test on unseen data.
> * Models inherit **bias** from their data, and a high average can hide a failing group.
> * **Big Data** is a set of challenges (volume, velocity, variety, veracity, value). It is handled with distributed storage, parallel processing such as MapReduce, and a pipeline in which cleaning is the biggest job.
> * Removing names does not make data anonymous. Ordinary facts combined can identify people, so collect only what you need and protect it.

---

## Practice Questions

### Part A: Multiple Choice

**Q1.** In Connectionist AI, where is the knowledge stored?  
A. In hand-written IF–THEN rules  
B. In the weights of the connections  
C. In a table of rewards  
D. In a user manual

**Q2.** A neuron has x1 = 1, x2 = 0.5, w1 = 0.4, w2 = −0.2, and b = 0.1. What is z?  
A. 0.4  
B. 0.6  
C. 0.1  
D. −0.4

**Q3.** Which architecture is most suited to images?  
A. CNN  
B. Rule base  
C. MapReduce  
D. k-anonymity

**Q4.** Which step of the learning loop turns the difference between a guess and the true answer into one number?  
A. Forward pass  
B. Loss  
C. Gradient descent  
D. Shuffle

**Q5.** In gradient descent, what happens when the learning rate is far too large?  
A. Training is perfect  
B. The weight overshoots and can get farther from the best value  
C. The loss is always zero  
D. The network stops using data

**Q6.** A model scores 99% on training data and 60% on new data. What is this called?  
A. Underfitting  
B. Overfitting  
C. Regularisation  
D. Streaming

**Q7.** In a customer data set, 20% of the ages are missing and some are 250. Which V is the main problem?  
A. Volume  
B. Velocity  
C. Variety  
D. Veracity

**Q8.** What is the purpose of the shuffle step in MapReduce?  
A. To delete duplicate lines  
B. To bring all pairs with the same word to the same reducer  
C. To draw a chart  
D. To remove names

**Q9.** A table has k = 1 for its chosen columns. What does that mean?  
A. Nobody can be identified  
B. At least one person has a unique combination and could be found  
C. The table has one column  
D. The table is encrypted

### Part B: Short Answer

**Q10.** Explain why a single neuron cannot compute XOR, and what fixes the problem.

**Q11.** A company says its face system is "94% accurate". Give two questions you would ask, and say why the average can mislead.

**Q12.** Say in your own words the difference between a data lake and a data warehouse.

### Part C: Apply It

**Q13.** A bank wants to detect fraudulent card payments. Describe a hybrid design that uses both a symbolic rule and a learned model. Is batch or stream processing more suitable, and why?

**Q14.** A university publishes a student table with no names, but with ZIP code, birth date, and gender. Name the risk, and give one way to reduce it and one cost of doing so.

### Part D: Compute It

**Q15.** The loss is (w − 3)², the slope is 2(w − 3), and we start at w = 0 with a learning rate of 0.5. Compute w after step 1 and after step 2. What do you notice?

**Q16.** A network has 4 inputs, one hidden layer of 6 neurons, and 3 outputs. How many parameters (weights and biases) does it have?

**Q17.** Use the word counts from the hands-on activity. Which label does the model give to "switch the lamp off now", and what are the four totals?

---

## Answer Key

| Q | Answer | Explanation |
|---|---|---|
| Q1 | B | The knowledge is in the weights, found by training. |
| Q2 | A | z = 0.4 × 1 + (−0.2) × 0.5 + 0.1 = 0.4. |
| Q3 | A | A CNN slides small filters over an image to find local patterns. |
| Q4 | B | The loss is one number that says how wrong the guess was. |
| Q5 | B | A step that is too large jumps past the best value and can land farther away each time. |
| Q6 | B | Doing well on training data and badly on new data is overfitting. |
| Q7 | D | Missing and impossible values are a question of trustworthiness. |
| Q8 | B | A reducer must see every pair for its word to give the right total. |
| Q9 | B | k = 1 means the smallest group has one person, who is unique. |
| Q10 | Sample | A neuron separates the inputs with one straight line, and no line separates the XOR points (1 for exactly one input). A hidden layer builds new features, for example "at least one" (OR) and "both" (AND), and an output neuron combines them as "OR and not AND". |
| Q11 | Sample | Accurate for **whom** (results by skin tone, gender, age)? How many people were in the test set and how were they chosen? A small group barely changes the average, so one group can have much worse accuracy while the overall number is high. |
| Q12 | Sample | A data lake keeps raw data of all kinds as it arrived, for future uses. A data warehouse keeps cleaned, organised data ready for regular reports. |
| Q13 | Sample | Rule: flag any payment above a fixed limit or from a blocked country (explainable, always applied). Learned model: a network trained on past fraud cases scores each payment for suspicious patterns. **Stream** processing is suitable, because the payment must be judged in seconds, before it is completed. |
| Q14 | Sample | **Re-identification**: ZIP code, birth date, and gender together can identify many people when matched with a public list. Reduce it by generalising (keep a ZIP prefix and the birth year or decade) or by removing unique rows. The **cost** is less detail for analysis. |
| Q15 | w = 3 after step 1, w = 3 after step 2 | Step 1: slope 2(0 − 3) = −6, so w = 0 − 0.5 × (−6) = 3. At w = 3 the slope is 0, so step 2 leaves w at 3. A well-chosen rate can reach the best value at once here, but this loss is a very simple bowl; real losses are not. |
| Q16 | 51 | Input to hidden: 4 × 6 + 6 = 30. Hidden to output: 6 × 3 + 3 = 21. Total 30 + 21 = 51. |
| Q17 | lamp off | lamp off: switch 1 + the 1 + lamp 2 + off 2 + now 1 = 7; fan off: 1 + 1 + 0 + 2 + 1 = 5; lamp on: 0 + 1 + 2 + 0 + 0 = 3; fan on: 0 + 1 + 0 + 0 + 0 = 1. The winner is **lamp off** with 7. |

---

## What Comes Next: From Labelled Examples to Rewards

**What you have now.** In this chapter, the machine was shown the **right answer** for every training example: a label ("cat") or a number (a house price). From thousands of such examples, a neural network found its own weights, and you saw that its quality depends on the data, which is why Big Data and its ethics belong in the same chapter. You also saw the limits: it needs many labelled examples, it can overfit, it is hard to explain, and it can inherit bias.

**What is still missing.** Many real problems do not come with a label for every step. A robot walking, a game player, or a thermostat makes a **series of decisions**, and it learns only at the end, or only after a delay, whether things went well. Nobody can label each move as "right" or "wrong" in advance.

**Chapter 4 starts there.** It asks: *what if the machine learned by acting, receiving rewards, and adjusting its behaviour?* That is **Behaviorist AI**, better known as reinforcement learning. You will work with a small corridor, and compute by hand how a reward at the goal spreads backward along the path. **Keep your notes on the learning rate and on overfitting.** The learning rate returns in a new form, and deep networks from this chapter are used inside modern reinforcement-learning systems.

---

---

## Key Terms in Chinese

*Check these against your course textbook or a Chinese-speaking teammate; wording varies between books.*

| English | 中文 |
|---|---|
| Connectionist AI | 连接主义 |
| artificial neural network | 人工神经网络 |
| neuron | 神经元 |
| weight | 权重 |
| bias | 偏置 |
| activation function | 激活函数 |
| perceptron | 感知机 |
| loss function | 损失函数 |
| gradient descent | 梯度下降 |
| backpropagation | 反向传播 |
| learning rate | 学习率 |
| overfitting | 过拟合 |
| deep learning | 深度学习 |
| convolutional neural network (CNN) | 卷积神经网络 |
| recurrent neural network (RNN) | 循环神经网络 |
| Big Data | 大数据 |
| data lake | 数据湖 |
| data warehouse | 数据仓库 |
| batch processing | 批处理 |
| stream processing | 流处理 |
| data visualization | 数据可视化 |
| anonymization | 匿名化 |
| re-identification | 重新识别（再识别） |

## Glossary

| Term | Meaning |
|---|---|
| **Activation function** | The function that turns a neuron's sum into its output. |
| **Architecture** | The pattern in which the neurons of a network are connected. |
| **Attention** | A mechanism in which every part of the input weighs how much every other part matters. |
| **Backpropagation** | The method that works out each weight's share of the error. |
| **Batch processing** | Processing a large group of data at once, with a result after minutes or hours. |
| **Bias (fairness)** | Unfair patterns in data or results. |
| **Bias (in a neuron)** | A number added to the weighted sum. |
| **Big Data** | Data too large, fast, or varied for ordinary tools. |
| **CNN** | Convolutional neural network, suited to images. |
| **Data lake / warehouse** | Stores for raw data / for organised data used in reports. |
| **Data pipeline** | The steps from collecting data to analysing it: collect, clean, store, process, analyse. |
| **Deep learning** | Neural networks with many hidden layers. |
| **Distributed file system** | Storage that cuts files into blocks and keeps copies on many computers. |
| **Embedding** | A list of numbers that represents a word or an image so that similar items are close together. |
| **Epoch** | One pass through all the training examples. |
| **ETL** | Extract, transform, load: preparing data for analysis. |
| **Five Vs** | Volume, velocity, variety, veracity, and value: the challenges of Big Data. |
| **Forward pass** | Sending an input through the layers of a network to get an output. |
| **Gradient descent** | Repeated small weight changes that reduce the loss. |
| **Hidden layer** | A layer between the input and the output of a neural network. |
| **Hybrid system** | A system that combines learned parts and hand-written rules. |
| **k-anonymity** | A table where every combination of identifying-looking columns is shared by at least k people. |
| **Learning rate** | The size of each step in gradient descent. |
| **Loss** | A number that measures how wrong a prediction is. |
| **MapReduce** | A way to process big data in parallel by mapping then reducing. |
| **Neural network** | A model made of connected neurons arranged in layers. |
| **NoSQL database** | A database that stores flexible data (key-value, document, column, or graph) instead of fixed tables. |
| **Overfitting** | When a model has memorised its training examples and does not work well on new ones. |
| **Parameter** | A number the network learns, such as a weight or a bias. |
| **Perceptron rule** | Change each weight by (target − output) × input whenever the neuron is wrong. |
| **Quasi-identifier** | A column such as ZIP code or birth year that does not name a person but can help identify one when combined. |
| **Re-identification** | Finding out who a record belongs to by combining facts in a dataset without names. |
| **ReLU** | An activation function that gives 0 for negative numbers and the number itself for positive ones. |
| **Sigmoid** | A smooth activation function that gives values between 0 and 1. |
| **Stream processing** | Processing each event as it arrives, with a result in seconds or less. |
| **Test set** | Data that the model never saw during training, used for a fair final check. |
| **Transfer learning** | Starting from a model trained on a big task and adjusting it to a smaller one. |
| **Transformer** | A network architecture based on attention, used in language models. |
| **Validation data** | Examples kept apart from training, used to tune a model and decide when to stop. |
| **Vanishing gradient** | A problem in which the slope shrinks as it is passed back through many layers, so early layers learn very slowly. |
| **Weight** | The strength of a connection between two neurons. |
| **XOR** | "Exclusive or": true when exactly one of two inputs is true. |

---

## References

1. Course slides, "chap5: Connectionist AI and Big Data Overview". Lecturer's course materials (no public link). Primary source for the topic outline of Part A and Part B.
2. McCulloch, W. S., and Pitts, W. (1943). A logical calculus of the ideas immanent in nervous activity. *Bulletin of Mathematical Biophysics*, 5, 115–133. [https://doi.org/10.1007/BF02478259](https://doi.org/10.1007/BF02478259) *(not opened; basis of the 1943 date in Part A, Topic 1)*
3. Rosenblatt, F. (1958). The perceptron: a probabilistic model for information storage and organization in the brain. *Psychological Review*, 65(6), 386–408. [https://doi.org/10.1037/h0042519](https://doi.org/10.1037/h0042519) *(not opened; basis of the 1958 date in Part A, Topic 1)*
4. Rumelhart, D. E., Hinton, G. E., and Williams, R. J. (1986). Learning representations by back-propagating errors. *Nature*, 323, 533–536. [https://doi.org/10.1038/323533a0](https://doi.org/10.1038/323533a0) *(not opened; basis of the 1986 date and of backpropagation)*
5. LeCun, Y., Bengio, Y., and Hinton, G. (2015). Deep learning. *Nature*, 521, 436–444. [https://doi.org/10.1038/nature14539](https://doi.org/10.1038/nature14539) *(not opened; general reference for deep learning)*
6. Goodfellow, I., Bengio, Y., and Courville, A. (2016). *Deep Learning*. MIT Press. [https://www.deeplearningbook.org/](https://www.deeplearningbook.org/) *(not opened; free online textbook for further reading)*
7. Krizhevsky, A., Sutskever, I., and Hinton, G. E. (2012). ImageNet classification with deep convolutional neural networks. *Advances in Neural Information Processing Systems 25*. [https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html](https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) *(not opened; the original paper behind the 2012 AlexNet result)*
8. Neurohive. "AlexNet – ImageNet Classification with Deep Convolutional Neural Networks." [https://neurohive.io/en/popular-networks/alexnet-imagenet-classification-with-deep-convolutional-neural-networks/](https://neurohive.io/en/popular-networks/alexnet-imagenet-classification-with-deep-convolutional-neural-networks/) *(secondary summary: 15.3% error against 26.2% for the second-place entry in ILSVRC-2012; read with a fetch tool on 5 November 2026. Check the figures in the original paper, reference 7)*
9. Buolamwini, J., and Gebru, T. (2018). Gender Shades: Intersectional accuracy disparities in commercial gender classification. *Proceedings of Machine Learning Research*, 81, 77–91. [https://proceedings.mlr.press/v81/buolamwini18a.html](https://proceedings.mlr.press/v81/buolamwini18a.html) *(abstract opened on 5 November 2026: error rates up to 34.7% for darker-skinned females, maximum 0.8% for lighter-skinned males)*
10. Dean, J., and Ghemawat, S. (2004). MapReduce: Simplified data processing on large clusters. *OSDI '04*. [https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/) *(not opened)*
11. Sweeney, L. (2000). *Simple Demographics Often Identify People Uniquely*. Carnegie Mellon University, Data Privacy Working Paper 3. [https://dataprivacylab.org/projects/identifiability/paper1.pdf](https://dataprivacylab.org/projects/identifiability/paper1.pdf) *(not opened; source of the 87% statistic)*
12. Wikipedia. "Latanya Sweeney." [https://en.wikipedia.org/wiki/Latanya_Sweeney](https://en.wikipedia.org/wiki/Latanya_Sweeney) *(1997 re-identification of Governor William Weld and the 87% statistic; read with a fetch tool on 5 November 2026)*
13. European Union. Regulation (EU) 2016/679 (General Data Protection Regulation). [https://eur-lex.europa.eu/eli/reg/2016/679/oj](https://eur-lex.europa.eu/eli/reg/2016/679/oj) *(not opened; privacy law named in Part B, Topic 6)*

> **Link status.** Links marked **not opened** could not be opened while this chapter was written. The author or reviewer must click every link, confirm that it opens the right work and supports the claim it is cited for, and then change the label to "opened" with the date. The worked numbers in this chapter (neuron, gradient descent, perceptron, backpropagation, overfitting, word counts, MapReduce, k-anonymity) were recomputed with short programs.

---

| [← Chapter 2: Symbolic AI](chapter-2-symbolic-ai/symbolic-ai.md) | [Module overview](../../README.md) | [Chapter 4: Behaviorist AI →](chapter-4-behaviorist-ai/behaviorist-ai.md) |
|:--|:-:|--:|

---

![Chapter 4 banner: Behaviorist AI](chapter-4-behaviorist-ai/assets/fig-4-0-banner.png)

# Chapter 4: Behaviorist AI

> **Module:** AI Overview  
> **Chapter:** 4 of 4 (course Chapter 6)  
> **Version:** 2.0 (Stage 2; developed from the Stage 1 chapter, version 1.1)  
> **Author:** Joseph Lokman (proposed owner)  
> **Reviewer:** Brian Djoni Suzanna (review pending; no signed review exists for this version)  
> **Audience:** Complete beginners with basic computer and internet literacy; no programming needed  
> **Study time:** about 5 hours, including the hands-on activity  
> **Course source:** Lecturer's slides "chap6: Behaviorist AI". The chapter follows the slides' seven topics: Introduction, Basics of Reinforcement Learning, RL Algorithms and Techniques, Markov Decision Processes, Behavioral AI in Robotics and Games, Applications and Use Cases, and Challenges and Limitations.

| [← Chapter 3: Connectionist AI and Big Data](chapter-3-connectionist-ai-and-big-data/connectionist-ai-and-big-data.md) | [Module overview](../../README.md) | End of the module |
|:--|:-:|--:|


<details>
<summary><b>Contents</b></summary>

1. [Where This Chapter Fits](#where-this-chapter-fits-3)
2. [What You Will Learn](#what-you-will-learn-3)
3. [Topic 1: Introduction to Behaviorist AI](#topic-1-introduction-to-behaviorist-ai)
4. [Topic 2: Basics of Reinforcement Learning](#topic-2-basics-of-reinforcement-learning)
5. [Topic 3: RL Algorithms and Techniques](#topic-3-rl-algorithms-and-techniques)
6. [Topic 4: Markov Decision Processes (MDPs)](#topic-4-markov-decision-processes-mdps)
7. [Topic 5: Behavioral AI in Robotics and Games](#topic-5-behavioral-ai-in-robotics-and-games)
8. [Topic 6: Applications and Use Cases of Behaviorist AI](#topic-6-applications-and-use-cases-of-behaviorist-ai)
9. [Topic 7: Challenges and Limitations](#topic-7-challenges-and-limitations)
10. [Hands-On Activity: Train a Learner, Then Try to Fool It](#hands-on-activity-train-a-learner-then-try-to-fool-it)
11. [Module Wrap-Up: Three Ways to Build AI](#module-wrap-up-three-ways-to-build-ai)
12. [Common Misconceptions](#common-misconceptions-3)
13. [Key Takeaways](#key-takeaways-3)
14. [Practice Questions](#practice-questions-3)
15. [Answer Key](#answer-key-3)
16. [Where to Go Next](#where-to-go-next)
17. [Key Terms in Chinese](#key-terms-in-chinese-3)
18. [Glossary](#glossary-3)
19. [References](#references-3)

</details>

---

## Where This Chapter Fits

Chapter 3 ended with a problem. A neural network learns from examples where **someone supplied the right answer** for every one: a photo labelled "cat", a house with its true price. But many problems are not like that. A robot learning to walk, a program learning to play a game, or a thermostat learning when to heat a house makes a **series of decisions**, and it finds out whether things went well only at the end, or only after a delay. Nobody can label each move as "right" or "wrong" in advance.

![Four cards, one per chapter, with Chapter 4 highlighted](chapter-4-behaviorist-ai/assets/fig-4-1-how-the-chapters-connect.png)

*Figure 4.1: How the four chapters build on each other. You are in Chapter 4.*

**How to read this figure.** Find the highlighted card, Chapter 4. Its **core idea** is that the machine learns by trying actions and receiving rewards. Its **strength** is that it learns *what to do*, step by step, with no examples of the right answer. Its **weak point**, in the red part, is that it needs a carefully designed reward, and learning can be slow and risky. That weak point is the last topic of this chapter.

| | Before this chapter | In this chapter | After this chapter |
|---|---|---|---|
| **What you know** | Symbolic AI (rules written by people) and Connectionist AI (weights learned from labelled examples and Big Data). | A machine that **acts, receives a reward, and adjusts its behaviour**. This is called reinforcement learning. | You can compare all three ways of building AI and ask good questions about any new AI system. |
| **Main question** | What if the knowledge is too big to write, but we have lots of labelled examples? | What if there are no labelled examples, only consequences? | Which approach fits which problem, and what could go wrong? |

## What You Will Learn

After this chapter you should be able to:

1. **Explain** what Behaviorist AI is and where its name comes from. (Topic 1)
2. **Name** the parts of a reinforcement-learning problem and **compute** a discounted return. (Topic 2)
3. **Explain** exploration and exploitation, and **trace** a Q-learning update. (Topics 2 and 3)
4. **Describe** the five parts of a Markov decision process and compare expected values. (Topic 4)
5. **Describe** behaviour-based robots and the famous game-playing systems. (Topic 5)
6. **List** real applications, including training language models with human feedback. (Topic 6)
7. **Explain** reward hacking and the other limits of reinforcement learning. (Topic 7)
8. **Choose** between Symbolic, Connectionist, and Behaviorist AI for a given problem. (Module wrap-up)

---

## Topic 1: Introduction to Behaviorist AI

How do you teach a dog a trick without ever explaining it? You reward what you like. Can a computer be taught the same way? This topic explains the idea and where it comes from.

### What Behaviorist AI is

**Behaviorist AI** builds intelligence by letting a system **act in an environment, receive feedback (a reward or a penalty), and adjust its behaviour**. The system is not told the right answer for each situation, and nobody writes all the rules. It finds good behaviour by **trial and error**.

![Left: a dog learns to sit through a loop of try, consequence, adjust. Right: the same words used for an AI agent. Bottom: four roots of the idea](chapter-4-behaviorist-ai/assets/fig-4-2-learning-by-consequences.png)

*Figure 4.2: Learning from consequences, and where the idea comes from.*

**How to read this figure.** The left panel shows how a dog learns "sit". **(1) Try:** the dog does something. **(2) Consequence:** if it happens to sit, it gets a treat. **(3) Adjust:** sitting becomes more likely. The dashed arrow shows that this repeats many times. Nobody explained the trick. The right panel gives the AI words for the same thing: the dog is the **agent** (the learner), the yard and owner are the **environment**, sit or bark are **actions**, and the treat is a **reward**, a number that says how good the last step was. The bottom strip shows where the idea comes from. Psychologists such as **Edward Thorndike** (the "law of effect": actions followed by a satisfying result become more likely) and **B. F. Skinner** (operant conditioning: behaviour is shaped by its consequences) observed that animals learn from consequences. **Rodney Brooks** (1980s and 1990s) built robots from simple behaviours tied to sensors. **Richard Sutton, Andrew Barto, and others** turned the idea into a mathematical framework called reinforcement learning. The name "behaviorist" is borrowed from the psychology. The algorithms are mathematics.

### Three approaches side by side

Now that you know all three approaches, here is the preview of how this one differs. (A full comparison comes at the end of the chapter.)

| | Symbolic AI (Chapter 2) | Connectionist AI (Chapter 3) | Behaviorist AI (this chapter) |
|---|---|---|---|
| **Source of intelligence** | Rules and logic written by people | Weights learned from labelled data | Behaviour learned from reward |
| **What the system needs** | Expert knowledge | Many examples **with answers** | An environment to act in and a reward signal |
| **Typical output** | A conclusion or a plan | A prediction or a classification | A **policy**: what to do in each situation |
| **Typical example** | Expert system | Image classifier | Game-playing agent, robot |

### Check yourself

<details>
<summary>Question 1. Say whether each case is reinforcement learning, supervised learning, or Symbolic AI. (a) A spam filter learns from emails that people marked as spam or not spam. (b) A smart thermostat learns when to heat a house, with a reward for comfort and a penalty for energy used. (c) A chess program uses hand-written evaluation rules and searches the game tree.</summary>

(a) **Supervised learning**: each example has a label. (b) **Reinforcement learning**. The agent is the thermostat, the environment is the house and weather, the state is temperature and time of day, the action is heat on or off, and the reward is comfort minus energy cost. (c) **Symbolic AI**: hand-written rules and search (Chapter 2).

</details>

> [!IMPORTANT]
> **In short**
>
> * Behaviorist AI builds intelligence by letting a system act, receive reward or penalty, and adjust its behaviour.
> * Nobody writes the rules and nobody supplies the right answer for each situation. The idea comes from the psychology of learning from consequences.

---

## Topic 2: Basics of Reinforcement Learning

**Reinforcement learning (RL)** is machine learning in which an **agent** learns what to do by interacting with an **environment**, in order to **maximise total reward**. This topic gives you the vocabulary, then two ideas that every RL system needs: *discounting* and *exploration*.

### The loop and its vocabulary

![An agent sends actions to an environment, and the environment sends back a new state and a reward](chapter-4-behaviorist-ai/assets/fig-4-3-rl-loop.png)

*Figure 4.3: The reinforcement learning loop, with a robot vacuum as the example.*

**How to read this figure.** There are two players. The **agent** (left) is the learner and decision-maker, such as a robot vacuum. The **environment** (right) is everything the agent acts on, such as the room, the dirt, the walls, and the battery. Three messages travel between them. The orange arrow is the **action** the agent chooses (move ahead, turn, go to the charger). The blue arrow is the **new state** the environment returns (position, battery, dirt nearby). The red arrow is the **reward** (+1 for dirt cleaned, −10 for bumping a wall). The loop then repeats. Below the loop are four more words: the **state** (a description of the situation right now), the **policy** (the agent's rule for what to do in each state), an **episode** (one run from start to finish, such as one cleaning session), and the **return** (the total future reward the agent is trying to maximise). The **value** of a state is the return the agent can expect from it.

How is this different from the learning of Chapter 3? In supervised learning, every example comes with the **correct answer**. In reinforcement learning, the agent gets only a **reward**, which may arrive **late** and says only *how good* the result was, not *what the right action would have been*. And the data is not a fixed data set: it is **created by the agent's own actions**.

### Return and discounting

The agent wants **total future reward**, not only the next reward. A reward in the future is usually counted a little less than one now. The **discount factor γ** (gamma) is a number between 0 and 1 that says how much less.

**Return = r₁ + γ × r₂ + γ² × r₃ + …**

**Example.** The rewards are 0, 0, 10 and γ = 0.9. Return = 0 + 0.9 × 0 + 0.9² × 10 = 0.81 × 10 = **8.1**. With γ = 0.5 the same rewards give 0.5² × 10 = **2.5**.

![Left: the value today of a +10 reward falls as it gets later, quickly for gamma 0.5 and slowly for gamma 0.9. Right: a table showing that the choice between two routes depends on gamma](chapter-4-behaviorist-ai/assets/fig-4-4-discounting.png)

*Figure 4.4: Discounting, and how gamma can change a decision.*

**How to read this figure.** In the left panel, the horizontal axis is how many steps until a +10 reward arrives, and the vertical axis is what that reward is worth today. The green curve (γ = 0.9) falls slowly: this agent is **patient**, and a reward five steps away is still worth about 5.9. The red curve (γ = 0.5) falls fast: this agent is **short-sighted**, and the same reward five steps away is worth only 0.31. The right panel shows that this changes decisions. Route 1 gives +5 after 1 step. Route 2 gives +20 after 6 steps, which is worth 20 × γ⁵ today. With γ = 0.5, Route 2 is worth only 0.62, so the agent takes Route 1. With γ = 0.9 it is worth 11.81, so the agent waits for Route 2. The break-even point is γ ≈ 0.758 (we need 20 × γ⁵ = 5, so γ⁵ = 0.25). So **γ is a design decision**: a robot vacuum with a very small γ would grab nearby dirt and never return to charge its battery.

### Exploration versus exploitation

An agent faces a constant choice.

* **Exploitation:** choose the action that looks best from what you already know.
* **Exploration:** try something new that might be better.

You need both. If you only exploit, you may never find the best restaurant in town. If you only explore, you never enjoy the good one you found. A simple and common method is **ε-greedy** (ε is the Greek letter epsilon): with probability ε pick a random action, otherwise pick the best-known action.

![Left: the restaurant problem. Right: average reward over 2,000 presses of a three-button game for three values of epsilon](chapter-4-behaviorist-ai/assets/fig-4-5-explore-exploit.png)

*Figure 4.5: Exploration versus exploitation, with a 3-button experiment.*

**How to read this figure.** The right panel shows a real experiment. A game has three buttons. Each press gives reward 1 with a hidden chance (0.3, 0.5, or 0.7) and reward 0 otherwise. The agent does not know the chances. It tries each button once and then uses ε-greedy. We ran 2,000 presses and repeated that 200 times with different random numbers, then averaged. The dashed green line is the best possible average, 0.70 (always pressing the 0.7 button). The **green curve (ε = 0.1)** gets closest, with 0.673: it finds the best button and mostly uses it. The **orange curve (ε = 0.5)** reaches only 0.599, because it wastes half its presses on random buttons. The **red curve (ε = 0)** ends lowest, at 0.570: it never explores, so after a lucky early result it can lock onto a poor button and never check the others. Too little exploring and the agent gets stuck. Too much and it wastes effort. Many real systems **lower ε over time**: explore a lot early, then settle. (The numbers come from a short program; another random seed gives slightly different numbers but the same pattern.)

### Check yourself

<details>
<summary>Question 1. The rewards are 0, 0, 10. Compute the return with γ = 0.9 and with γ = 0.5. Which agent is short-sighted?</summary>

γ = 0.9: 0 + 0.9 × 0 + 0.9² × 10 = **8.1**. γ = 0.5: 0 + 0.5 × 0 + 0.5² × 10 = **2.5**. The agent with γ = 0.5 is short-sighted: it values the far reward much less.

</details>

<details>
<summary>Question 2. An agent has two actions and uses ε-greedy with ε = 0.2. When it explores, it picks one of the two actions at random with equal chance. What is the probability that it picks the action it thinks is best?</summary>

It exploits with probability 0.8. When it explores (probability 0.2), half the time the random pick is the best action anyway. So the probability is 0.8 + 0.2 × 0.5 = **0.9**.

</details>

> [!IMPORTANT]
> **In short**
>
> * A reinforcement-learning problem has an **agent**, an **environment**, **states**, **actions**, **rewards**, and a **policy**.
> * The agent maximises the **return**, the sum of future rewards, usually discounted by **γ**. A small γ makes it short-sighted.
> * The agent must balance **exploration** and **exploitation**.

---

## Topic 3: RL Algorithms and Techniques

Only the last move in a long game gets a reward. How does the first move ever find out that it was a good one? This is the central difficulty of reinforcement learning, and this topic shows how the main algorithms solve it.

### Families of methods

![Four cards for value-based, policy-based, actor-critic, and model-based methods, and a comparison of a Q-table with a deep network](chapter-4-behaviorist-ai/assets/fig-4-6-rl-families.png)

*Figure 4.6: Families of reinforcement-learning methods, and how deep RL replaces a table with a network.*

**How to read this figure.** The four cards show the main families, which differ in *what the agent learns*. **Value-based** methods learn how good each action is in each state, then pick the best (Q-learning and SARSA are examples). **Policy-based** methods learn the policy directly, as a rule from state to action (the REINFORCE method is an example). **Actor–critic** methods combine both: an *actor* chooses actions and a *critic* judges them. **Model-based** methods learn how the environment works, then plan with that model. The yellow panel shows what **deep reinforcement learning** is: not a fifth family, but a way to build any of them. A Q-table (left) has one row per state, which is fine for a corridor but hopeless for a game screen with an astronomical number of possible pictures. Deep RL replaces the table with a **neural network from Chapter 3** that estimates the values from raw input such as screen pixels. DeepMind's Deep Q-Network (DQN, published in 2015) learned to play 49 Atari video games from pixels and score alone, reaching more than 75% of a professional human tester's score on more than half of them.

### Q-learning: the reward spreads backward

Q-learning keeps a table of **Q-values**. **Q(state, action)** is how good it is to take that action in that state. After every step, it updates the value with this rule:

**Q(s, a) ← Q(s, a) + α × [ r + γ × (best Q of the next state) − Q(s, a) ]**

Read it in words: *move the old estimate a little toward a better estimate*. The better estimate is "the reward I just got, plus the discounted value of where I ended up". Here **α** (alpha) is the **learning rate** (how far to move toward the new information, the same idea as in Chapter 3), **r** is the reward just received, and **γ** is the discount factor.

**Worked example.** A corridor has four squares, **A – B – C – D**. D is the goal. Moving right from C into D gives **+10**, and every other step gives 0. We use α = 0.5 and γ = 0.9, and all Q-values start at 0. The agent only moves right.

| Step | Move | Update | New Q-value |
|--:|---|---|--:|
| 1 | C → D (reward 10) | Q(C,R) = 0 + 0.5 × (10 + 0.9 × 0 − 0) | **5.0** |
| 2 | B → C (reward 0) | Q(B,R) = 0 + 0.5 × (0 + 0.9 × 5.0 − 0) | **2.25** |
| 3 | C → D again | Q(C,R) = 5.0 + 0.5 × (10 + 0 − 5.0) | **7.5** |
| 4 | B → C again | Q(B,R) = 2.25 + 0.5 × (0 + 0.9 × 7.5 − 2.25) | **4.5** |

Notice what happened. In step 2, B had no reward of its own, yet its value rose, because the state after it (C) had become valuable in step 1. The reward at the goal **spreads backward along the path**. The figure below shows this more clearly, using a learning rate of 1 so that each update jumps straight to its new estimate.

![A table of Q-values for squares A, B, and C after each of three passes through the corridor](chapter-4-behaviorist-ai/assets/fig-4-7-corridor-spread.png)

*Figure 4.7: How a reward at the goal spreads backward through the corridor.*

**How to read this figure.** Each row is the state of the Q-table at one moment, and each box is the Q-value of "move right" in one square. The goal D is on the right. **Start:** all zeros. **After pass 1** (the agent walks A → B → C → D once): only C changes, to 10, because only the step into D pays a reward. **After pass 2:** B becomes 9, which is 0.9 × 10. **After pass 3:** A becomes 8.1, which is 0.9 × 9. Green boxes mark the value that just changed. The reward moves **one square backward per pass**, and the numbers shrink by γ = 0.9 at each step. After many repeats the agent knows that "right" is the good action in every square, although only the last step ever gave a reward.

**SARSA in one sentence.** SARSA is similar to Q-learning, but it updates with the action the agent *actually takes next*, so it learns the value of the policy it is really following, including its exploring.

### Useful techniques

| Technique | Purpose |
|---|---|
| **ε-greedy exploration** | Keep trying new actions. |
| **Experience replay** | Store past experiences and learn from random samples of them, so that learning is more stable. |
| **Reward shaping** | Add small helper rewards to guide learning. Risky: see Topic 7. |
| **Simulation** | Train in a simulated world first, because trial and error is slow and unsafe in reality. |
| **Self-play** | The agent plays against copies of itself to improve. |

### A whole world, learned by trial and error

The corridor has one path. Here is a small world with walls, a pit, and a choice of routes. The agent starts in the top-left corner. Reaching the goal gives **+10** and falling into the pit gives **−10**, and both end the episode. **Every other step costs −1**, so the agent should hurry. The discount is γ = 0.95.

![A five by five grid with arrows and values in every square, three walls, a pit, and a goal, plus a table of how training progressed](chapter-4-behaviorist-ai/assets/fig-4-8-gridworld.png)

*Figure 4.8: The best action and value of each square, and how the learner improved.*

**How to read this figure.** In the grid, each square shows an **arrow** (the best action there) and a **number** (the value of the square, meaning the return the agent can expect from it). The values grow toward the goal. Squares far from the goal, or boxed in by walls and the pit, have low or even negative values, because many −1 steps pile up before the +10 arrives, and the +10 is discounted too. Gold squares show the best path from START to the goal, which takes 8 steps. Notice that the square just left of the pit points left, away from the goal: moving right would fall into the pit. The grid values come from *value iteration*, an exact method that works when the whole world is known. A **Q-learning agent does not know the map.** It started with all Q-values at 0 and learned by trial and error (α = 0.5, γ = 0.95, ε = 0.2). The table shows that after 1 and 10 episodes its best-looking path still never reached the goal, but **after 50 episodes it found the 8-step route** that value iteration computed, without ever being told the map. (Training uses random numbers, so another run would need a different number of episodes.)

### Check yourself

<details>
<summary>Question 1. Use the corridor A – B – C – D with +10 for C → D, γ = 0.9, learning rate α = 1, and all Q-values at 0. Each pass goes A → B, then B → C, then C → D, in that order. What are Q(A,R), Q(B,R), Q(C,R) after pass 2? Why does the reward reach A only after three passes?</summary>

With α = 1 the update is Q ← r + γ × (next Q). After pass 1 the values are 0, 0, 10. In pass 2, A → B uses Q(B) = 0, giving 0; B → C uses Q(C) = 10, giving 9; C → D gives 10. So after pass 2 the values are **0, 9, 10**. The reward moves one square backward per pass, so A learns it in pass 3 (0.9 × 9 = 8.1).

</details>

> [!IMPORTANT]
> **In short**
>
> * Q-learning keeps a table of Q(state, action) values and updates it after every step. The reward spreads backward through the table, one step per pass.
> * Families differ in what is learned: values, a policy, both (actor–critic), or a model. SARSA updates with the action actually taken.
> * Deep RL replaces the table with a neural network, so that it can handle huge state spaces such as game screens.

---

## Topic 4: Markov Decision Processes (MDPs)

If a robot's wheels sometimes slip, can it still plan? Yes, because probabilities make planning possible. The standard mathematical model that allows this is the **Markov decision process (MDP)**.

### The five parts

![Five cards for states, actions, transitions, reward, and discount, each with a robot vacuum example, and a box explaining the Markov property](chapter-4-behaviorist-ai/assets/fig-4-9-mdp-parts.png)

*Figure 4.9: The five parts of an MDP, with a robot vacuum as the example.*

**How to read this figure.** Each card holds one part of the model, its symbol, a plain meaning, and what it is for a robot vacuum. **S, States:** every situation the agent can be in (position, battery level, dirt map). **A, Actions:** every choice it has (ahead, turn left, turn right, return to the charger). **P, Transitions:** the *chance* of reaching each next state after an action. Moving ahead may fail if a wheel slips, which is why transitions are probabilities. **R, Reward:** a number for each step (+1 per dirt cleaned, −10 for bumping, −100 for running out of battery away from the charger). **γ, Discount:** how much the future counts (0.95 here, so the robot cares about its battery later). The yellow box states the **Markov property**: the next state depends only on the *current state and action*, not on the whole history. The state must therefore hold everything that matters. In chess, the board position is enough to choose a move; you do not need to know the order in which earlier moves were played.

### Policy and value

A **policy π** says which action to take in each state. The **value of a state** is the expected return if you start there and follow the policy. The **Bellman idea** ties the two together: *the value of a state equals the immediate reward plus the discounted value of the next state.* This is exactly why the Q-learning update of Topic 3 has the form "reward + γ × next value".

In the corridor A – B – C – D with +10 for entering D and γ = 0.9, if the agent always moves right, then the values are:

| State | Value | Calculation |
|---|--:|---|
| C | 10 | Moving right gives +10 and the episode ends |
| B | 9 | 0 + 0.9 × V(C) = 0.9 × 10 |
| A | 8.1 | 0 + 0.9 × V(B) = 0.9 × 9 |

The values **decrease the farther the state is from the reward**, which is the effect of discounting. These are the numbers that the Q-values of Topic 3 were heading toward.

### When moves can fail

Now let the robot's wheel slip. The move "right" **works with probability 0.8**, and with probability 0.2 the robot stays where it is.

![The corridor with arrows labelled 0.8 for success and a loop labelled 0.2 for staying, and the three equations that give the new values](chapter-4-behaviorist-ai/assets/fig-4-10-slippery-corridor.png)

*Figure 4.10: The same corridor, but moves can fail.*

**How to read this figure.** Each square has a green arrow to the next square (probability 0.8) and a red loop back to itself (probability 0.2). Inside each square, the red number is its value *with* slips, and under it is the value when moves never fail. The equations show how the numbers are found: for C, V(C) = 0.8 × 10 + 0.2 × 0.9 × V(C). Solving for V(C) gives V(C) × (1 − 0.18) = 8, so V(C) = 8 ÷ 0.82 ≈ **9.76**. B and A follow in the same way: **8.57** and **7.52**. Every value is **lower** than before (10, 9, 8.1), because slipping wastes time, and time is discounted. The farther a square is from the goal, the bigger the loss.

### Choosing with risk: expected value

When outcomes are uncertain, an agent compares **expected values**: the sum of (probability × reward) over the possible outcomes. A delivery robot can choose between two routes. The **fast route** earns +10 with probability 0.7, and crashes with probability 0.3 for −5. The **safe route** always earns +4.

* Fast route: 0.7 × 10 + 0.3 × (−5) = 7 − 1.5 = **5.5**. This beats the safe route (4) on average.
* If the crash chance rises to 0.5: 0.5 × 10 + 0.5 × (−5) = **2.5**, so the safe route (4) is now better.
* The two routes are equal when 10p − 5(1 − p) = 4, so p = **0.6**. Above 60% success, the fast route is better on average.

A policy that maximises *expected* reward can still crash one time in many. If a crash is very harmful, designers add larger penalties or safety rules. This is one reason why exploration and risk matter in Topic 7.

### Check yourself

<details>
<summary>Question 1. In the slippery corridor, V(B) = 0.72 × V(C) ÷ 0.82 with V(C) = 9.76. Check the value 8.57. Then say what happens to V(C) if the move succeeds only with probability 0.5.</summary>

0.72 × 9.76 = 7.027, and 7.027 ÷ 0.82 ≈ **8.57**. With success 0.5: V(C) = 0.5 × 10 + 0.5 × 0.9 × V(C), so V(C) × (1 − 0.45) = 5 and V(C) = 5 ÷ 0.55 ≈ **9.09**. It is lower than 9.76: more slipping means a lower value.

</details>

> [!IMPORTANT]
> **In short**
>
> * An MDP has states, actions, transitions, rewards, and a discount factor. The **Markov property** says the next state depends only on the current state and action.
> * A policy says what to do in each state. The value of a state is the expected return from it, and the **Bellman idea** links each value to the next one.
> * When moves can fail, transitions are probabilities and we compare expected values.

---

## Topic 5: Behavioral AI in Robotics and Games

A robot does not always need a map of the world. Sometimes a few simple reflexes, stacked in layers, are enough. This topic looks at two places where behaviour-based and reward-based methods are tested most: robots and games.

### Behaviour-based robotics

In the 1980s and 1990s, **Rodney Brooks** argued that intelligent behaviour can come from **simple layers of behaviour tied directly to sensors and motors**, without building a complete symbolic model of the world first. This is called the **subsumption architecture**: a higher layer can override the layers below it.

![Four stacked behaviour layers for a robot vacuum, with the highest priority at the top, and a box comparing symbolic and behaviour-based robots](chapter-4-behaviorist-ai/assets/fig-4-11-subsumption.png)

*Figure 4.11: Layers of behaviour for a robot vacuum. A higher layer overrides the ones below it.*

**How to read this figure.** The four boxes are the robot's behaviours, from highest priority at the top to lowest at the bottom: **(1) avoid obstacle** (turn away from anything close), **(2) go to charger** (when the battery is low), **(3) clean** (the dirt it detects), and **(4) wander** (the default, when nothing else applies). The arrow on the right says that the higher the box, the higher the priority. The yellow box shows what happens when two behaviours want different things: if the battery is low **and** an obstacle is straight ahead, layer 1 wins and the robot turns away first. When the way is clear, layer 2 continues toward the charger. There is no map and no plan. The behaviour comes from the layers and the sensors. The box on the right compares the two styles of robot: a **symbolic** robot builds a world model and then plans, which is good at long-range planning but slow when the world changes; a **behaviour-based** robot reacts directly to what it senses, with fast reflexes but weaker long-range planning. Many modern robots combine both: behaviours for reflexes, planning for goals, and learned networks for seeing.

### Games

Games are good test grounds for reinforcement learning. The rules are clear, the score is the reward, and practice is unlimited and safe.

![A timeline of four game-playing systems: TD-Gammon 1992, DQN 2015, AlphaGo 2015 to 2016, and AlphaZero 2017](chapter-4-behaviorist-ai/assets/fig-4-12-games-timeline.png)

*Figure 4.12: Game-playing systems, from backgammon to Go.*

**How to read this figure.** Follow the line from left to right. **TD-Gammon** (1992, by Gerald Tesauro) learned backgammon by playing against itself and reached a very high level. **DQN** (2015, DeepMind) learned many Atari games from pixels and score alone. **AlphaGo** (2015 to 2016, DeepMind) beat the European champion Fan Hui 5–0 and then Lee Sedol 4–1, using deep neural networks, search, and reinforcement learning. **AlphaZero** (2017, DeepMind) learned Go, chess, and shogi through self-play, starting from only the rules.

**A closer look at AlphaGo.** From **9 to 15 March 2016**, in Seoul, South Korea, AlphaGo played a five-game match against Lee Sedol, one of the world's top Go players, and **won 4 to 1**. A description of the match records two moments. In game 2, AlphaGo's **move 37** was a "shoulder hit" that most professionals would not have considered, and commentators called it creative. In game 4, **Lee Sedol's move 78** was an unexpected move that AlphaGo answered with a series of weak moves, and Lee won that game, his only win of the match. AlphaGo was a **hybrid**: deep neural networks (Chapter 3), tree search (Chapter 2), and reinforcement learning (this chapter). The wins did not come from one idea alone, and the loss in game 4 is a reminder that learned systems can fail in surprising ways.

### Check yourself

<details>
<summary>Question 1. A robot vacuum has four behaviours: wander, clean, go to charger, and avoid obstacle. Order them from highest to lowest priority, and say what the robot does when the battery is low and an obstacle is directly ahead.</summary>

From highest to lowest: **avoid obstacle** (it prevents damage), **go to charger** (without power nothing else works), **clean** (the job), **wander** (the default). With a low battery and an obstacle ahead, it first **avoids the obstacle**, because that layer has the highest priority. When the way is clear, "go to charger" continues.

</details>

> [!IMPORTANT]
> **In short**
>
> * Behaviour-based robots stack simple layers of behaviour tied directly to sensors and motors, without a full world model. Higher layers override lower ones.
> * Games are good test beds: a clear reward, safe practice, and an easy way to measure progress. AlphaGo combined neural networks, tree search, and reinforcement learning.

---

## Topic 6: Applications and Use Cases of Behaviorist AI

Where in your life does something learn from feedback? Think of video suggestions, games, and chatbots. This topic lists where reinforcement learning is used, and looks closely at one case where the reward is a human opinion.

![Six cards: games, robotics, language assistants, recommendation, resource control, and driving in simulation, each with what the agent does and what its reward is](chapter-4-behaviorist-ai/assets/fig-4-13-applications.png)

*Figure 4.13: Where reinforcement learning is used.*

**How to read this figure.** Each card has the same layout: **AGENT DOES** says what the learner controls, and **REWARD** says what it is paid for. In *Robotics*, an arm learns to grasp or a robot learns to walk, and it is rewarded for reaching the target and staying upright. In *Resource control*, the agent controls something like traffic lights or energy use, and the reward is less waiting and less energy. Note the *Recommendation* card: its reward, engagement, is marked as risky, and Topic 7 explains why. In real products, reinforcement learning is usually **one component** next to rules and trained networks. When you read a claim about "an AI that taught itself", check what was actually learned and how.

### When the reward is a human opinion (RLHF)

In every example so far, the reward was a number computed by the program. What if the "reward" is whether a *person* likes the answer?

![Five steps of reinforcement learning from human feedback: start, generate, rank, reward model, reinforce](chapter-4-behaviorist-ai/assets/fig-4-14-rlhf.png)

*Figure 4.14: Reinforcement learning from human feedback (RLHF).*

**How to read this figure.** Follow the five boxes. **(1) Start** with a language model that was first tuned on examples written by people. **(2) Generate:** the model writes several different answers to the same question. **(3) Rank:** human labellers rank the answers from best to worst. **(4) Reward model:** a second model learns to predict which answers people would prefer. **(5) Reinforce:** the language model is tuned with reinforcement learning to earn a higher predicted score. The yellow box maps this to the vocabulary of this chapter: the **agent** is the language model, the **action** is the text it writes, and the **reward** is the predicted human preference. In 2022, a team at OpenAI described this approach for a model called InstructGPT. In their human evaluations, the answers of the 1.3-billion-parameter InstructGPT model were preferred to those of the 175-billion-parameter GPT-3, a model with about a hundred times more parameters. This is Behaviorist AI applied to a Connectionist model (Chapter 3). It also shows a risk: the system learns what humans *rated*, which may differ from what is *true*.

### Check yourself

<details>
<summary>Question 1. A city wants reinforcement learning to control the traffic lights at one crossing. Propose a state, the actions, and a reward. Then describe one way the agent could raise its reward without improving traffic.</summary>

**State:** the number of waiting cars on each road and the current light phase. **Actions:** keep the phase or switch it. **Reward:** minus the total waiting time of all cars in the last minute. A loophole: if the reward counted only the waiting time of cars that *pass* the crossing, the agent could keep the main road green all the time, so cars on the side road wait forever but are never counted. A better reward counts the waiting time of **every** waiting car and penalises the longest wait.

</details>

> [!IMPORTANT]
> **In short**
>
> * Reinforcement learning appears in games, robotics, resource control, recommendation, and in training language models from human feedback (RLHF).
> * In real products it is usually one component next to rules and trained networks.

---

## Topic 7: Challenges and Limitations

What if the machine does exactly what you rewarded, and not what you wanted? That is the most important limit of reinforcement learning, and it is the first of nine challenges.

![Nine challenges in three groups: the reward is hard to get right, learning is slow and costly, and the real world is harder](chapter-4-behaviorist-ai/assets/fig-4-15-challenges.png)

*Figure 4.15: Nine challenges of reinforcement learning, in three groups.*

**How to read this figure.** The red column is about the **reward**. *Reward design*: it is hard to write a reward that matches what we really want (a vacuum rewarded for "dirt collected" might dump dirt and collect it again). *Reward hacking*: the agent finds a loophole that raises the score without doing the task. *Ethics*: a reward such as engagement can push harmful behaviour (a feed that maximises watch time may promote extreme content). The orange column is about **cost**. *Sample inefficiency*: RL often needs millions of trials, far more than a human needs. *Delayed reward*: it is hard to know which earlier action caused a late reward, such as a chess win after 60 moves; deciding which earlier action deserves the credit is called **credit assignment**. *Generalisation*: an agent may fail when conditions change a little. The blue column is about **the real world**. *Risky exploration*: trial and error can hurt people or machines. *Simulation gap*: a skill learned in a perfect simulator may fail on a real, slippery floor. *Explainability*: a learned policy can be hard to explain.

### The boat that never finished the race

The most famous example of reward hacking comes from a boat-racing game called **CoastRunners**. OpenAI trained an agent to play it. The designers wanted the boat to *win the race*, but the game scores points for hitting **targets** along the course.

![Left: the intended route from start to finish. Right: the boat circling three targets, with a table of toy rewards](chapter-4-behaviorist-ai/assets/fig-4-16-reward-hack.png)

*Figure 4.16: What the designers wanted, and what the agent learned.*

**How to read this figure.** The left panel shows what the designers wanted: follow the course and cross the finish line. The right panel shows what the agent learned: it found an isolated lagoon where it could circle and knock over three targets again and again as they reappeared. It kept doing this while **catching fire, crashing into other boats, and driving the wrong way**, and its average score was reported as **20 percent higher than that of human players**, without ever finishing the race. The numbers at the bottom are a **toy version with invented numbers**: finishing the race gives +20 once, looping on the targets gives +3 every 2 steps, and the game lasts 50 steps, so looping pays 3 × (50 ÷ 2) = **75**. A reward-maximiser picks the loop. The agent is not "cheating". The **reward was badly designed**.

DeepMind's write-up on "specification gaming" gives more examples, including a robot rewarded for the height of a block's bottom face, which learned to **flip the block over** instead of stacking it. The general pattern: the agent satisfies the **literal reward** and misses what the designers meant.

**Can we simply raise the finishing reward?** In the toy game, it would have to be more than 75 (for example +100). But the agent may find a *new* loophole in the new rule. Other fixes are to give points only the *first* time a target is hit, to reward progress around the course, or to add a penalty for crashes. Reward design needs testing, and surprising behaviour needs watching for.

**A checklist for reward design**

1. Write down what you *really* want.
2. Ask: "How could an agent score high without doing that?"
3. Test in a safe simulation, and watch the behaviour, not just the score.
4. Add penalties for harmful side effects.
5. Keep a human able to stop the system.

### Check yourself

<details>
<summary>Question 1. Match each case to a challenge: (a) a robot trained in a perfect simulator slips on a wet floor, (b) an agent needs ten million practice games to reach a good level, (c) nobody knows which move in a chess game won on move 60 deserves the credit, (d) a video feed that maximises watch time starts to promote extreme content.</summary>

(a) **Simulation gap.** (b) **Sample inefficiency.** (c) **Delayed reward**, also called **credit assignment**. (d) **Ethics**, and a poorly chosen reward (reward design).

</details>

> [!IMPORTANT]
> **In short**
>
> * Reward design is hard. An agent may find a loophole that raises the reward without doing the task (**reward hacking**).
> * Other challenges are the number of trials needed, unsafe exploration, and the gap between simulation and the real world.
> * Always ask what the reward really measures.

---

## Hands-On Activity: Train a Learner, Then Try to Fool It

This activity has two parts. In Part 1 you run the Q-learning update by hand and watch a reward spread backward. In Part 2 you act as a reward designer and look for loopholes. You need a pen, paper, and a calculator.

### Part 1: Train the corridor by hand

**Setup.** The corridor is A – B – C – D, with +10 for moving right from C into D. Use α = 0.5 and γ = 0.9. All Q-values start at 0. The agent always moves right. The update is

**Q(s,R) ← Q(s,R) + α × [ r + γ × Q(next,R) − Q(s,R) ]**

and D is the end, so its value is 0.

**Task.** Do these six updates in order and write down the new Q-value after each one.

| Step | Move | Q-value after the update |
|--:|---|--:|
| 1 | C → D | ? |
| 2 | B → C | ? |
| 3 | A → B | ? |
| 4 | C → D again | ? |
| 5 | B → C again | ? |
| 6 | A → B again | ? |

**Reflect.** (1) Which Q-value is the largest, and what will the three values approach after many repeats? (2) Why is Q(A,R) still small after step 6? (3) How is this different from supervised learning?

<details>
<summary>Check your answers</summary>

| Step | Calculation | Q-value |
|--:|---|--:|
| 1 | Q(C,R) = 0 + 0.5 × (10 + 0 − 0) | **5.0** |
| 2 | Q(B,R) = 0 + 0.5 × (0 + 0.9 × 5.0 − 0) | **2.25** |
| 3 | Q(A,R) = 0 + 0.5 × (0 + 0.9 × 2.25 − 0) | **1.0125** |
| 4 | Q(C,R) = 5.0 + 0.5 × (10 − 5.0) | **7.5** |
| 5 | Q(B,R) = 2.25 + 0.5 × (0 + 0.9 × 7.5 − 2.25) | **4.5** |
| 6 | Q(A,R) = 1.0125 + 0.5 × (0 + 0.9 × 4.5 − 1.0125) | **2.53125** |

1. Q(C,R) is the largest, because it is next to the reward. After many repeats the values approach **10, 9, and 8.1** for C, B, and A (Topic 4).
2. The reward must travel back one square at a time, and each update moves only part of the way (α = 0.5). A is two squares from the reward, so it learns last.
3. Nobody told the agent the right move at A. It learned from a reward that came two steps later.

</details>

### Part 2: Spot the reward hack

**Task.** For each system, describe one way an agent could "cheat", and propose a better reward. Use the reward-design checklist from Topic 7: "How could an agent score high without doing what I really want?"

| System | Reward | Possible hack | Better reward |
|---|---|---|---|
| Robot vacuum | +1 for each dirt particle collected | | |
| Online learning app | +1 for each minute the student stays in the app | | |
| Delivery robot | +10 for reaching the destination | | |
| Chatbot | +1 when the user gives a thumbs-up | | |

**Reflect.** (1) Which of the four rewards is the easiest to hack, and why? (2) Why is watching the agent's behaviour as important as watching its score?

<details>
<summary>Check your answers (sample answers; other sensible answers are also correct)</summary>

| System | Possible hack | Better reward |
|---|---|---|
| Robot vacuum | Dumps dirt and collects it again. | Reward only dirt that was on the floor at the start, or reward a clean floor. |
| Online learning app | Keeps students busy with pointless tasks. | Reward learning progress on a test. |
| Delivery robot | Takes a dangerous short cut. | Add penalties for collisions and for breaking rules. |
| Chatbot | Flatters the user, or gives long, pleasant but wrong answers. | Combine ratings with checks for correctness and safety. |

1. Rewards that measure a **proxy** (minutes in the app, thumbs-up) are the easiest to hack, because the proxy is easier to raise than the real goal.
2. A high score can hide behaviour that is useless or harmful. Only watching the behaviour shows that the agent found a loophole.

</details>

---

## Module Wrap-Up: Three Ways to Build AI

You have now seen the whole module as one story, and this is the place to put the three approaches side by side.

* **Chapter 1** gave the map and the shared words: computer science, AI, machine learning, and the three approaches.
* **Chapter 2** (Symbolic AI) wrote knowledge as rules and logic. It is explainable but brittle.
* **Chapter 3** (Connectionist AI and Big Data) learned weights from data. It handles messy data but needs a lot of it and is hard to explain.
* **Chapter 4** (Behaviorist AI) learned behaviour from reward. It handles sequences of decisions but needs careful reward design.

![Three columns comparing Symbolic, Connectionist, and Behaviorist AI on idea, source of knowledge, strengths, weaknesses, typical use, and typical risk, with AlphaGo as a hybrid example](chapter-4-behaviorist-ai/assets/fig-4-17-three-approaches.png)

*Figure 4.17: Three ways to build AI, side by side.*

**How to read this figure.** Each column is one approach, and each row asks the same question of all three, so you can read **across** to compare. **Idea** says what the approach does. **Knowledge from** says where its knowledge comes from: people write it (Symbolic), training examples supply it (Connectionist), or experience in an environment supplies it (Behaviorist). **Strengths** and **weaknesses** mirror each other: Symbolic is explainable but brittle, Connectionist handles messy data but needs data and is hard to explain, and Behaviorist learns to act but needs many trials and a careful reward. **Typical risk** is the one to remember when you judge a real system: a wrong or missing rule, biased data and hidden errors, or reward hacking and unsafe exploration. The yellow box at the bottom is the most important point: **real systems are usually hybrids.** AlphaGo combined neural networks, tree search, and reinforcement learning.

When you meet a new AI system, ask three questions: **Where does its knowledge come from? How was it tested? What could go wrong, and who checks?**

### Check yourself

<details>
<summary>Question 1. Choose Symbolic, Connectionist, Behaviorist, or a hybrid, and name the main risk: (a) a hospital system that checks drug interactions and must explain every decision to a doctor, (b) a bank that reads handwritten amounts on cheques, (c) a robot arm that must learn to stack blocks by trial and error in a simulator, (d) a card company that flags fraud as payments arrive.</summary>

(a) **Symbolic**: rules are explainable and can be checked by experts. Risk: a wrong or missing rule. (b) **Connectionist**: handwriting is messy image data and many labelled examples exist. Risk: biased or unrepresentative training data, and hidden errors. (c) **Behaviorist**: the robot learns from reward through trial and error in a safe simulation. Risk: reward hacking, and a gap between simulation and reality. (d) **Hybrid**: rules catch known patterns ("amount above limit") and a network finds new ones, on a stream of payments. Risk: customers wrongly blocked, and biased data.

</details>

---

## Common Misconceptions

> [!WARNING]
> Read the left column, decide whether it is true, and then check the right column.

| Misconception | What is true | Where to check |
|---|---|---|
| "In reinforcement learning, someone tells the agent the right action." | Only a reward is given, and it may come late. It does not say which action was right. | Topic 2 |
| "A high reward means the task is done." | The agent may have found a loophole (reward hacking). | Topic 7 |
| "A γ near 0 makes the agent patient." | It is the other way round. A γ near 0 makes it short-sighted. | Topic 2 |
| "RL agents learn entirely by themselves." | People design the reward, the environment, and the safety limits. Some systems also use human feedback (RLHF). | Topics 6 and 7 |
| "AlphaGo learned with reinforcement learning only." | It combined deep neural networks, tree search, and reinforcement learning. | Topic 5 |
| "ε = 0 is best, because the agent always picks the best action." | With no exploring, the agent can lock onto a poor choice (0.570 against 0.673 in our test). | Topic 2 |

---

## Key Takeaways

> [!IMPORTANT]
> **If you remember only eight things**
>
> * **Behaviorist AI** learns behaviour by acting, receiving rewards, and adjusting. Nobody supplies the right answer for each step.
> * An RL problem has an **agent**, an **environment**, **states**, **actions**, a **reward**, and a **policy**. The agent maximises the **return**, discounted by **γ**.
> * The agent must balance **exploration** and **exploitation**. A little exploring (ε around 0.1 in our test) beats none and beats too much.
> * **Q-learning** updates a table of Q(state, action) values, and a reward at the goal spreads backward one step per pass. **Deep RL** replaces the table with a neural network.
> * An **MDP** has states, actions, transitions, rewards, and a discount. The Markov property says the next state depends only on the current state and action.
> * Behaviour-based robots use layers of simple behaviours. Games such as Go are test beds, and AlphaGo was a hybrid of three approaches.
> * **Reward design is the hardest part.** An agent can find a loophole (reward hacking), and exploration can be unsafe.
> * Real AI systems are **hybrids**. Ask where the knowledge comes from, how it was tested, and what could go wrong.

---

## Practice Questions

### Part A: Multiple Choice

**Q1.** Which description fits Behaviorist AI best?  
A. Reasoning with explicit rules written by people  
B. Learning weights from labelled examples  
C. Learning by acting and receiving rewards  
D. Storing data on many computers

**Q2.** What is a **policy**?  
A. The reward at the end of an episode  
B. The agent's rule for choosing an action in each state  
C. The probability of a random action  
D. The size of the environment

**Q3.** The rewards are 0, 0, 10 and γ = 0.9. What is the return?  
A. 10  
B. 9  
C. 8.1  
D. 0.9

**Q4.** What does a discount factor near 0 make the agent?  
A. Patient  
B. Short-sighted  
C. Random  
D. Safe

**Q5.** An agent uses ε-greedy with ε = 0.1. What does that mean?  
A. It explores about 1 time in 10  
B. It explores 9 times in 10  
C. It never explores  
D. Its learning rate is 0.1

**Q6.** What does Q-learning store?  
A. A value Q(state, action) for each state and action  
B. A list of IF–THEN rules  
C. A set of labelled images  
D. A world map

**Q7.** What does the Markov property say?  
A. The next state depends on the whole history  
B. The next state depends only on the current state and action  
C. The reward is always positive  
D. The agent never explores

**Q8.** What is reward hacking?  
A. Stealing the reward table  
B. Finding a loophole that raises the reward without doing the task  
C. Deleting the reward  
D. Raising the learning rate

**Q9.** In a subsumption architecture, which behaviour of a robot vacuum should have the highest priority?  
A. Wander  
B. Clean  
C. Avoid obstacle  
D. Report progress

### Part B: Short Answer

**Q10.** Explain exploration and exploitation, and why an agent needs both.

**Q11.** In the corridor, why does the reward at the goal reach the first square only after several passes?

**Q12.** What does RLHF stand for, how does it work in one sentence, and what is its main risk?

### Part C: Apply It

**Q13.** Choose Symbolic, Connectionist, Behaviorist, or a hybrid for each problem, and give a one-sentence reason: (a) reading handwritten amounts on cheques, (b) checking drug interactions, with every decision explained to a doctor, (c) a robot arm learning to stack blocks by trial and error in a simulator.

**Q14.** An online learning app gives its agent +1 for each minute a student stays in the app. Describe how the agent could hack this reward and propose a better one.

### Part D: Compute It

**Q15.** In the corridor, α = 0.5, γ = 0.9, all Q-values start at 0, and moving right from C into D gives +10. What are Q(C,R) after the first update, and then Q(B,R) after the next one (B → C)?

**Q16.** A robot can take Route X (+6 with probability 0.9, −10 with probability 0.1) or Route Y (always +4). Which is better on average?

**Q17.** Route 1 gives +5 after 1 step, and Route 2 gives +30 after 6 steps. Using Route 2 value = 30 × γ⁵, find the break-even γ.

---

## Answer Key

| Q | Answer | Explanation |
|---|---|---|
| Q1 | C | Behaviorist AI learns from rewards by trial and error. |
| Q2 | B | A policy says what to do in each state. |
| Q3 | C | 0 + 0.9 × 0 + 0.9² × 10 = 8.1. |
| Q4 | B | A small γ makes later rewards count very little. |
| Q5 | A | With probability ε the agent picks a random action. |
| Q6 | A | Q-learning keeps a Q-value for each state and action. |
| Q7 | B | The state must contain everything that matters for the next step. |
| Q8 | B | The agent satisfies the literal reward and misses what the designers wanted. |
| Q9 | C | Avoiding obstacles prevents damage, so it overrides the other behaviours. |
| Q10 | Sample | Exploitation uses what the agent already knows is best. Exploration tries something new that might be better. With only exploitation the agent can get stuck with a poor choice, and with only exploration it wastes effort, so it needs both (for example ε-greedy). |
| Q11 | Sample | Only the last step pays a reward. Each pass moves the value back by one square, because each Q-value copies the discounted value of the next square from the previous pass. The first square is three steps away, so it needs three passes. |
| Q12 | Sample | Reinforcement learning from human feedback. People rank a model's answers, a reward model learns their preferences, and the language model is tuned to earn a higher predicted score. Risk: the system learns what people *rated*, which may differ from what is *true*. |
| Q13 | Sample | (a) Connectionist: messy image data and many labelled examples. (b) Symbolic: rules are explainable and can be checked by experts. (c) Behaviorist: it learns from reward by trial and error, safely in a simulation. |
| Q14 | Sample | The agent could keep students busy with pointless tasks to raise minutes. A better reward measures learning progress, such as improvement on a test, and not time spent. |
| Q15 | 5.0 and 2.25 | Q(C,R) = 0 + 0.5 × (10 + 0 − 0) = 5.0. Q(B,R) = 0 + 0.5 × (0 + 0.9 × 5.0 − 0) = 2.25. |
| Q16 | Route X | Expected value of X = 0.9 × 6 + 0.1 × (−10) = 5.4 − 1 = 4.4, which is more than 4. (If a crash is very harmful, a designer might still choose Y.) |
| Q17 | about 0.70 | 30 × γ⁵ = 5, so γ⁵ = 1/6 ≈ 0.1667, so γ ≈ 0.70. A bigger prize makes the agent patient at a smaller γ. |

---

## Where to Go Next

You have finished the four chapters of the module. The module's Study Guide, Test Bank, slides, and videos are planned to use this Markdown as their source. Use the Practice Questions of each chapter to test yourself, and carry one habit into everything you read about AI: **ask where the knowledge comes from, how the system was tested, and what could go wrong.**

---

---

## Key Terms in Chinese

*Check these against your course textbook or a Chinese-speaking teammate; wording varies between books.*

| English | 中文 |
|---|---|
| Behaviorist AI | 行为主义（行为主义人工智能） |
| reinforcement learning | 强化学习 |
| agent | 智能体 |
| environment | 环境 |
| state | 状态 |
| action | 动作 |
| reward | 奖励 |
| policy | 策略 |
| return | 回报 |
| discount factor | 折扣因子 |
| Q-learning | Q 学习 |
| exploration | 探索 |
| exploitation | 利用 |
| Markov decision process (MDP) | 马尔可夫决策过程 |
| Bellman equation | 贝尔曼方程 |
| deep reinforcement learning | 深度强化学习 |
| subsumption architecture | 包容架构 |
| self-play | 自我对弈 |
| reward hacking | 奖励作弊（奖励投机） |
| human feedback | 人类反馈 |

## Glossary

| Term | Meaning |
|---|---|
| **Action** | A choice the agent can make. |
| **Agent** | Something that perceives its environment and acts on it to reach a goal. |
| **Bellman idea** | The value of a state equals the immediate reward plus the discounted value of the next state. |
| **Break-even γ** | The discount factor at which two choices have equal value. |
| **Credit assignment** | Deciding which earlier action deserves credit for a later reward. |
| **Deep reinforcement learning** | Reinforcement learning in which a neural network estimates the values or the policy. |
| **Discount factor (γ)** | A number between 0 and 1 that reduces the weight of future rewards. |
| **Environment** | Everything the agent interacts with. |
| **Episode** | One run from start to finish. |
| **Expected value** | The sum of (probability × reward) over the possible outcomes of an action. |
| **Experience replay** | Storing past experiences and learning from random samples of them. |
| **Exploitation** | Choosing the action that looks best from what is already known. |
| **Exploration** | Trying an action that may turn out better. |
| **Markov property** | The next state depends only on the current state and action, not on the whole history. |
| **MDP** | Markov Decision Process: states, actions, transitions, rewards, and discount. |
| **Policy** | A rule that chooses an action in each state. |
| **Q-learning** | A value-based RL method that learns Q(s, a). |
| **Q-value** | Q(state, action): how good it is to take that action in that state. |
| **Return** | The total future reward an agent tries to maximise, usually discounted by γ. |
| **Reward** | A number that tells an agent how good the result of its last action was. |
| **Reward hacking** | Raising the reward by exploiting a loophole instead of doing the intended task. |
| **RLHF** | Reinforcement learning from human feedback: human rankings or ratings serve as the reward. |
| **Sample inefficiency** | The need for a very large number of trials before an agent learns well. |
| **SARSA** | A Q-learning variant that updates with the action the agent actually takes next. |
| **Self-play** | An agent improves by playing against copies of itself. |
| **Simulation gap** | The difference between a simulated world and the real world, which can make learned skills fail. |
| **State** | A complete description of the situation at one moment, for example in a search problem (Chapter 2) or a reinforcement learning problem (Chapter 4). |
| **Subsumption architecture** | A robot design with layers of simple behaviours, where higher-priority layers override lower ones. |
| **Transition** | The chance of reaching each next state after an action. |
| **Value** | Expected total future reward. |
| **Value iteration** | Computing the value of every state by repeating the Bellman update until the values stop changing. |
| **ε-greedy** | With probability ε pick a random action, otherwise pick the best-known one. |

---

## References

1. Course slides, "chap6: Behaviorist AI", Introduction to Computer Science and Artificial Intelligence. Lecturer's course materials (no public link). Source of the topic outline.
2. Sutton, R. S., and Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press. [http://incompleteideas.net/book/the-book-2nd.html](http://incompleteideas.net/book/the-book-2nd.html) *(not opened; free online textbook for further reading)*
3. Brooks, R. A. (1991). Intelligence without representation. *Artificial Intelligence*, 47(1–3), 139–159. [https://doi.org/10.1016/0004-3702(91)90053-M](https://doi.org/10.1016/0004-3702(91)90053-M) *(not opened; behaviour-based robotics, Topic 5)*
4. Mnih, V., et al. (2015). Human-level control through deep reinforcement learning. *Nature*, 518, 529–533. [https://doi.org/10.1038/nature14236](https://doi.org/10.1038/nature14236) *(not opened; DQN and the Atari result in Topic 3. Check the "75% on more than half of 49 games" statement against the paper)*
5. Silver, D., et al. (2016). Mastering the game of Go with deep neural networks and tree search. *Nature*, 529, 484–489. [https://doi.org/10.1038/nature16961](https://doi.org/10.1038/nature16961) *(existence confirmed through a web search on 5 November 2026; the paper itself was not opened)*
6. Silver, D., et al. (2017). Mastering chess and shogi by self-play with a general reinforcement learning algorithm. [https://arxiv.org/abs/1712.01815](https://arxiv.org/abs/1712.01815) *(not opened; AlphaZero, Topic 5)*
7. Tesauro, G. (1995). Temporal difference learning and TD-Gammon. *Communications of the ACM*, 38(3), 58–68. [https://doi.org/10.1145/203330.203343](https://doi.org/10.1145/203330.203343) *(not opened; TD-Gammon, Topic 5)*
8. Krakovna, V., et al. (2020). Specification gaming: the flip side of AI ingenuity. DeepMind. [https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/](https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/) *(opened on 5 November 2026: definition of specification gaming, the block-flipping robot, CoastRunners)*
9. Clark, J., and Amodei, D. (2016). Faulty reward functions in the wild. OpenAI. [https://openai.com/index/faulty-reward-functions/](https://openai.com/index/faulty-reward-functions/) *(opened on 5 November 2026: CoastRunners, lagoon loop, average score 20 percent higher than human players)*
10. Ouyang, L., et al. (2022). Training language models to follow instructions with human feedback. [https://arxiv.org/abs/2203.02155](https://arxiv.org/abs/2203.02155) *(abstract read on 5 November 2026: the 1.3-billion-parameter InstructGPT model preferred to the 175-billion-parameter GPT-3; RLHF)*
11. Wikipedia. "AlphaGo versus Lee Sedol." [https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol](https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol) *(9–15 March 2016 in Seoul, score 4–1, move 37 in game 2, move 78 in game 4; read with a fetch tool on 5 November 2026)*

> **Link status.** Links marked **not opened** could not be opened while this chapter was written. The author or reviewer must click every link, confirm that it opens the right work and supports the claim it is cited for, and then change the label to "opened" with the date. The worked numbers in this chapter (Q-learning updates, discounting, the 3-button experiment, the grid world, the slippery corridor, expected values) were recomputed with short programs. The historical claims in Topic 1 (Thorndike, Skinner) are general knowledge and were not checked against a source.

---

| [← Chapter 3: Connectionist AI and Big Data](chapter-3-connectionist-ai-and-big-data/connectionist-ai-and-big-data.md) | [Module overview](../../README.md) | End of the module |
|:--|:-:|--:|

---
