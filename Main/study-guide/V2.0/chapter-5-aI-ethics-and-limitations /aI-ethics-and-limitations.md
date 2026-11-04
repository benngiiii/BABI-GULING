# Chapter 5: AI Ethics and Limitations

**Team:** Babi Guling | **Module:** AI Overview | **Version:** 2.0
**Audience:** Learners with no technical background in AI
**Estimated time:** 3 to 4 hours (including activities)
**How to work through it:** Predict, read, try the activity, check yourself, then compare with the answers.

---

## Table of Contents

1. [Where We Are](#where-we-are)
2. [Learning Outcomes](#learning-outcomes)
3. [Chapter Map](#chapter-map)
4. [Prerequisites and Framing](#prerequisites-and-framing)
5. [5.1 Bias](#51-bias)
6. [5.2 Privacy](#52-privacy)
7. [5.3 Hallucinations](#53-hallucinations)
8. [5.4 Responsible AI](#54-responsible-ai)
9. [5.5 Discussion Scenario and Synthesis](#55-discussion-scenario-and-synthesis)
10. [5.6 Chapter Summary and Self-Check](#56-chapter-summary-and-self-check)
11. [Glossary](#glossary)
12. [References](#references)

---

## Where We Are

In Chapter 4 you saw AI at work in healthcare, education, transportation, everyday life, and finance and trading. In every one of those fields AI brings real benefits, and in every one of them it can also go wrong.

This chapter asks the questions that come with that power:

- When does an AI system treat some people worse than others?
- What happens to the personal information that AI systems collect and receive?
- Why does AI sometimes state false things with complete confidence?
- How can people build and use AI responsibly?

## Learning Outcomes

By the end of this chapter, learners will be able to:

- **Explain** what bias, privacy risk, and hallucination mean in an AI context.
- **Identify** where in an AI system's life cycle bias can enter.
- **Calculate** a simple fairness check (selection rate and the four-fifths rule) and interpret the result.
- **Trace** how "anonymous" data can be linked back to a person, and suggest a safer way to share it.
- **Verify** an AI-generated claim using a short checking routine, and spot errors in an AI summary.
- **Apply** responsible AI principles to a realistic scenario and justify a decision.

## Chapter Map

| Section | Topic | What you will do | Time |
|---|---|---|---|
| 5.1 | Bias | Predict, read cases, run a fairness calculation (by hand and in code), find a mistake | 70 min |
| 5.2 | Privacy | Predict, link "anonymous" records to people, make the data safer | 40 min |
| 5.3 | Hallucinations | Predict, verify a fake citation, find errors in an AI summary | 45 min |
| 5.4 | Responsible AI | Apply a checklist to a realistic scenario | 30 min |
| 5.5 | Discussion and synthesis | Discuss a real court case, then classify mixed situations | 40 min |
| 5.6 | Summary and self-check | Review key ideas and test yourself | 15 min |

## Prerequisites and Framing

This chapter builds on terms introduced earlier in the module. They are used here with the same meaning and are not redefined:

| Term | Where it was introduced |
|---|---|
| AI, model, training, inference, labels | Chapter 1, §1.4 *Basic AI Terminology* |
| Generative AI | Chapter 2, §2.4 *Machine Learning and Generative AI* |
| Training data | Chapter 3, §3.3 *Data: The Fuel of AI* |
| Language models (how they produce text) | Chapter 3, §3.7 *How Modern Language AI Works* |
| Training versus inference | Chapter 3, §3.8 *Training vs. Inference* |

Terms that are **specific to ethics and limitations** (for example *proxy variable*, *impact ratio*, *re-identification*, *hallucination*) are defined where they first appear and collected in the [Glossary](#glossary).

> **Core idea of this chapter:** AI systems do not have opinions or intentions. They reflect the data, goals, and choices of the people who build and use them. Ethics is about those choices.

---

## 5.1 Bias

### 5.1.1 Predict first (2 minutes)

A hiring tool is **90% accurate overall**. Do you think it could still treat some groups of applicants unfairly? Write down yes or no and one reason. We return to your answer in §5.1.4.

### 5.1.2 What is bias?

In everyday language, *bias* means unfair preference. In AI, **bias** means that a system produces results that are **systematically** less accurate or less favourable for some people or groups than for others.

Two words in that definition matter:

- **Systematically:** the unfairness follows a pattern. It is not random bad luck.
- **Groups:** bias is usually discovered by comparing results across groups (for example by gender, age, skin tone, language, or region).

Bias is not always intentional. Most harmful AI bias happens even when the builders had good intentions.

### 5.1.3 Where does bias come from?

Bias can enter at several stages of an AI system's life cycle:

![Flowchart of the AI life cycle (collect data, label data, train model, test model, deploy and use) showing where each type of bias can enter](assets/bias-occurence-diagram.png)

*Figure 5.1. Where bias can enter an AI system's life cycle.*

If the image does not display in your viewer, use this table instead (it contains the same information):

| Stage | Type of bias | Plain-language meaning | Example |
|---|---|---|---|
| Collect data | **Historical bias** | The world was unfair, so the data is too | Past hiring records favour one gender |
| Collect data | **Sampling bias** | Some groups are barely in the data | A face dataset with mostly light-skinned faces |
| Label data | **Labelling bias** | Human labellers add their own assumptions | Labelling certain dialects as "rude" |
| Train model | **Proxy variable** | A harmless-looking input correlates with a protected trait | Postcode standing in for ethnicity |
| Test model | **Measurement bias** | Success is only checked on a convenient group | Testing accuracy overall, not per group |
| Use model | **Feedback loop** | Biased outputs create new biased data | Police sent to a "high-crime" area record more crime there |

**Terms defined:**

- **Protected characteristic:** a trait that laws or ethics say should not be used to treat people unfairly, such as race, sex, religion, age, or disability.
- **Proxy variable:** an input that is not itself a protected characteristic but is strongly linked to one.
- **Feedback loop:** when a system's outputs influence the data it later learns from, which can amplify an original error.

### 5.1.4 Real-world evidence

| Case | What happened | Lesson |
|---|---|---|
| **Gender Shades (2018)** | Researchers tested commercial facial-analysis systems and found much higher error rates for darker-skinned women than for lighter-skinned men (Buolamwini & Gebru, 2018). | Overall accuracy can hide large gaps between groups. |
| **Healthcare risk algorithm (2019)** | An algorithm used to decide who gets extra care used past healthcare *spending* as a stand-in for health *need*. Because less money had been spent on Black patients with the same level of illness, it under-estimated their needs (Obermeyer et al., 2019). | A proxy variable (cost) quietly encoded unequal access to care. |
| **Recruiting tool (reported 2018)** | Reuters reported that Amazon abandoned an experimental hiring tool that learned to downgrade résumés associated with women, because it was trained on past, male-dominated hiring (Dastin, 2018). | Historical bias in training data is reproduced by the model. |

**Back to your prediction (§5.1.1).** Yes, a tool can be 90% accurate overall and still be unfair. If one group is small in the data, the tool can be wrong for that group most of the time while the overall number still looks excellent. This is why fairness checks compare results **group by group**.

### 5.1.5 Worked example: checking a hiring tool for unequal outcomes

**Scenario.** A company uses an AI tool to shortlist job applicants. You are asked to check whether it treats two groups, Group A and Group B, fairly. (The numbers below are invented for teaching.)

| | Applicants | Shortlisted by the tool |
|---|---|---|
| Group A | 100 | 60 |
| Group B | 100 | 30 |

We will use a common screening measure called the **four-fifths rule**.

**Terms defined:**

- **Selection rate:** the share of a group that receives the favourable outcome. Formula: `shortlisted ÷ applicants`.
- **Impact ratio:** a group's selection rate divided by the **highest** group's selection rate.
- **Four-fifths (80%) rule:** a rule of thumb from US employment guidance. If one group's selection rate is **less than 80% (4/5)** of the highest group's rate, this is treated as a warning sign of possible adverse impact (US EEOC et al., 1978, 29 CFR §1607.4(D)). It is a **screening indicator, not proof** of discrimination.

**Step 1: Calculate each group's selection rate.**

- Group A: 60 ÷ 100 = **0.60** (60%)
- Group B: 30 ÷ 100 = **0.30** (30%)

**Step 2: Identify the highest rate.** Group A, at 0.60.

**Step 3: Divide each group's rate by the highest rate.** This is the impact ratio.

- Group B: 0.30 ÷ 0.60 = **0.50**

**Step 4: Compare to the threshold of 0.80.**

- 0.50 is less than 0.80, so the tool **fails** the screening check. Group B is shortlisted at half the rate of Group A.

**Step 5: Decide what to do next.** The result is a warning, not a verdict. A sensible next step is to investigate: Which inputs does the model use? Are any of them proxies? Was it trained on biased historical hiring decisions? Do qualified applicants in Group B get rejected more often?

**Why rates, not counts?** Suppose Group A has 100 applicants with 60 shortlisted, and a smaller Group B has 20 applicants with 12 shortlisted. Group B has far fewer shortlisted people (12 against 60), but its selection rate is 12 ÷ 20 = 0.60, the same as Group A. The impact ratio is 1.00. Comparing raw counts would wrongly suggest unfairness, so always compare **rates**.

You can reproduce the main calculation with this short Python script:

```python
# Fairness check: selection rates and the four-fifths rule
groups = {
    "Group A": {"applicants": 100, "shortlisted": 60},
    "Group B": {"applicants": 100, "shortlisted": 30},
}

# Step 1: selection rate for each group
rates = {name: g["shortlisted"] / g["applicants"] for name, g in groups.items()}

# Step 2: highest rate
highest = max(rates.values())

# Steps 3 and 4: impact ratio and comparison with 0.8
for name, rate in rates.items():
    ratio = rate / highest
    status = "PASS" if ratio >= 0.8 else "FLAG for review"
    print(f"{name}: selection rate = {rate:.2f}, impact ratio = {ratio:.2f} -> {status}")
```

**Expected output:**

```text
Group A: selection rate = 0.60, impact ratio = 1.00 -> PASS
Group B: selection rate = 0.30, impact ratio = 0.50 -> FLAG for review
```

> **Limitation of this check.** The four-fifths rule only compares outcome rates. It does not tell you *why* the gap exists, and a tool can pass this check while still making more *mistakes* for one group. There are several competing definitions of fairness, and they cannot all be satisfied at once (Chouldechova, 2017). Real audits use several measures plus human judgment.

### 5.1.6 Activity 5.1: Fairness detective

**Goal:** Calculate and interpret a fairness check, recognise proxy variables, and catch a common calculation mistake.

**Preparation:** A calculator (or Python, for Task D). Have the steps in §5.1.5 open for reference. Time: about 30 minutes.

**Task**

**Part A: Calculation.** A different company's tool produces these results:

| | Applicants | Shortlisted |
|---|---|---|
| Group C | 50 | 20 |
| Group D | 80 | 36 |

1. Calculate the selection rate for each group.
2. Calculate the impact ratio for each group.
3. Does the tool pass the four-fifths rule? Explain in one sentence.

**Part B: Spot the proxy.** A bank builds a loan-approval model. It is **not** given any information about race or gender, but it **is** given the applicant's postcode, first language, and job title.

1. Which input might act as a proxy variable? Why?
2. Name one way the team could check whether the proxy is causing unfair results.

**Part C: Find the mistake.** A classmate worked on Part A and wrote:

> "Group C: 20 ÷ 50 = 0.40. Group D: 36 ÷ 80 = 0.45. Impact ratio = 0.45 ÷ 0.40 = 1.125. That is above 0.8, so it passes."

1. What step is wrong?
2. Would this mistake ever change the conclusion? Test it on the Group A and Group B data from §5.1.5.

**Part D: Predict, then run.** Copy the Python script from §5.1.5. Before running, **predict** the output for each change, then run it to check:

1. Change Group B's `shortlisted` from 30 to 45.
2. Change Group B's `shortlisted` from 30 to 50.

**Part E: Reflect.** In 3 to 4 sentences, explain why "we removed the sensitive column from the data" does not guarantee a fair model.

**Observation:** While doing Parts A to D, note which numbers surprised you and where you needed to re-read the steps.

**Reflection:** Part E above, plus one sentence on what you would investigate next if a real tool failed the check.

**Feedback (answers and expected outcomes)**

**Part A**

1. Group C: 20 ÷ 50 = **0.40**. Group D: 36 ÷ 80 = **0.45**.
2. The highest rate is Group D (0.45). Impact ratio for Group C = 0.40 ÷ 0.45 ≈ **0.89**. Group D = 1.00.
3. 0.89 is above 0.80, so the tool **passes** this screening check; the gap is small enough that this rule does not flag it. (A good answer also notes that passing does not prove the tool is fair, because the rule ignores error rates and the reasons for the gap.)

**Part B**

1. **Postcode** is the strongest candidate, because neighbourhoods are often strongly linked to ethnicity and income through historical patterns. First language can act as a proxy for national origin. Job title may be a weaker proxy for gender in some fields. *Accept any well-reasoned answer.*
2. Acceptable checks: compare approval rates and error rates across groups (using group information held *only for auditing*); test the model without the suspected proxy and see whether outcomes change; review whether the input is truly relevant to repayment ability.

**Part C**

1. The classmate divided the **higher** rate by the **lower** one (0.45 ÷ 0.40). The impact ratio must divide each group's rate by the **highest** rate, so the correct value is 0.40 ÷ 0.45 ≈ 0.89.
2. Here the conclusion (pass) happens to stay the same, but the method can fail badly. On the Group A and B data, 0.60 ÷ 0.30 = 2.0, which would "pass" even though the correct ratio is 0.30 ÷ 0.60 = 0.50 and the tool should be flagged.

**Part D**

1. Group B's rate = 0.45; impact ratio = 0.45 ÷ 0.60 = 0.75 → **FLAG for review**.
2. Group B's rate = 0.50; impact ratio = 0.50 ÷ 0.60 ≈ 0.83 → **PASS**.

Expected printed lines for Group B: `selection rate = 0.45, impact ratio = 0.75 -> FLAG for review` and `selection rate = 0.50, impact ratio = 0.83 -> PASS`. Lesson: the threshold turns a small change in numbers into a different outcome, which is why the result is a warning to investigate, not a final judgment.

**Part E** *(Model answer)*: Other inputs can still carry the same information (proxy variables), and the historical data may already reflect unfair past decisions. Removing the column also makes it impossible to measure whether groups are treated differently, so unfairness can become harder to detect, not easier.

**Teacher check:** Learners show understanding if they (a) compute rates correctly, (b) divide by the highest rate and interpret relative to 0.8, and (c) recognise that fairness requires investigating causes, not only removing columns.

### 5.1.7 Ways to reduce bias (overview)

| Approach | What it means | Example |
|---|---|---|
| Better data | Collect more representative data | Add faces with a wider range of skin tones |
| Per-group testing | Report accuracy for each group, not just overall | Publish results by gender and skin tone |
| Documentation | Describe a model's intended use and limits | **Model cards** (Mitchell et al., 2019); **datasheets for datasets** (Gebru et al., 2021) |
| Human oversight | A person can review and override decisions | Manager reviews all automated rejections |
| Ongoing monitoring | Re-check after launch | Re-run the fairness check every quarter |

### 5.1.8 Check your understanding

Try these without looking back, then compare with the answers below.

1. True or false: if a model never receives a protected characteristic as an input, it cannot be biased.
2. A tool has an impact ratio of 0.65. What does this tell you, and what should you do next?
3. A face dataset contains mostly light-skinned faces. Which stage of the life cycle and which type of bias is this?

**Answers**

1. **False.** Proxy variables (such as postcode) can carry the same information, and historical data can already be unfair.
2. It is below 0.80, so it is a **warning sign** of possible adverse impact, not proof. Next, investigate the inputs, the training data, and error rates by group.
3. **Collect data stage, sampling bias.**

---

## 5.2 Privacy

### 5.2.1 Predict first (2 minutes)

A hospital removes the **names** from a table of patient records and publishes it for researchers. The table still shows each patient's age, postcode, and job. Is the data now truly anonymous? Write yes or no and a reason. We return to this in §5.2.4.

### 5.2.2 What is privacy in AI?

**Privacy** is a person's ability to control information about themselves. **Personal data** (also called **personally identifiable information, PII**) is any information that can identify a person, directly (name, ID number, face) or indirectly (a combination of age, postcode, and job).

AI raises privacy concerns because it:

1. **Is trained on large amounts of data**, which may include personal information collected without clear consent.
2. **Can memorise** parts of its training data. Researchers have shown that large language models can sometimes be prompted to reproduce text from their training sets, including personal details (Carlini et al., 2021).
3. **Can infer sensitive facts** (such as health conditions) from innocent-looking data.
4. **Receives user input.** Anything typed into an AI tool may be stored or used according to that service's policy.

### 5.2.3 Risks and protections

| Risk | Plain-language description | Protection |
|---|---|---|
| Data collection without consent | Data gathered for one purpose is reused for another | Collect only what is needed (**data minimisation**); get clear consent |
| Memorisation / leakage | The model repeats private training text | Remove personal data before training; test for leakage |
| Re-identification | "Anonymous" data is matched with other data to find the person | Make data less specific (**generalisation**) or add noise (**differential privacy**) |
| Oversharing by users | A user pastes confidential text into a chatbot | Read the tool's data policy; never paste secrets or personal data |

**Terms defined:**

- **Data minimisation:** collecting and keeping only the data that is necessary for a stated purpose.
- **Anonymisation:** removing identifying details. It is hard to do perfectly, which is why re-identification is a risk.
- **Re-identification:** working out who a record belongs to by matching it with other information.
- **Generalisation:** making data less specific so that many people look alike, for example replacing an exact age with an age band.
- **Differential privacy:** a technique that adds carefully measured random noise so that results reveal patterns about a group without revealing facts about any one individual.

**Legal context:** Laws such as the EU's General Data Protection Regulation (GDPR) give people rights over their personal data, including rights of access and erasure, and require a lawful basis for processing (European Union, 2016).

### 5.2.4 Worked example: how "anonymous" data is linked back to people

**Scenario.** A hospital releases this table after deleting the names. A community choir also has a public member list. (All data below is invented for teaching.)

**Hospital table (names removed)**

| Record | Age | Postcode | Job | Diagnosis |
|---|---|---|---|---|
| R1 | 34 | 1001 | Teacher | Asthma |
| R2 | 37 | 1002 | Teacher | Migraine |
| R3 | 52 | 1001 | Chef | Diabetes |
| R4 | 55 | 1003 | Chef | Hypertension |
| R5 | 29 | 2001 | Nurse | Anxiety |
| R6 | 26 | 2002 | Nurse | Back pain |

**Public choir list**

| Name | Age | Postcode | Job |
|---|---|---|---|
| Budi | 34 | 1001 | Teacher |
| Citra | 37 | 1002 | Teacher |
| Chen | 52 | 1001 | Chef |
| Dodi | 55 | 1003 | Chef |
| Ana | 29 | 2001 | Nurse |
| Maya | 26 | 2002 | Nurse |

**Step 1: Pick the shared columns.** Both tables contain Age, Postcode, and Job.

**Step 2: Match.** Budi is 34, lives in 1001, and is a Teacher. Only R1 has that exact combination, so Budi's diagnosis is **Asthma**.

**Step 3: Repeat.** Citra matches R2, Chen matches R3, Dodi matches R4, Ana matches R5, and Maya matches R6. **All six patients are re-identified**, even though no names were in the hospital table.

**Step 4: Make the data safer by generalisation.** Replace exact age with a decade band, and the four-digit postcode with its first digit:

| Record | Age band | Postcode area | Job |
|---|---|---|---|
| R1, R2 | 30s | 1xxx | Teacher |
| R3, R4 | 50s | 1xxx | Chef |
| R5, R6 | 20s | 2xxx | Nurse |

Now every combination fits **two** records. Matching Budi gives two possible diagnoses (Asthma or Migraine), so an outsider cannot tell which is his.

> **Limitation.** Generalisation helps only if the people in each group do not share the same sensitive value. If R1 and R2 both had asthma, an outsider would still learn Budi's diagnosis. Generalising also makes the data less precise, so researchers lose some detail. Privacy always involves a trade-off.

**Back to your prediction (§5.2.1).** No. Removing names is not enough, because a combination of ordinary details (age, postcode, job) can be unique to one person.

### 5.2.5 Activity 5.2: Linkage detective

**Goal:** Experience how re-identification works and practise protecting data and user input.

**Preparation:** The two tables in §5.2.4 (you may cover the worked steps and try first). Time: about 25 minutes.

**Task**

**Part A: Match.** Without reading Steps 2 and 3, match each choir member to a hospital record. Write each person's diagnosis.

**Part B: Test a different release.** The hospital instead releases only **Age band (decade)** and **Job**, with no postcode. Count how many records share each combination. Can you still tell which diagnosis belongs to Ana?

**Part C: The clinic scenario.** You work for a clinic. A colleague wants to paste a patient's full name, date of birth, and symptoms into a public AI chatbot to "help draft a letter faster."

1. Identify two privacy risks.
2. Suggest a safer way to get help with the letter.

**Observation:** Note how many columns you needed before each person became unique.

**Reflection:** In 2 to 3 sentences, explain why a dataset with no names can still reveal who someone is.

**Feedback (answers and expected outcomes)**

**Part A:** Budi → Asthma; Citra → Migraine; Chen → Diabetes; Dodi → Hypertension; Ana → Anxiety; Maya → Back pain.

**Part B:** Combinations: 30s Teacher (R1, R2), 50s Chef (R3, R4), 20s Nurse (R5, R6). Each is shared by two records. Ana is a 20s Nurse, so she could be R5 (Anxiety) or R6 (Back pain). An outsider cannot tell which, so the release is safer than the original. *(Note: the diagnoses still differ within each pair, which is why generalisation works here.)*

**Part C**

1. Possible risks: the data may be stored or used for training under the provider's terms; it may be exposed to people without authorisation; it may breach the clinic's policies or health-privacy law; the patient did not consent to this use.
2. Safer options: remove all identifying details and use placeholders such as "[Patient]"; use an approved tool covered by the clinic's data agreement; or write the sensitive parts manually.

**Reflection (model answer):** Ordinary details such as age, postcode, and job can be unique in combination, so anyone who has another list containing the same details can match the records and recover identities.

### 5.2.6 Check your understanding

1. Name two ways AI systems can create privacy risks.
2. True or false: deleting names from a dataset makes it anonymous.
3. In one sentence, what is data minimisation?

**Answers**

1. Any two of: training on personal data without consent; memorising and repeating training data; inferring sensitive facts; storing or reusing what users type in.
2. **False.** Remaining details can be linked to other data (re-identification).
3. Collecting and keeping only the data that is necessary for a stated purpose.

---

## 5.3 Hallucinations

### 5.3.1 Predict first (2 minutes)

You ask an AI chatbot a question it has no reliable information about. What do you think it will do: say "I don't know", or something else? Write your guess. We return to this in §5.3.2.

### 5.3.2 What is a hallucination?

In AI, a **hallucination** is an output that is **fluent and confident but false, made up, or unsupported** by the source it should rely on (Ji et al., 2023).

**Why does it happen?** As explained in Chapter 3 (§3.7), a language model generates text by predicting which words are likely to come next. It is optimised to produce **plausible** text, not to check **truth**. When it lacks information, it may still generate something that *sounds* right.

**Back to your prediction (§5.3.1).** Often the model does not say "I don't know". It may produce a confident, fluent answer anyway, which is exactly what makes hallucinations dangerous.

**Terms defined:**

- **Grounding:** connecting a model's answer to trusted sources, for example by letting it retrieve documents and cite them.
- **Fabricated citation:** a reference that looks real (author, title, journal) but does not exist.

### 5.3.3 Common types

| Type | Example |
|---|---|
| Made-up facts | Stating a wrong date or statistic with confidence |
| Fabricated sources | Inventing a court case, paper, or URL |
| Wrong reasoning | A maths or logic answer that looks neat but is incorrect |
| Unfaithful summary | A summary that adds or changes details not in the original document |

### 5.3.4 Worked example: verifying an AI-generated claim

**Scenario.** You ask an AI assistant for a source on a claim, and it replies (this citation is invented for teaching):

> "According to Henderson & Zhou (2019), published in the *Journal of Applied Cognitive Ethics*, 87% of students prefer AI tutors."

**Step 1: Flag it.** It contains specific details (names, year, journal, percentage). Specific does not mean true.

**Step 2: Search the exact title and authors** in a scholarly database or a search engine.

**Step 3: Check the journal exists** and whether that article, volume, and page are listed.

**Step 4: Check the claim inside the source** (if found). Does the paper actually report 87%?

**Step 5: Decide and record.**

- *Not found anywhere* → treat as **likely fabricated**; do not cite or use it.
- *Found but says something different* → use what the real source says.
- *Found and matches* → cite the **original source**, not the AI.

**Rule of thumb:** *Trust, but verify; the more important the decision, the more you verify.*

### 5.3.5 Reducing the risk

- Ask the AI to **cite sources, then check them yourself.** A link or reference from an AI is not proof; it can also be invented.
- Ask for **uncertainty**: "If you are unsure, say so."
- Provide the source text and ask the AI to answer **only from that text.**
- Cross-check with a second, independent source.
- Keep a **human in the loop** for high-stakes uses (legal, medical, financial).

**Term defined:** **Human in the loop** means a person reviews and can correct the AI's output before it is used for something important.

### 5.3.6 Activity 5.3: Spot the hallucination

**Goal:** Practise comparing an AI summary with its source and writing a prompt that reduces hallucination.

**Preparation:** Read the source text first, then the AI summary. Have the types table (§5.3.3) open. Time: about 25 minutes. (Both texts are invented for teaching.)

**Source text**

> Riverside Library will extend its weekend opening hours from 1 December. The library will open 9 a.m. to 6 p.m. on Saturdays and 10 a.m. to 4 p.m. on Sundays. The change follows a survey of 400 residents. The library's budget is unchanged. Chief librarian Maria Santos said the extra hours are a trial for six months.

**AI summary**

> Riverside Library will extend its weekend hours from 1 December, opening 9 a.m. to 8 p.m. on both Saturdays and Sundays. After a survey of 4,000 residents, the council increased the library's budget by 10%. Chief librarian Maria Santos said the extension is permanent.

**Task**

**Part A: Find the errors.** Compare the summary with the source, sentence by sentence. List every claim in the summary that the source does not support. (Hint: there are four.)

**Part B: Classify.** Which type from §5.3.3 is each error? Which one do you think could cause the most harm to a reader, and why?

**Part C: Write a better prompt.** Write one prompt that asks an AI to summarise the source text in a way that reduces the chance of these errors.

**Part D: Quick check.** An AI summary of a news article says: "The mayor announced a 20% tax cut." You have the original article, and it never mentions a tax cut. What type of hallucination is this, and what two steps do you take before sharing the summary?

**Observation:** Note which errors were easy to spot and which you almost missed. Did the fluent wording make any of them look believable?

**Reflection:** In 2 to 3 sentences, explain why a summary can be dangerous even when most of it is correct.

**Feedback (answers and expected outcomes)**

**Part A:** The four unsupported claims are:
1. Hours: "9 a.m. to 8 p.m. on both Saturdays and Sundays" (source: Saturday 9 to 6, Sunday 10 to 4).
2. Survey size: "4,000 residents" (source: 400).
3. Budget: "the council increased the library's budget by 10%" (source: budget unchanged; no council or percentage mentioned).
4. Permanence: "permanent" (source: a six-month trial).

**Part B:** All four are **unfaithful summary** errors (details added or changed). Each is a valid choice for "most harmful" if reasoned: wrong hours could make someone arrive when the library is closed; the false budget claim could mislead public opinion. *Accept well-reasoned answers.*

**Part C** *(Model answer)*: "Summarise the text below in three sentences. Use only facts stated in the text. Do not add numbers or reasons that are not in it. If something is not stated, write 'not stated'. [paste source text]"

**Part D:** An **unfaithful summary** (an unsupported added detail). Steps: re-read the original and compare; re-run the summary with the instruction "only use facts stated in the article"; check another news source; do not share until verified.

**Reflection (model answer):** Readers tend to trust a whole summary when most of it matches, so one wrong detail slips through. Because hallucinations are fluent and confident, they look just like correct statements.

### 5.3.7 Check your understanding

1. Why can a language model give a confident answer that is false?
2. A reference an AI gave you cannot be found in any database. What should you do?
3. True or false: if an AI gives you a web link for a claim, the claim is verified.

**Answers**

1. It is trained to predict plausible next words, not to check whether the statement is true.
2. Treat it as likely fabricated; do not cite or use it, and look for a real source.
3. **False.** The link can be invented or may not say what the AI claims. Open it and check.

---

## 5.4 Responsible AI

### 5.4.1 Predict first (2 minutes)

When an AI system makes a harmful mistake, who is responsible: the AI, the company that built it, or the person who used it? Write your answer. We test it again in §5.5.

### 5.4.2 What is responsible AI?

**Responsible AI** means designing, building, and using AI in ways that are safe, fair, transparent, and accountable, and that respect human rights. It turns the concerns in §5.1 to §5.3 into practical commitments.

Many organisations have published similar principles. The OECD AI Principles (2019) and the NIST AI Risk Management Framework (2023) are widely referenced starting points.

### 5.4.3 Core principles

| Principle | Meaning | Question to ask |
|---|---|---|
| **Fairness** | Treat people and groups equitably | Have we tested results across groups? |
| **Transparency** | Be open about when and how AI is used | Do users know AI is involved? |
| **Explainability** | Be able to give understandable reasons for outputs | Can we explain why this decision was made? |
| **Privacy and security** | Protect data and systems | Do we collect only what we need? |
| **Accountability** | A person or organisation is answerable for outcomes | Who is responsible if it goes wrong? |
| **Reliability and safety** | The system works as intended, including in unusual cases | What happens when it fails? |
| **Human oversight** | People can review, challenge, and override | Can a human step in? |

**Term defined:**

- **Accountability:** the idea that humans and organisations, not "the algorithm," are responsible for outcomes.

### 5.4.4 A simple pre-use checklist

```text
Before using AI for a task, ask:
[ ] What is the purpose, and is AI appropriate for it?
[ ] What could go wrong, and who could be harmed?
[ ] Is any personal or confidential data involved?
[ ] Have outputs been checked for accuracy and bias?
[ ] Is a human reviewing high-stakes outputs?
[ ] Is it clear to others that AI was used?
[ ] Who is accountable, and how can someone appeal a decision?
```

### 5.4.5 Regulation snapshot

Governments are introducing rules. For example, the EU AI Act (Regulation (EU) 2024/1689) takes a **risk-based approach**: it bans a small set of practices, sets stricter requirements for **high-risk** uses (its list includes some uses in employment, such as recruitment, and in access to essential services, such as assessing creditworthiness), and sets lighter requirements for lower-risk uses (European Union, 2024). The full text is available from the [official EUR-Lex page](https://eur-lex.europa.eu/eli/reg/2024/1689/oj). Learners should check the rules that apply in their own country and sector, as these are changing.

### 5.4.6 Activity 5.4: Apply the principles

**Goal:** Use the seven principles and the checklist to review a realistic AI use and propose fixes.

**Preparation:** Have §5.4.3 and §5.4.4 open. Time: about 20 minutes. (The scenario is invented for teaching.)

**Scenario.** A school starts using an AI tool that scans student essays and gives each one a score for "likely written by AI." Essays above a set score are **automatically given zero marks**. Students are not told how the score is calculated, and essays are uploaded to the tool's company servers.

**Task**

**Part A:** For each of the seven principles, write **Met**, **Not met**, or **Unknown** for this school, with one reason.

**Part B:** Propose three changes that would make the school's use of the tool more responsible.

**Observation:** Note which principles you could judge from the scenario and which you could not, and what extra information you would need.

**Reflection:** In 2 to 3 sentences, say whether the school should use the tool at all, and justify your decision.

**Feedback (answers and expected outcomes)**

**Part A** *(Model answers; accept well-reasoned alternatives)*

| Principle | Rating | Reason |
|---|---|---|
| Fairness | Unknown / Not met | No evidence the tool was tested across groups of students; a wrong flag could fall more often on some groups |
| Transparency | Not met | Students are not told how the score works |
| Explainability | Not met | The tool gives a score, not understandable reasons |
| Privacy and security | Not met | Essays are uploaded to a third party; no mention of consent or data policy |
| Accountability | Not met | No one is named who answers for wrong penalties |
| Reliability and safety | Not met | A score is only an estimate, yet it triggers an automatic penalty |
| Human oversight | Not met | Zero marks are applied automatically, with no human review or appeal |

**Part B** *(Examples)*: require a teacher to review every flagged essay before any penalty; tell students how the tool is used and let them appeal; test the tool's results across student groups and check its error rate; use the score only as one piece of evidence; review the tool's data policy and limit what is uploaded.

**Reflection (model answer):** The tool could be used as a prompt for a conversation, but not as an automatic judge. A mistaken penalty harms a student, so a human must review decisions and someone must be accountable.

### 5.4.7 Check your understanding

1. In one sentence, what is accountability?
2. Which principle is met when a manager can overrule an automated rejection?
3. Why is "the algorithm decided" not an acceptable answer to an unfair outcome?

**Answers**

1. Humans and organisations, not "the algorithm," are answerable for outcomes.
2. Human oversight.
3. Because people chose the data, goals, and how the output is used, so people remain responsible and must be able to explain and correct decisions.

---

## 5.5 Discussion Scenario and Synthesis

### 5.5.1 Case: Fabricated court cases (hallucination)

In 2023, in the US case *Mata v. Avianca, Inc.*, lawyers submitted a legal brief that cited several court decisions. The decisions had been produced by an AI chatbot and **did not exist**. The court later sanctioned the lawyers and their firm, noting that they continued to stand by the citations after questions were raised (*Mata v. Avianca, Inc.*, 2023).

### 5.5.2 Activity 5.5: Case discussion

**Goal:** Connect hallucination, verification, and accountability using a real case.

**Preparation:** Read §5.5.1. Have §5.3.3 (types), §5.3.4 (verification steps), and §5.4.3 (principles) open. Work alone or in a small group. Time: about 25 minutes.

**Task: Guided discussion questions**

1. **Identify:** Which type of hallucination is this (see §5.3.3)?
2. **Process:** At what step could the error have been caught? Use the verification steps in §5.3.4.
3. **Responsibility:** Who was accountable, the AI, the tool's maker, or the lawyers? Why? Compare with your prediction in §5.4.1.
4. **Principles:** Which responsible AI principles (§5.4.3) were not followed?
5. **Prevention:** Write three rules a law firm should adopt for AI use.
6. **Compare:** How is this different from a *bias* problem? Could a tool be free of hallucination and still biased? Give an example.

**Alternative scenario: a biased résumé screener (bias).** A company's screener rejects many applicants who have career gaps. Data shows women, who more often take caregiving breaks, are rejected at a much higher rate. Discuss: Is "career gap" a proxy? Is it job-relevant? Who should decide, and how should the company monitor outcomes?

**Observation:** Note where your group disagreed, and which evidence from the chapter settled the disagreement.

**Reflection:** In 3 to 4 sentences, say what the case teaches about using AI in a profession where mistakes have serious consequences.

**Feedback (expected discussion points and teacher notes)**

- **Q1:** Fabricated sources (invented court cases).
- **Q2:** Step 2 or 3 of the verification routine: looking up the case in an official legal database would have shown the cases did not exist.
- **Q3:** Accountability rests with the **professionals who signed and submitted** the brief. Tool makers may share responsibility for communicating limits, but users cannot hand off professional duties to a tool.
- **Q4:** Accountability, human oversight, reliability, transparency.
- **Q5:** Acceptable rules include: all citations independently verified; AI use disclosed internally; no confidential client data in public tools; a named reviewer signs off.
- **Q6:** Hallucination is about **truth**; bias is about **fair treatment across groups**. A system can give accurate answers yet systematically serve one group worse.
- **Résumé screener:** Strong answers recognise that the gap may be a proxy for sex, question its relevance to the job, and propose outcome monitoring by group plus human review.

### 5.5.3 Activity 5.6: Which problem is it?

**Goal:** Tell bias, privacy, and hallucination apart, and notice when one situation involves more than one.

**Preparation:** Review the three concepts in §5.1, §5.2, and §5.3. Time: about 15 minutes. (Situations are invented for teaching.)

**Task:** For each situation, label it **Bias**, **Privacy**, **Hallucination**, or **More than one**, and give one reason.

1. A voice assistant understands male voices more accurately than female voices.
2. A customer-service chatbot tells a customer about a refund policy the company does not have.
3. A student pastes a classmate's medical note into a chatbot to ask for advice.
4. A bank model uses postcode as an input and rejects more applicants from one neighbourhood. The chat assistant that explains rejections invents reasons that are not in the model's real logic.

**Observation:** Note which situations were easy to label and which needed more than one label.

**Reflection:** Which principle from §5.4.3 would you apply first to prevent each situation?

**Feedback (answers)**

1. **Bias.** Results are systematically worse for one group (likely sampling or measurement bias; see §5.1.3).
2. **Hallucination.** The chatbot states a confident, unsupported "fact". The company, not the chatbot, is accountable for what it tells customers.
3. **Privacy.** Someone else's sensitive information is shared with a tool without that person's consent.
4. **More than one.** Postcode acting as a proxy is **bias**; invented explanations are **hallucination**; both also affect **explainability** and **accountability**.

*Reflection (examples):* fairness testing (1, 4); human oversight and reliability (2); privacy and security (3); explainability and accountability (4).

---

## 5.6 Chapter Summary and Self-Check

### 5.6.1 Key takeaways

- **Bias** is systematically worse or less favourable results for some groups. It can enter at every stage of the life cycle, and removing a sensitive column does not remove it. Check results **group by group**, using rates (selection rate and impact ratio), and treat the four-fifths rule as a warning, not proof.
- **Privacy** risks come from collecting too much, memorising data, inferring sensitive facts, and users oversharing. Removing names is not anonymisation, because ordinary details can be linked back to people.
- **Hallucinations** are fluent, confident, and wrong. AI is built to produce plausible text, not verified truth, so important claims must be checked against real sources.
- **Responsible AI** turns these concerns into practice: fairness, transparency, explainability, privacy and security, accountability, reliability and safety, and human oversight.
- **People remain accountable.** AI reflects the data, goals, and choices of the people who build and use it.

### 5.6.2 Self-check (answer without looking back)

1. A tool selects 45% of Group X and 30% of Group Y. Calculate the impact ratio for Group Y and say whether it passes the four-fifths rule.
2. Give one example of a proxy variable and say what it might stand in for.
3. Why does generalising data (for example, age bands) protect privacy, and what is its cost?
4. An AI cites a study you cannot find anywhere. What do you do?
5. Name two principles a hospital should check before using an AI tool to screen patients.
6. In your own words, explain the core idea of this chapter.

**Answers**

1. 0.30 ÷ 0.45 ≈ **0.67**, which is below 0.80, so Group Y is **flagged** for review (a warning, not proof).
2. Example: postcode standing in for ethnicity or income; first language standing in for national origin; healthcare cost standing in for health need.
3. It makes many people look alike, so a record cannot be matched to one person. The cost is less precise data, and it fails if everyone in a group shares the same sensitive value.
4. Treat it as likely fabricated, do not use or cite it, and look for a real source (§5.3.4).
5. Any two with reasons, for example fairness (tested across patient groups), privacy and security, human oversight (clinician reviews decisions), reliability and safety.
6. *Model answer:* AI does not decide to be fair or unfair; people's data and choices shape what it does, so people must test, check, and take responsibility for it.

---

## Glossary

| Term | Definition |
|---|---|
| **Accountability** | Humans and organisations are responsible for AI outcomes. |
| **Anonymisation** | Removing identifying details from data. |
| **Bias (AI)** | Systematically less accurate or less favourable results for some groups. |
| **Data minimisation** | Collecting only the data needed for a purpose. |
| **Differential privacy** | Adding measured noise so group patterns are visible but individuals are not. |
| **Explainability** | Being able to give understandable reasons for an AI output. |
| **Fabricated citation** | A reference that looks real but does not exist. |
| **Feedback loop** | Outputs that influence future data, possibly amplifying errors. |
| **Four-fifths rule** | Screening indicator: a group's selection rate below 80% of the highest group's rate is a warning sign, not proof of discrimination. |
| **Generalisation (of data)** | Making data less specific so many people look alike, for example using age bands. |
| **Grounding** | Tying AI answers to trusted, citable sources. |
| **Hallucination** | A confident but false or unsupported AI output. |
| **Human in the loop** | A person reviews and can correct AI output before it is used for something important. |
| **Impact ratio** | A group's selection rate divided by the highest group's selection rate. |
| **Personal data / PII** | Information that can identify a person. |
| **Protected characteristic** | A trait (e.g. race, sex, age) that should not be a basis for unfair treatment. |
| **Proxy variable** | An input that stands in for a protected characteristic. |
| **Re-identification** | Working out who an "anonymous" record belongs to by matching it with other information. |
| **Responsible AI** | Building and using AI safely, fairly, transparently, and accountably. |
| **Selection rate** | The share of a group receiving the favourable outcome. |

*Terms such as model, training data, inference, and language model are defined earlier in the module (see Chapter 1 §1.4 and Chapter 3 §3.3, §3.7, §3.8).*

---

## References

Buolamwini, J. and Gebru, T. (2018) 'Gender Shades: Intersectional accuracy disparities in commercial gender classification', *Proceedings of Machine Learning Research*, 81, pp. 77-91. Conference on Fairness, Accountability and Transparency. https://proceedings.mlr.press/v81/buolamwini18a.html

Carlini, N. et al. (2021) 'Extracting training data from large language models', *30th USENIX Security Symposium*. https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-extracting

Chouldechova, A. (2017) 'Fair prediction with disparate impact: A study of bias in recidivism prediction instruments', *Big Data*, 5(2), pp. 153-163. https://doi.org/10.1089/big.2016.0047

Dastin, J. (2018) 'Amazon scraps secret AI recruiting tool that showed bias against women', *Reuters*, 10 October. Republished at: https://www.euronews.com/2018/10/10/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women

European Union (2016) *Regulation (EU) 2016/679 (General Data Protection Regulation)*. https://eur-lex.europa.eu/eli/reg/2016/679/oj

European Union (2024) *Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act)*. https://eur-lex.europa.eu/eli/reg/2024/1689/oj

Gebru, T. et al. (2021) 'Datasheets for datasets', *Communications of the ACM*, 64(12), pp. 86-92. https://doi.org/10.1145/3458723

Ji, Z. et al. (2023) 'Survey of hallucination in natural language generation', *ACM Computing Surveys*, 55(12), Article 248. https://doi.org/10.1145/3571730

*Mata v. Avianca, Inc.* (2023) No. 22-cv-1461 (PKC) (S.D.N.Y.), opinion and order on sanctions, 22 June 2023, 678 F. Supp. 3d 443. Court filings: https://storage.courtlistener.com/recap/gov.uscourts.nysd.575368/

Mitchell, M. et al. (2019) 'Model cards for model reporting', *Proceedings of the Conference on Fairness, Accountability, and Transparency*, pp. 220-229. https://doi.org/10.1145/3287560.3287596

National Institute of Standards and Technology (NIST) (2023) *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. NIST AI 100-1. https://doi.org/10.6028/NIST.AI.100-1

Obermeyer, Z. et al. (2019) 'Dissecting racial bias in an algorithm used to manage the health of populations', *Science*, 366(6464), pp. 447-453. https://doi.org/10.1126/science.aax2342

OECD (2019) *Recommendation of the Council on Artificial Intelligence*. OECD/LEGAL/0449. https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449

US Equal Employment Opportunity Commission et al. (1978) *Uniform Guidelines on Employee Selection Procedures*, 29 CFR Part 1607 (the four-fifths rule is at §1607.4(D)). https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XIV/part-1607

> **Note on examples:** The following are **invented for teaching purposes**: the hiring-tool numbers in §5.1.5 and §5.1.6, the hospital and choir tables in §5.2.4 and §5.2.5, the "Henderson & Zhou" citation in §5.3.4, the Riverside Library texts in §5.3.6, the school essay-scanner scenario in §5.4.6, and the situations in §5.5.3. All other cases are real and cited above.
