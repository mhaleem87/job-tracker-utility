# Job Tracker Utility

A CLI tool for tracking job applications with the following features:

## Overview
- Add new job applications (company, position, date applied, status)
- Track application status (applied, interviewing, rejected, accepted)
- View all applications with filters (by status, company, date range)
- Export data to CSV
- Store data in JSON format locally
- Simple, user-friendly CLI interface

## Project Structure
```
src/
  ├── main.py          # Entry point & CLI
  ├── tracker.py       # Core job tracking logic
  └── utils.py         # Helper functions (CSV export, formatting)
tests/
  └── test_tracker.py  # Unit tests
output/
  └── jobs.json        # Data storage (auto-created)
```

## Running the App
```bash
python3 src/main.py
```

## Data Format
Jobs stored as JSON in `output/jobs.json`:
```json
{
  "jobs": [
    {
      "id": 1,
      "company": "TechCorp",
      "position": "Senior Product Manager",
      "date_applied": "2026-03-01",
      "status": "applied",
      "notes": "Applied via LinkedIn"
    }
  ]
}
```

## CLI Commands
- `add` — Add new job application
- `list` — Show all applications
- `status <id> <new_status>` — Update job status
- `delete <id>` — Remove application
- `export` — Export to CSV
- `search <query>` — Search by company or position

## Testing
```bash
python3 tests/test_tracker.py
```
