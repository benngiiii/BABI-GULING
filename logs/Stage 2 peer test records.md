# Stage 2 — Peer Test Records

**Project:** Introduction to Computer Science and Artificial Intelligence  
**Team:** BABI GULING · **Module:** AI Overview · **Stage:** Stage 2  
**Document Path:** `logs/Stage 2 peer test records.md`

---

## 1. Why this record exists

The Stage 2 assignments ask that every core section is checked by someone **other than its author**, and that a teammate who did not write a selected explanation or activity **follows it as a learner**. The record shows what the tester did, what the tester understood, where the answers differed from the key, and what was changed.

## 2. Who tested, and the limits of these tests

All tests in this file (PT-01 to PT-05) were carried out on **7 November 2026 by Claude (AI)**, working as a learner who used only the question text and the instructions. Claude was the tester, and **no human teammate is recorded as the tester here**.

Two limits are stated openly so that the record stays honest:

- **Independence is limited.** Claude also helped to produce the Study Guide, the Test Bank and the answer keys (see AI-S2-002 and AI-S2-003 in the AI-use record). For each test, Claude answered first, without the key in view, and compared afterwards by script. Even so, an AI that helped to write a text is not an independent reader. These tests are therefore a **technical check of the answer keys and of whether the questions can be answered from the information given**. They are not evidence of how a first-time human learner experiences the material.
- **Human tests are still open.** The "someone other than the author" requirement is met in full only when a teammate also does a test and records it. The planned human tests are in section 6. They are listed as **not done yet**.

The tests themselves are also AI use. They are recorded in the AI-use record as **AI-S2-005**.

## 3. How each test was run

1. The tester took only the question text (no key, no explanations) from the Test Bank source or the Study Guide Markdown.
2. The tester answered every question, doing all calculations from the numbers in the question.
3. Answers were compared with the answer key by script (Test Bank) or by reading (Study Guide).
4. Every number in the questions and keys was recomputed with Python.
5. Every difference, ambiguity or weak point was written down. If the source needed a change, the Markdown was to be fixed first.

## 4. Test records

### PT-01 — Test Bank, True/False questions 1–24

| Field | Entry |
| ----- | ----- |
| **Date and duration** | 7 Nov 2026 · about 10 minutes |
| **Item tested** | Test Bank, Part A: True/False, TF1–TF24 (Chapters 1–8). Source: `BABI-GULING_Stage2_TestBank_V1` |
| **Author** | BABI GULING team, with Claude's help (AI-S2-003) |
| **Tester (not the author)** | Claude (AI). Independence is limited, see section 2 |
| **What the tester did** | Answered all 24 statements True or False from the statement text only, then compared with the key by script. TF9 (precision 30 ÷ 40) was recalculated by hand and in Python |
| **What the tester understood** | Each statement can be judged on its own. The false statements each contain one clear error (for example TF2 swaps "programmer writes rules" and "computer finds rules", TF3 swaps training and inference, TF11 says MIN picks the largest score) |
| **Where the tester was confused** | Nowhere. No statement needed outside knowledge, and no statement had two defensible answers |
| **Answers vs key** | 24 of 24 match. 12 statements are True and 12 are False, so a pattern cannot be guessed. No answer was right for the wrong reason |
| **What was changed and why** | Nothing. No error was found |
| **Where to find the change** | Not applicable |
| **Other resources updated** | None |
| **Unresolved** | A human learner should still attempt the set (task S2-20) |
| **Evidence** | Result of the script comparison: `TF total 24, mismatch []` |

### PT-02 — Test Bank, Multiple Choice questions 1–24

| Field | Entry |
| ----- | ----- |
| **Date and duration** | 7 Nov 2026 · about 15 minutes |
| **Item tested** | Test Bank, Part B: Multiple Choice, MC1–MC24 (Chapters 1–8), including the four "choose TWO" questions (MC1, MC9, MC14 and MC21) |
| **Author** | BABI GULING team, with Claude's help (AI-S2-003) |
| **Tester (not the author)** | Claude (AI). Independence is limited, see section 2 |
| **What the tester did** | Answered all 24 questions from the question text. Worked the calculation questions with the formulas given in the question: MC9 (accuracy 85%, recall 80%), MC13 (z = 2 × 1 − 1 = 1, output 1), MC17 (new Q = 0 + 0.5 × (10 + 0 − 0) = 5) |
| **What the tester understood** | The calculation questions give every formula and number needed, so a learner does not need the chapter open. The wrong options are mistakes a learner could really make (for example MC13 option C uses + bias, MC17 option A forgets α) |
| **Where the tester was confused** | Nowhere in the answering. One observation for the team (not an error): the single-answer questions have the correct letter A six times, B six times, C six times and D only twice (plus four "choose TWO" questions), so D is the correct answer less often than the others |
| **Answers vs key** | 24 of 24 match, including all "choose TWO" pairs. No answer was right for the wrong reason |
| **What was changed and why** | Nothing. The letter spread is a minor point and does not affect correctness. The team may re-order the options of a few questions if it rebuilds the Test Bank anyway |
| **Where to find the change** | Not applicable |
| **Other resources updated** | None |
| **Unresolved** | The option order (optional). A human attempt is still open |
| **Evidence** | Result of the script comparison: `MC total 24, mismatch []`. All numbers recomputed in Python |

### PT-03 — Test Bank, Open-ended questions 1–8

| Field | Entry |
| ----- | ----- |
| **Date and duration** | 7 Nov 2026 · about 20 minutes |
| **Item tested** | Test Bank, Part C: Open-ended questions OE1–OE8 (10 marks each), question text, tables and tasks only |
| **Author** | BABI GULING team, with Claude's help (AI-S2-003) |
| **Tester (not the author)** | Claude (AI). Independence is limited, see section 2 |
| **What the tester did** | Read each scenario and table and checked whether the question can be answered from the information in it. Recomputed every number in the tables and wrote out the facts an answer would need |
| **What the tester understood** | Every question can be answered from its own table. Examples recomputed: OE1 rule-based filter right on 2 of 4 emails and learning-based on 4 of 4; OE3 a filter that flags nothing scores 1,900 ÷ 2,000 = 95%; OE5 cases P, Q and R give z = +2, −1, 0, and a bias of −1 makes R output 1 (z = +1) while Q stays 0 (z = 0); OE7 precision 90 ÷ 300 = 30% and 70 ÷ 100 = 70%, recall 90% and 70%; OE8 selection rates 60%, 40% and 56%, impact ratios 0.67 and 0.93; OE4 forward chaining ends with "Go to the pump station" |
| **Where the tester was confused** | Nowhere. All table totals add up (for example OE7: 90 + 210 = 300 flagged, 70 + 30 = 100 flagged) |
| **Answers vs key** | The facts and numbers an answer needs agree with the marking key in all 8 questions. Open-ended answers are not machine-graded, so the comparison covers numbers and required points, not wording |
| **What was changed and why** | Nothing. No numerical error or unanswerable question was found |
| **Where to find the change** | Not applicable |
| **Other resources updated** | None |
| **Unresolved** | A human should write at least one full essay answer (at least 100 words) and have the marking key applied to it, to check that the mark scheme is usable |
| **Evidence** | Python recomputation of all table numbers (all equal to the figures printed in the questions and keys) |

### PT-04 — Study Guide Markdown, all missions and Quick Check numbers (Chapters 1–8)

| Field | Entry |
| ----- | ----- |
| **Date and duration** | 7 Nov 2026 · about 30 minutes |
| **Item tested** | The Mission 1 and Mission 2 tasks and the Answer Key of each chapter in `Main/study-guide/V2.0/` (Chapters 1–8), and the calculation questions in each Quick Check |
| **Author** | BABI GULING team chapter authors, with Claude's help (AI-S2-002) |
| **Tester (not the author)** | Claude (AI). Independence is limited, see section 2 |
| **What the tester did** | Did each mission as a learner would, with the numbers given in the task, and recomputed every calculation in Python: Chapter 3 (accuracy, precision 40 ÷ 45 = 88.9%, recall 80%), Chapter 4 (search and rules), Chapter 5 (neuron outputs), Chapter 6 (Q-learning update = 5), Chapter 7 (threshold tables), Chapter 8 (selection rates 60% and 30%, impact ratio 0.50, after retraining 0.83, Quick Check 0.75). The classification and judgment tasks (Chapter 2 Mission 1 and 2, Chapter 6 Mission 2, Chapter 7 Mission 1) were worked through while reading the task and the key side by side, so they are a check of the key, not a blind attempt (the blind learner attempt is PT-05) |
| **What the tester understood** | The missions follow the Observe, Reflect, Feedback pattern, and each can be finished from the chapter alone. In Chapter 8 the key correctly states that passing the four-fifths rule (0.83) does not prove fairness |
| **Where the tester was confused** | Two places where a learner may argue with the key, both already covered by the key's own wording: Chapter 2 Mission 1 system 2 (phone keyboard): a modern keyboard may use a generative model, and the key says so; Chapter 7 Mission 1 system 5 (unusual card payments): the key accepts a symbolic answer if the reason is stated ("other well-argued answers are acceptable") |
| **Answers vs key** | All calculation answers match. The classification answers match the key or fall within the key's accepted alternatives. No answer key contained a numerical error |
| **What was changed and why** | Nothing in the content. No answer-key error was found |
| **Where to find the change** | Not applicable |
| **Other resources updated** | None |
| **Unresolved** | A non-author human should still follow one chapter's missions with pen and paper |
| **Evidence** | Python recomputation output for each chapter's numbers |

### PT-05 — Learner walkthrough of one Markdown activity: Chapter 8 Mission 2 "Verify the Claims"

| Field | Entry |
| ----- | ----- |
| **Date and duration** | 7 Nov 2026 · about 10 minutes |
| **Item tested** | `Main/study-guide/V2.0/chapter-8-ai-ethics-and-limitations/ai-ethics-and-limitations.md`, §8.10 Mission 2 (four claims, Parts A to C) |
| **Author** | BABI GULING team chapter author, with Claude's help (AI-S2-002) |
| **Tester (not the author)** | Claude (AI). Independence is limited, see section 2 |
| **What the tester did** | Read the task only (not the Answer Key) and answered Parts A, B and C, then read the Answer Key and compared |
| **What the tester understood** | Claim 1 (EU AI Act bans social scoring): Supported; check the official text. Claim 2 (an invented reference saying every AI system is fair above 90% accuracy): Not supported; the source cannot be found, and accuracy alone does not show fairness. Claim 3 (chatbots update themselves from each conversation): Not supported; training and inference are separate (Chapters 1 and 3). Claim 4 (a 95% accurate spam filter is always good): Misleading; with rare spam a filter that flags nothing also gets about 95%. Part B: the authors' names, the year, the journal-like title and the fancy index name make claim 2 look real; the one test that matters is finding the real source. Part C: "I checked each claim against Section 8.7 and Chapter 3, searched for the cited paper, found no record of it, and rejected it" |
| **Where the tester was confused** | Nowhere. The task says the reference in claim 2 is invented, which keeps the exercise honest. Claim 3 needs the idea from Chapter 3 (training vs using a model), which the Observe prompt points to |
| **Answers vs key** | Verdicts for claims 1 to 4 and the Part B answer match the key. Part C matches the key's example in meaning |
| **What was changed and why** | Nothing |
| **Where to find the change** | Not applicable |
| **Other resources updated** | None |
| **Unresolved** | The test should also be repeated by a human who has not read the chapter |
| **Evidence** | The tester's answers above, written before the key was opened |

## 5. Summary table

| ID | Item | Author | Tester | Date | Main finding | Fixed? |
| -- | ---- | ------ | ------ | ---- | ------------ | ------ |
| PT-01 | Test Bank True/False 1–24 | Team (with Claude) | Claude (AI) | 7 Nov 2026 | 24 of 24 match the key; 12 True and 12 False | No change needed |
| PT-02 | Test Bank Multiple Choice 1–24 | Team (with Claude) | Claude (AI) | 7 Nov 2026 | 24 of 24 match; calculations correct; correct letter D appears only twice | No change needed (optional re-order) |
| PT-03 | Test Bank Open-ended 1–8 | Team (with Claude) | Claude (AI) | 7 Nov 2026 | All questions answerable from their tables; all numbers correct | No change needed |
| PT-04 | Study Guide missions and Quick Check numbers, Chapters 1–8 | Team (with Claude) | Claude (AI) | 7 Nov 2026 | No numerical error; two judgment tasks have accepted alternatives already in the key | No change needed |
| PT-05 | Chapter 8 Mission 2 as a learner | Team (with Claude) | Claude (AI) | 7 Nov 2026 | Answers match the key | No change needed |

## 6. Human tests still to be done and recorded

These are not done yet. Each one should be added as PT-06 and later, with the real tester's name, date and findings. Fill them in only after they have really happened.

| Planned test | Suggested tester | Status |
| ------------ | ---------------- | ------ |
| A teammate attempts all 24 True/False and 24 Multiple Choice questions without the key (task S2-20) | A member who did not write the Test Bank | Not done yet |
| A teammate writes one full open-ended answer and applies the marking key | A member who did not write the Test Bank | Not done yet |
| A non-author follows one Study Guide station or one Markdown mission | Any member who did not write that chapter | Not done yet |
| A member rehearses one PPT section using the presenter notes | Any member | Not done yet |

A teammate may also read this file, repeat any one test above and note whether the result is the same.
