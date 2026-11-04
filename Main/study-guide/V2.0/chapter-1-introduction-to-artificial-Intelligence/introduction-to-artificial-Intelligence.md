# Chapter 1: Introduction to Artificial Intelligence

**Team:** Babi Guling | **Module:** AI Overview | **Version:** 2.0
**Author:** Jonathan Sugianto
**Audience:** Complete beginners. No programming or AI background needed.
**Estimated time:** about 2 hours and 35 minutes (including activities)
**How to work through it:** Predict, read, try the activity, check yourself, then compare with the answers.

---

## Table of Contents

1. [Start Here](#start-here)
2. [Learning Outcomes](#learning-outcomes)
3. [Chapter Map](#chapter-map)
4. [1.1 What is AI?](#11-what-is-ai)
5. [1.2 A Brief History of AI](#12-a-brief-history-of-ai)
6. [1.3 AI vs Traditional Programming](#13-ai-vs-traditional-programming)
7. [1.4 Basic AI Terminology](#14-basic-ai-terminology)
8. [1.5 Worked Example: A Spam Filter That Learns](#15-worked-example-a-spam-filter-that-learns)
9. [1.6 Practice Questions and Answers](#16-practice-questions-and-answers)
10. [1.7 Summary, Bridge to Chapter 2, and References](#17-summary-bridge-to-chapter-2-and-references)

---

## Start Here

How does your email app know that a message is spam, when nobody can write a rule for every new scam?

By the end of this chapter you will have built a tiny version of that spam filter by hand. You will see how it learns from examples, where it works, and where it fails. Along the way you will learn what AI is, where it came from, and the nine basic terms used in the rest of this module.

### Where this chapter fits

This module tells one story in five chapters. This chapter gives you the basic vocabulary, and each later chapter builds on it.

| Chapter | Question it answers | What it builds on from this chapter |
|---------|---------------------|-------------------------------------|
| 1. Introduction to AI | What is AI, and what are its basic ideas? | (this chapter) |
| 2. Types of AI | What different kinds of AI are there? | The nine terms, and the idea that AI is usually built for one job (§1.1) |
| 3. How Artificial Intelligence Works | How does an AI system actually work? | Data, model, training, and inference (§1.4) |
| 4. Applications of AI | Where is AI used? | The idea that AI is built for specific tasks, like the AI around you (§1.1) |
| 5. AI Ethics and Limitations | What can go wrong, and how do we use AI responsibly? | The idea that a model depends on its data and can make mistakes (§1.5) |

**Running example.** The spam filter you build in §1.5 is the module's shared example. Chapter 2 uses spam detection to explain types of AI, and Chapter 5 returns to it to show how training data shapes results.

## Learning Outcomes

After this chapter, you should be able to:

1. Explain in your own words what Artificial Intelligence (AI) is.
2. Describe important moments in the history of AI.
3. Explain the difference between traditional programming and AI that learns from data.
4. Use nine basic AI terms correctly: data, algorithm, label, machine learning, model, training, inference, neural network, deep learning.
5. Walk through a simple example of a program that learns from examples, and explain why it works and where it fails.

## Chapter Map

| Section | Topic | What you will do | Time |
|:-------:|-------|------------------|:----:|
| 1.1 | What is AI? | Predict, then look for AI in your own day | 20 min |
| 1.2 | A Brief History of AI | Order key events and find a wrong claim | 20 min |
| 1.3 | AI vs Traditional Programming | Find a rule from examples, like a computer would | 25 min |
| 1.4 | Basic AI Terminology | Learn nine terms and check them | 15 min |
| 1.5 | Worked Example: A Spam Filter That Learns | Trace the filter, label its parts, retrain it, and look ahead to Chapter 2 | 45 min |
| 1.6 | Practice Questions and Answers | Practice, apply, and find mistakes | 25 min |
| 1.7 | Summary, Bridge to Chapter 2, and References | Review and self-check | 5 min |

---

## 1.1 What is AI?

### Predict first (2 minutes)

Write down **three things you did today** that you think used AI. Keep your list. We compare it with the table below.

### A simple definition

**Artificial Intelligence (AI)** is the part of computer science that tries to make computers do tasks that normally need human intelligence. Examples are recognizing faces, understanding speech, translating languages, and making decisions.

Three things to keep in mind:

- **AI is a field of study**, just like biology or physics. People also say "an AI" for a specific system built using that field, such as a chatbot.
- **There is no single official definition.** Different textbooks describe AI in slightly different ways. For example, Russell and Norvig (2021) organize the field around building systems that *act rationally*, meaning they choose actions that are likely to reach a goal. In this module, we use the simple definition above.
- **AI is usually built for one specific job.** A system that is very good at chess cannot cook rice or drive a car. We will come back to this in Chapter 2 (§2.2.1, Artificial Narrow Intelligence).

### AI around you

You probably used AI several times today without noticing.

| Situation | What the AI is doing |
|-----------|----------------------|
| Unlocking your phone with your face | Checking if the face matches the owner |
| Watching a video app | Predicting which videos you may like next |
| Typing a message | Suggesting the next word |
| Pointing your camera at a foreign sign | Reading the text and translating it |
| Checking your email | Moving suspicious emails to the spam folder |
| Using a chatbot | Writing a reply to your question |

Compare this table with the list you wrote. Did you miss any? Most people are surprised by how much AI hides inside ordinary apps.

### Three common myths

| Myth | What is actually true |
|------|-----------------------|
| "AI is a robot." | Most AI is just software with no body. A robot is a machine, and AI can act as its "brain," but they are not the same thing. |
| "AI thinks like a human." | Today's AI finds patterns in data. Scientists still debate what "understanding" means for a machine, but AI does not work like a human brain. |
| "AI is always right." | AI makes mistakes, sometimes confident ones. We cover this in Chapter 5. |

### Activity 1.1: AI in your day

**Goal:** Look at familiar AI as a system with an input, an output, and possible mistakes.

**Preparation:** The "AI around you" table above. Time: about 10 minutes.

**Task**

Pick **two** rows from the "AI around you" table (or two examples from your own list). For each one, write:

1. What goes **in** (the input)?
2. What comes **out** (the output)?
3. What is **one mistake** it could make, and who would notice?

**Observation:** Notice that every example has the same shape: something goes in, something comes out, and the output can be wrong.

**Reflection:** In 2 sentences, explain why a system that is "usually right" can still be a problem for someone.

**Feedback (sample answers and expected outcome)**

| Example | Input | Output | Possible mistake |
|---------|-------|--------|------------------|
| Face unlock | A camera image of a face | "Match" or "no match" | Rejects the real owner in poor light, so the owner notices and has to type a passcode |
| Spam folder | The text of an email | "Spam" or "not spam" | Moves a real email into spam, so the receiver may miss it without noticing |

*Accept any well-reasoned example.* **Reflection (model answer):** Even a system that is right most of the time will sometimes fail, and the person who is affected by a failure may not be able to tell that it happened.

---

## 1.2 A Brief History of AI

### Predict first (2 minutes)

Without looking at the table: which came first, the chatbot ELIZA or the chess computer Deep Blue? Which came first, Alan Turing's paper on machine intelligence or the Dartmouth workshop? Write your guesses.

### Key moments

The history of AI has exciting breakthroughs and also long periods of disappointment. Here are some important moments. The sources for each event are listed in Section 1.7.

![Timeline of key moments in AI history from 1950 to 2022](assets/fig-1-2-timeline.png)
*Figure 1.1: Timeline of key moments in AI history. Source: created by our team, based on the references in Section 1.7.*

| Year | Event | Why it matters |
|:----:|-------|----------------|
| 1950 | Alan Turing publishes the paper *Computing Machinery and Intelligence* (Turing, 1950). He suggests the "imitation game" (later called the **Turing Test**): if a person chatting with a machine cannot tell it apart from a human, can we say the machine is intelligent? | He turned the question "Can machines think?" into something that can be tested. |
| 1955–1956 | John McCarthy, Marvin Minsky, Nathaniel Rochester, and Claude Shannon write a proposal in 1955 for a summer workshop at Dartmouth College (McCarthy et al., 1955/2006). The proposal uses the term "artificial intelligence." The workshop takes place in summer 1956. | Many people see this as the start of AI as a research field. |
| 1959 | Arthur Samuel describes a checkers program that improves by playing and learning from experience (Samuel, 1959). | One of the first examples of a computer **learning** instead of only following fixed instructions. |
| 1966 | Joseph Weizenbaum creates **ELIZA**, a program that chats using simple keyword rules (Weizenbaum, 1966). | An early chatbot. Many users felt that ELIZA understood them, even though it did not. |
| 1997 | IBM's **Deep Blue** beats world chess champion Garry Kasparov in a six-game match (3½ to 2½) (Campbell et al., 2002). | A machine beat the best human at a game people linked with intelligence. |
| 2012 | A neural network called **AlexNet** wins the ImageNet image recognition competition by a large margin (Krizhevsky et al., 2012). | Started the modern boom of **deep learning**. |
| 2016 | **AlphaGo** (made by Google DeepMind) beats Lee Sedol, a top Go player, 4 games to 1 (Silver et al., 2016). | Go is much harder for computers than chess. AlphaGo learned from many human games and then improved by playing against itself. |
| 2017 | Google researchers publish the **Transformer**, a new design for neural networks (Vaswani et al., 2017). | It is the base of today's large language models. |
| 2022 | OpenAI releases **ChatGPT** to the public on 30 November (OpenAI, 2022). | Made generative AI available to millions of ordinary users. |

Check your predictions: Turing's paper (1950) came before the Dartmouth workshop (1956), and ELIZA (1966) came before Deep Blue (1997).

### Where you will meet these again

Several events in the table come back in later chapters:

| Event | Where it returns |
|-------|------------------|
| ELIZA (1966), which followed hand-written keyword rules | Chapter 2, §2.4.7: rule-based systems and symbolic AI |
| Deep Blue (1997) | Chapter 2, §2.3.1: reactive machines |
| AlexNet (2012) and deep learning | Chapter 2, §2.4.4, and Chapter 3, §3.6 |
| The Transformer (2017) and ChatGPT (2022) | Chapter 2, §2.4.5 (generative AI) and Chapter 3, §3.7 (how modern language AI works) |

In the table above, **generative AI** means AI that creates new content such as text or images, and a **large language model** is an AI model trained on very large amounts of text so that it can generate text. Chapters 2 and 3 explain both in detail.

### Two famous moments in pictures

![Alan Turing at age 16](assets/turing-aged-16.jpg)
*Figure 1.2: Alan Turing at age 16 (passport photo, around 1927–1928). Source: Wikimedia Commons, "File:Alan Turing Aged 16.jpg" (https://commons.wikimedia.org/wiki/File:Alan_Turing_Aged_16.jpg). License: public domain (Public Domain Mark 1.0), as stated on the Commons file page.*

![A computer similar to Deep Blue at the Computer History Museum](assets/deep-blue-chm.jpg)
*Figure 1.3: A computer similar to Deep Blue, displayed at the Computer History Museum. Photo by James (originally on Flickr). Source: Wikimedia Commons, "File:Deep Blue.jpg" (https://commons.wikimedia.org/wiki/File:Deep_Blue.jpg), also used in the Wikipedia article "Deep Blue (chess computer)". License: CC BY 2.0 (https://creativecommons.org/licenses/by/2.0/).*

### Booms and "AI winters"

In the early years, researchers expected fast progress. But computers were slow, and there was little data, so many promises were not kept. Funding and interest dropped, first in the 1970s and again from the late 1980s into the early 1990s. These quiet periods are called **AI winters**.

Progress became fast again when three things came together: **much more data** (from the internet), **much faster computers**, and **better learning methods**.

### Activity 1.2: Timeline detective

**Goal:** Place key events in order, catch a wrong claim, and think about what "sounding intelligent" means.

**Preparation:** Try Parts A and B from memory first, then check with the table. Time: about 10 minutes.

**Task**

**Part A: Order the events.** Put these five events in order from earliest to latest:
ChatGPT is released; AlphaGo beats Lee Sedol; Turing publishes *Computing Machinery and Intelligence*; Deep Blue beats Kasparov; ELIZA is created.

**Part B: Find the mistake.** A classmate wrote: "In 2016, IBM's Deep Blue beat world chess champion Garry Kasparov. In 1997, AlphaGo beat Lee Sedol." What is wrong?

**Part C: Think.** ELIZA used only simple keyword rules, yet many users felt that it understood them. Why is this a useful warning when we judge modern chatbots?

**Observation:** Note which events you could place without the table, and which clue helped you (for example, "chess came before Go").

**Reflection:** In 2 sentences, say what ELIZA teaches us about the difference between *sounding* intelligent and *being* intelligent.

**Feedback (answers and expected outcomes)**

**Part A:** Turing's paper (1950) → ELIZA (1966) → Deep Blue (1997) → AlphaGo (2016) → ChatGPT (2022).

**Part B:** The years are swapped. Deep Blue beat Kasparov in **1997**, and AlphaGo beat Lee Sedol in **2016** (4 games to 1). The two systems were also built by different organizations: Deep Blue by IBM, AlphaGo by Google DeepMind.

**Part C:** *(Model answer)* A program can produce replies that feel human without understanding anything, so a fluent, friendly reply is not proof of understanding. We should judge a chatbot by what it actually does and by whether its answers are correct, not only by how natural it sounds.

---

## 1.3 AI vs Traditional Programming

### Predict first (3 minutes)

Try to write **three exact rules** that decide whether a mango is ripe. Where do your rules break? (For example, what about a mango that is green but soft?) Keep your attempt for later.

### Traditional programming: a human writes the rules

Think of a **recipe**. It gives exact steps, and if you follow them, you get the same dish every time.

Traditional programming works the same way. The programmer writes exact instructions, called **rules**. The computer takes the **rules** and the **data**, and gives **answers**.

*Example:* A program that changes Celsius to Fahrenheit uses the fixed rule `F = C × 9/5 + 32`. The rule is clear and always correct.

### Machine learning: the computer finds the rules

Now imagine you must write exact rules to decide "Is this mango ripe?" You would need to describe color, smell, softness, and more, and every mango is a little different. It is very hard to write rules for this.

Instead, a person learns from experience: after seeing and touching many mangoes, you can tell if one is ripe, even if you cannot explain every rule. **Machine learning** does something similar. We give the computer many **examples with the correct answers**, and it finds the patterns by itself.

> This is an example of **supervised learning**, where a model learns from labeled data. Other machine learning approaches may learn without labeled answers. Chapter 2 (§2.4.2) introduces the three common approaches: supervised, unsupervised, and reinforcement learning.

![Diagram comparing traditional programming (rules and data go in, answers come out) with machine learning (data and correct answers go in, rules come out)](assets/fig-1-3-traditional-vs-ml.png)
*Figure 1.4: Traditional programming vs machine learning. Source: created by our team.*

### Side-by-side comparison

| | Traditional Programming | Machine Learning |
|---|------------------------|------------------|
| Who creates the rules? | The programmer | The computer, from examples |
| What goes in? | Data + rules | Data + correct answers |
| What comes out? | Answers | Rules (a **model**) that can give answers for new data |
| Works best when | Rules are clear and exact (calculating tax, sorting names) | Rules are hard to write (recognizing faces, understanding speech) |
| Main weakness | Fails on cases the programmer did not think of | Needs a lot of good data, and learns mistakes if the data is bad |

> **Important note:** Not all AI learns from data. Some early AI systems, such as *expert systems*, used rules written by human experts. We focus on learning-based AI because it powers most modern tools, but the two ideas are not the same thing. Chapter 2 (§2.4.7) calls the rule-based approach symbolic AI.

In Section 1.5, you will see both approaches solve the same task, so you can compare them directly.

### Activity 1.3: Rules or examples?

**Goal:** Tell rule-based programs from learned ones, and experience finding a rule from labeled examples, as a computer would.

**Preparation:** The side-by-side comparison table above. Time: about 20 minutes.

**Task**

**Part A: Which approach fits best?** For each task, write **Rules** (a programmer can write exact rules) or **Examples** (it is easier to learn from labeled examples), and give a reason:

1. Calculating tax from a fixed formula
2. Recognizing a friend's face in photos
3. Sorting a list of names from A to Z
4. Turning speech into text
5. Turning a light on at 7:00 p.m.

**Part B: Be the learner.** A farmer labeled six mangoes. Find the pattern.

| # | Color | Feel | Label |
|:-:|-------|------|-------|
| 1 | Yellow | Soft | Ripe |
| 2 | Yellow | Hard | Not ripe |
| 3 | Green | Hard | Not ripe |
| 4 | Green | Soft | Not ripe |
| 5 | Yellow | Soft | Ripe |
| 6 | Green | Hard | Not ripe |

1. Write the pattern as one sentence.
2. **Predict** the label for each new mango: (a) yellow and soft, (b) green and soft, (c) yellow and hard.
3. Using the words from the table in this section, who found the rule here: a programmer or you? What did you use instead of rules?

**Part C: Think.** The farmer now hands you an orange-yellow, soft mango from a different farm. Can your rule handle it? What would you need?

**Observation:** Notice that you never wrote a rule first. You looked at labeled examples and the rule appeared.

**Reflection:** In 2 sentences, explain how this is similar to what a spam filter does with labeled emails.

**Feedback (answers and expected outcomes)**

**Part A:** 1 **Rules** (fixed formula, always correct). 2 **Examples** (hard to write exact rules for every face, light, and angle). 3 **Rules** (a clear step-by-step method). 4 **Examples** (voices and accents vary too much for hand-written rules). 5 **Rules** (a fixed time).

**Part B**

1. A mango is ripe only when it is **yellow and soft**.
2. (a) **Ripe**. (b) **Not ripe**. (c) **Not ripe**.
3. **You** found the rule, from **labeled examples** (the labels were "Ripe" and "Not ripe"). No one gave you a rule. This is the supervised learning idea from this section.

**Part C:** Your examples only contained yellow and green mangoes, so your rule does not say what to do with orange-yellow. You would need more labeled examples that include that kind of mango. A learned rule only covers what the examples showed.

**Reflection (model answer):** A spam filter also gets labeled examples (Spam and Not spam) and finds which words signal each label, instead of a programmer writing every rule. Like your mango rule, it only knows what its examples showed.

---

## 1.4 Basic AI Terminology

These terms appear again in the rest of the module.

| Term | Simple meaning | Example |
|------|----------------|---------|
| **Data** | Information a computer can process, like numbers, text, images, or sound. | A collection of 1,000 emails |
| **Algorithm** | A step-by-step method for solving a problem. | The steps for sorting names from A to Z |
| **Label** | The correct answer attached to an example. | "Spam" or "Not spam" |
| **Machine Learning (ML)** | A way of building AI where the computer learns patterns from data, instead of being given exact rules, to make predictions or other outputs. | A system that learns to detect spam from examples |
| **Model** | What the computer has learned: patterns used to make predictions on new data. | A spam filter after it has studied many emails |
| **Training** | Showing data to a learning algorithm so it can build a model. | Studying 10,000 labeled emails |
| **Inference** | Using a trained model on new data to get a result. | Checking a brand-new email |
| **Neural network** | A model made of many simple connected units. It is loosely inspired by the brain, and it learns by adjusting how strong each connection is. | A network that recognizes handwritten digits |
| **Deep learning** | Machine learning that uses neural networks with many layers. | Speech recognition and image recognition |

### Where these terms are developed further

| Term | Developed further in |
|------|----------------------|
| Data | Chapter 3, §3.3 *Data: The Fuel of AI* |
| Algorithm, model | Chapter 3, §3.4 *Algorithms and Models* |
| Machine learning, label | Chapter 2, §2.4.1 and §2.4.2 (supervised, unsupervised, and reinforcement learning); Chapter 3, §3.5 |
| Neural network, deep learning | Chapter 2, §2.4.4; Chapter 3, §3.6 |
| Training, inference | Chapter 3, §3.8 *Training vs. Inference* |

Later chapters use these terms with the meaning given in the table above.

### Training vs inference: an everyday comparison

Think of studying for an exam and taking the exam.

- **Training** is like studying many past questions. It takes a long time, and you do it before the exam.
- **Inference** is like answering questions in the real exam. You use what you learned on questions you have not seen before.

![Diagram showing training (data and labels go into a learning algorithm to build a model) and inference (new data goes through the model to give a prediction)](assets/fig-1-4b-training-vs-inference.png)
*Figure 1.5: Training vs inference. Source: created by our team.*

### How the fields fit together

![Nested circles showing deep learning inside machine learning inside artificial intelligence](assets/fig-1-4-ai-ml-dl.png)
*Figure 1.6: How AI, machine learning, and deep learning fit together. Source: created by our team.*

Deep learning is a part of machine learning, and machine learning is a part of AI.

### Check your understanding

Decide whether each situation is **training** or **inference**.

1. A phone app studies 5,000 photos that people tagged "cat" or "dog."
2. The same app looks at a new photo and says "dog."
3. A bank feeds one million transactions labeled "normal" or "fraud" into a learning algorithm.
4. The bank's trained model checks a brand-new transaction.

**Answers**

1. **Training** (learning from labeled data).
2. **Inference** (using the trained model on new data).
3. **Training** (building a model from labeled data).
4. **Inference** (using the trained model on a new case).

---

## 1.5 Worked Example: A Spam Filter That Learns

### Predict first (2 minutes)

Look at the email **"free lunch at noon"** (a friend inviting you to eat). Would you call it spam? Which words make you hesitate? Keep your guess. We come back to it in Step 5.

Let's build a very small spam filter by hand. Real filters are much more advanced, but this shows the full cycle: **data → training → model → inference**. At the end, we also compare it with a filter made of hand-written rules.

### Step 1: Collect labeled data

We have six short emails with labels.

| # | Email text | Label |
|:-:|-----------|:-----:|
| 1 | win free prize now | Spam |
| 2 | free money offer | Spam |
| 3 | meeting at noon | Not spam |
| 4 | project report due | Not spam |
| 5 | claim your free prize | Spam |
| 6 | lunch at noon tomorrow | Not spam |

### Step 2: Train by counting

For each word, count how many spam emails contain it, and how many not-spam emails contain it. Then calculate the word's **score**:

> **score = (number of spam emails with the word) − (number of not-spam emails with the word)**

| Word | In spam | In not spam | Score |
|------|:-------:|:-----------:|:-----:|
| free | 3 | 0 | **+3** |
| prize | 2 | 0 | **+2** |
| win, now, money, offer, claim, your | 1 each | 0 | **+1** each |
| meeting, project, report, due, lunch, tomorrow | 0 | 1 each | **−1** each |
| at | 0 | 2 | **−2** |
| noon | 0 | 2 | **−2** |

This score table is our **model**. We never wrote a rule like "the word *free* means spam." The scores came from the examples.

> **Note:** These scores are simple counts taken from the six training emails. They are **not probabilities** and they do not measure how confident the filter is. They are only used together with this model's decision rule (Step 3).

### Step 3: Make a decision rule

> Add up the scores of all the words in an email. If the total is **greater than 0**, predict **Spam**. Otherwise, predict **Not spam**. A word that is not in the table scores 0.

### Step 4: Inference on a new email

New email: **"free offer tomorrow"**

| Word | Score |
|------|:-----:|
| free | +3 |
| offer | +1 |
| tomorrow | −1 |
| **Total** | **+3** |

The total is above 0, so the prediction is **Spam**.

### Step 5: See where it struggles

New email: **"free lunch at noon"** (a friend inviting you to eat)

| Word | Score |
|------|:-----:|
| free | +3 |
| lunch | −1 |
| at | −2 |
| noon | −2 |
| **Total** | **−2** |

The prediction is **Not spam**, which is correct here. But look at how it happened: the harmless words "at" and "noon" pulled the score down. Now try **"free prize at noon"**: +3 +2 −2 −2 = **+1**, so the filter says **Spam**. Is it really spam? The filter cannot know, because it only counts words.

Compare with your guess from the start of this section: did the same words make you hesitate?

### Step 6: Compare with a rule-based filter

Now let's solve the same task the traditional way. A programmer looks at the emails and writes a rule by hand:

> **Rule:** If the email contains the word "free" or "prize", predict **Spam**. Otherwise, predict **Not spam**.

On our six training emails, this rule is correct every time: emails 1, 2, and 5 contain "free", and emails 3, 4, and 6 contain neither word. Now test both filters on two new emails:

| New email | What it really is | Rule-based filter | Learning-based filter (score table) |
|-----------|-------------------|-------------------|-------------------------------------|
| win money now | Spam | Not spam ✗ (no "free" or "prize") | Spam ✓ (total +3) |
| free lunch at noon | Not spam (a friend's invitation) | Spam ✗ (contains "free") | Not spam ✓ (total −2) |

What we can learn from this comparison:

- The rule-based filter only knows what the programmer thought of. To fix its mistakes, the programmer must edit the rule by hand.
- The learning-based filter found useful words such as "money" and "noon" from the examples. To improve it, we add more labeled examples and count again.
- Neither filter is perfect. The learning-based filter predicts "Spam" for "free prize at noon" (Step 5) because its total score is +1, but the prediction may still be unreliable because the model uses only simple word counts from six training emails. The rule-based filter would also call that email spam.

### What this example teaches

- **A model depends on its training data.** The words "at" and "noon" look "safe" only because our six emails happened to include them in not-spam messages.
- **More and varied data makes a better model.** Six emails is far too few. Real filters learn from millions.
- **Models make mistakes.** Even good filters sometimes block real emails or let spam through.
- **Training and inference are separate.** We counted once (training), then used the same table for any number of new emails (inference).
- **Hand-written rules and learned rules have different weaknesses.** Rules only cover what the programmer imagined, while learned models only cover what the data showed.
- **A model can fit its few examples too closely.** Chapter 2 (§2.4.3) explains a related problem called overfitting, where a model learns its training examples too closely and performs poorly on new data.

> **Note:** This word-scoring method is a simplified teaching version. Real spam filters use more advanced statistical or neural network methods, and they look at much more than single words.

### Activity 1.5: Label the parts, then retrain the filter

**Goal:** Connect the nine terms to a real process, see how changing the training data changes the model, and preview how Chapter 2 would describe the filter.

**Preparation:** The six emails and score table from Steps 1 to 3. Pen and paper (or a calculator). Time: about 30 minutes.

**Task**

**Part A: Label the parts.** Match each item to one term: *data, label, algorithm, training, model, inference*.

1. The six email texts
2. The words "Spam" and "Not spam" attached to each email
3. Counting words to fill the score table
4. The score table
5. Adding up the scores for "free offer tomorrow"
6. The step-by-step counting method

**Part B: Retrain the filter.** Add two new labeled emails to the training data:

| # | Email text | Label |
|:-:|-----------|:-----:|
| 7 | claim free lunch now | Spam |
| 8 | team lunch at noon | Not spam |

1. **Predict:** after adding these two emails, will "free prize at noon" still be classified as Spam? Write your guess.
2. Recount the scores for the words that appear in emails 7 and 8 (claim, free, lunch, now, team, at, noon).
3. Recompute the totals for **"free lunch at noon"** and **"free prize at noon"** using the new table.
4. Compare with Step 5. What changed?

**Part C: Look ahead.** Chapter 2 describes AI systems from several perspectives. Using only what you know so far, answer for our spam filter:

1. Does it do one narrow job, or many different jobs?
2. Did it learn from examples that had correct answers attached?
3. Does it sort emails into categories, or create new content?

**Observation:** Look at which word scores moved the most, and why.

**Reflection:** In 3 to 4 sentences, explain what this shows about how a model depends on its training data. In Chapter 5 you will see how the same effect can treat groups of people unfairly.

**Feedback (answers and expected outcomes)**

**Part A:** 1 **data**. 2 **labels**. 3 **training** (running the method on the data). 4 **model** (what was learned). 5 **inference** (using the model on a new email). 6 **algorithm** (the method itself). Training is the act of running the algorithm on the data; the algorithm is the method.

**Part B**

Updated score table (eight training emails):

| Word | In spam | In not spam | Score |
|------|:-------:|:-----------:|:-----:|
| free | 4 | 0 | **+4** |
| prize | 2 | 0 | **+2** |
| now | 2 | 0 | **+2** |
| claim | 2 | 0 | **+2** |
| win, money, offer, your | 1 each | 0 | **+1** each |
| lunch | 1 | 2 | **−1** |
| meeting, project, report, due, tomorrow, team | 0 | 1 each | **−1** each |
| at | 0 | 3 | **−3** |
| noon | 0 | 3 | **−3** |

New totals:

| Email | Calculation | Total | Prediction |
|-------|-------------|:-----:|:----------:|
| free lunch at noon | +4 −1 −3 −3 | **−3** | Not spam |
| free prize at noon | +4 +2 −3 −3 | **0** | Not spam |

**What changed:** Before, "free prize at noon" scored **+1** and was called Spam (Step 5). After adding two emails it scores **0**, which is not greater than 0, so it is now called **Not spam**. The words "at" and "noon" became more negative because the new not-spam email used them again.

**Part C**

1. It does **one narrow job** (sorting emails). Chapter 2 calls this **ANI**, Artificial Narrow Intelligence (§2.2.1).
2. **Yes.** Every training email had a Spam or Not spam label, so Chapter 2 would call this **supervised learning** (§2.4.2).
3. It **sorts emails into categories**, so it is a **discriminative** system, not a generative one (§2.4.6).

One system can have several valid descriptions at once. That is the main idea of Chapter 2 (§2.1).

**Reflection (model answer):** Adding just two emails changed the model and flipped a prediction. The model only reflects the examples it was shown, so if some words or patterns are over-represented in one label, the model learns that pattern even when it is not meaningful. More data helps only when it is varied and balanced.

---

## 1.6 Practice Questions and Answers

### Part A: Check your understanding

**Q1.** Which statement describes AI best?

- A. A robot that looks like a human
- B. Computer systems that do tasks that normally need human intelligence
- C. Any program that connects to the internet
- D. A computer that thinks exactly like a human brain

**Q2.** In traditional programming, who writes the rules? In machine learning, where do the rules come from?

**Q3.** Put these steps in the correct order:

- A. Use the model to check a new email
- B. Train the model
- C. Collect emails with labels

Which step is **inference**?

**Q4.** What is the difference between **data** and a **model**?

**Q5.** True or False: "All AI systems learn from data." Explain your answer.

**Q6.** Give one reason why it is hard to recognize a cat in a photo using hand-written rules.

### Part B: Apply the idea

Use the model from Section 1.5 (the score table and the rule "total > 0 means spam").

**Q7.** Classify the email **"win money now"**. Show the total.

**Q8.** Classify the email **"project meeting tomorrow"**. Show the total.

**Q9.** Classify the email **"claim free money at noon"**. Show the total, then explain in one sentence why this result is uncertain.

**Q10.** Classify the email **"hello friend"**. What does the result tell you about the model's limits?

**Q11 (Think).** Our filter was trained on only six emails. Name **two** ways to improve it.

### Part C: Find the mistake and explain

**Q12 (Find the mistake).** A classmate classifies **"win free lunch at noon"** with the model from Section 1.5. They write: "The words 'at' and 'noon' are boring, so I skipped them. win +1, free +3, lunch −1 = +3, so Spam." What is wrong, and what is the correct result?

**Q13.** Classify the email **"claim your prize"**. Show the total, and say which training emails taught the model about these words.

**Q14 (Explain).** In 3 to 4 sentences, explain why the learning-based filter did better than the rule-based filter on "win money now" (Section 1.5, Step 6), but still cannot be trusted completely.

### Answers and Explanations

**A1. B.** AI is about systems that do tasks needing human-like intelligence. A is wrong because most AI has no body. C is wrong because AI and the internet are different things. D is wrong because AI does not work like a human brain.

**A2.** In traditional programming, the **programmer** writes the rules. In machine learning, the **computer finds the rules** by studying examples with correct answers.

**A3.** The order is **C → B → A**. Step **A** is **inference**, because it uses the trained model on a new email. Step B is training.

**A4.** **Data** is the information the computer receives (for example, emails). A **model** is what the computer learns from that data: patterns used to make predictions.

**A5. False.** Many modern AI systems learn from data, but not all. Some early systems, such as expert systems, used rules written by people. Chapter 2 (§2.4.7) explains symbolic AI.

**A6.** Any one of these: cats come in many colors, sizes, and poses; photos have different lighting and angles; a cat may be partly hidden. It is almost impossible to write exact rules for every case.

**A7.** win (+1) + money (+1) + now (+1) = **+3**, so **Spam**.

**A8.** project (−1) + meeting (−1) + tomorrow (−1) = **−3**, so **Not spam**.

**A9.** claim (+1) + free (+3) + money (+1) + at (−2) + noon (−2) = **+1**, so **Spam**. The total is barely above 0, and harmless words ("at", "noon") pulled the score down, so a small change in the training data could flip the result. The score is not a probability or a direct measure of confidence. Since the model uses only a small training dataset and simple word counts, its predictions may not always be reliable.

**A10.** Both words are not in the table, so each scores 0. The total is **0**, which is not greater than 0, so the prediction is **Not spam**. The model has no knowledge about words it never saw during training, so it may be wrong on new kinds of emails.

**A11.** Any two of these: add many more training emails; include more varied examples (different senders and topics); ignore very common words such as "at"; check the mistakes it makes and add them as new training examples; use a smarter scoring method.

**A12.** The classmate skipped "at" and "noon". The model counts **every** word that is in the score table, including words that look boring to a human. Correct total: win (+1) + free (+3) + lunch (−1) + at (−2) + noon (−2) = **−1**, so the prediction is **Not spam**, not Spam. Skipping words changed the result.

**A13.** claim (+1) + your (+1) + prize (+2) = **+4**, so **Spam**. "Claim" and "your" were learned from email 5 ("claim your free prize"), and "prize" from emails 1 and 5. All of them appeared only in spam emails during training.

**A14.** *(Model answer)* The rule-based filter only looks for "free" or "prize", so it misses "win money now". The learning-based filter found from the examples that words like "win", "money", and "now" also appear in spam, so it catches that email. But it still relies on simple word counts from only six emails, so harmless words such as "at" and "noon" can pull a score the wrong way, as in "free prize at noon". Learned rules only cover what the training data showed.

---

## 1.7 Summary, Bridge to Chapter 2, and References

### Key takeaways

- AI is the field of making computers do tasks that normally need human intelligence.
- AI has a history of breakthroughs and "winters." The recent boom came from more data, faster computers, and better methods.
- Traditional programming uses rules written by humans. Machine learning lets the computer find rules from examples.
- **Training** builds a model from data. **Inference** uses the model on new data.
- A model depends on its data, and it can make mistakes.

### Self-check (answer without looking back)

1. In your own words, what is AI?
2. Use the exam analogy to explain the difference between training and inference.
3. Why does a model that was trained on different emails give different answers?
4. Name one task where hand-written rules work well, and one where learning from examples works better.

**Answers**

1. *(Model answer)* AI is the part of computer science that tries to make computers do tasks that normally need human intelligence, such as recognizing faces or understanding speech.
2. Training is like studying many past exam questions in advance; inference is like answering new questions in the real exam using what you learned.
3. A model is built from its training data, so different data gives different patterns (and different scores), as you saw when you retrained the filter in Activity 1.5.
4. Rules work well for exact, clear tasks such as calculating tax or sorting names. Learning from examples works better when rules are hard to write, such as recognizing faces or understanding speech.

### Bridge to Chapter 2

This chapter treated "AI" as one big idea. But the word covers very different systems: a chess program, a spam filter, a chatbot, and an image generator are all called AI, yet they do very different jobs.

Chapter 2 (*Types of Artificial Intelligence*) sorts AI systems from four perspectives:

- **Capability:** how broadly a system can perform intellectual tasks (ANI, AGI, and ASI).
- **Functionality:** how a system behaves and uses information.
- **Learning approach:** how a system learns patterns from data (for example supervised learning and deep learning).
- **Output and application:** what a system produces or helps accomplish (for example generative AI).

You already took the first step: in Activity 1.5, Part C, you described our spam filter from several perspectives. Chapter 2 shows that these perspectives overlap, and that one system can have several valid descriptions.

### References

1. Turing, A. M. (1950). Computing machinery and intelligence. *Mind*, 59(236), 433–460. https://doi.org/10.1093/mind/LIX.236.433
2. McCarthy, J., Minsky, M. L., Rochester, N., & Shannon, C. E. (2006). A proposal for the Dartmouth summer research project on artificial intelligence, August 31, 1955. *AI Magazine*, 27(4), 12–14. https://doi.org/10.1609/aimag.v27i4.1904
3. Samuel, A. L. (1959). Some studies in machine learning using the game of checkers. *IBM Journal of Research and Development*, 3(3), 210–229. https://doi.org/10.1147/rd.33.0210
4. Weizenbaum, J. (1966). ELIZA: A computer program for the study of natural language communication between man and machine. *Communications of the ACM*, 9(1), 36–45. https://doi.org/10.1145/365153.365168
5. Campbell, M., Hoane, A. J., & Hsu, F.-h. (2002). Deep Blue. *Artificial Intelligence*, 134(1–2), 57–83. https://doi.org/10.1016/S0004-3702(01)00129-1
6. Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). ImageNet classification with deep convolutional neural networks. *Advances in Neural Information Processing Systems*, 25. https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks
7. Silver, D., et al. (2016). Mastering the game of Go with deep neural networks and tree search. *Nature*, 529, 484–489. https://doi.org/10.1038/nature16961
8. Vaswani, A., et al. (2017). Attention is all you need. *Advances in Neural Information Processing Systems*, 30. https://arxiv.org/abs/1706.03762
9. OpenAI. (2022, November 30). *Introducing ChatGPT*. https://openai.com/index/chatgpt/
10. Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.

> The spam filter in Section 1.5 is the team's own simplified teaching example, inspired by word-counting spam filters. It does not copy a specific source. The mango table in Activity 1.3 and the two extra emails in Activity 1.5 are also invented for teaching.
