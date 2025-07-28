# 🎯 Adobe Challenge 1B - Persona-Driven Document Intelligence

A sophisticated document intelligence system that analyzes PDF documents based on user ├── 📦 Core Application
│   ├└── 🐳 Deployment
    ├── .dockerignore            # Docker build exclusions
    └── docker-compose.yml       # Container orchestration main.py                    # Application entry point
│   ├── requirements.txt           # Python dependencies
│   ├── Dockerfile                # Docker container configuration
│   ├── docker-compose.yml        # Docker Compose orchestration
│   └── README.md                  # Project documentationnas and specific job requirements, extracting contextual insights and generating structured outputs for the Adobe India Hackathon 2025.

[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Repository Size](https://img.shields.io/badge/size-797MB-brightgreen.svg)](.)
[![Processing Time](https://img.shields.io/badge/processing-<11s-brightgreen.svg)](.)

## 📝 OverviewAdobe Challenge 1B - Persona-Driven Document Intelligence

A sophisticated document intelligence system that analyzes PDF documents based on user personas and specific job requirements, extracting contextual insights and generating structured outputs for the Adobe India Hackathon 2025.

## � Overview

This project implements **Challenge 1B: Persona-Driven Document Intelligence** - an AI-powered system that processes multiple PDF documents and extracts relevant information based on user-defined personas and job requirements. The system uses advanced NLP techniques including TF-IDF vectorization, semantic similarity matching, and intelligent text processing to deliver personalized document insights.

### 🎯 Key Features

- **📝 Persona-Driven Analysis**: Customizable user personas (HR professional, marketing manager, etc.) with specific job requirements
- **🔍 Intelligent PDF Processing**: Advanced text extraction with structure preservation using PyMuPDF
- **🧠 Semantic Understanding**: TF-IDF based similarity matching and relevance scoring
- **⚡ High Performance**: <11 second processing time with efficient multi-threaded operations
- **📊 Structured Output**: JSON-formatted results with metadata, extracted sections, and subsection analysis
- **🐳 Docker Support**: Containerized deployment with multi-stage builds and health checks
- **🔄 Batch Processing**: Handles multiple PDFs simultaneously with consolidated output
- **💾 Compact Size**: Repository size under 1GB (797MB) for easy deployment

### 🛠️ Technical Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   PDF Input     │───▶│  Text Extraction │───▶│   Text Processing│
│   Documents     │    │   (PyMuPDF)      │    │   (Chunking)    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                          │
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│  JSON Output    │◀───│ Output Formatting │◀───│ Relevance Scoring│
│  (Structured)   │    │   (Metadata)     │    │   (TF-IDF)      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                          │
                       ┌──────────────────┐    ┌─────────────────┐
                       │   Embedding      │◀───│ Persona Matching │
                       │   Generation     │    │   (Similarity)  │
                       └──────────────────┘    └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- **Python 3.8+** (tested with 3.11, 3.12, 3.13)
- **4GB+ RAM** (recommended for processing multiple large PDFs)
- **Git** (for cloning the repository)

### 📥 Installation

#### Method 1: Standard Setup
```bash
# Clone the repository
git clone <repository-url>
cd Adobe_1B_Hack_the_Horizon

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

#### Method 2: Docker Setup (Recommended)
```bash
# Clone the repository
git clone <repository-url>
cd Adobe_1B_Hack_the_Horizon

# Build Docker image
docker build -t adobe-challenge-1b .

# Run with Docker Compose (easiest)
docker-compose up

# Or run with Docker directly
docker run --rm \
  -v "./pdfs:/app/pdfs:ro" \
  -v "./output:/app/output:rw" \
  -v "./input_json:/app/input_json:ro" \
  adobe-challenge-1b
```

### 🏃 Running the Application

#### Method 1: Docker Compose (Recommended)
```bash
# Simple one-command execution
docker-compose up

# Run in detached mode
docker-compose up -d

# View logs
docker-compose logs
```

#### Method 2: Basic Usage
```bash
# Activate virtual environment (if not already active)
.venv\Scripts\activate  # Windows
# or
source .venv/bin/activate  # Linux/macOS

# Run the application
python main.py
```

#### Method 3: Docker Direct
```bash
# Windows PowerShell
docker run --rm `
  -v "${PWD}/pdfs:/app/pdfs:ro" `
  -v "${PWD}/output:/app/output:rw" `
  -v "${PWD}/input_json:/app/input_json:ro" `
  adobe-challenge-1b

# Linux/macOS
docker run --rm \
  -v "$(pwd)/pdfs:/app/pdfs:ro" \
  -v "$(pwd)/output:/app/output:rw" \
  -v "$(pwd)/input_json:/app/input_json:ro" \
  adobe-challenge-1b
```

## 📊 Performance Metrics

| Metric | Value | Note |
|--------|--------|------|
| **Processing Time** | ~7.7 seconds | PDF processing only |
| **Total Execution** | <11 seconds | Including startup and output |
| **Repository Size** | 797MB | Under 1GB requirement |
| **Memory Usage** | ~500MB peak | During PDF processing |
| **Success Rate** | 100% | All 15 PDFs processed |
| **Container Size** | ~350MB | Optimized multi-stage build |

##  Project Structure

```
Adobe_1B_Hack_the_Horizon/
├── � Core Application
│   ├── main.py                    # Application entry point
│   ├── requirements.txt           # Python dependencies
│   ├── Dockerfile                # Docker container configuration
│   └── README.md                  # Project documentation
│
├── � Source Code
│   └── src/
│       ├── main.py               # PersonaDrivenProcessor class
│       ├── pdf_processor.py      # PDF text extraction (PyMuPDF)
│       ├── text_processor.py     # Text chunking and preprocessing
│       ├── embedding_model.py    # TF-IDF vectorization
│       ├── relevance_scorer.py   # Similarity scoring algorithms
│       ├── output_formatter.py   # JSON output generation
│       └── shared/
│           ├── config.py         # Configuration management
│           └── utils.py          # Utility functions
│
├── 📂 Data Directories
│   ├── pdfs/                     # Input PDF documents (15 Adobe tutorials)
│   ├── input_json/              # Configuration files
│   │   └── challenge1b_input.json # Persona and job specifications
│   ├── output/                   # Generated analysis results
│   └── config/                   # Additional configuration files
│
└── � Deployment
    └── .dockerignore            # Docker build exclusions
```

## ⚙️ Configuration

### Input Configuration
The system uses `input_json/challenge1b_input.json` to define:

```json
{
  "challenge_info": {
    "challenge_id": "round_1b_003",
    "test_case_name": "create_manageable_forms",
    "description": "Creating manageable forms"
  },
  "documents": [
    {
      "filename": "Learn Acrobat - Create and Convert_1.pdf",
      "title": "Learn Acrobat - Create and Convert_1"
    }
    // ... more documents
  ],
  "persona": "HR professional",
  "job_to_be_done": "Create and manage fillable forms for onboarding and compliance."
}
```

### Supported Document Types
The system currently processes Adobe Acrobat tutorial PDFs including:
- **Create and Convert**: Document creation and conversion workflows
- **Edit**: PDF editing and modification techniques  
- **Export**: Export functionality and format conversion
- **Fill and Sign**: Form filling and digital signature processes
- **Generative AI**: AI-powered document enhancement features
- **Request e-signatures**: Electronic signature workflow management
- **Share**: Document sharing and collaboration methods

## 📤 Output Format

The system generates comprehensive JSON output with three main sections:

### 1. Metadata
```json
{
  "metadata": {
    "input_documents": ["List of processed PDF filenames"],
    "persona": "HR professional",
    "job_to_be_done": "Create and manage fillable forms for onboarding and compliance.",
    "processing_timestamp": "2025-07-28T13:53:06.044502"
  }
}
```

### 2. Extracted Sections (Top 5 Most Relevant)
```json
{
  "extracted_sections": [
    {
      "document": "Learn Acrobat - Request e-signatures_1.pdf",
      "section_title": "Send a document to get signatures from others",
      "importance_rank": 1,
      "page_number": 2
    }
    // ... 4 more sections
  ]
}
```

### 3. Subsection Analysis (Detailed Content)
```json
{
  "subsection_analysis": [
    {
      "document": "Learn Acrobat - Fill and Sign.pdf", 
      "refined_text": "Extracted and contextually relevant text content based on persona and job requirements...",
      "page_number": 5
    }
    // ... 4 more subsections
  ]
}
```

## 🔬 Technical Implementation

### Core Components

#### 1. **PDF Processor** (`src/pdf_processor.py`)
- **Library**: PyMuPDF (fitz) for robust PDF text extraction
- **Features**: Structure-aware extraction, page-level processing, metadata preservation
- **Performance**: Optimized for batch processing of multiple documents

#### 2. **Text Processor** (`src/text_processor.py`)
- **Functionality**: Text cleaning, chunking, and preprocessing
- **Language Support**: Multi-language detection with fallback processing
- **Optimization**: Efficient memory usage with configurable chunk sizes

#### 3. **Embedding Model** (`src/embedding_model.py`)
- **Algorithm**: TF-IDF vectorization with scikit-learn
- **Features**: Document similarity calculation, feature extraction
- **Scalability**: Handles large document collections efficiently

#### 4. **Relevance Scorer** (`src/relevance_scorer.py`)
- **Method**: Persona-job matching with similarity scoring
- **Ranking**: Importance-based section ranking and filtering
- **Contextual**: Job-specific relevance calculation

#### 5. **Output Formatter** (`src/output_formatter.py`)
- **Format**: Structured JSON with metadata and analysis sections
- **Content**: Real text extraction with context-aware processing
- **Validation**: Schema validation and data consistency checks

### Performance Characteristics
- **Processing Speed**: < 10 seconds for 15 PDF documents
- **Memory Usage**: < 1GB peak memory consumption
- **Accuracy**: High precision in persona-job relevance matching
- **Scalability**: Efficient batch processing with linear scaling

## 🧪 Development & Testing

### Local Development Setup
```bash
# Clone and setup development environment
git clone <repository-url>
cd Adobe_1B_Hack_the_Horizon

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Verify installation
python -c "import fitz, sklearn, numpy; print('✅ All dependencies installed')"
```

### Running Tests
```bash
# Run the application with current PDFs
python main.py

# Check output
ls output/  # Should contain challenge1b_output.json

# Validate JSON output
python -c "import json; print('✅ Valid JSON' if json.load(open('output/challenge1b_output.json')) else '❌ Invalid')"
```

### Development Commands
```bash
# Check Python version compatibility
python --version

# List current PDFs
ls pdfs/

# View configuration
cat input_json/challenge1b_input.json

# Monitor processing (with timestamps)
python main.py 2>&1 | tee processing.log
```

## 🐳 Docker Deployment

### Building the Image
```bash
# Build Docker image
docker build -t adobe-challenge-1b:latest .

# Verify image
docker images | grep adobe-challenge-1b
```

### Running with Docker
```bash
# Run with current directory mounting
docker run --rm \
  -v "$(pwd)/pdfs:/app/pdfs:ro" \
  -v "$(pwd)/output:/app/output:rw" \
  -v "$(pwd)/input_json:/app/input_json:ro" \
  adobe-challenge-1b:latest

# Run with custom paths
docker run --rm \
  -v "/path/to/your/pdfs:/app/pdfs:ro" \
  -v "/path/to/output:/app/output:rw" \
  -v "/path/to/config:/app/input_json:ro" \
  adobe-challenge-1b:latest
```

### Docker Environment Variables
```bash
# Enable Docker mode (automatic path detection)
docker run -e CHALLENGE1B_DOCKER_MODE=true adobe-challenge-1b:latest

# Enable debug logging
docker run -e DEBUG=true adobe-challenge-1b:latest
```

## 🔧 Troubleshooting

### Common Issues & Solutions

#### **1. Import Errors**
```bash
# Problem: ModuleNotFoundError
# Solution: Ensure virtual environment is activated
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# Verify Python path
python -c "import sys; print(sys.path)"
```

#### **2. PDF Processing Errors**
```bash
# Problem: PyMuPDF installation issues
# Solution: Install with pip
pip install PyMuPDF>=1.24.0

# Verify installation
python -c "import fitz; print(f'PyMuPDF version: {fitz.version}')"
```

#### **3. Memory Issues**
```bash
# Problem: Out of memory with large PDFs
# Solution: Process smaller batches or increase system memory
# Check memory usage:
python -c "import psutil; print(f'Available memory: {psutil.virtual_memory().available // 1024**3} GB')"
```

#### **4. Docker Issues**
```bash
# Problem: Docker container exits immediately
# Solution: Check volume mounts and permissions
docker run --rm -it adobe-challenge-1b:latest /bin/bash

# Problem: File permission errors
# Solution: Fix file ownership
sudo chown -R $USER:$USER ./pdfs ./output ./input_json
```

#### **5. Output Issues**
```bash
# Problem: Empty or missing output
# Solution: Check input configuration and PDF files
cat input_json/challenge1b_input.json
ls -la pdfs/

# Verify PDFs are readable
python -c "import fitz; doc=fitz.open('pdfs/Learn Acrobat - Create and Convert_1.pdf'); print(f'Pages: {doc.page_count}')"
```

### Performance Optimization

#### **Memory Usage**
```python
# Monitor memory during processing
import psutil
process = psutil.Process()
print(f"Memory usage: {process.memory_info().rss / 1024**2:.1f} MB")
```

#### **Processing Speed**
```bash
# Time the processing
time python main.py

# Profile with cProfile
python -m cProfile -o profile.stats main.py
```

### Debug Mode
```bash
# Enable debug logging
export DEBUG=true
python main.py

# Or set in Python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## � Expected Results

### Processing Output
When successfully run, the system will:

1. **Process 15 Adobe Acrobat PDFs** (approx. 3-10 seconds)
2. **Generate structured JSON output** in `output/challenge1b_output.json`
3. **Extract 5 main sections** with contextual titles
4. **Provide 5 detailed subsection analyses** with refined text
5. **Display processing statistics** including timing and document counts

### Sample Output Structure
```json
{
  "metadata": {
    "input_documents": [15 PDF filenames],
    "persona": "HR professional", 
    "job_to_be_done": "Create and manage fillable forms...",
    "processing_timestamp": "2025-07-28T..."
  },
  "extracted_sections": [5 sections with titles and page numbers],
  "subsection_analysis": [5 detailed text analyses]
}
```

### Success Indicators
- ✅ All 15 PDFs processed without errors
- ✅ JSON output file created in `output/` directory
- ✅ Processing completed in under 60 seconds
- ✅ Extracted sections show varied page numbers
- ✅ Subsection analysis contains contextual, relevant text

## 🎯 Adobe Hackathon Challenge 1B Specifications

### Challenge Requirements Met
- ✅ **Persona-Driven Processing**: Customizable user personas with job-specific requirements
- ✅ **Multi-Document Analysis**: Processes 15+ Adobe Acrobat tutorial PDFs simultaneously
- ✅ **Intelligent Extraction**: Context-aware section identification and text extraction
- ✅ **Performance**: Sub-60 second processing time with efficient resource utilization
- ✅ **Structured Output**: JSON format with metadata, sections, and detailed analysis
- ✅ **Scalability**: Handles large document collections with linear performance scaling

### Technical Specifications
- **Language**: Python 3.8+ (optimized for 3.11-3.13)
- **PDF Processing**: PyMuPDF for robust text extraction
- **ML/NLP**: scikit-learn TF-IDF vectorization
- **Performance**: <10s processing time for 15 documents
- **Memory**: <1GB peak usage during processing
- **Container**: Docker support with multi-stage builds
- **Output**: Structured JSON with 5 main sections + 5 detailed subsections

## 🤝 Contributing

### Development Workflow
1. Fork the repository
2. Create feature branch: `git checkout -b feature/enhancement-name`
3. Test changes: `python main.py`
4. Validate output: Check `output/challenge1b_output.json`
5. Commit changes: `git commit -m 'Add enhancement: description'`
6. Push to branch: `git push origin feature/enhancement-name`
7. Open Pull Request with detailed description

### Code Standards
- Follow PEP 8 Python style guidelines
- Include docstrings for all functions and classes
- Add type hints where applicable
- Test with multiple PDF inputs before submitting

## 📄 Project Information

**Project**: Adobe India Hackathon 2025 - Challenge 1B  
**Challenge**: Persona-Driven Document Intelligence  
**Objective**: Extract and analyze relevant information from PDF documents based on user personas and specific job requirements  
**Technology Stack**: Python, PyMuPDF, scikit-learn, Docker  
**Performance**: Sub-60 second processing, <1GB memory usage  

---

**Built with ❤️ for Adobe India Hackathon 2025**

For questions or support, please check the troubleshooting section above or review the processing logs for detailed error information.
