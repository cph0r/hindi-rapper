#!/bin/bash

# Hindi Rap Generator Launcher Script
# This script sets up and launches the Hindi Rap Generator UI

set -e

echo "🎤 Hindi Rap Generator (हिंदी रैप जनरेटर)"
echo "=========================================="
echo ""

# Set Python path
export PYTHONPATH=$PYTHONPATH:$PWD

# Set espeak path for macOS
if [[ "$OSTYPE" =~ ^darwin ]]; then
    if [ -d "/opt/homebrew/Cellar/espeak-ng" ]; then
        ESPEAK_VERSION=$(ls /opt/homebrew/Cellar/espeak-ng/ | head -n 1)
        export PHONEMIZER_ESPEAK_LIBRARY="/opt/homebrew/Cellar/espeak-ng/${ESPEAK_VERSION}/lib/libespeak-ng.dylib"
        echo "✅ Detected macOS - espeak-ng configured"
    fi
fi

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "Please install Python 3.10 or higher"
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "📦 Python version: $PYTHON_VERSION"

# Check if in virtual environment
if [ -z "$VIRTUAL_ENV" ] && [ -z "$CONDA_DEFAULT_ENV" ]; then
    echo ""
    echo "⚠️  Warning: No virtual environment detected"
    echo "It's recommended to use a virtual environment:"
    echo "  conda create -n hindi-rap python=3.10"
    echo "  conda activate hindi-rap"
    echo ""
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Check if gradio is installed
if ! python3 -c "import gradio" &> /dev/null; then
    echo "📦 Installing Gradio..."
    pip install gradio
fi

# Check CUDA availability
DEVICE=$(python3 -c "import torch; print('CUDA' if torch.cuda.is_available() else 'CPU')" 2>/dev/null || echo "CPU")
echo "🖥️  Running on: $DEVICE"

if [ "$DEVICE" = "CPU" ]; then
    echo "⚠️  Warning: No GPU detected. Generation will be slower."
fi

echo ""
echo "🚀 Starting Hindi Rap Generator UI..."
echo "📱 Web interface will open at: http://localhost:7860"
echo ""
echo "Press Ctrl+C to stop the server"
echo "=========================================="
echo ""

# Launch the UI
python3 hindi_rap_ui.py "$@"

