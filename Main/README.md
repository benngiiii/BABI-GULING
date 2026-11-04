# BABI GULING — AI OVERVIEW

**Module:** AI Overview
**Team Name:** BABI GULING
**Project:** Introduction to Computer Science and Artificial Intelligence
**Current Stage:** Stage 2 — Content Development and Learning Resource Production
**Last Updated:** November 5, 2026

---

## 1. Team Information

### Team Members

| No. | Name                      | Chinese Name | GitHub Username  | Student ID | Role               |
| :-: | ------------------------- | ------------ | ---------------- | :--------: | ------------------ |
|  1  | Benedict Subhata          | 王志伟          | benngiiii        | 1820262181 | Visual Design Lead |
|  2  | Brian Djoni Suzanna       | 吴梓诚          | brizz0-0         | 1820262162 | Quality Lead       |
|  3  | Gandhi Bestin Dhammananda | 熊特友          | bestinsiuuu77    | 1820262168 | Video Lead         |
|  4  | Jonathan Sugianto         | 蔡德辉          | JonathanSugianto | 1820262245 | CIO                |
|  5  | Joseph Lokman             | 骆韦铨          | JosephLokman     | 1820262233 | CEO                |

---

## 2. Project Overview

### Project Purpose

The BABI GULING team project aims to introduce **Artificial Intelligence (AI)** to beginners with little or no previous knowledge of AI or programming.

The project focuses on explaining fundamental AI concepts through structured learning materials, practical examples, and beginner-friendly explanations.

The module covers four chapters, taken from the lecturer's course chapters:

1. Introduction to CS and AI.
2. Symbolic AI.
3. Connectionist AI and Big Data.
4. Behaviorist AI.

The project uses a shared Markdown content base as the main reference for developing three learning resources.

| Learning Resource           | Purpose                                                                                      |
| --------------------------- | -------------------------------------------------------------------------------------------- |
| **Study Guide + Test Bank** | Provides structured explanations, examples, and practice questions for independent learning. |
| **PPT Slides**              | Presents important concepts visually through diagrams, examples, and concise explanations.   |
| **Video Tutorials**         | Explains selected AI concepts through narration, visual demonstrations, and examples.        |

The Markdown content serves as the main reference for these resources. This approach helps maintain consistency and makes future revisions easier.

### Intended Learners

The target audience consists of beginners with no previous background in AI or programming.

Learners are expected to have basic computer and internet literacy. Technical terms are introduced and explained using beginner-friendly language.

### Learning Outcomes

After completing this module, learners should be able to:

1. Define Computer Science and Artificial Intelligence, describe their history and main areas, and explain the three families of machine learning.
2. Explain Symbolic AI: logic, knowledge representation, rule-based and expert systems, planning and search, and symbolic natural language processing.
3. Explain Connectionist AI (neural networks and deep learning) and Big Data (the Vs, technologies, processing, visualization, and ethics).
4. Explain Behaviorist AI: reinforcement learning, Markov decision processes, Q-learning, applications in robotics and games, and its challenges.
5. Compare the three approaches, match them to suitable applications, and identify the typical risks of each.

---

## 3. Module Content

The AI Overview module consists of four chapters. Each chapter follows one of the lecturer's course chapters.

| Chapter | Topic | Main Content | Version |
| :-----: | ----------------------------- | -------------------------------------------------------------------------------------------------- | :-----: |
| 1 | **Introduction to CS and AI** | Definitions and history of CS and AI, main areas, machine-learning families, and hands-on machine learning. | 1.1 |
| 2 | **Symbolic AI** | Logic and reasoning, knowledge representation, rule-based and expert systems, planning and search, and symbolic NLP. | 1.1 |
| 3 | **Connectionist AI and Big Data** | Neural networks, architectures, deep learning, applications and ethics; Big Data technologies, analytics, visualization, and privacy. | 1.1 |
| 4 | **Behaviorist AI** | Reinforcement learning, Q-learning, Markov decision processes, robotics and games, applications, and limitations. | 1.1 |

For detailed chapter descriptions, learning objectives, and the planned module structure, refer to the [Module Outline](module-outline.md).

---

## 4. Team Roles and Responsibilities

Each team member has a specific role supporting project development and coordination.

| Team Member                   | Role               | Main Responsibilities                                                                                                                      |
| ----------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Joseph Lokman**             | CEO                | Writes Chapter 4, coordinates overall progress and deadlines, keeps the Project Log, and manages the GitHub repository.                    |
| **Jonathan Sugianto**         | CIO and Content Lead | Writes Chapter 1, supports repository organization, and compiles the project materials and submissions.                                 |
| **Benedict Subhata**          | Visual Design Lead | Writes Chapter 3, and supports visual consistency, presentation design, diagrams, and the Study Guide.                                     |
| **Gandhi Bestin Dhammananda** | Video Lead         | Writes Chapter 2, and coordinates video tutorials, narration planning, and the live teaching session.                                     |
| **Brian Djoni Suzanna**       | Quality Lead       | Reviews all four chapters independently (he writes no chapter), maintains the project documents and Quality Standards, and records findings. |

All members contribute to the development, revision, and improvement of the AI Overview learning materials.

Detailed task assignments, deadlines, and progress are recorded in the [Master Task List](master-task-list.md).

---

## 5. Project Documents

The main project documents are maintained together to provide continuous documentation throughout all project stages.

| Document                     | Purpose                                                                                           | Link                                                                      |
| ---------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Project Plan**             | Explains project objectives, workflow, timeline, team responsibilities, and development approach. | [project-plan.md](project-plan.md)                                        |
| **Master Task List**         | Records project tasks, assigned members, deadlines, and completion status across all stages.      | [master-task-list.md](master-task-list.md)                                |
| **Module Outline**           | Describes the module structure, learning outcomes, chapter topics, and content development plan.  | [module-outline.md](module-outline.md)                                    |
| **Quality Standards**        | Defines the criteria used to review learning materials and project documentation.                 | [quality-standards.md](../quality/reviews/quality-standards.md)           |
| **Quality Review Register**  | Tracks quality review reports, identified issues, and review progress.                            | [review-register.md](../quality/reviews/review-register.md)               |
| **Final Submission Audit**   | Records final quality checks for submission preparation.                                          | [final-submission-audit.md](../quality/reviews/final-submission-audit.md) |
| **Stage 1 AI Use Log**       | Records AI-assisted activities during Stage 1.                                                    | [stage1-ai-use-log.md](../logs/stage1-ai-use-log.md)                      |
| **Stage 1 Combined Content** | Preserves the combined learning content developed during Stage 1.                                 | [stage1_Content.md](stage1_Content.md)                                    |

The project documents remain in the main branch and are updated when necessary.

Stage-specific learning content and development records are maintained separately to preserve the history of each stage.

---

## 6. Repository Structure and Version Management

The repository uses separate branches and content versions to organize development while preserving previous work.

### Repository Organization

```text
BABI-GULING/
│
├── Main/
│   ├── README.md
│   ├── project-plan.md
│   ├── master-task-list.md
│   ├── module-outline.md
│   │
│   └── study-guide/
│       ├── v1.0/
│       │   └── Chapter 1–4 (Stage 1, rebuilt on the course chapters)
│       │   └── stage1_Content.md
│       │
│       └── v2.0/
│           └── Chapter 1–4 (Stage 2)
│           └── stage2_Content.md
│
├── logs/
│   ├── stage1-ai-use-log.md
│   └── Stage 2 activity and AI-use records.md
│
└── quality/
    └── reviews/
        ├── quality-standards-V1.0.md
        ├── quality-standards-V2.0.md 
        ├── review-register.md
        ├── final-submission-audit-V1.0.md
        ├── final-submission-audit-V1.0.md
        │
        ├── detailed review V1.0/
        │   └── Individual quality review reports
        └── detailed review V2.0/
            └── Individual quality review reports
```

*The diagram describes the logical organization of the project. Stage-specific content is maintained in its corresponding development branch.*

### Branch Management

The team uses different Git branches to separate development stages while keeping the same repository.

| Branch                     | Purpose                                                                                                               |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `main`                     | Maintains the main project documentation, project management files, quality review records, and shared documentation. |
| `AI-Overview`              | Preserves the Stage 1 content development and its V1.0 learning materials.                                            |
| Stage 2 development branch | Supports the development and revision of V2.0 learning materials for Chapters 1–4.                                    |

The Stage 1 branch is preserved to maintain the history of the original learning materials.

Stage 2 uses a separate development branch so that the team can improve the content without overwriting the previous version.

### Content Versioning

| Version  | Stage   | Description                                                                                |
| -------- | ------- | ------------------------------------------------------------------------------------------ |
| **V1.0** | Stage 1 | Original learning content developed during the initial project stage.                      |
| **V2.0** | Stage 2 | Revised and expanded learning content developed using the Stage 1 foundation and feedback. |

The version numbers apply to the learning content, not to the entire repository.

Project management documents and quality review records remain in their shared locations instead of being duplicated into separate V1.0 and V2.0 folders.

### Development Workflow

1. Team members work on their assigned development branches.
2. Learning content is written and revised in Markdown.
3. Changes are reviewed before being integrated.
4. Quality review reports and issue records are maintained in the shared quality documentation.
5. Approved changes are incorporated into the appropriate project version.
6. Previous versions remain available for reference and traceability.

---

## 7. Project Workflow

The team follows a structured workflow throughout the project.

### Step 1 — Planning

The team identifies project objectives, learning outcomes, responsibilities, deadlines, and required deliverables.

The Project Plan and Master Task List are used to coordinate activities and monitor progress.

### Step 2 — Content Development

Team members develop learning materials for the four AI Overview chapters.

The materials are written in Markdown and organized according to the Module Outline.

New revisions are maintained as separate content versions to preserve previous work.

### Step 3 — Quality Review

The Quality Lead reviews learning materials and project documents based on:

* Content accuracy and clarity.
* Consistency with learning outcomes.
* Completeness of explanations and examples.
* Logical organization and readability.
* Markdown formatting and document structure.
* Consistency between project documents.

Identified issues and review results are recorded in the shared quality review documentation.

### Step 4 — Revision and Improvement

Team members review feedback and make corrections to improve the materials.

Updated content may be reviewed again to verify whether the identified issues have been addressed.

### Step 5 — Learning Resource Development

The approved Markdown content is used as the reference for developing the Study Guide, PPT Slides, and Video Tutorials.

This helps maintain consistency between the different learning resources.

### Step 6 — Teaching Preparation

The team prepares the live teaching session and rehearses the presentation.

Feedback from practice sessions is used to improve explanations, timing, and presentation flow.

### Step 7 — Documentation and Submission

The team organizes the completed materials, checks the required documents, and prepares the files for submission.

The final quality checks are documented before each stage is submitted.

---

## 8. Quality Assurance

Quality assurance is an important part of the project because the materials are designed for beginner learners.

The review process focuses on ensuring that the content is understandable, logically organized, accurate, and consistent with the project objectives.

### Quality Review Documents

| Document                    | Description                                                                   |
| --------------------------- | ----------------------------------------------------------------------------- |
| **Quality Standards**       | Establishes the review criteria used throughout the project.                  |
| **Detailed Review Reports** | Records observations, identified issues, and recommendations for improvement. |
| **Review Register**         | Provides a centralized record of quality reviews and their status.            |
| **Final Submission Audit**  | Supports the final verification of project documentation and deliverables.    |

### Review History and Continuity

Quality review reports from Stage 1 are preserved as part of the project's quality history.

Reports QR-001 to QR-008 document the initial review activities conducted during Stage 1 for the earlier five-chapter version. Reviews of the rebuilt four-chapter version use QR-121 to QR-125. A chapter is called Checked only after the Quality Lead has signed its report.

For Stage 2, new review reports will be added to the same quality review system. The Review Register will continue to track review IDs, reviewed files, findings, corrections, and final results.

This approach avoids duplicating the quality documentation for every content version and maintains a continuous record of the project's quality development.

The latest review information is maintained in the [Quality Review Register](../quality/reviews/review-register.md).

---

## 9. AI Tool Usage

AI tools may be used to support selected activities during project development.

Examples include:

* Understanding technical concepts.
* Organizing learning materials.
* Improving explanations and document structure.
* Checking grammar and readability.
* Identifying possible inconsistencies.
* Supporting the preparation of learning resources.

AI-generated suggestions are treated as supporting material rather than automatically accepted final content.

Team members remain responsible for checking information, verifying important details, editing generated suggestions, and deciding what is included in the final work.

### AI Usage Documentation

AI-assisted activities are documented throughout the project.

The records include relevant information such as:

1. Date and AI tool used.
2. Purpose of using the tool.
3. Important prompts or instructions.
4. Important outputs or suggestions.
5. Verification and revision decisions.
6. Final outcome and learning.

Stage 1 and Stage 2 AI-use records are maintained separately to preserve the history of AI-assisted activities.

---

## 10. Current Project Progress

**Last Updated:** November 5, 2026
**Current Stage:** Stage 2 — Content Development and Learning Resource Production

### Stage 1 — Completed

Stage 1 established the foundation for the AI Overview project.

Completed activities included:

* Establishing the team structure and assigning project roles.
* Defining the project purpose, intended learners, and learning outcomes.
* Organizing the AI Overview module into chapters (rebuilt on 5 November 2026 to follow the lecturer's four course chapters).
* Developing the initial learning materials for Chapters 1–4.
* Preparing the combined Stage 1 learning content.
* Preparing the Project Plan and Master Task List.
* Organizing the Module Outline.
* Establishing the GitHub repository structure and development workflow.
* Preparing quality standards and review documentation.
* Conducting quality reviews and recording review results.
* Documenting AI-assisted activities.
* Preparing and completing the Stage 1 submission.

The original Stage 1 content and review records are preserved for reference.

### Stage 2 — In Progress

Stage 2 focuses on improving and expanding the existing learning materials and preparing the learning resources.

Current activities include:

* Expanding the rebuilt Chapters 1–4 into V2.0 with more depth, examples, and a full Study Guide and Test Bank.
* Waiting for the Quality Lead's signed review of the rebuilt chapters.
* Improving explanations, examples, diagrams, and learning activities.
* Checking consistency between chapters.
* Conducting quality reviews of the revised content.
* Developing the Study Guide and Test Bank.
* Preparing PPT Slides.
* Developing Video Tutorials.
* Preparing for the live teaching session.

The detailed progress of each task is maintained in the [Master Task List](master-task-list.md).

### Stage 2 Main Objective

The main objective is to produce a more complete, consistent, and beginner-friendly version of the AI Overview module.

The Markdown content remains the primary reference for the Study Guide, PPT Slides, and Video Tutorials.

---

## 11. Project Deliverables

The project produces several connected learning and documentation deliverables.

| Deliverable                        | Description                                                                  |
| ---------------------------------- | ---------------------------------------------------------------------------- |
| **Project Plan**                   | Documents project objectives, workflow, timeline, and team responsibilities. |
| **Master Task List**               | Records assigned tasks, deadlines, and progress across all stages.           |
| **Module Outline**                 | Defines the learning structure and topics of the AI Overview module.         |
| **Markdown Study Guide**           | Contains the main educational content for all four chapters.                 |
| **Study Guide + Test Bank**        | Provides structured learning materials and practice questions.               |
| **PPT Slides**                     | Presents key concepts through visual explanations and examples.              |
| **Video Tutorials**                | Provides narrated explanations and demonstrations of selected topics.        |
| **Live Teaching Materials**        | Supports the team's live mini lecture and teaching activities.               |
| **Quality Review Documentation**   | Records quality standards, review reports, findings, and corrections.        |
| **AI Use Logs**                    | Documents AI-assisted activities during project development.                 |
| **Project Logs and Meeting Notes** | Records activities, decisions, contributions, and project progress.          |

Deliverables are developed and updated according to the requirements of each project stage.

---

## 12. Next Steps

Following the Stage 2 development schedule, the team will:

1. Merge the rebuilt chapters, complete the signed quality review and corrections, then expand the chapters into V2.0.
2. Conduct cross-reviews and quality checks.
3. Improve the Study Guide and Test Bank.
4. Complete the first version of the PPT Slides.
5. Complete the first version of the Video Tutorials.
6. Collect feedback from trial activities.
7. Prepare and rehearse the live teaching session.
8. Compile and submit the Stage 2 deliverables.

After Stage 2, the team will use feedback and review results to prepare the final improvements for Stage 3.

Task ownership, deadlines, and progress are maintained in the [Master Task List](master-task-list.md).

---

## 13. Conclusion

The BABI GULING AI Overview project aims to make Artificial Intelligence easier to understand for beginners through clear explanations, structured learning materials, and practical examples.

Stage 1 established the project's foundation and initial learning content.

Stage 2 builds on that foundation by revising and expanding the four chapters, improving the learning resources, and preparing the teaching materials.

By maintaining shared project documentation, organized content versions, and continuous quality reviews, the team aims to produce consistent and useful learning materials throughout the project.
