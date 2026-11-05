# Stage 2 Revision Summary (Markdown V2.0)

> **Project:** Babi Guling – AI Overview | **Date:** 2026-11-05 | **Prepared with AI assistance.** The team must check each row against the repository before it goes into the Submission Report.

This table lists the main problems and feedback points, what changed in Markdown V2.0, and where to find it. This edition replaces the earlier Stage 2 packages, which were too close to Stage 1 and then too heavy with exercises.

| # | Problem or feedback | What was changed | Location |
|--:|---|---|---|
| 1 | The lecturer's Stage 1 feedback asked for a module that follows the course materials | The module has four chapters titled after the lecturer's four course chapters, with the topics in the order of the slides | All chapters, header line "Course source" and the section list |
| 2 | Feedback of 5 November: readers cannot tell what the chapters are explaining; the explanations are too short; the page is mostly exercises | Every topic of the lecturer's slides now has a full explanation in plain sentences before any question. Exercises were reduced to one to three *Check yourself* questions per topic and one hands-on activity per chapter. The deep-dive and case-study sections and the *Try It* blocks were removed; real examples sit inside the topic that needs them | All chapters (51,171 words, 66 *Check yourself* questions, 7 hands-on activities) |
| 3 | Too many numbered branches (1.2, 1.3, ...) make the path through a chapter hard to follow | Topics are `##` sections with a few `###` parts and no numbered sub-sections. Nothing is nested deeper than `###` | All chapters; `Main/style-guide.md` |
| 4 | The roadmap figure did not help a reader | The roadmap was replaced by **Where This Chapter Fits**: a figure of the four chapters with the current one highlighted, and a table with *Before this chapter*, *In this chapter*, *In the next chapter*. Each chapter ends with **What Comes Next**, which states the problem left open and how the next chapter answers it | The first section and the last section of every chapter |
| 5 | Figures did not explain what they mean, and the text was small | All 66 numbered figures were redrawn with larger text, a title that states the point, and labels on the parts. Each figure is followed by a **How to read this figure** paragraph that explains every labelled part | Every chapter's `assets/` folder; Module Outline, "Figures and Assets" |
| 6 | The first pages only covered the cover of the topic, as if the reader already knew the field | Each topic starts from a question the reader can imagine, defines every term where it first appears, and builds the idea with one running example | Opening of each topic in every chapter |
| 7 | Stage 2 requires activities where the learner does something and sees the result | Each chapter has a hands-on activity written in steps with the expected result: Chapter 1 has three (Rock Paper Scissors, Smart Classroom, nearest neighbour), Chapter 2 has two (write rules, break the rules), Chapter 3 has a word-vote learner trained by hand, and Chapter 4 has the corridor trained by hand and a reward-hack spotting task. All can be done with pen and paper | Chapter 1 Topic 4; Chapter 2 hands-on; Chapter 3 hands-on; Chapter 4 hands-on |
| 8 | The Smart Classroom was inconsistent: Chapter 2's rule 1 accepted "Fan on please" while Chapter 1 predicted exact-match rules | Chapters 1 and 2 use the same four exact-match rules; the "contains" extension is a separate step. Chapter 3 builds the learned version of the same task | Chapter 1 Activity B; Chapter 2 hands-on; Chapter 3 hands-on |
| 9 | Chapters must read as one story | Each chapter has a "before, now, next" table and a closing bridge; terms are explained once and listed in a shared glossary; the Module Wrap-Up in Chapter 4 compares the three approaches | *Where This Chapter Fits*, *What Comes Next*, shared-glossary.md (138 terms), Chapter 4 *Module Wrap-Up* |
| 10 | The history tables had no sources and diagrams were Mermaid code | All figures are PNG files in `assets/` folders with alt text and captions. Chapter 1 history is given in tables and explained in text | Every chapter's `assets/` folder |
| 11 | References had no links | Every reference except the lecturer's slides has a link (47 references). A register tracks which links were opened. Most were not opened and are labelled so | Chapter reference lists; reference-check-register-DRAFT.md |
| 12 | Frequent mistakes were not addressed | A *Common Misconceptions* table is in every chapter | Before *Key Takeaways* in each chapter |
| 13 | Practice was limited to recall | Each chapter has 17 practice questions in four parts (multiple choice, short answer, apply it, and compute or trace), every one with an explained answer | Practice Questions and Answer Key (68 questions) |
| 14 | The page had to be easy to read directly on GitHub, in a serious academic tone, without games | Every chapter has a banner, a navigation table, a collapsed contents list, callout boxes, and hidden answers. The mascot, game wording, emoji, and interactive pages are not used. The style is described in `Main/style-guide.md` | Every chapter; `Main/style-guide.md` |
| 15 | Quality criteria did not match the new structure | Quality Standards V2.2, Section 23, was rewritten for the new structure (lecturer's topics, explained before practised, figures that explain themselves, understandability, sub-section depth) | quality-standards-V2.2.md |

## Not Done in This Revision

* No reviewer has signed the V2.0 chapters (QR-221-I01 to QR-224-I01 are drafts with the decision Pending Review).
* Most reference links have not been opened.
* Learner testing has not been done. The most useful test is to ask a person who has not studied AI to read one topic and say what each figure means.
* The optional tools mentioned in Chapter 1 were not run. Every activity has a paper version.
* The page layout and the figures have not yet been checked on the live GitHub repository (light and dark themes, phone width).
* The lecturer's slides for Chapters 5 and 6 were only topic outlines, so the explanations in Chapters 3 and 4 come from standard sources and must be compared with the lecture notes.

## Mapping to the Other Resources (to be completed by the resource owners)

The Submission Report needs a table that maps each Markdown section to the Study Guide and Test Bank, the PPT, and the videos. The columns below stay empty until those resources exist. Fill them with the real section numbers, question numbers, slide numbers, and video file names. Write "not selected for video" where a section is not covered by a video.

| Markdown section | Study Guide and Test Bank | PPT | Video |
|---|---|---|---|
| Chapter 1: Where This Chapter Fits | | | |
| Chapter 1: Topic 1: Computer Science | | | |
| Chapter 1: Topic 2: Artificial Intelligence | | | |
| Chapter 1: Topic 3: Machine Learning, a First Look | | | |
| Chapter 1: Topic 4: Hands-On Activity, Machine Learning | | | |
| Chapter 1: Topic 5: Using an AI Assistant for Study | | | |
| Chapter 1: Common Misconceptions | | | |
| Chapter 1: Key Takeaways | | | |
| Chapter 1: Practice Questions | | | |
| Chapter 1: What Comes Next: From Words to Rules | | | |
| Chapter 2: Where This Chapter Fits | | | |
| Chapter 2: Topic 1: Introduction to Symbolic AI | | | |
| Chapter 2: Topic 2: Logic and Reasoning | | | |
| Chapter 2: Topic 3: Knowledge Representation | | | |
| Chapter 2: Topic 4: Rule-Based Systems and Expert Systems | | | |
| Chapter 2: Topic 5: Planning and Problem Solving | | | |
| Chapter 2: Topic 6: Natural Language Processing in Symbolic AI | | | |
| Chapter 2: Hands-On Activity: A Rule-Based Smart Classroom | | | |
| Chapter 2: Common Misconceptions | | | |
| Chapter 2: Key Takeaways | | | |
| Chapter 2: Practice Questions | | | |
| Chapter 2: What Comes Next: From Written Rules to Learned Weights | | | |
| Chapter 3: Where This Chapter Fits | | | |
| Chapter 3: Part A, Topic 1: Introduction to Connectionist AI | | | |
| Chapter 3: Part A, Topic 2: Basics of Neural Networks | | | |
| Chapter 3: Part A, Topic 3: Architectures of Neural Networks | | | |
| Chapter 3: Part A, Topic 4: Deep Learning and Advanced Concepts | | | |
| Chapter 3: Part A, Topic 5: Key Applications of Connectionist AI | | | |
| Chapter 3: Part A, Topic 6: Ethical Considerations and Challenges | | | |
| Chapter 3: Part B, Topic 1: Introduction to Big Data | | | |
| Chapter 3: Part B, Topic 2: Big Data Technologies | | | |
| Chapter 3: Part B, Topic 3: Data Processing and Analytics | | | |
| Chapter 3: Part B, Topic 4: Data Analysis and Visualization | | | |
| Chapter 3: Part B, Topic 5: Big Data Use Cases | | | |
| Chapter 3: Part B, Topic 6: Big Data Ethics and Privacy | | | |
| Chapter 3: Hands-On Activity: A Learner You Train and Then Break | | | |
| Chapter 3: Common Misconceptions | | | |
| Chapter 3: Key Takeaways | | | |
| Chapter 3: Practice Questions | | | |
| Chapter 3: What Comes Next: From Labelled Examples to Rewards | | | |
| Chapter 4: Where This Chapter Fits | | | |
| Chapter 4: Topic 1: Introduction to Behaviorist AI | | | |
| Chapter 4: Topic 2: Basics of Reinforcement Learning | | | |
| Chapter 4: Topic 3: RL Algorithms and Techniques | | | |
| Chapter 4: Topic 4: Markov Decision Processes (MDPs) | | | |
| Chapter 4: Topic 5: Behavioral AI in Robotics and Games | | | |
| Chapter 4: Topic 6: Applications and Use Cases of Behaviorist AI | | | |
| Chapter 4: Topic 7: Challenges and Limitations | | | |
| Chapter 4: Hands-On Activity: Train a Learner, Then Try to Fool It | | | |
| Chapter 4: Module Wrap-Up: Three Ways to Build AI | | | |
| Chapter 4: Common Misconceptions | | | |
| Chapter 4: Key Takeaways | | | |
| Chapter 4: Practice Questions | | | |
| Chapter 4: Where to Go Next | | | |
