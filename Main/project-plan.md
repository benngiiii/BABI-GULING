# Learning Resources Project Plan

## Babi Guling – AI Overview

**Document status:** Version 4.0 (2026-11-05). Updated for Stage 2. The module follows the lecturer's four course chapters, and Markdown V2.0 of all four chapters has been rewritten around the lecturer's topics after the feedback that the earlier text was hard to understand. The earlier five-chapter plan (v1.0–v1.4) and the Stage 1 rebuild (v2.0) are kept in the version table.

| Version | Date | Change |
|---|---|---|
| 1.0–1.4 | 2026-10-23 | Stage 1 plan for the five-chapter structure, revised after QR-007-I01 to QR-007-I03 |
| 2.0 | 2026-11-05 | Rebuilt on the four course chapters; added five content parts, a detailed schedule, a three-stage task list, honest development statuses, and a response to each lecturer feedback point (Section 15) |
| 3.0 | 2026-11-05 | Stage 2: Markdown V2.0 chapters, what Stage 2 adds to each chapter, Stage 2 requirements coverage, Test Bank distribution, Stage 2 submission package, risks, and review plan QR-221 to QR-225 |
| 4.0 | 2026-11-05 | The V2.0 chapters were rewritten from the lecturer's topics: full explanations, "Where This Chapter Fits" storyline, explained figures, fewer exercises; counts, requirements coverage, and statuses updated |

## 1. Project Overview

The purpose of this project is to introduce Artificial Intelligence (AI) to first-year university students and other beginners with no technical background. We develop three connected learning resources from one shared Markdown content base: a **Study Guide and Test Bank**, **PPT Slides**, and **Video Tutorials**. We also prepare a **Live Mini Lecture**.

All resources use the same explanations, examples, terms, and references. If we find an error, we correct the shared Markdown first and then update every affected resource.

Stage 1 gave the module structure and a first version of every chapter. **Stage 2 is the current priority.** It develops the four chapters into Markdown V2.0 and produces the Study Guide and Test Bank, the PPT, the videos, the logs, and a Submission Report. Stage 3 improves everything using the feedback and prepares the live teaching session.

### Intended Learners

Learners have basic computer and internet literacy but no prior knowledge of AI or programming. We explain technical terms in simple language and use familiar examples.

### Learning Outcomes

After completing the module, learners should be able to:

1. Define Computer Science and AI, describe their history and main areas, and explain the three families of machine learning.
2. Explain Symbolic AI: logic, knowledge representation, rule-based and expert systems, planning and search, and symbolic natural language processing.
3. Explain Connectionist AI (neural networks, deep learning) and Big Data (the Vs, technologies, processing, visualization, ethics).
4. Explain Behaviorist AI: reinforcement learning, Markov decision processes, Q-learning, robotics and games, and its challenges.
5. Compare the three approaches, match them to suitable applications, and identify the typical risks of each.

## 2. Shared Markdown Content

The shared Markdown content is the single source for all resources. It has **four chapters**. Each chapter takes its title and topic order from one of the lecturer's course chapters.

| Our chapter | Title | Course source | Owner | Reviewer |
|---|---|---|---|---|
| 1 | Introduction to CS and AI | chap1 | Jonathan Sugianto | Brian Djoni Suzanna |
| 2 | Symbolic AI | chap4 | Gandhi Bestin Dhammananda | Brian Djoni Suzanna |
| 3 | Connectionist AI and Big Data | chap5 | Benedict Subhata | Brian Djoni Suzanna |
| 4 | Behaviorist AI | chap6 | Joseph Lokman | Brian Djoni Suzanna |

### Chapter 1: Introduction to CS and AI

Follows the lecturer's outline: history, definitions, main topics, and the hands-on machine-learning activity.

- **Topic 1: Computer Science.** Definitions, a history table (year, key events, key people, key technologies), and a map of CS topics based on the ACM classification.
- **Topic 2: Artificial Intelligence.** Definitions, a history table, a map of AI areas, and a first look at the three approaches.
- **Topic 3: Machine Learning: A First Look.** Supervised, unsupervised, and reinforcement learning, with a rules-versus-learning example.
- **Topic 4: Hands-On Activity.** Rock Paper Scissors and Smart Classroom.
- **Topic 5: Ask, Then Verify.** The lecturer's questions to ask an AI assistant, with a verification routine.
- Key takeaways, practice questions and answers, glossary, references.

### Chapter 2: Symbolic AI

Follows the lecturer's six topics.

- **Topic 1:** Introduction: GOFAI, a rule example, applications, benefits, limitations.
- **Topic 2:** Logic and reasoning: propositional logic, predicate logic, inference rules.
- **Topic 3:** Knowledge representation: logic, semantic networks, frames and scripts, rules, ontologies.
- **Topic 4:** Rule-based and expert systems.
- **Topic 5:** Planning and problem solving: state space, BFS, DFS, A*, minimax, local search.
- **Topic 6:** Natural language processing in Symbolic AI.
- Hands-on rule-based Smart Classroom, key takeaways, practice questions and answers, glossary, references.

### Chapter 3: Connectionist AI and Big Data

Follows the two groups of topics in the lecturer's overview.

- **Part A, Connectionist AI:** introduction, basics of neural networks, architectures, deep learning and advanced concepts, key applications, ethical considerations.
- **Part B, Big Data:** introduction, technologies, data processing and analytics, analysis and visualization, use cases, ethics and privacy.
- Hands-on activities, key takeaways, practice questions and answers, glossary, references.

### Chapter 4: Behaviorist AI

Follows the lecturer's seven topics.

- Introduction to Behaviorist AI; basics of reinforcement learning; RL algorithms and techniques; Markov decision processes; behavioral AI in robotics and games; applications and use cases; challenges and limitations.
- Hands-on activities, a comparison of the three approaches, key takeaways, practice questions and answers, glossary, references.

### What Stage 2 Adds to Each Chapter (Markdown V2.0)

Version 2.0 keeps the lecturer's topic order and explains every topic in full. The counts were taken from the files on 5 November 2026 by a script.

| Chapter | Words (approx.) | Lecturer's topics | Figures (numbered) | *Check yourself* questions | Hands-on activities | Practice questions | References |
|---|--:|--:|--:|--:|--:|--:|--:|
| 1 Introduction to CS and AI | 12,254 | 5 | 14 | 14 | 3 | 17 | 12 |
| 2 Symbolic AI | 12,959 | 6 | 13 | 18 | 2 | 17 | 11 |
| 3 Connectionist AI and Big Data | 15,067 | 12 (two groups of six) | 22 | 22 | 1 | 17 | 13 |
| 4 Behaviorist AI | 10,891 | 7 | 17 | 12 | 1 | 17 | 11 |

Every chapter has the same routine: **Where This Chapter Fits** (before, now, next), **What You Will Learn**, the topics in the lecturer's order, a **hands-on activity**, **Common Misconceptions**, **Key Takeaways**, **Practice Questions** with an Answer Key, and **What Comes Next**. Inside each topic, the idea is explained in plain sentences with one running example; every figure is followed by a **How to read this figure** paragraph; and one to three **Check yourself** questions with hidden, explained answers and a short **In short** box close the topic. The chapters share one set of terms (see the [shared glossary](study-guide/v2.0/shared-glossary.md)) and two running examples: the Smart Classroom (Chapters 1 to 3) and the corridor and robot vacuum (Chapter 4).

### How the Shared Markdown Content Is Used

- **Study Guide and Test Bank:** explanations, terms, worked examples, and activities become the study guide. Practice questions seed the test bank.
- **PPT Slides:** concepts, comparisons, diagrams, timelines, and worked examples become slides with presenter notes.
- **Video Tutorials:** explanations and demonstrations guide the video scripts.

## 3. Development Status Overview

Statuses: **Outline only**, **Drafted** (written, no signed review), **Checked** (a signed review exists for the current version), **Needs revision**.

| Chapter | Version | Owner | Status | Signed review | Remaining work |
|---|---|---|---|---|---|
| 1 Introduction to CS and AI | 2.0 | Jonathan | Drafted | None yet (QR-221-I01 pending) | Owner reads and fact-checks; signed review; open the reference links; learner test |
| 2 Symbolic AI | 2.0 | Gandhi | Drafted | None yet (QR-222-I01 pending) | Same; also run the Smart Classroom rules by hand |
| 3 Connectionist AI and Big Data | 2.0 | Benedict | Drafted | None yet (QR-223-I01 pending) | Same; also redo the perceptron and word-vote tables by hand |
| 4 Behaviorist AI | 2.0 | Joseph | Drafted | None yet (QR-224-I01 pending) | Same; also redo the Q-learning tables by hand |
| Project documents | 4.0 | Brian | Drafted | None yet (QR-225-I01 pending, by Joseph) | Joseph's review |

### Stage 2 Requirements and Where the Markdown Meets Them

| Requirement | Present in the files | Where |
|---|---|---|
| Explanations and learning outcomes | Yes | Each chapter: *Where This Chapter Fits*, *What You Will Learn*, and the topics |
| Terminology | Yes | Glossary in each chapter; one [shared glossary](study-guide/v2.0/shared-glossary.md) |
| Worked examples | Yes | Binary conversion, nearest neighbour, truth tables, forward chaining, search of the farmer puzzle, a neuron, gradient descent, a perceptron learning OR, backpropagation, Q-learning, expected value |
| Visuals | Yes (PNG) | 66 numbered chapter figures (plus banners) and 2 project figures, each explained in text |
| Activities with feedback | Yes | 7 hands-on activities, each doable with pen and paper |
| Practice with explained answers | Yes | 68 practice questions with an Answer Key; 66 *Check yourself* questions with hidden answers |
| References | Yes | 47 references; most links not yet opened (see the reference register) |
| Independent review | **Not yet** | QR-221-I01 to QR-225-I01 pending |

## 4. Study Guide and Test Bank

**Purpose:** Help learners study alone, practise, and check their understanding.

The Study Guide follows the four chapters and reuses the V2.0 explanations, figures, *Check yourself* questions, and hands-on activities. The Test Bank will contain, at a minimum for Stage 2, **20 true/false, 20 multiple-choice, and 6 open-ended questions**, each with an answer key. Questions come from the practice sections and key takeaways of the chapters. The Quality Lead checks that every question tests a stated learning outcome and that the answers are correct.

Proposed distribution (the team may change it, but every chapter should be covered):

| Chapter | True/false | Multiple-choice | Open-ended |
|---|--:|--:|--:|
| 1 Introduction to CS and AI | 5 | 5 | 1 |
| 2 Symbolic AI | 5 | 5 | 2 |
| 3 Connectionist AI and Big Data | 5 | 5 | 2 |
| 4 Behaviorist AI | 5 | 5 | 1 |
| **Total** | **20** | **20** | **6** |

Each question records its chapter, section, learning outcome, difficulty, and the section of the Markdown that explains the answer. Do not copy a practice question unchanged: reword it and check the answer again.

## 5. PPT Slides

**Purpose:** Present the four chapters visually, in the same order as the Study Guide. Every slide has presenter notes.

- **Chapter 1:** Outline; CS definitions; CS history table; CS map; AI definitions; AI history table; AI map; machine-learning families; hands-on demonstration.
- **Chapter 2:** Symbolic AI idea and the pneumonia rule; logic (truth tables, modus ponens); knowledge representation (semantic network, frames, ontologies); rule-based and expert systems; BFS and DFS trace; A* and minimax example; symbolic NLP and why rules break; Smart Classroom.
- **Chapter 3:** Connectionist idea; the neuron with a calculation; learning by gradient descent; architectures; deep learning and overfitting; applications; ethics; Big Data Vs; technologies; MapReduce example; chart choice; privacy example.
- **Chapter 4:** Behaviorist idea; the RL loop; return and discounting; exploration versus exploitation; Q-learning table; MDP; robots and games; applications; reward hacking; comparison of the three approaches.

## 6. Video Tutorials

**Purpose:** Reinforce the chapters through narration and demonstrations. Stage 2 requires 1 to 8 MP4 files, each no larger than 250 MB, with a VideoGuide.

| Video | Content | Owner |
|---|---|---|
| 1 | Chapter 1: what CS and AI are; history; maps; machine-learning families | Gandhi |
| 2 | Chapter 1 hands-on: Rock Paper Scissors and Smart Classroom | Gandhi |
| 3 | Chapter 2: logic and rules; the thermostat and forward chaining | Gandhi |
| 4 | Chapter 2: search (BFS, DFS, A*, minimax) | Gandhi |
| 5 | Chapter 3: neurons and learning | Gandhi |
| 6 | Chapter 3: Big Data and privacy | Gandhi |
| 7 | Chapter 4: reinforcement learning and Q-learning | Gandhi |
| 8 | Chapter 4: robots, games, and reward hacking; comparing the three approaches | Gandhi |

The team confirms the final number of videos. Brian reviews the scripts against the chapters before recording.

## 7. Live Mini Lecture

**Proposed topic:** Three Ways to Teach a Machine: Rules, Examples, and Rewards (to be confirmed by the team).

**Central question:** How can one task, such as controlling a Smart Classroom, be solved with rules, with examples, and with rewards?

1. **Introduction:** Ask learners how they would make a fan turn on from a spoken command.
2. **Rules (Chapter 2):** Show IF-THEN rules and where they fail ("Turn on the fan").
3. **Examples (Chapter 3):** Show a classifier trained with labelled sentences.
4. **Rewards (Chapter 4):** Show how an agent could learn by trial and error, and how a bad reward can be exploited.
5. **Audience activity:** Learners decide which approach suits three given problems.
6. **Conclusion:** Compare the three approaches.

We avoid unnecessary mathematics.

## 8. How the Resources Support One Another

| Resource | Main function | Connection |
|---|---|---|
| Study Guide and Test Bank | Detailed explanation, practice | Full content, examples, questions |
| PPT Slides | Visual summary | Key concepts and diagrams from the guide |
| Video Tutorials | Narrated demonstration | Step-by-step explanation of hard ideas |
| Live Mini Lecture | Interactive teaching | Uses the Smart Classroom thread in all four chapters |

## 9. Submission Plan

### Stage 2 package

The file names below follow the team's summary of the assignment. **Compare them with the lecturer's assignment text before submitting.** Tick an item only when the file exists and has been opened and checked.

| Deliverable | Proposed file | Owner | Done |
|---|---|---|---|
| A. Markdown V2.0 package (snapshot with assets, rendered PDF, Submission Report with Revision Summary table, review results, mapping table, GitHub evidence, known gaps) | `BABI_GULING_Stage2_Markdown_V2.zip` | Jonathan compiles; Brian checks | [ ] |
| B. Study Guide and Test Bank (at least 20 true/false, 20 multiple-choice, 6 open-ended; activities in six parts) | `BABI_GULING_Stage2_StudyGuide_TestBank_V1.zip` | Benedict | [ ] |
| C. PPT with presenter notes | `BABI_GULING_Stage2_PPT_V1.pptx` | Benedict | [ ] |
| D. Videos (1 to 8 MP4 files, each at most 250 MB) and the video guide | `BABI_GULING_Stage2_VideoGuide` | Gandhi | [ ] |
| E. Project Log | `BABI_GULING_Stage2_ProjectLog` | Joseph | [ ] |
| F. Personal Logs | `BABI_GULING_Stage2_PersonalLogs` | Each member | [ ] |

Checklist for package A:

- [ ] V2.0 chapter folders (each with its `assets/` folder) uploaded to the Stage 2 branch, and every figure shown in the GitHub preview.
- [ ] README, Module Outline, Project Plan, Master Task List, and Quality Standards V2.2 merged.
- [ ] Signed review records QR-221 to QR-224 (chapters) and QR-225 (project documents).
- [ ] Reference links opened and recorded in the reference check register.
- [ ] Revision Summary table in the Submission Report matches the repository.
- [ ] Mapping table (Markdown section to Study Guide and Test Bank, PPT, and video) filled with real numbers.
- [ ] Repository evidence: URL, snapshot date, latest commit identifier, and links to commits and pull requests.
- [ ] Readable PDF of the content.
- [ ] ZIP extracted into a clean folder and checked.

The Stage 1 redo rule: if the Stage 1 score is below 80%, the lecturer's policy allows one resubmission with a report; the resubmission score is capped at 80%. Decision task S2-18 in the [Master Task List](master-task-list.md).

### Peer-Review Record (to be completed by Brian)

| Field | Entry |
|---|---|
| Topic reviewed | Chapter 2, Symbolic AI |
| Version reviewed | 2.0 |
| Author | Gandhi Bestin Dhammananda |
| Reviewer | Brian Djoni Suzanna |
| Review date | (reviewer fills in) |
| What was checked | (reviewer fills in) |
| Findings | (reviewer fills in) |
| Final outcome | Pending |
| Record stored at | `quality/reviews/detailed-review-Stage2-V2.0-DRAFT/QR-222-I01-DRAFT.md` |

## 10. Team Responsibilities

| Member | Role | Main responsibilities |
|---|---|---|
| Benedict Subhata | Visual Design Lead | Chapter 3; Study Guide and Test Bank; PPT Slides |
| Brian Djoni Suzanna | Quality Lead | Independent review of all chapters and resources; Quality Standards; Review Register; project documents |
| Gandhi Bestin Dhammananda | Video Lead | Chapter 2; video tutorials; live teaching |
| Jonathan Sugianto | CIO and Content Lead | Chapter 1; compiling submissions; task-list upkeep |
| Joseph Lokman | CEO | Chapter 4; Project Log; GitHub repository; team coordination |

Brian writes no chapter. Joseph reviews Brian's project documents.

## 11. Repository Evidence and Individual Contributions

These registers are templates. Fill them in with real links and dates. Do not fill them in from memory or guesswork.

| Evidence | Where to find it | Link or ID | Date |
|---|---|---|---|
| Commits for each chapter | GitHub commit history | (add) | |
| Pull requests | GitHub pull requests | (add) | |
| Issues | GitHub Issues | (add) | |
| Review records | `quality/reviews/` | (add) | |

| Member | Contribution (describe what the member did) | Evidence |
|---|---|---|
| Benedict Subhata | (add) | (add) |
| Brian Djoni Suzanna | (add) | (add) |
| Gandhi Bestin Dhammananda | (add) | (add) |
| Jonathan Sugianto | (add) | (add) |
| Joseph Lokman | (add) | (add) |

## 12. AI-Use Documentation

The team records AI assistance in the shared AI-use log and in personal logs. The rebuilt chapters and their V2.0 development were drafted with an AI assistant from the lecturer's slides and standard sources. Each author must read their chapter, check its facts, open the references, and record the check in their personal log. Do not copy AI output without checking.

| Record | File |
|---|---|
| Stage 1 shared AI-use log | `logs/stage1-ai-use-log.md` |
| Stage 2 records | `logs/Stage 2 activity and AI-use records.md` |

## 13. Timeline and Workflow

Official deadlines: Stage 1 was due October 24; **Stage 2 is due Saturday November 7, 2026, 23:59 Beijing time** (internal deadline 18:00); Stage 3 is due November 28. The day-by-day schedule is in the [Master Task List](master-task-list.md#detailed-schedule).

Workflow:

1. Research and outline from the lecturer's slides.
2. Draft the shared Markdown and self-check it.
3. Peer review with a signed review report.
4. Record AI assistance and how it was verified.
5. Produce the resources.
6. Rehearse and collect feedback.
7. Correct the Markdown first, then every affected resource.
8. Collect repository and contribution evidence.
9. Run the checklist and compile the submission.

## 14. Risks and Quality Assurance

| Risk | Response |
|---|---|
| Slides for Chapters 5 and 6 (course numbering) are only outlines, so explanations come from general knowledge | Reviewer compares with the lecture notes; authors check references |
| References not yet opened | Mark them "Not opened" and check before submission |
| Little time before Stage 2 | Use the day-by-day schedule; Brian reviews while authors fix |
| The V2.0 chapters are long (about 8,000 to 10,000 words each) and authors may not read them closely | Each author reads the whole chapter, checks the calculations with a calculator, and signs their personal log; the reviewer samples at least all numbers and all answers |
| Links in the reference lists may not open or may not support the claim | Record each check in the reference check register; replace a bad link before submission |
| Figures break on GitHub because of a wrong file name or missing `assets/` folder | Copy each chapter file and its `assets/` folder together; check the preview |
| Videos, PPT, and Study Guide drift away from the Markdown | Fill the mapping table; correct the Markdown first |
| Online tools in the activities change or are blocked | Every activity has a version that needs no software |
| Uneven workload | Check at every meeting and share tasks |
| Fake or unchecked evidence | Review reports and logs are signed or dated by the person who did the work |

Quality checks use the [Quality Standards V2.2](../quality/reviews/quality-standards-V2.2.md). Section 23 holds the Stage 2 criteria for Markdown V2.0.

## 15. Response to the Stage 1 Lecturer Feedback

| # | Feedback point | Action | Where | Status |
|--:|---|---|---|---|
| 1 | The plan needs five content parts | Five parts listed with owner, reviewer, Stage 2 form, and task IDs. Compare the names with the exact assignment wording. | [Master Task List](master-task-list.md#five-content-parts-of-the-project) | Done; wording to confirm |
| 2 | A detailed schedule is required | Day-by-day Stage 2 schedule and weekly Stage 3 schedule | [Detailed Schedule](master-task-list.md#detailed-schedule) | Done |
| 3 | The task list must cover all assignments of the three stages | Stage 1, Stage 1 fix, Stage 2, Stage 3, and ongoing tasks | [Master Task List](master-task-list.md#master-task-list) | Done; Stage 3 to check against the assignment |
| 4 | Sensible column widths | Tables shortened to seven columns or fewer | Master Task List | Done |
| 5 | Review PPT2024 and three previous-year projects before deciding the structure | The structure now follows the lecturer's four course chapters. The previous-year review is task S2-17. | Module Outline; S2-17 | Structure done; previous-year review **not yet done** |
| 6 | GitHub Markdown shows the complete structure and at least one full chapter | Module Outline v3.0 lists all sections; all four chapters exist as V2.0 | [Module Outline](module-outline.md) | Done; GitHub rendering to confirm |
| 7 | Detailed logs with light-theme screenshots | Project Log and Personal Logs (S2-13, S2-14) | Project Log | **Open** (human task) |
| 8 | Redo policy: below 80% allows one resubmission with a report, capped at 80% | Decision task S2-18 | Master Task List | Open |

### Previous-Year Project Review Record (to be completed by the team)

| Project reviewed | Approach it represents | What we adopted | What we did differently | Reviewed by / date |
|---|---|---|---|---|
| (name and link) | Symbolic | | | |
| (name and link) | Connectionist | | | |
| (name and link) | Behaviorist | | | |

Leave this table empty until the review has been done.

## 16. Expected Outcome

By the final deadline we aim to deliver a consistent set of beginner-friendly AI learning materials: shared Markdown content, a Study Guide and Test Bank, PPT slides, video tutorials, and a live mini lecture. Together they should help learners understand what CS and AI are, how the three classic approaches work, and where each one succeeds and fails.
