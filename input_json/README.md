# Input JSON Directory

Place your `challenge1b_input.json` configuration file in this directory.

## Format:
```json
{
  "challenge_info": {
    "challenge_id": "round_1b_XXX",
    "test_case_name": "your_test_case",
    "description": "Your description"
  },
  "documents": [
    {
      "filename": "document.pdf",
      "title": "Document Title"
    }
  ],
  "persona": {
    "role": "Your Role"
  },
  "job_to_be_done": {
    "task": "Your specific task description"
  }
}
```

## Current Configuration:
- `challenge1b_input.json` - Main input configuration file

The system will automatically read this file when you run `python main.py`
