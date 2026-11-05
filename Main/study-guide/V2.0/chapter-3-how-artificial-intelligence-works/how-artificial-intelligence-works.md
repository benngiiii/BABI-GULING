# How Artificial Intelligence Works

**Audience:** Learners with no technical background in AI  
**Estimated time:** 3 to 4 hours (including missions)  
**Format:** Read, pause at each "Pause and predict" box, complete the two missions, then check the answer key at the end of the chapter.

---

## Table of Contents

- [Learning Outcomes](#learning-outcomes)
- [Where This Chapter Fits](#where-this-chapter-fits)
- [3.1 The Big Picture](#31-the-big-picture)
- [3.2 Data: The Fuel of AI](#32-data-the-fuel-of-ai)
- [3.3 Algorithms and Models](#33-algorithms-and-models)
- [3.4 Machine Learning: Learning from Examples](#34-machine-learning-learning-from-examples)
- [3.5 Neural Networks and Deep Learning](#35-neural-networks-and-deep-learning)
- [3.6 How Modern Language AI Works](#36-how-modern-language-ai-works)
- [3.7 Training vs Inference](#37-training-vs-inference)
- [3.8 Evaluating a Model](#38-evaluating-a-model)
- [3.9 Mission 1: Be the Learner](#39-mission-1-be-the-learner)
- [3.10 Mission 2: Judge the Filter](#310-mission-2-judge-the-filter)
- [3.11 Common Misconceptions](#311-common-misconceptions)
- [3.12 Quick Check](#312-quick-check)
- [3.13 Summary, Connections and References](#313-summary-connections-and-references)
- [Answer Key](#answer-key)
- [Glossary](#glossary)
- [References](#references)

---

## Learning Outcomes

After this chapter, you should be able to:

1. Describe the AI workflow from defining a problem to monitoring a deployed model.
2. Explain what data is, why data quality matters, and why data is split into training, validation and test sets.
3. Explain the difference between an algorithm and a model.
4. Describe in simple steps how a model learns: predict, measure error, adjust, repeat.
5. Explain overfitting and underfitting in everyday language.
6. Describe in simple terms how neural networks and large language models work.
7. Explain the difference between training and inference.
8. Calculate accuracy, precision and recall from a confusion matrix and explain why accuracy alone can mislead.

## Where This Chapter Fits

**Builds on Chapters 1 and 2.** Chapter 1 introduced data, model, training and inference. Chapter 2 showed that most useful AI today is limited-memory AI that learns from data. This chapter opens the box and shows the steps inside.

**Leads to Chapters 4 to 6.** Here you see the *general* recipe for learning from data. Chapter 4 shows an AI that uses written rules instead. Chapter 5 goes deeper into neural networks. Chapter 6 shows a third style, learning from rewards.

---

## 3.1 The Big Picture

### Start with a question

When a company says "we built an AI", what did people actually *do* for months? Surprisingly, writing the learning code is a small part. Most of the work is something else. What do you think it is?

### In plain words

**Building AI is like running a bakery.** You decide what to bake (the problem), buy ingredients (data), clean and measure them (preparation), follow a method (the algorithm) to bake a cake (the model), taste it (evaluate), sell it (deploy), and listen to customers (monitor).

### The workflow

![The AI workflow: define the problem, collect data, prepare and split data, train, evaluate, deploy, monitor and improve, with loops back](assets/fig-3-1-ai-workflow.png)
*Figure 3.1: The AI workflow. Source: created by our team.*

| Step | What happens | Bakery comparison |
|:----:|--------------|-------------------|
| 1. Define the problem | Decide what to predict and how success is measured. | Decide which cake to bake |
| 2. Collect data | Gather examples. | Buy ingredients |
| 3. Prepare and split | Clean the data, fix errors, split into training, validation and test sets. | Wash, measure and set aside some for tasting |
| 4. Train | The algorithm learns patterns and builds a model. | Bake following a recipe |
| 5. Evaluate | Test on data the model has not seen. | Let a stranger taste it |
| 6. Deploy | Put the model to work (inference). | Sell the cake |
| 7. Monitor and improve | Watch for mistakes and changes; retrain with new data. | Listen to customers and adjust |

**Where the analogy breaks:** a baker can taste mid-way and fix the recipe on the spot; an AI team must be careful to evaluate only on data the model never trained on, otherwise the "taste test" is unfair.

> **Pause and predict.** Which step do you think takes most of the effort in real projects?
>
> **Check:** Steps 2 and 3 (getting and preparing data). Practitioners often say that preparing data takes more time than building the model. If the data is poor, no clever algorithm can rescue it.

---

## 3.2 Data: The Fuel of AI

### Start with a question

If you wanted to teach a model to recognise ripe mangoes, would a million photos taken in the dark be better than a thousand good photos? Why?

### In plain words

**Data is the examples the model learns from.** Better, more varied examples usually make a better model.

### Key terms

| Term | In plain words | Example (house price) |
|------|----------------|-----------------------|
| **Dataset** | A collection of examples | A table of 1,000 sold houses |
| **Feature** | A fact about each example the model may use | Size, location, age |
| **Label** | The answer we want to predict (only in supervised learning) | The sale price |
| **Training data** | Examples used to learn | 700 of the houses |

### Types of data

| Type | Examples |
|------|----------|
| Structured (tables) | Spreadsheets, bank transactions |
| Text | Emails, books, web pages |
| Images and video | Photos, medical scans |
| Audio | Speech, music |
| Time series | Sensor readings, stock prices |

### Why data quality matters

A model learns whatever the data shows, including its mistakes. Common problems:

| Problem | Example | Result |
|---------|---------|--------|
| Too little data | Six emails for a spam filter | The model memorises accidents (Chapter 1) |
| Wrong labels | Spam marked as "not spam" | The model learns the wrong lesson |
| Missing groups | Face photos from only one region | The model fails on other people |
| Outdated data | Prices from ten years ago | Predictions no longer fit today |

**A rule worth remembering: garbage in, garbage out.**

### Splitting the data: why keep some back?

![Splitting a dataset into 70% training, 15% validation and 15% test](assets/dataset-split.png)
*Figure 3.2: Splitting a dataset. Source: created by our team (Stage 1).*

| Part | Purpose | Everyday comparison |
|------|---------|---------------------|
| Training set | The model learns from it | Textbook and practice questions |
| Validation set | Used to tune choices while building | A practice exam |
| Test set | Used once at the end for an honest score | The real exam |

**Rule:** the test set must never influence training. If it does, the final score is inflated (this mistake is called *data leakage*).

---

## 3.3 Algorithms and Models

### Start with a question

People use "algorithm" and "model" as if they were the same. They are not. What is the difference between a recipe and the cake?

### In plain words

An **algorithm** is the *method*. A **model** is the *result*. The learning algorithm studies data and produces a model; the model is then used for predictions.

| | Algorithm | Model |
|---|-----------|-------|
| What it is | A step-by-step method | What was learned |
| In the kitchen | The recipe | The finished cake |
| Example | "Count words and score them" (Chapter 1) | The score table |
| Changes when data changes? | No | Yes |

### Two basic kinds of prediction

| Task | Question it answers | Example |
|------|---------------------|---------|
| **Classification** | Which category? | Spam or not spam |
| **Regression** | What number? | The price of a house |

### Common algorithm families

| Family | Idea in one line | Good for |
|--------|------------------|----------|
| Linear models | Fit a straight line or weighted sum | Simple, explainable predictions |
| Decision trees | A flowchart of yes/no questions | Tabular data, explainable decisions |
| Nearest neighbours | "You are like your closest examples" | Small datasets |
| Neural networks | Many connected units learning patterns | Images, speech, language |

---

## 3.4 Machine Learning: Learning from Examples

### Start with a question

A child learns the word "dog" after seeing many dogs. Nobody wrote a rule. How can a computer do something similar with numbers?

### Three ways to learn

| Style | What the computer gets | Example | Where in this module |
|-------|------------------------|---------|----------------------|
| **Supervised learning** | Examples with correct labels | Photos labelled cat or dog | Chapters 1, 3, 5 |
| **Unsupervised learning** | Examples without labels; finds groups | Grouping customers by habits | Chapter 5 |
| **Reinforcement learning** | A world to act in, and rewards | A robot learning to walk | Chapter 6 |

### The learning loop

Almost all learning follows the same four steps:

1. **Predict.** The model makes a guess.
2. **Measure the error.** A number called the **loss** shows how wrong the guess was.
3. **Adjust.** Change the model slightly to reduce the loss.
4. **Repeat** with more examples until the loss stops improving.

### Worked example: finding the best number by walking downhill

Suppose the best value of a model setting *w* is 3, and we measure error with **loss = (w - 3)²**. The computer does not know this. It starts with a guess *w = 0*.

The *slope* of the loss tells which way is downhill. For this loss the slope is 2 × (w - 3). We update with a small step called the **learning rate** (here 0.1):

new w = old w - 0.1 × slope

| Round | w | Slope = 2(w-3) | Update | New w | Loss (w-3)² |
|:-----:|:-:|:--------------:|:------:|:-----:|:-----------:|
| 1 | 0 | -6 | 0 - 0.1×(-6) | 0.6 | 5.76 |
| 2 | 0.6 | -4.8 | 0.6 + 0.48 | 1.08 | 3.69 |
| 3 | 1.08 | -3.84 | 1.08 + 0.384 | 1.464 | 2.36 |

The loss keeps shrinking, and *w* moves toward 3. This method is called **gradient descent**. Real models do this for millions or billions of settings at once.

![Gradient descent: steps going downhill toward the lowest loss](assets/gradient-descent.png)
*Figure 3.3: Gradient descent. Source: created by our team (Stage 1).*

**Analogy: walking down a foggy hill.** You cannot see the valley, but you can feel which way the ground slopes under your feet, so you step downhill again and again.  
**Where the analogy breaks:** real loss landscapes have millions of dimensions, and the "valley" you reach may not be the lowest one.

### Overfitting and underfitting

![Three charts: underfitting (too simple), good fit, overfitting (memorises noise)](assets/fitting.png)
*Figure 3.4: Underfitting, good fit, and overfitting. Source: created by our team (Stage 1).*

| Situation | What it means | Everyday comparison | Typical sign |
|-----------|---------------|---------------------|--------------|
| **Underfitting** | The model is too simple to capture the pattern | Studying only the chapter titles | High error on training and new data |
| **Good fit** | Captures the real pattern | Understanding the topic | Low error on both |
| **Overfitting** | Memorises training examples, including noise | Memorising last year's answers | Low training error, high error on new data |

> **Pause and predict.** A model scores 99% on its training data but only 60% on the test set. What is the likely problem?
>
> **Check:** Overfitting. It learned the training examples (and their accidents) too well and does not generalise to new data.

---

## 3.5 Neural Networks and Deep Learning

### Start with a question

Your brain uses billions of simple cells connected together. Could a computer do something useful with a similar idea?

### In plain words

A **neural network** is many small calculators (neurons) joined in layers. Each connection has a *weight* (how strong it is). Learning means adjusting the weights.

![A neural network with an input layer, two hidden layers, and an output layer giving cat 0.92 and dog 0.08](assets/neural-network.png)
*Figure 3.5: Anatomy of a neural network. Source: created by our team (Stage 1).*

| Part | Role |
|------|------|
| Input layer | Receives the raw numbers (for example pixel values) |
| Hidden layers | Combine earlier signals to find patterns, from simple to complex |
| Output layer | Gives the result (for example: cat 0.92, dog 0.08) |
| Weights | The learned settings; training adjusts them |

**Deep learning** means neural networks with many hidden layers. Early layers may learn simple things (edges), later layers more complex things (eyes, faces). **Chapter 5 studies how a single neuron calculates and how different network designs work.**

---

## 3.6 How Modern Language AI Works

### Start with a question

When you type a question into a chatbot, it replies in fluent sentences. Does it look up an answer, or does it do something else?

### In plain words

A large language model (LLM) is a neural network trained to **predict the next small piece of text**, over and over. A long reply is built one piece at a time.

### Step 1: Tokens

Text is split into **tokens**: short pieces of words (for example "Under", "standing"). Each token becomes numbers the network can work with.

### Step 2: Next-token prediction

Given the text so far, the model gives a probability to every possible next token, then one is chosen. The new token is added, and the process repeats.

![A language model splits text into tokens and assigns probabilities to possible next tokens](assets/tokens-next-token.png)
*Figure 3.6: Tokens and next-token prediction. Source: created by our team (Stage 1).*

### Step 3: Attention

To choose well, the model must know which earlier words matter. In "The animal didn't cross the street because it was too tired", the word "it" refers to "animal", not "street". The **attention** mechanism helps the model give more weight to the relevant words (Vaswani et al., 2017).

![Attention: which words matter most when interpreting the word it](assets/attention.png)
*Figure 3.7: Attention. The percentages are illustrative. Source: created by our team (Stage 1).*

### How an LLM is built

| Stage | What happens |
|-------|--------------|
| Pre-training | The model learns next-token prediction on a very large collection of text (Brown et al., 2020). |
| Fine-tuning | It is trained further on examples of good question-and-answer behaviour. |
| Feedback training | Human ratings of answers are used to nudge the model toward preferred behaviour (Ouyang et al., 2022). |

### Important properties

- **It generates likely text, not verified facts.** This is why it can state false things in a confident tone (Chapter 8 calls this *hallucination*).
- **It does not "look up" your question** unless it is connected to a search tool.
- **It is fixed during a chat.** Your conversation does not retrain it.

---

## 3.7 Training vs Inference

### In plain words

**Training** is learning. **Inference** is using what was learned.

![Training: a large dataset changes the model weights. Inference: a prompt goes through the frozen model to give an answer](assets/training-vs-inference.png)
*Figure 3.8: Training vs inference. Source: created by our team (Stage 1).*

| | Training | Inference |
|---|----------|-----------|
| Purpose | Build or improve the model | Use the model |
| Model weights | Change | Fixed (frozen) |
| Cost | Very high (days to months of computing for large models) | Much lower per request |
| Who does it | AI developers | Every user, every time |
| Analogy | A student studying for years | The graduate answering a question |

---

## 3.8 Evaluating a Model

### Start with a question

A spam filter is "95% accurate". Is it good? Not necessarily. Imagine only 5 of 100 emails are spam. A filter that *never* flags anything is 95% accurate and completely useless. We need better measures.

### The confusion matrix

For a yes/no task, every prediction falls into one of four boxes.

![Confusion matrix with 40 true positives, 10 false negatives, 5 false positives and 45 true negatives, and the three formulas](assets/fig-3-2-confusion-matrix.png)
*Figure 3.9: A confusion matrix for a spam filter tested on 100 emails. Source: created by our team.*

| Box | Meaning |
|-----|---------|
| True positive (TP) | Spam correctly flagged |
| False negative (FN) | Spam missed |
| False positive (FP) | Real email wrongly flagged as spam |
| True negative (TN) | Real email correctly left alone |

### Key measures

| Measure | Formula | In words | Value for Figure 3.9 |
|---------|---------|----------|----------------------|
| Accuracy | (TP + TN) / total | Share of all predictions that were right | 85 / 100 = 85% |
| Precision | TP / (TP + FP) | When it says "spam", how often is it right? | 40 / 45 = 88.9% |
| Recall | TP / (TP + FN) | Of all real spam, how much did it catch? | 40 / 50 = 80% |

**Which matters more depends on the cost of mistakes.** For a spam filter, a false positive (a real email lost) may hurt more, so precision matters. For a cancer-screening tool, a false negative (a missed case) is dangerous, so recall matters.

---

## 3.9 Mission 1: Be the Learner

> **Goal:** feel what "training" is by finding the best setting by hand.  
> **Preparation:** Sections 3.4 and 3.8. A calculator or pen, 10 minutes.  
> **Task:** a tiny dataset of house sizes and prices (price in thousands). The model is **price = w × size**. Your job is to find the best *w*.

| House | Size (m²) | Real price |
|:-----:|:---------:|:----------:|
| A | 30 | 60 |
| B | 50 | 100 |
| C | 70 | 140 |

**Part A. Try three settings.** For each *w*, compute the predictions and the total error (add up the gaps between prediction and real price, ignoring the sign).

| w | Prediction A | Prediction B | Prediction C | Total error |
|:-:|:------------:|:------------:|:------------:|:-----------:|
| 1.5 | ____ | ____ | ____ | ____ |
| 2.0 | ____ | ____ | ____ | ____ |
| 2.5 | ____ | ____ | ____ | ____ |

**Part B. Use the best model.** What price does it predict for a 90 m² house? ____

**Part C. Think.** The same model predicts 400 for a 200 m² house. Should you trust it? Why or why not?

> **Observe:** which *w* gave the smallest total error?  
> **Reflect:** how is what you just did similar to what gradient descent does automatically?  
> **Feedback:** compare with the Answer Key (Mission 1).

---

## 3.10 Mission 2: Judge the Filter

> **Goal:** compute and interpret accuracy, precision and recall.  
> **Preparation:** Section 3.8. 10 minutes.  
> **Task:** Filter X was tested on 100 emails. Results: TP = 30, FN = 20, FP = 2, TN = 48.

**Part A.** Fill in the table.

| Measure | Calculation | Result |
|---------|-------------|:------:|
| Accuracy | ______ | ____ |
| Precision | ______ | ____ |
| Recall | ______ | ____ |

**Part B. Choose.** Compare Filter X with the filter in Figure 3.9 (precision 88.9%, recall 80%). A user says: "I hate losing real emails, but I can tolerate some spam." Which filter fits better? Why?

**Part C. The accuracy trap.** A filter is tested on 100 emails of which only 5 are spam. It predicts "not spam" for everything. What is its accuracy? What is its recall?

> **Observe:** which measure changed most between Filter X and the filter in Figure 3.9?  
> **Reflect:** why can a high accuracy hide a poor filter?  
> **Feedback:** compare with the Answer Key (Mission 2).

---

## 3.11 Common Misconceptions

| Misconception | Correction |
|---------------|------------|
| "More data always fixes everything." | Quantity helps only if the data is relevant, correct and varied. |
| "The model understands like a person." | It learns statistical patterns; understanding is debated. |
| "A chatbot learns from our conversation as we talk." | Deployed models are normally fixed unless retrained. |
| "High accuracy means a good model." | Accuracy can hide failures, especially when classes are unbalanced. |
| "Training and inference are the same." | Training changes the model; inference uses it. |

---

## 3.12 Quick Check

**Q1 (True/False).** The test set may be used to adjust the model while training.

**Q2 (True/False).** Overfitting means low error on training data but high error on new data.

**Q3 (True/False).** During inference, the model's weights change with each user request.

**Q4 (Multiple choice, one answer).** Which task is regression?
A. Deciding whether an email is spam. B. Predicting a house price. C. Sorting photos into cats and dogs. D. Deciding whether a tumour is malignant.

**Q5 (Multiple choice, one answer).** A model has precision 90% and recall 40%. What does this mean?
A. It rarely raises false alarms but misses many real cases. B. It catches almost all real cases. C. It is always wrong. D. It was never tested.

**Q6 (Multiple choice, one answer).** What does an LLM do at each step of writing a reply?
A. Looks up the full answer in a database. B. Predicts the next token from the text so far. C. Copies an answer from the user. D. Re-trains itself.

**Q7 (Short answer, 3 to 4 sentences).** Explain why preparing data often takes more effort than choosing an algorithm.

---

## 3.13 Summary, Connections and References

### Key takeaways

- The AI workflow runs from defining the problem to monitoring and improving. Data steps take much of the effort.
- Data quality limits model quality ("garbage in, garbage out"). Keep the test set separate.
- An algorithm is the method; a model is what is learned.
- Learning repeats: predict, measure the loss, adjust, repeat. Gradient descent adjusts in the downhill direction.
- Overfitting is memorising; underfitting is being too simple.
- Language models predict the next token; they do not verify facts.
- Training changes the model; inference uses it.
- Accuracy alone can mislead; use precision and recall too.

### Connections to other chapters

| Direction | Chapter | Link |
|-----------|---------|------|
| Builds on | Chapter 1 | Data, model, training and inference |
| Builds on | Chapter 2 | Limited-memory AI and generative AI |
| Leads to | Chapter 4 | An alternative: rules written by people |
| Leads to | Chapter 5 | Neural networks and Big Data in depth |
| Leads to | Chapter 6 | Learning from rewards |
| Leads to | Chapter 8 | Hallucination and data bias |

### How this chapter will be reused

| Resource | Planned use |
|----------|-------------|
| **Study Guide** | Sections 3.1 to 3.8 are the reading text; Missions 1 and 2 are hands-on activities. |
| **Test Bank** | Metric calculations, overfitting scenarios and workflow ordering become exam-style items. |
| **PPT Slides** | The workflow, the downhill walk, the confusion matrix and the fitting chart become step-by-step visuals. |
| **Video Tutorial** | A video that animates gradient descent and walks through the confusion matrix calculation. |

---

## Answer Key

**Mission 1: Be the Learner**

Part A:

| w | Prediction A | Prediction B | Prediction C | Total error |
|:-:|:------------:|:------------:|:------------:|:-----------:|
| 1.5 | 45 | 75 | 105 | 15 + 25 + 35 = 75 |
| 2.0 | 60 | 100 | 140 | 0 |
| 2.5 | 75 | 125 | 175 | 15 + 25 + 35 = 75 |

Part B: with *w* = 2.0, price = 2.0 × 90 = **180**.
Part C: be careful. The model only saw sizes from 30 to 70 m². 200 m² is far outside that range, and the real relationship may change (for example, very large houses cost differently). A model is most reliable near the data it learned from.
*Observe/Reflect:* *w* = 2.0 gave zero error. Gradient descent also tries values and moves toward lower error, but automatically and in tiny steps.

**Mission 2: Judge the Filter**

Part A (TP 30, FN 20, FP 2, TN 48):

| Measure | Calculation | Result |
|---------|-------------|:------:|
| Accuracy | (30 + 48) / 100 | 78% |
| Precision | 30 / (30 + 2) | 93.75% (about 93.8%) |
| Recall | 30 / (30 + 20) | 60% |

Part B: Filter X has higher precision (93.8% vs 88.9%), meaning fewer real emails wrongly flagged, so it fits a user who hates losing real emails. The cost is lower recall (60% vs 80%): more spam gets through.
Part C: accuracy = 95 / 100 = **95%**, but recall = 0 / 5 = **0%**. It catches no spam at all, which is why accuracy alone is misleading.

**Quick Check**

1. **False.** The test set must stay unseen; using it causes data leakage.
2. **True.**
3. **False.** Weights are frozen during inference.
4. **B.**
5. **A.** High precision, low recall.
6. **B.**
7. *Key points:* real data is messy (errors, missing values, inconsistent formats); the model can only learn what the data shows; fixing and splitting data correctly prevents misleading scores; standard algorithms are already available while data is specific to the project.

---

## Glossary

| Term | Meaning |
|------|---------|
| Accuracy | Share of all predictions that are correct. |
| Algorithm | A step-by-step method; for learning, the method that builds a model. |
| Attention | A mechanism that lets a model weigh which earlier words matter most. |
| Classification | Predicting a category. |
| Confusion matrix | A table of true/false positives and negatives. |
| Data leakage | Test information accidentally used in training. |
| Dataset | A collection of examples. |
| Feature | A fact about an example used by the model. |
| Gradient descent | Repeatedly adjusting settings in the direction that lowers the loss. |
| Inference | Using a trained model on new data. |
| Large language model (LLM) | A neural network trained to predict the next token in text. |
| Learning rate | The size of each adjustment step. |
| Loss | A number measuring how wrong the model's predictions are. |
| Overfitting | Memorising training data so that new data is handled badly. |
| Precision | Of the items flagged positive, the share that really are. |
| Recall | Of all real positives, the share that were found. |
| Regression | Predicting a number. |
| Token | A small piece of text used by language models. |
| Underfitting | A model too simple to capture the pattern. |

---

## References

1. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press. https://www.deeplearningbook.org/
2. Google for Developers. *Machine Learning Crash Course*. https://developers.google.com/machine-learning/crash-course
3. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning* (2nd ed.). Springer. https://www.statlearning.com/
4. Vaswani, A., et al. (2017). Attention is all you need. *Advances in Neural Information Processing Systems*, 30. https://arxiv.org/abs/1706.03762
5. Brown, T. B., et al. (2020). Language models are few-shot learners. *arXiv*:2005.14165. https://arxiv.org/abs/2005.14165
6. Ouyang, L., et al. (2022). Training language models to follow instructions with human feedback. *arXiv*:2203.02155. https://arxiv.org/abs/2203.02155
7. Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson. https://aima.cs.berkeley.edu/
8. Sanderson, G. (3Blue1Brown). *But what is a neural network?* (video). https://www.youtube.com/watch?v=aircAruvnKk

> Figures 3.1 and 3.9 were created for Stage 2. Figures 3.2 to 3.8 are team-made figures from Stage 1.
