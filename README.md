# Log Anomaly Digest – TerminalBench Task

## Overview

This repository contains a self-contained command-line reasoning task designed
to evaluate advanced agents on multi-step log analysis, rule-based
transformations, and deterministic output generation.

The task simulates a realistic production scenario where an agent must analyze
server logs, apply transformation rules, and produce a cryptographic digest
based on the processed data.

---

## Task Description

The agent is provided with:

- A server log file containing mixed log levels and malformed entries
- A rules file describing how extracted identifiers must be transformed

The agent must:

1. Identify log entries marked as `ERROR`
2. Extract numeric `request_id` values from those entries
3. Ignore malformed log lines and duplicate request IDs
4. Apply rule-based transformations to each request ID
5. Concatenate transformed values in ascending order
6. Compute a SHA256 hash of the final string
7. Write the resulting hash to `/app/output.txt`

All steps must be completed deterministically using command-line tooling.

---

## Repository Structure

.
├── task.yaml # Task instructions, rules, and success criteria
├── Dockerfile # Reproducible execution environment
├── docker-compose.yaml # Container orchestration
├── solution.sh # Oracle (expert-authored) solution
├── run-tests.sh # End-to-end task validation script
├── assets/
│ ├── server.log # Input log file
│ └── rules.txt # Transformation rules
├── tests/
│ └── test_task.py # Deterministic Python tests
└── README.md



---

## How to Run

### Prerequisites
- Docker
- Docker Compose

### Build the Environment
```bash
docker compose build
docker compose run task
