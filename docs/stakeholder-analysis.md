# Stakeholder Analysis: Dino Bot

## Metadata

| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History

| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | S01 | S01 | First edition | [872bd57] |
| 2026-11-21 | Accepted | S01 | S01 | Accepted by S01 in chat on 2026-11-21; review RC-002 Go, stand-in, not independent | [872bd57] |

---

## Stakeholders

| ID | Stakeholder | Role and context | Power | Interest | Strategy |
| --- | --- | --- | --- | --- | --- |
| S01 | Course participant | Product Owner, developer and reviewer of every artifact; owns the repository | High | High | Manage Closely |
| S02 | Udemy coursists | Fellow students who share code and compare solutions to Day 94; they get readable, runnable code with the assignment's function names and run instructions in the README | Low | High | Keep Informed |
| S03 | GitHub and Gitea viewers | People who browse the repository for ideas; they get a clear description, topics and README and few runtime dependencies | Low | Low | Monitor |

## Power/Interest Grid

| | Low interest | High interest |
| --- | --- | --- |
| **High power** | none | S01 |
| **Low power** | S03 | S02 |

## Concern Register

| ID | Raised by | Concern (business language) | Quality characteristic (ISO/IEC 25010) | Business Case objective |
| --- | --- | --- | --- | --- |
| CN-001 | S01 | The assignment works end to end and is finished within the course time | Functional Suitability | OBJ-1 |
| CN-002 | S01 | The work practises screen capture, pixel analysis and keyboard automation | Functional Suitability | OBJ-2 |
| CN-003 | S02 | Code is readable and runnable, with function names that match the assignment (`is_collision`, `hit`) | Maintainability, Interaction Capability | OBJ-3, OBJ-4 |
| CN-004 | S02 | The bot really survives long and works at other screen sizes | Functional Suitability, Reliability | OBJ-1 |
| CN-005 | S03 | The repository has a clear description, topics and README, and only the runtime dependencies that are needed | Interaction Capability, Flexibility | OBJ-3, OBJ-4 |
| CN-006 | S01 | Personal tokens in `.env` never reach the repository, and no test takes over the desktop | Security, Safety | OBJ-5 |
| CN-007 | S01 | Each step is documented with a screenshot and what was learned, in en, da and ms | Interaction Capability | OBJ-4 |

## Conflicts and Resolutions

| Conflict | Between | Resolution |
| --- | --- | --- |
| Few runtime dependencies (CN-005) against the assignment's tools Pillow and pyautogui (CN-003) | S03, S02 | Only those two are runtime dependencies; the headless mode needs Playwright, which is an optional extra (BC-001 SC-5) |
| A live check of the bot (CN-004) against never driving the host desktop (CN-006) | S02, S01 | The live check runs in a headless Chrome; the desktop adapters are thin and not unit tested (BC-001 AS-5, AS-6) |
| Full review workflow of the framework against the 200-minute course budget (CN-001) | S01 with itself | One use case, lean artifacts; documents are short and reviewed once per milestone |
| Readers in three languages (CN-007) against time (CN-001) | S01, S02 | English is authoritative and written first; da and ms follow page by page in the same milestone, kept short |

## Communication Plan

| Stakeholder | Channel | Frequency | Deliverable | Milestones |
| --- | --- | --- | --- | --- |
| S01 | Pull requests and the project chat | Every milestone | Plan, review records, merged pull request | MIL-001 to MIL-006 |
| S02 | Udemy Q&A and the repository README | Once, at release | Link to the repository and run instructions | MIL-006 |
| S03 | Repository description, topics, README, wiki | Continuous after publication | Public pages | MIL-002, MIL-006 |

---

[BC-001]: ./business-case.md
[872bd57]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/094-assignment-automate-the-google-dinosaur-game/commit/872bd573e49894903f1a134950ab479d0e78c47b
