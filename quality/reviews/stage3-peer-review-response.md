# Stage 3 Peer-Review Response

**Team:** BABI GULING · **Module:** AI Overview · **Version reviewed by peers:** Stage 2 V1.0 materials  
**Reviews received:** AeroAI (team of their choice) · FengweiFriedRice (team of their choice)  
**Response prepared:** 20 November 2026 · **Owners:** Brian Djoni Suzanna (Quality Lead), Joseph Lokman (CEO)

This file lists every finding from the two peer reviews, what we changed, where the change is, and how it was checked. Findings we did not adopt are explained. Status: **Done** = change made in the final files; **In progress** = change agreed, final file not yet exported.

## 1. Scores received

| Reviewer | Study Guide + Test Bank | PPT Slides | Video Tutorials |
|----------|:-----------------------:|:----------:|:---------------:|
| AeroAI (reviewer-devised criteria) | 34 / 38 (89%) | 31 / 35 (89%) | 20 / 24 (83%) |
| FengweiFriedRice (course rubric) | 89 / 100 | 94 / 100 | 93 / 100 |

## 2. Findings and responses

### Study Guide and Markdown

| # | Finding (source) | Our change and reason | Location | Check | Status |
|:-:|------------------|-----------------------|----------|-------|:------:|
| G1 | "TEAM:" notes and "to be checked by the team" left on pp. 20, 75, 101, 130, 158, 212 (Fengwei) | Each platform link tested; every internal note removed | Study Guide V2 pp. 21, 76, 102, 131, 159, 215 | Text search of V2 for "TEAM:" and "to be checked" returns nothing; each link opened again | Done |
| G2 | Eight Video Stops describe "planned" videos; links missing; numbering wrong from Station 4 (Fengwei; AeroAI) | Video Stops rewritten for the six real videos, with start times; Stations 4–6 all point to Video 04 | Study Guide Video Stops; Markdown "Use this chapter with the other resources" in every chapter; `Main/resource-mapping.md` §2 | Times taken from the final MP4s and the peer reviews; Video Lead to confirm each time when watching the final files | Done (times to be confirmed by Video Lead) |
| G3 | Status pages pp. 235 and 241 claim "REVIEWED" and "DONE" while pages say otherwise (Fengwei) | Status pages rewritten to match the final state | Study Guide pp. 238 and 244 | Cross-checked with G1 and G2 | Done |
| G4 | "Free prize at noon": guide calls +1 a weakness, video labels it spam (Fengwei) | One clear statement: the email **is spam**, the +1 prediction is correct, and the thin margin is the warning sign; Mission 2 answer now says the −1 result is wrong | Markdown §1.5 Step 5 and §1.7 Answer Key; Test Bank OE-01 key; slide 14 notes | Guide, Test Bank and Video 01 now give the same label | Done (Markdown, Study Guide p. 20 and Control Room p. 34, Test Bank, PPT slide 14 and notes) |
| G5 | Supporting file labels a calculator "Narrow" with functionality "Yes"; contradicts guide p. 31 (Fengwei) | Calculator marked **Not AI**; functionality column uses the four real types | `BABIGULING_SupportedFiles_V2.pdf` | Compared with §1.1 and §2.3 | Done |
| G6 | 21–29 hours is heavy for beginners; add a minimum route or schedule (AeroAI) | New Module Overview with prerequisites, a 10-hour minimum route and a four-week plan | Markdown Module Overview; new Study Guide page 6 "Short on time? Take the minimum route first" | Every section in the minimum route checked to exist | Done |
| G7 | Contents page gives slide numbers, not page numbers; some cards repeated (Fengwei) | Contents uses page numbers; the repeated mission card is removed from all six "(2/2)" worksheet pages, which now use the full width | Study Guide p. 4; pp. 26, 106, 135, 137, 165, 190 | Page numbers match the station boards in the V2 PDF | Done |
| G8 | Two identities: "Rebuild Bit" vs "Babi Guling's Kitchen" (both reviews) | Shared "BABI GULING · AI Overview" label on every resource, and Bit appears in the kitchen on the slide and video title cards. **Not adopted:** merging into one theme, because both themes are already built into 242 guide pages, 67 slides and six videos, and rebuilding them would take time from content fixes | Study Guide cover (pig chef + "Slides and videos: Babi Guling's Kitchen"); PPT slide 1 (Bit in the kitchen) | Visual check of both covers | Done |

### Test Bank

| # | Finding (source) | Our change and reason | Location | Check | Status |
|:-:|------------------|-----------------------|----------|-------|:------:|
| T1 | 46 of 56 questions were Remember/Understand (Fengwei) | 15 questions rewritten as short cases; levels now Remember 6, Understand 23, Apply 21, Analyse/Evaluate 6 | TF-05, 11, 15, 19, 23, 24; MC-04, 10, 12, 15, 16, 18, 20, 23, 24; OE-02, OE-06 | Level counts recomputed from the tags | Done |
| T2 | Implausible distractors in MC-20, MC-23, MC-24 (Fengwei) | All options are now real course concepts that a learner must reason about | MC-20, MC-23, MC-24 and their keys | Each wrong option has a reason in the key | Done |
| T3 | Video 02 solves the "MegaMind" case used in OE-02 (Fengwei) | OE-02 replaced with a new case ("StudyBuddy") that also tests a rule-based + ML mix; the video keeps MegaMind as a worked example | Test Bank OE-02 and key | New key points checked against §2.2–2.5 | Done |
| T4 | Learners may think a good score means full mastery (AeroAI) | Note added: the Test Bank samples each station | Test Bank §4; Module Overview "About the Test Bank" | — | Done |
| T5 | Open-ended answers rely on self-marking (AeroAI) | **Kept** the self-marking design, because the Test Bank is for independent study; each OE has key points, a sample answer and a marking guide with marks per criterion | Test Bank Key 3 | — | Not adopted (reason given) |

### PPT Slides

| # | Finding (source) | Our change and reason | Location | Check | Status |
|:-:|------------------|-----------------------|----------|-------|:------:|
| P1 | Notes add up to 144 minutes; no split point or optional slides (Fengwei) | Two-lesson split after slide 28, or three lessons (1–28, 29–47, 48–68); optional slides 10, 22, 38, 42, 44, 46, 60, 63 marked in the notes | Notes of slides 2, 28, 29, 47 | TIME lines re-added: 147 min in total | Done |
| P2 | Slide 61 lists guide, Test Bank and game but not the videos (Fengwei) | Fourth card for the videos; video number (and start time for Video 04) in the footer of each chapter's first slide | Slide 62; slides 7, 16, 20, 30, 37, 43, 49, 54 | — | Done |
| P3 | Dense slides 27–28 and 54–56 need a back-of-room check (AeroAI) | Small labels enlarged (15–17 pt to 18–19 pt); classroom slideshow check still to be done by the team | Slides 27, 54, 55, 56 | Back-of-room check record | Done (labels); room check pending |

### Video Tutorials

| # | Finding (source) | Our change and reason | Location | Check | Status |
|:-:|------------------|-----------------------|----------|-------|:------:|
| V1 | No timestamp index; six videos vs eight stations (both reviews) | Video Guide with chapter timestamps; Resource Mapping §2 | Video Guide; `Main/resource-mapping.md` | Each time checked by watching | In progress |
| V2 | Narration, pacing and audio not fully checked (AeroAI) | A non-creator watches every final video in full and records issues with timestamps | Video Guide verification section | Watch-through record | In progress |
| V3 | Video 02 is 960×544, lower than the others (Fengwei) | Re-export at 1280×720 if the source project allows | Video 02 | File properties | In progress |
| V4 | Three technical chapters share one 8-minute video (Fengwei) | **Not adopted for this version:** the eight-video maximum allows splitting, but re-recording three videos before 28 November would leave no time for checking. We give exact start times instead and list it as a limitation | README §8 | — | Not adopted (reason given) |

## 3. Change that came from the mini lecture

Our mini lecture, *"What If AI Doesn't Need Emotions to Harm Us?"*, explained AI agents, tool permissions and objective misalignment. These ideas were not in the module, although they connect Chapter 6 (reward hacking) and Chapter 8 (safety). We added a short subsection with a table of terms, the "reward is not emotion" point, four safeguards and a Pause-and-predict question with an answer.

**Location:** Markdown §8.6; Study Guide pp. 211–212 and Control Room p. 228; PPT slide 58;  "Can AI harm us without feeling anything?"; new glossary terms (AI agent, least permission, objective misalignment); Chapter 8 learning outcome 6; one new misconception; reference Amodei et al. (2016); Test Bank TF-23 now tests it. **Check:** definitions compared with the mini-lecture script so that the lecture and the guide agree.
