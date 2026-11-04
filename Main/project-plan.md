# Learning Resources Project Plan

## Babi Guling – AI Overview

**Document status:** Version 2.0 (2026-11-05). This plan was rebuilt after the lecturer's Stage 1 feedback. The module now follows the lecturer's four course chapters. The earlier five-chapter plan (v1.0–v1.4) is kept in the repository history.

| Version | Date | Change |
|---|---|---|
| 1.0–1.4 | 2026-10-23 | Stage 1 plan for the five-chapter structure, revised after QR-007-I01 to QR-007-I03 |
| 2.0 | 2026-11-05 | Rebuilt on the four course chapters; added five content parts, a detailed schedule, a three-stage task list, honest development statuses, and a response to each lecturer feedback point (Section 15) |

## 1. Project Overview

The purpose of this project is to introduce Artificial Intelligence (AI) to first-year university students and other beginners with no technical background. We develop three connected learning resources from one shared Markdown content base: a **Study Guide and Test Bank**, **PPT Slides**, and **Video Tutorials**. We also prepare a **Live Mini Lecture**.

All resources use the same explanations, examples, terms, and references. If we find an error, we correct the shared Markdown first and then update every affected resource.

For Stage 1 the priority is a clear module structure and at least one fully developed chapter, supported by a documented review, meaningful GitHub work, and a self-contained submission. Stage 2 and Stage 3 deepen the content and produce the other resources.

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

### How the Shared Markdown Content Is Used

- **Study Guide and Test Bank:** explanations, terms, worked examples, and activities become the study guide. Practice questions seed the test bank.
- **PPT Slides:** concepts, comparisons, diagrams, timelines, and worked examples become slides with presenter notes.
- **Video Tutorials:** explanations and demonstrations guide the video scripts.

## 3. Development Status Overview

Statuses: **Outline only**, **Drafted** (written, no signed review), **Checked** (a signed review exists for the current version), **Needs revision**.

| Chapter | Version | Owner | Status | Signed review | Remaining work |
|---|---|---|---|---|---|
| 1 Introduction to CS and AI | 1.1 | Jonathan | Drafted | None yet (QR-121-I01 pending) | Signed review; verify references marked "Not opened"; learner test |
| 2 Symbolic AI | 1.1 | Gandhi | Drafted | None yet (QR-122-I01 pending) | Signed review; verify references; learner test |
| 3 Connectionist AI and Big Data | 1.1 | Benedict | Drafted | None yet (QR-123-I01 pending) | Signed review; verify references; learner test |
| 4 Behaviorist AI | 1.1 | Joseph | Drafted | None yet (QR-124-I01 pending) | Signed review; verify references; learner test |
| Project documents | 2.0 | Brian | Drafted | None yet (QR-125-I01 pending, by Joseph) | Joseph's review |

### Stage 1 Focus Topic

| Field | Entry |
|---|---|
| Selected topic | Chapter 2, Symbolic AI (the most developed chapter; 52 lecturer slides) |
| Selection date | 2026-11-05 |
| Selected by | Team (to confirm) |
| Verified status | Drafted. Becomes Checked only after the QR-122-I01 signed review. |

| Required element | Present in the file | Where |
|---|---|---|
| Explanations | Yes | Topics 1–6 |
| Terminology | Yes | Glossary; definitions at first use |
| Worked examples | Yes | Truth tables, forward chaining, BFS/DFS, A*, minimax |
| Visual | Yes | Figures 2.1–2.6 (PNG files in the chapter's `assets/` folder) |
| Learner activity | Yes | Rule-based Smart Classroom; practice questions |
| Explained answers | Yes | Answer Key |
| References | Yes | References (some marked "Not opened") |

## 4. Study Guide and Test Bank

**Purpose:** Help learners study alone, practise, and check their understanding.

The Study Guide follows the four chapters. The Test Bank will contain, at a minimum for Stage 2, **20 true/false, 20 multiple-choice, and 6 open-ended questions**, each with an answer key. Questions come from the practice sections and the key takeaways of the chapters. The Quality Lead checks that every question tests a stated learning outcome and that the answers are correct.

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

### Stage 1 (rebuilt content)

The lecturer's Stage 1 package is a ZIP named `TeamName_Stage1_GitHub_Markdown_V1.zip` with a Submission Report, a Markdown source snapshot, and a readable PDF of the learning content. The checklist is unticked because the rebuilt files have not yet been merged and packaged. Tick an item only when the file exists.

- [ ] Rebuilt chapters merged into the repository.
- [ ] README, Module Outline, Project Plan, and Master Task List v2.0 merged.
- [ ] Signed review records for the chapters (QR-121 to QR-124) and the project documents (QR-125).
- [ ] Submission Report with repository URL, snapshot date, latest commit identifier, content status, evidence, contributions, review outcome, and next steps.
- [ ] Markdown source snapshot with assets (every `assets/` folder included and every image link checked).
- [ ] Readable PDF of the content.
- [ ] Project Log and Personal Logs with light-theme screenshots.
- [ ] ZIP extracted into a clean folder and checked.

If the Stage 1 score is below 80%, the lecturer's policy allows one resubmission with a report; the resubmission score is capped at 80%. Decision task: S2-18 in the [Master Task List](master-task-list.md).

### Peer-Review Record (to be completed by Brian)

| Field | Entry |
|---|---|
| Topic reviewed | Chapter 2, Symbolic AI |
| Version reviewed | 1.1 |
| Author | Gandhi Bestin Dhammananda |
| Reviewer | Brian Djoni Suzanna |
| Review date | (reviewer fills in) |
| What was checked | (reviewer fills in) |
| Findings | (reviewer fills in) |
| Final outcome | Pending |
| Record stored at | `quality/reviews/detailed review Stage 1 fix/QR-122-I01` |

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

The team records AI assistance in the shared AI-use log and in personal logs. The rebuilt chapters were drafted with an AI assistant from the lecturer's slides. Each author must read their chapter, check its facts, and record the check in their personal log. Do not copy AI output without checking.

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
| Uneven workload | Check at every meeting and share tasks |
| Fake or unchecked evidence | Review reports and logs are signed or dated by the person who did the work |

Quality checks use the [Quality Standards V2.1](../quality/reviews/quality-standards-V2.1.md).

## 15. Response to the Stage 1 Lecturer Feedback

| # | Feedback point | Action | Where | Status |
|--:|---|---|---|---|
| 1 | The plan needs five content parts | Five parts listed with owner, reviewer, Stage 2 form, and task IDs. Compare the names with the exact assignment wording. | [Master Task List](master-task-list.md#five-content-parts-of-the-project) | Done; wording to confirm |
| 2 | A detailed schedule is required | Day-by-day Stage 2 schedule and weekly Stage 3 schedule | [Detailed Schedule](master-task-list.md#detailed-schedule) | Done |
| 3 | The task list must cover all assignments of the three stages | Stage 1, Stage 1 fix, Stage 2, Stage 3, and ongoing tasks | [Master Task List](master-task-list.md#master-task-list) | Done; Stage 3 to check against the assignment |
| 4 | Sensible column widths | Tables shortened to seven columns or fewer | Master Task List | Done |
| 5 | Review PPT2024 and three previous-year projects before deciding the structure | The structure now follows the lecturer's four course chapters. The previous-year review is task S2-17. | Module Outline; S2-17 | Structure done; previous-year review **not yet done** |
| 6 | GitHub Markdown shows the complete structure and at least one full chapter | Module Outline v2.0 lists all sections; all four chapters exist | [Module Outline](module-outline.md) | Done; GitHub rendering to confirm |
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
