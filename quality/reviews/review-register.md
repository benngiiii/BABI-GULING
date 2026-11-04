# Quality Review Register

## 1. Purpose

This register provides a centralized record of all quality reviews conducted for the *Introduction to Computer Science and Artificial Intelligence* project under the AI Overview module.

It covers both Stage 1 (V1.0) and Stage 2 (V2.0), recording review IDs, reviewed documents, review iterations, and the latest known review status.

The register also helps track the review history, revision progress, and quality assurance activities throughout the project.

## 2. Stage 1 — Quality Review Records (V1.0)

| No. | Review ID  | Document / Chapter                    | Review Iteration | Latest Known Status         |
| --: | ---------- | ------------------------------------- | ---------------- | --------------------------- |
|   1 | QR-001-I01 | Chapter 1                             | Initial Review   | Changes Required            |
|   2 | QR-002-I01 | Chapter 2                             | Initial Review   | Changes Required            |
|   3 | QR-002-I02 | Chapter 2                             | Second Review    | Changes Required            |
|   4 | QR-003-I01 | Chapter 3                             | Initial Review   | Changes Required            |
|   5 | QR-003-I02 | Chapter 3                             | Second Review    | Changes Required            |
|   6 | QR-003-I03 | Chapter 3                             | Third Review     | Changes Required            |
|   7 | QR-004-I01 | Chapter 4                             | Initial Review   | Minor Revisions Recommended |
|   8 | QR-005-I01 | Chapter 5                             | Initial Review   | Minor Revisions Recommended |
|   9 | QR-005-I02 | Chapter 5                             | Second Review    | Pass                        |
|  10 | QR-006-I01 | Master Task List                      | Initial Review   | Changes Required            |
|  11 | QR-007-I01 | Project Plan                          | Initial Review   | Changes Required            |
|  12 | QR-007-I02 | Project Plan                          | Second Review    | Changes Required            |
|  13 | QR-008-I01 | README                                | Initial Review   | Changes Required            |
|  14 | QR-009-I01 | Module Outline and Development Status | Initial Review   | Changes Required            |
|  15 | QR-001-I02 | Chapter 1                             | Second Review    | Changes Required            |
|  16 | QR-001-I03 | Chapter 1                             | Third Review     | Changes Required            |
|  17 | QR-001-I04 | Chapter 1                             | Fourth Review    | Pass                        |
|  18 | QR-003-I04 | Chapter 3                             | Fourth Review    | Changes Required            |
|  19 | QR-007-I03 | Project Plan                          | Third Review     | Changes Required            |
|  20 | QR-008-I02 | README                                | Second Review    | Minor Revisions Recommended |
|  21 | QR-002-I03 | Chapter 2                             | Third Review     | Changes Required            |
|  22 | QR-009-I02 | Module Outline                        | Second Review    | Minor Revisions Recommended |
|  23 | QR-003-I05 | Chapter 3                             | Fifth Review     | Pass                        |
|  24 | QR-009-I03 | Module Outline                        | Third Review     | Minor Revisions Recommended |
|  25 | QR-004-I02 | Chapter 4                             | Second Review    | Pass                        |
|  26 | QR-006-I02 | Master Task List                      | Second Review    | Minor Revisions Recommended |
|  27 | QR-010-I01 | stage1_Content                        | Initial Review   | Changes Required            |
|  28 | QR-101-I01 | Team Project Plan and Task List       | Initial Review   | Changes Required            |
|  29 | QR-010-I02 | stage1_Content                        | Second Review    | Pass                        |
|  30 | QR-101-I02 | Team Project Plan and Task List       | Second Review    | Minor Revisions Recommended |
|  31 | QR-101-I03 | Team Project Plan and Task List       | Third Review     | Pass                        |
|  32 | QR-008-I03 | README                                | Third Review     | Pass                        |

**Historical Record Verification Note:**

Some entries in the original register contained duplicate IDs or conflicting document descriptions. The records above consolidate the apparent review sequence where it can be identified, but the original detailed reports and review register should be checked before treating every historical ID as verified.

## 3. Stage 2 — Quality Review Records (V2.0)

| No. | Review ID  | Document / Chapter                                  | Review Iteration | Latest Known Status           |
| --: | ---------- | --------------------------------------------------- | ---------------- | ----------------------------- |
|   1 | QR-201-I01 | Chapter 1 — Introduction to Artificial Intelligence | Initial Review   | Approved with Minor Revisions |

**Stage 2 Review Notes:**

* QR-201-I01 is the initial quality review of Chapter 1 V2.0.
* The review result is Approved with Minor Revisions.
* The report identifies minor improvements involving learning outcomes, estimated learning time, visual asset verification, reference verification, and learner-testing evidence.
* Further reviews should use the next iteration number, such as QR-201-I02.

## 4. Review File Locations

Detailed review reports are organized according to their corresponding document version.

**Stage 1 — V1.0**

`quality/reviews/detailed review V1.0/`

**Stage 2 — V2.0**

`quality/reviews/detailed review V2.0/`

Each folder contains the individual quality review reports for its respective version.

The centralized review register remains located at:

`quality/reviews/review-register.md`

## 5. Review ID Convention

The following convention is used to identify quality review reports:

`QR-[Document Code]-I[Iteration Number]`

Where:

* **QR** = Quality Review.
* **Document Code** = The document or chapter identifier.
* **I** = Review iteration.
* **Iteration Number** = The sequence of the formal review.

To prevent ID conflicts between project stages, the following numbering convention is used:

| Stage          | Review ID Range         | Purpose                              |
| -------------- | ----------------------- | ------------------------------------ |
| Stage 1 — V1.0 | Existing historical IDs | Original Stage 1 review records      |
| Stage 2 — V2.0 | QR-2xx                  | Stage 2 chapter and document reviews |

For example:

* QR-201-I01 = Chapter 1, Stage 2, Initial Review.
* QR-201-I02 = Chapter 1, Stage 2, Second Review.
* QR-202-I01 = Chapter 2, Stage 2, Initial Review.

The document code and iteration number must remain consistent across the register and the corresponding detailed review report.

## 6. Review Tracking Notes

* Each review ID identifies a specific formal review iteration.
* The iteration number increases when a document undergoes another formally documented review.
* Stage 1 and Stage 2 review histories are maintained in the same register but recorded separately.
* A new review does not automatically mean that a document is approved.
* A document should only receive a Pass status when its review findings have been addressed and the relevant acceptance criteria have been met.
* Detailed findings, recommendations, evidence, and revision history must be recorded in the corresponding detailed review report.
* The latest known status should reflect the most recent completed review, not an earlier review result.
* Pending reviews must not be recorded as completed reviews.

## 7. Register Maintenance

This register must be updated whenever:

* A new detailed quality review report is created.
* An existing document undergoes another formal review.
* A review status is confirmed through a subsequent review.
* A review report is revised or its identification information is corrected.
* A new project stage or document version introduces additional quality review records.

The Quality Lead is responsible for maintaining the register and ensuring that every registered review corresponds to an actual detailed review report.

The register serves as a centralized index of quality review records. It does not replace the detailed reports, review evidence, or revision history stored in the corresponding version-specific folders.
