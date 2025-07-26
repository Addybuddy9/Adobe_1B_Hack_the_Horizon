# Adobe India Hackathon 2025 - Challenge 1b

## ⚠️ System Requirements

**Python Version**: Python 3.13.5 is required for this project. Please ensure you have the correct Python version installed before running the application.

```bash
python --version  # Should output: Python 3.13.5
```

## 🎯 Overview

**Challenge 1b: Persona-Driven Document Intelligence** - A sophisticated solution that processes PDFs with user-configurable personas to extract relevant content based on specific roles and job requirements.

## 🚀 Features

### Persona-Driven Document Intelligence
- **User-Configurable Personas**: Define your own role and specific job requirements
- **Intelligent PDF Processing**: Extracts structured text with headers and sections
- **Semantic Understanding**: TF-IDF based similarity matching
- **High Performance**: <60s processing, <1GB models, offline execution
- **Detailed Analytics**: Subsection analysis with confidence scores

## 🛠 Technology Stack

- **Language**: Python 3.13.5 (Required)
- **PDF Processing**: PyMuPDF (open source)
- **ML/NLP**: scikit-learn, transformers, sentence-transformers
- **Parallel Processing**: ThreadPoolExecutor
- **Container**: Docker with linux/amd64 platform

## 🏗 Architecture

```
Adobe_1b/
├── main.py              # Entry point
├── requirements.txt     # Dependencies
├── README.md           # Challenge 1b specific documentation
├── Dockerfile          # Docker configuration
├── .dockerignore       # Docker ignore file
├── config/
│   └── challenge_1b.json # Challenge 1b configuration
├── src/
│   ├── __init__.py     # Module initialization
│   ├── main.py         # Main processor class
│   ├── pdf_processor.py # PDF processing
│   ├── text_processor.py # Text processing
│   ├── embedding_model.py # Embeddings
│   ├── relevance_scorer.py # Scoring
│   ├── output_formatter.py # Output formatting
│   └── shared/         # Shared utilities
│       ├── config.py
│       └── utils.py
├── pdfs/               # Place PDF files here for analysis
├── input_json/         # Input JSON configuration files
│   └── challenge1b_input.json # Main input configuration
└── output/             # Generated JSON results
```

## 📦 Installation

### Option 1: Docker (Recommended)
```bash
# Build the Docker image
docker build -t adobe-challenge-1b .

# Run with persona and job parameters
docker run -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output adobe-challenge-1b --persona "Assistant Professor" --job "Research paper analysis"
```

### Option 2: Local Installation

**Prerequisites**: Ensure you have Python 3.13.5 installed

```bash
# Clone or extract the project
cd Adobe_1b

# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# On Windows:
.\.venv\Scripts\Activate.ps1
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py --persona "Assistant Professor" --job "Research paper analysis"
```

## 🎮 Usage

### Command Line Interface

```bash
# Interactive mode (prompts for persona and job)
python main.py

# Direct mode with parameters
python main.py --persona "Data Scientist" --job "Technical documentation review"
```

### Input Requirements

1. **PDF Files**: Place your PDF files in the `pdfs/` directory
2. **Input Configuration**: Place your `challenge1b_input.json` file in the `input_json/` directory
3. **Persona**: Your role (e.g., "Assistant Professor", "Researcher", "Data Scientist")
4. **Job**: Your specific task (e.g., "Research paper analysis", "Technical documentation review")

### Example Personas and Jobs

| Persona | Job Examples |
|---------|-------------|
| Assistant Professor | Research paper analysis, Course material review |
| Data Scientist | Technical documentation review, Algorithm analysis |
| PhD Student | Literature review, Methodology study |
| Researcher | Research paper analysis, Experimental design review |
| Software Engineer | API documentation review, Technical specification analysis |

## 📊 Output Format

The system generates JSON files in the `output/` directory with the following structure:

```json
{
  "persona": "Assistant Professor",
  "job": "Research paper analysis",
  "filename": "research_paper.pdf",
  "pages": 25,
  "sections": [
    {
      "title": "Introduction",
      "relevance_score": 0.85,
      "page_numbers": [1, 2, 3],
      "content": "...",
      "subsections": [
        {
          "title": "Background",
          "relevance_score": 0.78,
          "content": "..."
        }
      ]
    }
  ],
  "processing_time": 45.2,
  "total_sections": 8,
  "relevant_sections": 6
}
```

## ⚡ Performance

- **Processing Speed**: <60 seconds per document
- **Model Size**: <1GB total models
- **Memory Usage**: Optimized for 16GB RAM
- **Offline Operation**: No internet required
- **Resource Efficient**: CPU optimized processing

## 🔧 Configuration

The system uses `config/challenge_1b.json` for configuration:

```json
{
  "pdf_processing": {
    "max_chunk_size": 1000,
    "overlap_size": 100,
    "min_section_length": 50
  },
  "similarity": {
    "relevance_threshold": 0.3,
    "top_k_sections": 10
  },
  "output": {
    "include_subsections": true,
    "min_relevance_score": 0.2
  }
}
```

## 📁 Project Structure

```
Adobe_1b/
├── main.py              # Entry point
├── requirements.txt     # Dependencies
├── README.md           # This file
├── config/
│   └── challenge_1b.json # Configuration
├── src/
│   ├── main.py         # Core modules
│   └── shared/         # Utilities
├── pdfs/               # Place PDF files here
├── input_json/         # Input JSON configuration files
│   └── challenge1b_input.json # Main configuration
└── output/             # Generated JSON files
```

## 🧪 Testing

The system has been tested with:
- ✅ Research papers (10-50 pages)
- ✅ Technical documentation
- ✅ Multilingual documents
- ✅ Various PDF formats
- ✅ Different persona/job combinations

## 🚀 Quick Start

1. **Setup**: 
   - Place PDF files in `pdfs/` directory
   - Place `challenge1b_input.json` in `input_json/` directory
2. **Run**: Execute `python main.py`
3. **Configure**: System will use the JSON configuration automatically
4. **Results**: Check `output/` directory for `challenge1b_output.json` results

## 📋 Requirements

- Python 3.10+
- 8+ CPU cores recommended
- 16GB+ RAM
- 2GB+ available disk space

## 🔍 Troubleshooting

**Common Issues:**

1. **No PDF files found**: Ensure PDFs are in the `pdfs/` directory
2. **Memory errors**: Reduce batch size in configuration
3. **Slow processing**: Check available system resources
4. **Import errors**: Verify all dependencies are installed

## 📄 License

This project is developed for the Adobe India Hackathon 2025.
