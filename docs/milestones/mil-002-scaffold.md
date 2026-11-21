# Scaffold: Python project skeleton

## Metadata

| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001], [SA-001], [PP-001] |
| Language | en |
| Domain | it |

## Version History

| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-21 | Proposed | S01 | S01 | First edition | pending |
| 2026-11-21 | Accepted | S01 | S01 | Accepted by S01 in chat on 2026-11-21; review RC-005 Go, stand-in, not independent | pending |

---

## Purpose

Create an empty but runnable Python project, so every later step starts from a green test run in a local `.venv`.

## Target Date

2026-11-23

## Deliverable

A repository that installs into a `.venv`, runs a small pytest suite green and passes opengrep

## Business Case Objectives

OBJ-3, OBJ-5

## Owner and Reviewer

Owner: S01. Approving reviewer: S01.

## Dependencies

MIL-001

## Go/No-Go Criteria

- `python -m pip install --upgrade pip` and `python -m pip install -e ".[dev]"` work in a fresh `.venv`
- `python -m pytest` passes
- `README.md` has every section of the framework template and `check-readme.sh` finds nothing
- opengrep reports 0 findings

## Branch and Pull Request

One branch `milestone/mil-002-scaffold` and one pull request that closes the issues of the tasks below.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Project configuration | `pyproject.toml` with `requires-python >= 3.14`, the runtime dependencies Pillow and PyAutoGUI, a dev extra and the pytest settings | No | BC-001 AS-4 |
| 2 | Package skeleton and constants | Package `src/dino_bot/` with `constants.py` and a smoke test | No | BC-001 AS-3 |
| 3 | Repository files | Python `.gitignore`, `.editorconfig` and a `Doxyfile` | No | CN-005 |
| 4 | README from the template | Overview, requirements, `.venv` setup with `python -m pip install --upgrade pip`, run and test instructions | No | CN-003 |
| 5 | Screenshot and wiki step page | Screenshot of the smoke tests in `docs/images/`, README step list and a wiki step page in en, da and ms | No | CN-007 |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
