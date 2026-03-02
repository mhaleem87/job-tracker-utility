# job-tracker-utility

A lightweight CLI for tracking job applications locally.

## Usage

```bash
python3 src/main.py
```

## Menu Options

| Option | Description |
|--------|-------------|
| 1. Add | Add a new application (company, title, location, link, salary, recruiter, notes) |
| 2. List | View all applications in a table |
| 3. Update status | Change status and optionally append a timestamped note |
| 4. Delete | Remove an application (with confirmation) |
| 5. Search | Filter by company, title, status, or location |
| 6. Export | Save all applications to CSV |

## Statuses

`Applied` → `Phone Screen` → `Interview` → `Offer` → `Rejected` / `Withdrawn`

## Data

- Applications stored in `data/applications.json`
- CSV exports saved to `data/applications_export.csv`

## Requirements

Python 3 — no external dependencies.
