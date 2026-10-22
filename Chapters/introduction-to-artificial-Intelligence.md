# Chapter 1: Introduction to Artificial Intelligence

> **Status:** Drafted (V1.0), awaiting peer review
> **Author:** Jonathan Sugianto | **Reviewer:** Brian Djoni Suzanna
> **Audience:** Complete beginners. No programming or AI background needed.

---

## Learning Outcomes

After this chapter, you should be able to:

1. Explain in your own words what Artificial Intelligence (AI) is.
2. Describe five key moments in the history of AI.
3. Explain the difference between traditional programming and AI that learns from data.
4. Use eight basic AI terms correctly: data, algorithm, model, machine learning, training, inference, neural network, deep learning.
5. Walk through a simple example of a program that learns from examples, and explain why it works and where it fails.

## Chapter Map

| Section | Topic | Estimated time |
|:-------:|-------|:--------------:|
| 1.1 | What is Artificial Intelligence? | 10 min |
| 1.2 | A Brief History of AI | 10 min |
| 1.3 | AI vs Traditional Programming | 10 min |
| 1.4 | Basic AI Terminology | 10 min |
| 1.5 | Worked Example: A Spam Filter That Learns | 15 min |
| 1.6 | Practice Questions and Answers | 15 min |
| 1.7 | Summary, Reuse Plan, and References | 5 min |

---

## 1.1 What is Artificial Intelligence?

### Definition

**Artificial Intelligence (AI)** is the field of computer science that builds computer systems able to do tasks that normally need human intelligence, such as recognizing images, understanding language, making decisions, and learning from experience.

Two points are worth noticing:

- AI is a **field of study**, like biology or physics. We also say "an AI" or "an AI system" for a specific product built using that field.
- AI does not mean a machine that thinks like a human. Most AI today is built for **one specific job**, and it is good only at that job.

### Everyday examples

You probably use AI many times a day:

| Situation | What the AI does |
|-----------|------------------|
| Unlocking your phone with your face | Recognizes whether the face matches the owner |
| Video app recommendations | Predicts which videos you are likely to enjoy |
| Typing on a phone keyboard | Suggests the next word |
| Translating a sign with your camera | Reads the text and converts it to another language |
| Email inbox | Moves suspicious emails to the spam folder |
| Chatting with an AI assistant | Produces text in reply to your questions |

### Common misunderstandings

| Myth | Reality |
|------|---------|
| "AI is a robot." | Most AI is software with no body. A robot is a machine; AI can be (but is not always) its "brain." |
| "AI understands things like humans." | Current AI finds patterns in data. Whether this counts as "understanding" is debated, but it does not work like a human mind. |
| "AI is always correct." | AI makes mistakes. Chapter 5 covers this in detail. |

---

## 1.2 A Brief History of AI

AI has gone through periods of excitement, disappointment, and rapid growth. Here are key moments.

| Year | Event | Why it matters |
|:----:|-------|----------------|
| 1950 | Alan Turing publishes *Computing Machinery and Intelligence* and proposes the "imitation game" (now called the Turing Test). | Asked the question "Can machines think?" in a testable way. |
| 1956 | The Dartmouth summer workshop. The term "artificial intelligence" comes from the 1955 proposal for this workshop, written by John McCarthy and colleagues. | Often seen as the birth of AI as a research field. |
| 1966 | Joseph Weizenbaum creates ELIZA, a program that imitates a conversation using simple pattern matching. | An early chatbot. Showed that people may feel a program understands them even when it does not. |
| 1997 | IBM's Deep Blue defeats world chess champion Garry Kasparov. | A machine beat the best human at a task long seen as a sign of intelligence. |
| 2012 | A neural network called AlexNet wins an image recognition contest (ImageNet) by a large margin. | Started the modern wave of **deep learning**. |
| 2016 | DeepMind's AlphaGo defeats Lee Sedol, a top Go player. | Go is far more complex than chess. The program learned much of its skill by playing. |
| 2017 | Researchers at Google publish the **Transformer** architecture. | The basis of today's large language models. |
| 2022 | ChatGPT is released to the public (November). | Brought generative AI to millions of everyday users. |

### The pattern: boom and "winter"

Early researchers expected fast progress, but computers were slow and data was scarce. Funding and interest fell in the 1970s and again in the late 1980s. These periods are called **AI winters**. Progress returned when three things came together: **much more data**, **much faster computers**, and **better learning methods**.

---

## 1.3 AI vs Traditional Programming

### Traditional programming: humans write the rules

In traditional programming, a programmer writes exact instructions (**rules**). The computer takes **data** and the **rules**, and produces **answers**.

Example: a program that converts Celsius to Fahrenheit uses the fixed rule `F = C × 9/5 + 32`.

### AI (machine learning): the computer finds the rules

Some tasks are too hard to describe with rules. Try writing exact rules for "is this photo a cat?" Cats differ in color, size, pose, and lighting. Instead, we give the computer many **examples with correct answers**, and it works out the rules by itself.

```text
TRADITIONAL PROGRAMMING

   Rules (written by human) ──┐
                              ├──► Computer ──► Answers
   Data ──────────────────────┘


MACHINE LEARNING

   Data ──────────┐
                  ├──► Computer (learning) ──► Rules (the "model")
   Answers ───────┘
```

### Comparison

| | Traditional Programming | Machine Learning |
|---|------------------------|------------------|
| Who creates the rules? | The programmer | The computer, from examples |
| Input | Data + rules | Data + correct answers |
| Output | Answers | Rules (a model) that give answers for new data |
| Works best when | Rules are clear and exact (tax calculation, sorting a list) | Rules are hard to write (recognizing faces, understanding speech) |
| Typical weakness | Cannot handle cases the programmer did not foresee | Needs lots of good data and can learn mistakes from bad data |

> **Note:** Not all AI learns from data. Early AI such as expert systems used rules written by people. This module focuses on learning-based AI because it powers most modern applications.

---

## 1.4 Basic AI Terminology

Terms in **bold** are used throughout the rest of the module.

| Term | Simple definition | Example |
|------|-------------------|---------|
| **Data** | Information a computer can process: numbers, text, images, sound. | A collection of 1,000 emails |
| **Algorithm** | A step-by-step procedure for solving a problem. | The steps for sorting names alphabetically |
| **Model** | The result of learning: a set of patterns or rules learned from data, used to make predictions. | A spam filter after it has studied many emails |
| **Machine Learning (ML)** | A way of building AI where the computer learns patterns from data instead of being given exact rules. | Learning to detect spam from examples |
| **Training** | The process of showing data to a learning algorithm so it builds a model. | Studying 10,000 labelled emails |
| **Inference** | Using a trained model on new data to get a result. | Checking a brand-new email |
| **Label** | The correct answer attached to an example. | "Spam" or "Not spam" |
| **Neural network** | A model made of many simple connected units, loosely inspired by the brain, that learns by adjusting the strength of connections. | A network that recognizes handwritten digits |
| **Deep learning** | Machine learning that uses neural networks with many layers. | Speech recognition, image recognition |

### How the terms fit together

```text
Data (+ labels) ──► Training (algorithm) ──► Model ──► Inference ──► Prediction
```

Training happens first, usually once and slowly. Inference happens afterwards, every time someone uses the model.

### How the fields nest

```text
┌───────────────────────────────────────────┐
│ Artificial Intelligence                   │
│  ┌─────────────────────────────────────┐  │
│  │ Machine Learning                    │  │
│  │  ┌───────────────────────────────┐  │  │
│  │  │ Deep Learning                 │  │  │
│  │  └───────────────────────────────┘  │  │
│  └─────────────────────────────────────┘  │
└───────────────────────────────────────────┘
```

Deep learning is a part of machine learning, and machine learning is a part of AI.

---

## 1.5 Worked Example: A Spam Filter That Learns

We will build a tiny spam filter by hand. It is far simpler than real filters, but it shows the full cycle: **data → training → model → inference**.

### Step 1: Collect labelled data

We have six short emails, each with a label.

| # | Email text | Label |
|:-:|-----------|:-----:|
| 1 | win free prize now | Spam |
| 2 | free money offer | Spam |
| 3 | meeting at noon | Not spam |
| 4 | project report due | Not spam |
| 5 | claim your free prize | Spam |
| 6 | lunch at noon tomorrow | Not spam |

### Step 2: Train by counting

For each word, count how many **spam** emails contain it and how many **not-spam** emails contain it. The word's **score** is:

> **score = (number of spam emails containing the word) − (number of not-spam emails containing the word)**

| Word | In spam | In not spam | Score |
|------|:-------:|:-----------:|:-----:|
| free | 3 | 0 | **+3** |
| prize | 2 | 0 | **+2** |
| win, now, money, offer, claim, your | 1 each | 0 | **+1** each |
| meeting, project, report, due, lunch, tomorrow | 0 | 1 each | **−1** each |
| at | 0 | 2 | **−2** |
| noon | 0 | 2 | **−2** |

This table is our **model**. We never wrote a rule such as "free means spam." The scores came from the examples.

### Step 3: Make a decision rule

> Add up the scores of all words in an email. If the total is **greater than 0**, predict **Spam**. Otherwise, predict **Not spam**. A word that is not in the table scores 0.

### Step 4: Inference on a new email

New email: **"free offer tomorrow"**

| Word | Score |
|------|:-----:|
| free | +3 |
| offer | +1 |
| tomorrow | −1 |
| **Total** | **+3** |

The total is greater than 0, so the prediction is **Spam**.

### Step 5: Look at a failure

New email: **"free lunch at noon"** (a friend inviting you to eat)

| Word | Score |
|------|:-----:|
| free | +3 |
| lunch | −1 |
| at | −2 |
| noon | −2 |
| **Total** | **−2** |

The prediction is **Not spam**, which is correct here. But notice how close the result was, and how the harmless words "at" and "noon" decided it. Now try **"free prize at noon"**: the total is +3 +2 −2 −2 = **+1**, so the filter predicts **Spam**. Whether that is right depends on the sender. Our model cannot know.

### What this example teaches

- **The model depends on its training data.** The words "at" and "noon" look "safe" only because our six emails happened to be that way.
- **More and more varied data improves a model.** Six emails is far too few. Real filters learn from millions.
- **Models make mistakes.** Even a good filter sometimes marks real emails as spam or lets spam through.
- **Training and inference are separate.** We counted once (training), then reused the table on any number of new emails (inference).

---

## 1.6 Practice Questions and Answers

### Part A: Check your understanding

**Q1.** Which statement best describes Artificial Intelligence?

- A. A robot that looks like a human
- B. Computer systems that do tasks that normally need human intelligence
- C. Any program that uses the internet
- D. A computer that thinks exactly like a human brain

**Q2.** In traditional programming, who writes the rules? In machine learning, where do the rules come from?

**Q3.** Put these in order: *inference, collecting labelled data, training, using the model on a new email.*

**Q4.** What is the difference between **data** and a **model**?

**Q5.** Give **one** reason why it is hard to solve "recognize a cat in a photo" with hand-written rules.

### Part B: Apply the idea

Use the spam filter model from Section 1.5 (word scores and the rule "total > 0 means spam").

**Q6.** Classify the email **"win money now"**. Show the total.

**Q7.** Classify the email **"project meeting tomorrow"**. Show the total.

**Q8.** Classify the email **"claim free money at noon"**. Show the total, then explain in one sentence why this result is uncertain.

**Q9 (Think).** Our filter was trained on only six emails. Name **two** ways to make it better.

### Answers and Explanations

**A1.** **B.** AI is about systems that perform tasks needing human-like intelligence. A is wrong because most AI has no body. C is wrong because AI and the internet are different things. D is wrong because current AI does not work like a human brain.

**A2.** In traditional programming, the **programmer** writes the rules. In machine learning, the **computer finds the rules** by studying examples with correct answers.

**A3.** (1) Collecting labelled data → (2) Training → (3) Inference, which is (4) using the model on a new email. *Inference and "using the model on a new email" describe the same step.*

**A4.** **Data** is the raw information the computer receives (for example, emails). A **model** is what the computer learns from the data: the patterns or rules used to make predictions.

**A5.** Any one of: cats have many colors, sizes, and poses; photos differ in lighting and angle; a cat may be partly hidden. Writing exact rules for all cases is nearly impossible.

**A6.** win (+1) + money (+1) + now (+1) = **+3** → **Spam**.

**A7.** project (−1) + meeting (−1) + tomorrow (−1) = **−3** → **Not spam**.

**A8.** claim (+1) + free (+3) + money (+1) + at (−2) + noon (−2) = **+1** → **Spam**. The total is barely above 0, and the harmless words "at" and "noon" pulled it down, so a small change in the training data could flip the result.

**A9.** Any two of: add many more training emails; include more varied examples (different senders and topics); use a smarter scoring method; ignore common words such as "at"; check mistakes and add them as new training examples.

---

## 1.7 Summary, Reuse Plan, and References

### Key takeaways

- AI is the field of building computers that perform tasks needing human-like intelligence.
- AI has a history of progress and "winters." The recent boom came from more data, faster computers, and better methods.
- Traditional programming uses human-written rules. Machine learning lets the computer find rules from examples.
- Training builds a **model** from data. Inference uses the model on new data.
- Models depend on their data and can make mistakes.

### How this chapter will be reused

| Resource | Planned use |
|----------|-------------|
| **Study Guide** | Sections 1.1 to 1.4 become the reading text, with the terminology table as a glossary. Questions Q1 to Q9 go into the Test Bank with the answer explanations. |
| **PPT Slides** | The two flow diagrams in 1.3, the timeline in 1.2, and the nested-circles diagram in 1.4 become full-slide visuals. The spam filter example becomes a step-by-step animation of the score table. |
| **Video Tutorial** | A short video that follows Section 1.5: show the six emails, build the score table on screen, then test a new email while the narrator explains each step. |

### Development status of this chapter

| Section | Status | Notes |
|---------|:------:|-------|
| 1.1 What is AI? | Drafted | Needs a second example set checked for accuracy |
| 1.2 Brief History | Drafted | Dates and names need checking against the references |
| 1.3 AI vs Traditional Programming | Drafted | Diagram will be redrawn as an image by the Visual Design Lead |
| 1.4 Terminology | Drafted | Waiting for peer review |
| 1.5 Worked Example | Drafted | Scores recalculated by hand once; needs independent check |
| 1.6 Practice Questions | Drafted | Needs testing by a member who has not seen the answers |
| 1.7 References | Drafted | All references need to be verified by the Quality Lead |

### References

1. Turing, A. M. (1950). Computing machinery and intelligence. *Mind*, 59(236), 433–460.
2. McCarthy, J., Minsky, M. L., Rochester, N., & Shannon, C. E. (1955). *A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence.*
3. Weizenbaum, J. (1966). ELIZA: a computer program for the study of natural language communication between man and machine. *Communications of the ACM*, 9(1), 36–45.
4. Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). ImageNet classification with deep convolutional neural networks. *Advances in Neural Information Processing Systems*, 25.
5. Vaswani, A., et al. (2017). Attention is all you need. *Advances in Neural Information Processing Systems*, 30.
6. Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.

> The spam filter in Section 1.5 is the team's own simplified teaching example. It is inspired by word-counting spam filters but does not copy any specific source.
