"""
Hugging Face Spaces entry point for Hinglish Rap Generator
This file is required by Hugging Face Spaces
"""

# Simply import and run the main UI
from hindi_rap_ui import create_ui, initialize_models
import argparse

if __name__ == "__main__":
    # Initialize models on startup
    print("🎵 Hinglish Rap Generator Starting on Hugging Face Spaces...")
    print("📦 Loading AI models (this may take a minute)...")
    print("⏳ First-time setup will download ~3-5GB of models...")
    print("")
    
    # Load models before creating UI
    status = initialize_models(max_frames=2048)
    print(status)
    print("")
    
    # Create and launch UI
    demo = create_ui()
    
    print("🚀 Launching web interface...")
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False
    )

