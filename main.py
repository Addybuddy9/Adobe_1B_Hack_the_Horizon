#!/usr/bin/env python3
"""
Adobe India Hackathon 2025 - Challenge 1b
Persona-Driven Document Intelligence
"""

import argparse
import json
import logging
import os
import sys
import time
from pathlib import Path
from typing import Optional, Dict, Any

# Add src to Python path
sys.path.append(str(Path(__file__).parent / "src"))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_input_config(input_file: str) -> Dict[str, Any]:
    """Load the challenge1b_input.json configuration"""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        logger.info(f"Loaded input configuration from {input_file}")
        return config
    except Exception as e:
        logger.error(f"Error loading input config: {e}")
        raise


def display_banner():
    """Display the application banner"""
    print("\n" + "="*70)
    print("🎯 Adobe India Hackathon 2025 - Challenge 1b")
    print("="*70)
    print("🎯 Challenge 1b: Persona-Driven Document Intelligence")
    print("="*70)


def setup_directories():
    """Setup input and output directories"""
    base_dir = Path(__file__).parent
    
    # Create pdfs directory if it doesn't exist
    pdfs_dir = base_dir / "pdfs"
    pdfs_dir.mkdir(exist_ok=True)
    
    # Create input_json directory if it doesn't exist
    input_json_dir = base_dir / "input_json"
    input_json_dir.mkdir(exist_ok=True)
    
    # Create output directory if it doesn't exist
    output_dir = base_dir / "output"
    output_dir.mkdir(exist_ok=True)
    
    return str(pdfs_dir), str(output_dir), str(input_json_dir)


def run_challenge_1b_from_config(config: Dict[str, Any], pdfs_dir: str, output_dir: str) -> bool:
    """Run Challenge 1b using the input configuration"""
    try:
        print("\n🎯 Starting Challenge 1b - Persona-Driven Document Intelligence")
        print("-" * 50)
        
        from src import PersonaDrivenProcessor
        
        # Extract persona and job from config
        persona = config["persona"]["role"]
        job = config["job_to_be_done"]["task"]
        documents = config["documents"]
        
        print(f"👤 Persona: {persona}")
        print(f"💼 Job: {job}")
        print(f"📄 Documents: {len(documents)} files")
        
        # Verify all PDF files exist
        missing_files = []
        for doc in documents:
            pdf_path = Path(pdfs_dir) / doc["filename"]
            if not pdf_path.exists():
                missing_files.append(doc["filename"])
        
        if missing_files:
            print(f"❌ Missing PDF files: {missing_files}")
            print(f"📁 Please ensure all files are in {pdfs_dir}")
            return False
        
        # Initialize processor
        processor = PersonaDrivenProcessor(persona=persona, job=job)
        
        # Process PDFs according to config
        start_time = time.time()
        
        # Process each document specified in config
        all_results = []
        for doc in documents:
            pdf_file = doc["filename"]
            pdf_path = Path(pdfs_dir) / pdf_file
            
            print(f"📄 Processing: {doc['title']} ({pdf_file})")
            
            try:
                # Process single PDF
                result = processor.process_single_pdf(str(pdf_path), output_dir)
                all_results.append((pdf_file, result))
            except Exception as e:
                logger.error(f"Error processing {pdf_file}: {e}")
                all_results.append((pdf_file, None))
        
        processing_time = time.time() - start_time
        
        # Generate consolidated output in required format
        processor.generate_consolidated_output(
            all_results, 
            [doc["filename"] for doc in documents],
            config,
            output_dir
        )
        
        # Display results
        print(f"\n✅ Challenge 1b completed in {processing_time:.2f} seconds")
        print(f"📄 Processed {len(documents)} PDFs")
        
        success_count = sum(1 for _, result in all_results if result is not None)
        print(f"✅ Successful: {success_count}/{len(documents)}")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Challenge 1b failed: {e}")
        return False


def run_challenge_1b(pdfs_dir: str, output_dir: str) -> bool:
    """Run Challenge 1b - Interactive mode (fallback)"""
    try:
        print("\n🎯 Starting Challenge 1b - Interactive Mode")
        print("-" * 50)
        
        from src import PersonaDrivenProcessor
        
        # Get persona and job if not set
        persona = os.getenv('PERSONA', '').strip()
        job = os.getenv('JOB', '').strip()
        
        if not persona:
            print("\n👤 Please specify your persona/role:")
            print("Examples: Assistant Professor, Researcher, PhD Student, Data Scientist")
            persona = input("👤 Your persona: ").strip()
            
        if not job:
            print("\n💼 Please specify your specific task/job:")
            print("Examples: Research paper analysis, Technical documentation review")
            job = input("💼 Your job: ").strip()
        
        if not persona or not job:
            print("❌ Persona and job are required for Challenge 1b")
            return False
        
        # Initialize processor
        processor = PersonaDrivenProcessor(persona=persona, job=job)
        
        # Process PDFs
        start_time = time.time()
        results = processor.process_all_pdfs(pdfs_dir, output_dir)
        processing_time = time.time() - start_time
        
        # Display results
        print(f"\n✅ Challenge 1b completed in {processing_time:.2f} seconds")
        print(f"📄 Processed {len(results)} PDFs")
        print(f"👤 Persona: {persona}")
        print(f"💼 Job: {job}")
        
        for pdf_file, pdf_time, success in results:
            status = "✅" if success else "❌"
            print(f"   {status} {pdf_file}: {pdf_time:.2f}s")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Challenge 1b failed: {e}")
        return False


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Adobe Hackathon 2025 - Challenge 1b")
    parser.add_argument("--input", default="challenge1b_input.json", 
                       help="Input JSON configuration file (default: challenge1b_input.json)")
    parser.add_argument("--persona", help="Your persona/role (e.g., Assistant Professor)")
    parser.add_argument("--job", help="Your specific task/job")
    
    args = parser.parse_args()
    
    # Display banner
    display_banner()
    
    # Setup directories
    pdfs_dir, output_dir, input_json_dir = setup_directories()
    
    # Try to load input configuration first
    input_config_path = Path(input_json_dir) / args.input
    
    if input_config_path.exists():
        print(f"\n📋 Found input configuration: {args.input}")
        try:
            config = load_input_config(str(input_config_path))
            
            # Check if PDFs exist in pdfs directory
            documents = config.get("documents", [])
            missing_files = []
            for doc in documents:
                pdf_path = Path(pdfs_dir) / doc["filename"]
                if not pdf_path.exists():
                    missing_files.append(doc["filename"])
            
            if missing_files:
                print(f"\n⚠️  Missing PDF files: {missing_files}")
                print(f"📁 Please ensure all files are in {pdfs_dir}")
                return
            
            print(f"\n📁 Found all {len(documents)} required PDF files")
            
            # Run challenge 1b with configuration
            overall_start = time.time()
            success = run_challenge_1b_from_config(config, pdfs_dir, output_dir)
            overall_time = time.time() - overall_start
            
        except Exception as e:
            logger.error(f"Error with configuration file: {e}")
            print(f"\n❌ Error loading configuration file. Falling back to interactive mode.")
            success = False
    else:
        print(f"\n⚠️  No input configuration found at: {input_config_path}")
        print("🔄 Running in interactive mode...")
        
        # Set environment variables if provided
        if args.persona:
            os.environ['PERSONA'] = args.persona
        if args.job:
            os.environ['JOB'] = args.job
        
        # Check if PDFs exist in pdfs directory
        pdf_files = list(Path(pdfs_dir).glob("*.pdf"))
        if not pdf_files:
            print(f"\n⚠️  No PDF files found in {pdfs_dir}")
            print(f"📁 Please add PDF files to the pdfs directory and try again.")
            return
        
        print(f"\n📁 Found {len(pdf_files)} PDF files in pdfs directory")
        
        # Run challenge 1b in interactive mode
        overall_start = time.time()
        success = run_challenge_1b(pdfs_dir, output_dir)
        overall_time = time.time() - overall_start
    
    # Final summary
    print("\n" + "="*70)
    if success:
        print("🎉 Challenge 1b completed successfully!")
        print(f"📂 Results saved to: {Path(__file__).parent / 'output'}")
        if input_config_path.exists():
            print(f"📄 Output file: challenge1b_output.json")
    else:
        print("❌ Challenge 1b failed. Check logs for details.")
    
    print(f"⏱️  Total execution time: {overall_time:.2f} seconds")
    print("="*70)


if __name__ == "__main__":
    main()
