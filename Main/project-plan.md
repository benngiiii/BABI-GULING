# Initial Learning Resources Project Plan

## Babi Guling – AI Overview

**Document status:** Version 1.1, revised after Quality Reviews QR-007-I01 and QR-007-I02 (both Changes Required). Items marked "Verify", "Pending", or "Not verified" have not yet been confirmed against actual files or evidence and must not be marked complete until that evidence exists. A task being listed or assigned in this plan does not mean it has been completed.

| Version | Date       | Change                                                                                 |
| ------- | ---------- | -------------------------------------------------------------------------------------- |
| 1.0     | 2026-10-23 | Initial plan revised after QR-007-I01 (Sections 3, 9, 11, 12, 15 added).               |
| 1.1     | 2026-10-23 | Revised after QR-007-I02 (verification fields, evidence registers, record templates).  |

## 1. Project Overview

The purpose of this project is to introduce Artificial Intelligence (AI) to first-year university students and other beginners with no technical background. We will develop three connected learning resources using shared Markdown content: a Study Guide and Test Bank, PowerPoint Slides, and Video Tutorials. We will also deliver a Live Mini Lecture focusing on one manageable question within the broader topic of AI.

All resources will use consistent explanations, examples, terminology, and references. If an error is found, we will correct the shared Markdown source first and then update every affected resource.

For Stage 1, the immediate priority is not to finish all three learning resources. It is to demonstrate a coherent module outline, at least one well-developed Markdown topic, a documented review outcome, meaningful GitHub development, and a complete self-contained submission package (see Section 9).

### Intended Learners

Our target learners have basic computer and internet literacy but no prior knowledge of AI or programming. Therefore, we will explain technical terms in simple language and use familiar, real-world examples.

### Learning Outcomes

After completing the module, learners should be able to:

1. Explain what AI is and how it differs from traditional programming.
2. Explain four complementary perspectives for understanding AI systems: capability (ANI, AGI, and ASI), functionality (reactive machines, limited-memory AI, theory-of-mind AI, and self-aware AI), Machine Learning, and Generative AI, and describe how these perspectives differ and can overlap.
3. Describe the basic AI workflow, including data, algorithms, training, and inference.
4. Identify applications of AI in healthcare, education, transportation, and everyday life.
5. Recognize AI limitations and risks, including bias, privacy concerns, and hallucinations.

## 2. Shared Markdown Content

The Shared Markdown Content will serve as the main source for all learning resources. It consists of five chapters introducing Artificial Intelligence (AI), explaining its classifications and processes, exploring its applications, and examining its ethics and limitations. Each chapter will follow the structure and subtopics specified in its own Markdown file.

### Chapter 1: Introduction to Artificial Intelligence

This chapter introduces AI to complete beginners through the following sections:

- **Learning Outcomes:** Defines the knowledge and skills learners should gain.
- **Chapter Map:** Outlines the chapter's sections.
- **1.1 What Is AI?:** Explains the definition of AI, everyday applications, and common myths.
- **1.2 A Brief History of AI:** Introduces important milestones in AI development and explains AI winters.
- **1.3 AI vs Traditional Programming:** Compares rule-based programming with machine learning.
- **1.4 Basic AI Terminology:** Defines data, algorithms, labels, machine learning, models, training, inference, neural networks, and deep learning.
- **1.5 Worked Example: A Spam Filter That Learns:** Demonstrates how labelled email data can be used to build a simple spam filter, make predictions, and examine its limitations.
- **1.6 Practice Questions and Answers:** Provides comprehension and application questions with explanations.
- **1.7 Summary, Reuse Plan, and References:** Summarizes the main concepts, explains how the chapter will be adapted into other learning resources, records development status, and lists references.

### Chapter 2: Types of Artificial Intelligence

This chapter explains why AI can be classified from different perspectives and helps learners avoid treating the categories as one universal hierarchy. It distinguishes capability, functionality, Machine Learning, and Generative AI, while noting that the frameworks can overlap and are not a universally standardized taxonomy.

- **Learning Outcomes:** Covers the purpose of classification; the capability categories ANI, AGI, and ASI; the four commonly discussed functionality categories; the distinction between Machine Learning and Generative AI; and the application of these perspectives to familiar AI systems.
- **2.1 Introduction to AI Classification:** Explains why AI systems can be grouped by capability, functionality, learning approach, or output.
- **2.2 AI Based on Capability:** Describes Artificial Narrow Intelligence (ANI), Artificial General Intelligence (AGI), and Artificial Superintelligence (ASI), compares their scope and status, and clarifies that AGI has no universally accepted confirmation of achievement while ASI remains hypothetical.
- **2.3 AI Based on Functionality:** Introduces reactive machines, limited-memory AI, theory-of-mind AI, and self-aware AI. It uses examples such as Deep Blue and driving-assistance systems, while distinguishing established examples from proposed or unestablished capabilities.
- **2.4 Machine Learning and Generative AI:** Explains Machine Learning as an approach for learning patterns from data and Generative AI as AI focused on creating content. It compares their purposes, outputs, examples, and overlap.
- **2.5 Comparing the Classification Frameworks:** Explains what each of the four perspectives describes and applies them to a conversational AI example. A simplified relationship diagram reinforces that the perspectives are related but not interchangeable.
- **2.6 Classification Activity:** Asks learners to classify familiar applications such as spam detection, music recommendations, chatbots, driving assistance, image generation, and a hypothetical theory-of-mind system, with suggested answers and explanations.
- **2.7 Common Misunderstandings About AI Types:** Addresses misconceptions about AI capability, AGI, emotional language, functionality categories, Machine Learning, Generative AI, and whether a system can fit multiple descriptions.
- **2.8 Practice Questions and Answers:** Provides multiple-choice, short-answer, and application questions with explanations.
- **2.9 Summary and References:** Reviews the key takeaways and lists the chapter's supporting sources.

The chapter map estimates a total learning time of 55 minutes.

### Chapter 3: How Artificial Intelligence Works

This chapter explains the components and processes involved in AI systems, from data and models to evaluation and the overall workflow.

- **3.1 Learning Objectives:** Identifies what learners should understand by the end of the chapter.
- **3.2 The Big Picture:** Provides an overview of how AI works.
- **3.3 Data: The Fuel of AI:** Explains the role of data in AI systems.
- **3.4 Algorithms and Models:** Introduces algorithms and models and explains their roles.
- **3.5 Machine Learning: Learning from Examples:** Explains how machine learning identifies patterns from examples.
- **3.6 Neural Networks and Deep Learning:** Introduces neural networks and deep learning.
- **3.7 How Modern Language AI Works:** Explains the basic ideas behind modern language-based AI.
- **3.8 Training vs. Inference:** Distinguishes between training a model and using it to process new inputs.
- **3.9 Evaluating a Model:** Introduces how AI model performance can be assessed.
- **3.10 The AI Workflow:** Connects the main stages involved in developing and using AI.
- **3.11 From Beginner to Expert:** Covers progression from introductory knowledge toward more advanced understanding.
- **3.12 Misconceptions, Takeaways, Glossary:** Addresses common misconceptions, reviews important concepts, and defines key terminology.
- **Practice Questions and Activities:** Provides opportunities to review and apply the chapter's concepts.

**Open issue (Review Finding 6):** The supplied contents link to a Practice Questions section numbered 3.16, while the outline above lists sections 3.1–3.12 followed by an unnumbered Practice Questions and Activities section. The intended numbering has not yet been confirmed. Task: compare this outline with the actual Chapter 3 Markdown file, decide the correct numbering, correct either the outline or the chapter file, and check that every table-of-contents link points to the right heading. Owner, target date, and verification result are tracked in Section 10 (task T3), and the final decision is recorded below.

| Field                                              | Entry        |
| -------------------------------------------------- | ------------ |
| Actual Chapter 3 headings compared (date, by whom) | Pending      |
| Intended numbering decided                         | Pending      |
| Correction made in (outline / chapter file)        | Pending      |
| Table-of-contents links checked (date, by whom)    | Pending      |
| Final verification result                          | Not verified |

### Chapter 4: Applications of Artificial Intelligence

This chapter examines how AI is applied across different fields and everyday situations.

- **Learning Outcomes:** Defines the intended learning outcomes.
- **Prerequisites and Framing:** Establishes the background and context for studying AI applications.
- **Module Map:** Outlines the chapter's structure.
- **Applications at a Glance:** Introduces the application areas covered in the chapter.
- **Topic 1: Healthcare (Fully Developed):** Explores AI applications in healthcare in greater detail.
- **Topic 2: Education:** Examines how AI is used in teaching and learning.
- **Topic 3: Transportation:** Explores AI applications in transportation.
- **Topic 4: Everyday Life:** Examines AI tools and systems encountered in daily activities.
- **Topic 5: Finance and Trading:** Introduces AI applications in finance and trading.
- **Cross-Topic Synthesis Activity:** Encourages learners to connect and compare applications across the different fields.
- **Teacher Notes:** Provides supporting notes for teaching the chapter.
- **Glossary:** Defines relevant terminology.
- **References:** Lists the sources used in developing the content.

### Chapter 5: AI Ethics and Limitations

This chapter examines ethical concerns, limitations, and responsible practices associated with AI systems.

- **Learning Outcomes:** Defines the intended learning outcomes.
- **Module Map:** Outlines the chapter's topics.
- **Prerequisites and Framing:** Establishes the context for understanding AI ethics and limitations.
- **Topic 1: Bias (Fully Developed):** Explores bias in AI systems and its potential effects.
- **Topic 2: Privacy:** Examines privacy concerns related to AI and data.
- **Topic 3: Hallucinations:** Explains how AI systems can produce inaccurate or unsupported information.
- **Topic 4: Responsible AI:** Introduces responsible approaches to developing and using AI.
- **Topic 5: Discussion Scenario:** Uses a scenario to explore issues involving bias or hallucinations.
- **Glossary:** Defines key terms related to AI ethics and limitations.
- **References:** Lists the supporting sources.

### How the Shared Markdown Content Will Be Used

The five Markdown chapters will serve as the foundation for the three main learning resources:

- **Study Guide and Test Bank:** Chapter explanations, terminology, examples, and activities will support the study guide. Existing practice questions and answers will inform the test bank where applicable.
- **PPT Slides:** Chapter concepts, comparisons, diagrams, timelines, worked examples, application scenarios, and discussion topics will be adapted into presentation slides where relevant.
- **Video Tutorials:** The explanations, examples, classification activities, application scenarios, and discussion topics will guide video content according to each chapter's subject.

The team will preserve the meaning and key concepts of each chapter when adapting the Markdown content. The format and activities will vary according to each chapter's actual subtopics rather than forcing every chapter into an identical structure.

## 3. Development Status Overview

*(Added in response to Review Finding 1 and Finding 6.)*

This table distinguishes completed work from future intentions. Statuses use the following labels: **Outline only**, **Drafted**, **Checked** (peer-reviewed), **Awaiting revision**, and **Verify actual status** (not yet confirmed against the Markdown file). The plan describes the sections below, but their current status must be confirmed in the actual `.md` files before any label other than "Verify actual status" is recorded.

| Chapter   | Section or Topic                                 | Current Status       | Verified By / Date | Remaining Work                                                                                                                                                  |
| --------- | ------------------------------------------------ | -------------------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Chapter 1 | Full chapter (1.1–1.7)                           | Verify actual status | Not yet verified   | Confirm all sections exist; check explanations and definitions                                                                                                  |
| Chapter 1 | 1.5 Spam-filter worked example                   | Verify actual status | Not yet verified   | Check explanations, calculations, activity, and answers                                                                                                         |
| Chapter 1 | 1.6 Practice questions and answers               | Verify actual status | Not yet verified   | Check answer accuracy and explanations                                                                                                                          |
| Chapter 2 | Full chapter (2.1–2.9)                           | Verify actual status | Not yet verified   | Confirm all sections exist; check that AGI/ASI and functionality categories are not overstated; check terminology matches Learning Outcome 2 ("complementary perspectives") |
| Chapter 2 | 2.6 Classification activity                      | Verify actual status | Not yet verified   | Check examples and suggested answers                                                                                                                            |
| Chapter 3 | Full chapter (3.1–3.12)                          | Verify actual status | Not yet verified   | Confirm substantive content and resolve numbering (3.16 discrepancy)                                                                                            |
| Chapter 3 | AI workflow and evaluation (3.9, 3.10)           | Verify actual status | Not yet verified   | Confirm substantive content                                                                                                                                     |
| Chapter 3 | Practice questions and activities                | Verify actual status | Not yet verified   | Confirm section number and that links point to the correct heading                                                                                              |
| Chapter 4 | Topic 1: Healthcare (planned as fully developed) | Verify actual status | Not yet verified   | Check explanations, sources, and learning activity                                                                                                              |
| Chapter 4 | Topics 2–5 and synthesis activity                | Verify actual status | Not yet verified   | Confirm depth; mark any outline-only topics                                                                                                                     |
| Chapter 5 | Topic 1: Bias (planned as fully developed)       | Verify actual status | Not yet verified   | Check explanations, sources, and discussion activity                                                                                                            |
| Chapter 5 | Topics 2–5                                       | Verify actual status | Not yet verified   | Confirm depth; mark any outline-only topics                                                                                                                     |
| All       | References and source verification               | Pending              | Not yet verified   | Record which sources have been checked and by whom                                                                                                              |

To verify a row, the responsible person compares it with the actual Markdown file, records the status (distinguishing an outline from a substantive draft and from a peer-reviewed section), and enters their name and the date in the "Verified By / Date" column. The team will update this table whenever a section's status changes, and the Submission Report will summarize it.

### Stage 1 Focus Topic

At least one coherent topic must be substantively developed in Markdown. The team will inspect the actual files and select the strongest suitable topic. The selection is recorded here and in the Submission Report.

| Field                        | Entry                                                                                           |
| ---------------------------- | ----------------------------------------------------------------------------------------------- |
| Candidate topics             | Chapter 1 (1.5 spam-filter example), Chapter 4 (Topic 1: Healthcare), Chapter 5 (Topic 1: Bias) |
| Selected topic               | To be confirmed after file inspection                                                           |
| Proposed selection deadline  | October 23, 2026                                                                                |
| Selected by / date           | Pending                                                                                         |
| Verified status of the topic | Not verified                                                                                    |

Before the topic is accepted, each required element is checked in the actual file:

| Required element                         | Present in file (Yes / Partial / No) | Checked By / Date |
| ---------------------------------------- | ------------------------------------ | ----------------- |
| Explanations                             | Not checked                          | Pending           |
| Terminology                              | Not checked                          | Pending           |
| Worked example or demonstration          | Not checked                          | Pending           |
| Appropriate visual (where useful)        | Not checked                          | Pending           |
| Learner activity or application question | Not checked                          | Pending           |
| Explained answer or expected outcome     | Not checked                          | Pending           |
| References                               | Not checked                          | Pending           |

## 4. Study Guide and Test Bank

**Purpose:** Help learners study independently, practise applying concepts, and check their understanding.

The Study Guide will follow the five-chapter structure of the shared Markdown content. Each chapter will retain the sections listed in its own Markdown file rather than being forced into the exact structure of Chapter 1. For example, Chapter 1 includes a worked spam-filter example and a reuse plan; Chapter 2 includes an AI classification activity; Chapter 3 covers the AI workflow and model evaluation; Chapter 4 includes a cross-topic synthesis activity; and Chapter 5 includes a discussion scenario about bias or hallucinations.

Across the Study Guide, explanations will use beginner-friendly language and relevant definitions, comparisons, tables, diagrams, examples, or activities where suitable for the topic. Learning objectives or outcomes, chapter maps, practice materials, summaries, glossaries, teacher notes, development notes, and references will be included where they appear in the relevant chapter outline.

The Test Bank will draw on each chapter's actual subtopics and learning activities. It will include multiple-choice questions, true-or-false questions, short-answer questions, and simple scenario-based questions where appropriate. Questions will progress from basic recall to understanding and application.

For example, learners may compare a traditional rule-based spam filter with a machine-learning spam filter, then explain why either system might incorrectly classify an email.

We will review the answer key for accuracy and ensure that questions assess the stated learning outcomes. The goal is to help learners identify misunderstandings rather than simply memorize definitions.

## 5. PPT Slides

**Purpose:** Present the content of all five Markdown chapters visually, following the same chapter topics and sequence used in the Study Guide and Test Bank (Part 4). Slides will summarize rather than replace the detailed explanations, activities, and references in the shared Markdown content.

The presentation will be organized by chapter:

### Chapter 1: Introduction to Artificial Intelligence
- Introduce the learning outcomes and chapter map.
- Explain what AI is and show familiar examples.
- Present a brief AI history timeline, including important milestones and AI winters.
- Compare traditional rule-based programming with machine learning using a simple diagram.
- Define basic AI terminology, including data, algorithms, labels, models, training, inference, neural networks, and deep learning.
- Show the worked spam-filter example step by step, including labelled emails, word scores, predictions, and possible mistakes.
- End with key takeaways and selected practice questions.

### Chapter 2: Types of Artificial Intelligence
- Introduce why AI systems can be classified from different perspectives and note that the frameworks are teaching tools rather than one universally standardized taxonomy.
- Use a comparison table to explain the capability categories: Artificial Narrow Intelligence (ANI), Artificial General Intelligence (AGI), and Artificial Superintelligence (ASI), including their scope and current status.
- Explain the four functionality categories: reactive machines, limited-memory AI, theory-of-mind AI, and self-aware AI. Use Deep Blue and a driving-assistance example, and distinguish practical examples from hypothetical or unestablished capabilities.
- Compare Machine Learning and Generative AI, showing that ML is an approach for learning patterns from data while Generative AI focuses on creating content; many generative systems use ML.
- Include a simplified relationship diagram showing how capability, functionality, Machine Learning, and Generative AI describe different aspects and are not mutually exclusive categories.
- Present selected examples from the classification activity, such as spam detection, recommendations, chatbots, image generation, and driving assistance.
- Address common misunderstandings, then end with key takeaways and selected practice questions.

### Chapter 3: How Artificial Intelligence Works
- Present the big picture of how an AI system works.
- Illustrate how data is collected and used, and explain the roles of algorithms and models.
- Show how machine learning learns patterns from examples.
- Introduce neural networks and deep learning with a simplified visual.
- Explain the basic process behind modern language AI at an introductory level.
- Compare training with inference and show the stages of the AI workflow.
- Introduce model evaluation and the progression from beginner to more advanced understanding.
- Finish with misconceptions, key takeaways, glossary terms, and selected practice questions or activities.

### Chapter 4: Applications of Artificial Intelligence
- Present an overview of the application areas covered in the chapter.
- Use a consistent visual structure to explain the fully developed healthcare topic.
- Summarize AI applications in education, transportation, everyday life, and finance and trading.
- For each field, highlight the relevant use case and important considerations described in the chapter.
- Include the cross-topic synthesis activity so learners can compare applications across fields.
- Finish with key terms and a brief recap.

### Chapter 5: AI Ethics and Limitations
- Introduce the chapter learning outcomes, map, and framing.
- Use a simple scenario or diagram to explain AI bias and its possible effects.
- Summarize privacy concerns associated with AI and data.
- Show an example of an AI hallucination and why generated information may need checking.
- Present the key ideas behind responsible AI.
- Include the discussion scenario on bias or hallucinations, with prompts for learners to consider possible responses.
- Finish with key terms and a recap of the chapter's main points.

Slides will use concise text, readable diagrams, consistent visual design, and beginner-friendly examples. The order and subject of each chapter's slides will follow the corresponding Markdown chapter rather than repeating one generic slide template. More detailed explanations, full activities, and answer explanations will remain in the Study Guide and Test Bank.

## 6. Video Tutorials

**Purpose:** Reinforce the content of the five Markdown chapters through narration, visual demonstrations, and short activities. The tutorial plan will follow the chapter topics in Part 2 and the learning-resource structure described in Part 4, rather than covering only five broad, unrelated themes.

We plan to create a chapter-based tutorial sequence:

### Chapter 1: Introduction to Artificial Intelligence
- Introduce the chapter learning outcomes and explain what AI is through familiar examples.
- Narrate a short timeline of AI history and explain the idea of AI winters.
- Demonstrate the difference between traditional programming and machine learning using a simple comparison.
- Explain basic AI terms in plain language.
- Walk through the spam-filter example step by step: review labelled emails, build or read the word-score table, classify sample emails, and discuss why a prediction may be wrong.
- End with a recap and a short comprehension question.

### Chapter 2: Types of Artificial Intelligence
- Introduce the four perspectives used in the chapter: capability, functionality, Machine Learning, and Generative AI, explaining that each answers a different question.
- Compare ANI, AGI, and ASI, using familiar examples for ANI and clearly labelling AGI and ASI as proposed or hypothetical categories whose status should not be overstated.
- Explain reactive machines, limited-memory AI, theory-of-mind AI, and self-aware AI, using Deep Blue and driving assistance as examples and clarifying which capabilities remain unestablished.
- Demonstrate the difference between Machine Learning and Generative AI with a spam detector and an image generator; explain that many generative systems use ML.
- Walk through the simplified relationship diagram and apply multiple perspectives to a conversational AI example.
- Pause for learners to classify spam detection, music recommendations, a chatbot, driving assistance, and image generation, then discuss the suggested answers.
- Address common misunderstandings and finish with a recap and a review question about why one AI system may have several valid descriptions.

### Chapter 3: How Artificial Intelligence Works
- Start with an overview of the AI process.
- Explain the role of data, algorithms, and models using a simple example.
- Demonstrate how a model can learn patterns from examples.
- Introduce neural networks and deep learning with a simplified visual explanation.
- Explain the basic idea behind modern language AI without unnecessary technical detail.
- Contrast training and inference, then trace the stages of the AI workflow.
- Explain how a model is evaluated and discuss common misconceptions.
- End with a recap and a short question or activity.

### Chapter 4: Applications of Artificial Intelligence
- Introduce the application areas covered in the chapter.
- Use the healthcare topic as the main detailed demonstration, following the content developed in the Markdown chapter.
- Present shorter examples of AI in education, transportation, everyday life, and finance and trading.
- Compare the fields by asking learners to identify what AI is used for and what considerations apply in each example.
- Guide learners through the cross-topic synthesis activity.
- End with a recap and a short application question.

### Chapter 5: AI Ethics and Limitations
- Introduce the chapter's focus on risks, limitations, and responsible use.
- Demonstrate how bias may appear in an AI system and discuss its possible consequences.
- Explain privacy concerns using an accessible AI-and-data scenario.
- Show how an AI system can produce a hallucination and why its output should be verified.
- Introduce responsible AI practices covered in the chapter.
- Walk through the discussion scenario on bias or hallucinations and invite learners to justify their responses.
- End with a recap and a reflection question about responsible AI use.

Each tutorial will focus on a manageable set of learning objectives and use narration, diagrams, on-screen examples, or simple demonstrations as appropriate to the chapter. The scripts will be based on the shared Markdown content so that terminology, examples, and explanations remain consistent with the Study Guide and PPT Slides. Where the chapter includes practice questions or activities, the tutorial may use selected items for a brief pause-and-answer moment.

## 7. Live Mini Lecture

**Proposed topic:** How Can AI Learn to Recognize Spam Emails?

**Central question:** How does a machine-learning system distinguish spam emails from legitimate emails, and why can it make mistakes?

This topic is a manageable introduction to AI because email filtering is familiar to most learners. It also connects directly to the broader concepts of machine learning, training data, inference, and AI limitations.

### Proposed Lecture Structure

1. **Introduction:** Ask learners whether they have ever found a legitimate email in their spam folder or a spam message in their inbox.
2. **Explain the concept:** Introduce machine learning as a method through which a system learns patterns from examples rather than relying only on manually written rules.
3. **Visual demonstration:** Present a small set of fictional emails labeled as spam or legitimate. Highlight features such as suspicious phrases, unusual links, and sender information.
4. **Audience activity:** Ask learners to classify several sample emails and explain which clues influenced their decisions.
5. **Discuss mistakes:** Show how a legitimate promotional email could be incorrectly classified as spam and explain how incomplete or biased training data can affect predictions.
6. **Conclusion:** Summarize the relationship between training data, learned patterns, predictions, and errors.

We will avoid unnecessary mathematics and advanced technical details. The objective is to help beginners understand the basic idea of machine learning rather than build an actual spam-filtering system.

## 8. How the Three Learning Resources Support One Another

The three resources will serve different learning needs while sharing the same content foundation.

| Resource                  | Main Function                                          | How It Connects                                                        |
| ------------------------- | ------------------------------------------------------ | ---------------------------------------------------------------------- |
| Study Guide and Test Bank | Detailed explanations, independent study, and practice | Provides the complete content, examples, questions, and explanations.  |
| PPT Slides                | Visual summaries and structured presentation           | Highlights key concepts and diagrams from the Study Guide.             |
| Video Tutorials           | Narrated explanations and demonstrations               | Reinforces concepts that benefit from step-by-step visual explanation. |

Learners can begin with a video to gain an initial understanding, use the Study Guide to explore concepts in greater detail, and practise with the Test Bank to check their understanding. The PPT Slides provide a visual summary for revision or classroom discussion.

The Live Mini Lecture will bring these resources together by using the spam-filter example, supported by a slide diagram, a narrated explanation, and practice questions from the shared content.

This integrated approach will reduce inconsistencies and make the learning experience more coherent.

## 9. Stage 1 Submission Plan

*(Added in response to Review Finding 2.)*

The lecturer requires a self-contained ZIP package named `TeamName_Stage1_GitHub_Markdown_V1.zip`. Its required contents are:

1. A **Submission Report** (Word or PDF) including the repository URL, snapshot date, latest commit identifier, content-status summary, repository evidence, individual contributions, review outcome, and next steps.
2. A **Markdown source snapshot** containing the README, current `.md` files, and supporting assets in their working folder structure.
3. A **readable PDF of the current learning content**, including the Markdown learning content, module outline, and development status.

All required files and evidence must be inside the ZIP, not only available through external links. The official Stage 1 deadline is **October 24, 2026, 23:59 Beijing time**.

### Stage 1 Submission Checklist

An item is ticked only when the corresponding file, record, or evidence actually exists.

- [ ] Team GitHub repository is accessible to the lecturer if needed.
- [ ] README identifies the team, module, members, GitHub usernames, project purpose, intended learners, folder structure, progress, and remaining work.
- [ ] Current project plan and task list are included in the repository.
- [ ] Module outline and Markdown development statuses (Section 3) are included.
- [ ] At least one coherent topic is substantively developed in Markdown.
- [ ] Developed content includes explanations, terminology, a worked example or demonstration, an appropriate visual where useful, a learner activity or application question, an explained answer or expected outcome, and references.
- [ ] A peer-review record documents what was checked, what was found, and what was corrected or confirmed.
- [ ] Submission Report includes the repository URL, snapshot date, latest commit identifier, content-status summary, repository evidence, individual contributions, review outcome, and next steps.
- [ ] Markdown source snapshot includes the README, current `.md` files, and supporting assets in their working folder structure.
- [ ] Readable content PDF includes the current Markdown learning content, module outline, and development status.
- [ ] Required shared project AI-use records and separate personal logs are prepared according to the Shared Assignment Rules.
- [ ] Chapter 3 section numbering is resolved and table-of-contents links are checked.
- [ ] All required files and evidence are included in the ZIP rather than being available only through external links.
- [ ] ZIP is named `TeamName_Stage1_GitHub_Markdown_V1.zip`.
- [ ] ZIP is extracted into a different folder and checked to confirm that files open and images and assets are present.

### Submission Package Record

Filled in only when each file actually exists and has been checked. File names marked "proposed" are suggestions for the team to confirm.

| Item                            | Expected Name / Location                                   | Actual File | Created (date) | Verified By / Date | Result       |
| ------------------------------- | ---------------------------------------------------------- | ----------- | -------------- | ------------------ | ------------ |
| Submission Report (Word or PDF) | `Stage1_Submission_Report` (.docx or .pdf) (proposed)      | Pending     | Pending        | Pending            | Not verified |
| Markdown source snapshot        | README, current `.md` files, and assets in working folders | Pending     | Pending        | Pending            | Not verified |
| Readable content PDF            | `Stage1_Content.pdf` (proposed)                            | Pending     | Pending        | Pending            | Not verified |
| Shared AI-use records           | Path to be confirmed (Section 12)                          | Pending     | Pending        | Pending            | Not verified |
| Peer-review record              | Path to be confirmed (see below)                           | Pending     | Pending        | Pending            | Not verified |
| Final ZIP                       | `TeamName_Stage1_GitHub_Markdown_V1.zip`                   | Pending     | Pending        | Pending            | Not verified |
| Extraction test                 | Folder used for extraction: pending                        | n/a         | Pending        | Pending            | Not verified |

**Submission Report content check.** Before submission, confirm that the report contains: the repository URL, the snapshot date, the latest commit identifier, the content-status summary, repository evidence, individual contributions, the review outcome, next steps, and a brief statement of significant AI assistance with pointers to the relevant log entries. Also confirm that the content PDF includes the current learning content, the module outline, and the development status.

### Peer-Review Record (Stage 1 Topic)

The review record for the selected Stage 1 topic will contain the following fields. It is complete only when a review has actually taken place.

| Field                                       | Entry                             |
| ------------------------------------------- | --------------------------------- |
| Topic / file or section reviewed            | Pending (see Stage 1 Focus Topic) |
| Version or commit reviewed                  | Pending                           |
| Author                                      | Pending                           |
| Reviewer                                    | Pending                           |
| Review date                                 | Pending                           |
| What was checked                            | Pending                           |
| Findings                                    | Pending                           |
| Corrected (with commit or change reference) | Pending                           |
| Confirmed as correct                        | Pending                           |
| Still open                                  | Pending                           |
| Final review outcome                        | Pending                           |
| Record stored at                            | Pending                           |


## 10. Team Responsibilities

| Member                    | Role                 | Main Responsibilities                                                                                  |
| ------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------ |
| Benedict Subhata          | Visual Design Lead   | Develop the Study Guide layout, Word documents, and PowerPoint Slides.                                 |
| Brian Djoni Suzanna       | Quality Lead         | Review accuracy, consistency, and completeness across all resources.                                   |
| Gandhi Bestin Dhammananda | Video Lead           | Plan, record, and edit video tutorials and help develop the live teaching flow.                        |
| Jonathan Sugianto         | CIO and Content Lead | Coordinate content development, track overall progress, and compile the final submission.              |
| Joseph Lokman             | CEO                  | Record activities and progress, communicate on behalf of the team, and guide coordination when needed. |

All members will contribute to research, discussion, and peer review as needed. Individual responsibilities will be adjusted if workload or project requirements change.

### Stage 1 Task Tracker (Proposed)

*(Revised in response to Review Findings 1–6 and 8.)*

Owners, target dates, and file names are proposals for the team to confirm. "Task Status" records whether the work has been done; "Verification" records whether someone other than the doer has checked the result. A task is closed only when both are complete. Official Stage 1 deadline: October 24, 2026, 23:59 Beijing time.

| ID  | Task                                                                                        | Proposed Owner            | Target Date          | Expected Output / Path                            | Task Status | Verification | Blockers / Notes   |
| --- | ------------------------------------------------------------------------------------------- | ------------------------- | -------------------- | ------------------------------------------------- | ----------- | ------------ | ------------------ |
| T1  | Verify and maintain the development-status table (Section 3); check Chapter 2 terminology   | Jonathan Sugianto         | Oct 23, 2026         | Updated table in `project-plan.md`                | Pending     | Not verified | None recorded      |
| T2  | Select and verify the Stage 1 focus topic                                                   | Jonathan Sugianto         | Oct 23, 2026         | Completed focus-topic record in Section 3         | Pending     | Not verified | None recorded      |
| T3  | Resolve Chapter 3 section numbering and check table-of-contents links                       | Jonathan Sugianto         | Oct 23, 2026         | Chapter 3 `.md` file (exact path to be confirmed) | Pending     | Not verified | None recorded      |
| T4  | Conduct and file the peer-review record for the focus topic                                 | Brian Djoni Suzanna       | Oct 23, 2026         | Review record, path to be confirmed               | Pending     | Not verified | Depends on T2      |
| T5  | Communicate QR-007-I01 and QR-007-I02 feedback to the plan owner and record method and date | Brian Djoni Suzanna       | Oct 23, 2026         | Feedback Communication Record (Section 15)        | Pending     | Not verified | None recorded      |
| T6  | Collect repository evidence and contribution mapping (Section 11)                           | Joseph Lokman             | Oct 24, 2026 (noon)  | Evidence folder, path to be confirmed             | Pending     | Not verified | Depends on T2      |
| T7  | Maintain shared AI-use records and check them before submission (Section 12)                | Joseph Lokman             | Oct 24, 2026 (noon)  | Shared AI-use records, path to be confirmed       | Pending     | Not verified | None recorded      |
| T8  | Each member prepares their own personal AI-use log (private, not placed in the repository)  | Every member              | Oct 24, 2026 (noon)  | Submitted separately per Shared Assignment Rules  | Pending     | Not verified | None recorded      |
| T9  | Export the readable content PDF                                                             | Benedict Subhata          | Oct 24, 2026 (3 pm)  | `Stage1_Content.pdf` (proposed)                   | Pending     | Not verified | Depends on T1–T3   |
| T10 | Compile the Submission Report                                                               | Jonathan Sugianto         | Oct 24, 2026 (5 pm)  | `Stage1_Submission_Report` (proposed)             | Pending     | Not verified | Depends on T4–T7   |
| T11 | Compile the ZIP, extract it into a separate folder, and record the result                   | Jonathan Sugianto         | Oct 24, 2026 (8 pm)  | `TeamName_Stage1_GitHub_Markdown_V1.zip`          | Pending     | Not verified | Depends on T9, T10 |

Blockers are recorded in the last column as they arise. The final verification results for T2, T3, T4, and T11 are also copied into the Submission Package Record (Section 9).

## 11. Repository Evidence and Individual Contributions

*(Added in response to Review Finding 3.)*

The submission must show meaningful changes, individual contributions, and evidence of review or coordination, not only a repository link, a homepage screenshot, or commit counts. The team will collect:

- A repository overview showing the README and main folders.
- A readable commit history showing authors, dates, and meaningful change descriptions.
- Selected change views showing actual additions, corrections, or improvements.
- A contribution summary mapping each member to the relevant files or sections.
- A representative example of content review, task coordination, or problem resolution.

For each item, the team records where it is stored and who collects it (see the assignment table in Section 10). We will not create artificial commits merely to increase activity.

### Evidence Register

| Evidence item                                       | Repository path / file | Collected by | Date    | Verified |
| --------------------------------------------------- | ---------------------- | ------------ | ------- | -------- |
| Repository overview (README and main folders)       | Pending                | Pending      | Pending | No       |
| Readable commit history (authors, dates, messages)  | Pending                | Pending      | Pending | No       |
| Selected change views (additions or corrections)    | Pending                | Pending      | Pending | No       |
| Contribution summary                                | Pending                | Pending      | Pending | No       |
| Example of review, coordination, or problem solving | Pending                | Pending      | Pending | No       |

When verifying, confirm that commits show meaningful changes with identifiable authors and dates, and that the review or coordination example is more than a repository link or a homepage screenshot.

### Individual Contribution Map

| Member                    | Files / Sections Worked On | Representative Commits or Changes | Verified By / Date |
| ------------------------- | -------------------------- | --------------------------------- | ------------------ |
| Benedict Subhata          | Pending                    | Pending                           | Pending            |
| Brian Djoni Suzanna       | Pending                    | Pending                           | Pending            |
| Gandhi Bestin Dhammananda | Pending                    | Pending                           | Pending            |
| Jonathan Sugianto         | Pending                    | Pending                           | Pending            |
| Joseph Lokman             | Pending                    | Pending                           | Pending            |

These entries are filled in from the actual repository history, not from the role descriptions in Section 10.

## 12. AI-Use Documentation

*(Added in response to Review Finding 4.)*

The team will record significant AI assistance and verify its output. For each significant use, the shared project AI-use record will note:

- The date and AI tool used.
- The relevant prompt and output.
- How the output was checked and what judgment the team member made.
- The resulting change, decision, or learning.

The Stage 1 Submission Report will briefly identify significant AI assistance affecting the submitted work and point to the relevant log entries. The actual interaction and verification evidence must be included in the submitted logs, not only accessible through conversation links.

Shared project AI-use records are distinct from individual personal logs. Personal logs remain private and must not be placed in a publicly accessible GitHub repository; they are prepared and submitted separately according to the Shared Assignment Rules.

### AI-Use Record Register

| Record                                                   | Location | Covers (files or work affected) | Verified By / Date |
| -------------------------------------------------------- | -------- | ------------------------------- | ------------------ |
| Shared project AI-use record                             | Pending  | Pending                         | Pending            |
| Submission Report statement of significant AI assistance | Pending  | Pending                         | Pending            |

The verifier checks that the records exist, cover the significant AI assistance used in the submitted work, explain how AI-generated information was verified, and are pointed to from the Submission Report.

Personal logs are tracked by confirmation only. The logs themselves are never stored in the repository.

| Member                    | Personal log prepared (Yes / No) | Submitted separately (Yes / No) |
| ------------------------- | -------------------------------- | ------------------------------- |
| Benedict Subhata          | Pending                          | Pending                         |
| Brian Djoni Suzanna       | Pending                          | Pending                         |
| Gandhi Bestin Dhammananda | Pending                          | Pending                         |
| Jonathan Sugianto         | Pending                          | Pending                         |
| Joseph Lokman             | Pending                          | Pending                         |

## 13. Initial Timeline and Workflow

| Stage                     | Internal Deadline | Main Deliverables                                                                                                      |
| ------------------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Stage 1: Foundation       | October 23, 2026  | Project plan, chapter outlines, sample Markdown section, initial source collection, and the Stage 1 submission package (Section 9). |
| Stage 2: First Versions   | November 4, 2026  | Draft shared content, initial Study Guide and Test Bank, PPT Slides, and Video Tutorials.                              |
| Stage 3: Final Submission | November 24, 2026 | Revised and reviewed resources, completed mini lecture preparation, final consistency checks, and compiled submission. |

The corresponding official deadlines are October 24, November 7, and November 28, 2026. The Stage 1 official deadline is 23:59 Beijing time on October 24, so the one-day gap after the internal deadline should be reserved for closing the gaps identified in Quality Reviews QR-007-I01 and QR-007-I02.

Our workflow will be:

1. Research and outline the content.
2. Draft and self-check the shared Markdown files.
3. Review content with another team member and write a review record.
4. Record significant AI assistance and how its output was verified.
5. Produce or update the three learning resources.
6. Rehearse the mini lecture and collect feedback.
7. Correct the Markdown source and update affected resources.
8. Collect repository and contribution evidence.
9. Perform final quality checks, run the Stage 1 checklist, and compile the submission.

We will use one GitHub repository with separate folders for each project component. Members will work on individual branches, submit pull requests for review, and use GitHub Issues to track tasks and progress.

## 14. Initial Risks and Quality Assurance

Potential challenges include inaccurate information, inconsistent explanations between resources, uneven workloads, delays in video production, and an incomplete or poorly evidenced Stage 1 submission package.

To address these risks, we will:

- Verify important claims using reliable sources, and record which sources have been checked.
- Review each other's work before merging changes, and keep a written review record for the developed Markdown topic.
- Keep the Markdown content as the single source of truth.
- Test the learning materials with beginner-level questions and examples.
- Track tasks and deadlines through regular check-ins.
- Keep AI-use records and verify AI output before using it.
- Follow the Stage 1 Submission Checklist and test the ZIP by extracting it in a different folder.
- Do not mark any item complete until the corresponding file, record, or evidence exists.
- Revise the resources based on feedback before submission.

The exact depth of each chapter, the final video format, and the mini lecture delivery details may be revised after confirming the lecturer's expectations.

## 15. Quality Review Response Summary

*(Tracks Quality Reviews QR-007-I01 and QR-007-I02.)*

| Finding | Source     | Severity | Response in This Plan                                                                                                   | Status                                                     |
| ------- | ---------- | -------- | ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| 1       | QR-007-I01 | Medium   | Development-status table with "Verified By / Date" column (Section 3)                                                   | Process in place; statuses not yet verified                |
| 2       | QR-007-I01 | High     | Submission plan, checklist, Submission Package Record, and report content check (Section 9)                             | In place; items unticked until evidenced                   |
| 3       | QR-007-I01 | Medium   | Evidence Register and Individual Contribution Map (Section 11)                                                          | In place; evidence not yet collected                       |
| 4       | QR-007-I01 | Medium   | AI-Use Record Register and personal-log confirmation table (Section 12)                                                 | In place; records pending                                  |
| 5       | QR-007-I01 | Medium   | Peer-Review Record template (Section 9) and task T4 (Section 10)                                                        | In place; review not yet recorded                          |
| 6       | QR-007-I01 | Low      | Chapter 3 decision record (Section 2) and task T3                                                                       | Open; needs check against chapter file                     |
| 7       | QR-007-I01 | Low      | Learning Outcome 2 reworded (Section 1); Chapter 2 terminology check added to T1                                        | Addressed; terminology check pending                       |
| 8       | QR-007-I02 | Medium   | Task tracker with owners, target dates, expected paths, separate task and verification status, blockers (Section 10)    | Addressed in plan; owners and dates need team confirmation |
| 9       | QR-007-I02 | Medium   | Stage 1 Focus Topic selection record and required-element check (Section 3)                                             | Topic not yet selected                                     |

### Feedback Communication Record

| Review     | Communicated to | Method  | Date    | Recorded by |
| ---------- | --------------- | ------- | ------- | ----------- |
| QR-007-I01 | Joseph Lokman   | Pending | Pending | Pending     |
| QR-007-I02 | Joseph Lokman   | Pending | Pending | Pending     |

### Review History

| Review ID  | Result           | Outstanding                                                                                                   |
| ---------- | ---------------- | ------------------------------------------------------------------------------------------------------------- |
| QR-007-I01 | Changes Required | Addressed in Version 1.0 planning content                                                                     |
| QR-007-I02 | Changes Required | Actual statuses, focus topic, peer review, repository evidence, AI-use records, Chapter 3 numbering, ZIP test |

The next review should verify actual files and evidence, not only whether requirements appear in this plan.

## 16. Expected Outcome

By the final deadline, we aim to deliver a consistent set of beginner-friendly AI learning materials consisting of shared Markdown content, a Study Guide and Test Bank, PowerPoint Slides, Video Tutorials, and a Live Mini Lecture.

Together, these resources will help learners understand basic AI concepts, apply them to familiar situations, and recognize both the capabilities and limitations of AI.
