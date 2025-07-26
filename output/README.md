# Output Directory

This directory contains the generated analysis results.

## Generated Files:
- `challenge1b_output.json` - Main output file with analysis results

## Output Format:
```json
{
  "metadata": {
    "input_documents": ["list of processed files"],
    "persona": "Your persona",
    "job_to_be_done": "Your task",
    "processing_timestamp": "ISO timestamp"
  },
  "extracted_sections": [
    {
      "document": "source.pdf",
      "section_title": "Section Title",
      "importance_rank": 1,
      "page_number": 1
    }
  ],
  "subsection_analysis": [
    {
      "document": "source.pdf", 
      "refined_text": "Relevant content",
      "page_number": 1
    }
  ]
}
```

Results are automatically saved here after processing completes.
