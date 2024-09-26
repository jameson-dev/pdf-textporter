#!/bin/bash

# Define path to virtual environment
VENV_DIR="venv"

# Directory of app.py
APP_DIR="tasking_sheets"

# Path to requirements file
REQUIREMENTS_FILE="requirements.txt"

# Function to handle cleanup on exit
cleanup() {
    if [ -n "$VIRTUAL_ENV" ]; then
        echo "Deactivating virtual environment..."
        deactivate
    fi
}

# Ensure python3 is installed
if ! command -v python3 &>/dev/null; then
    echo "Python3 is not installed."
    echo "Run 'sudo apt install python3-full'"
    exit 1
fi

# Set a trap to ensure cleanup happens on EXIT (0) and SIGINT (2)
trap cleanup 0 2

# Check if virtual environment exists
if ! python3 -m venv "$VENV_DIR"; then
    echo "Virtual environment not yet set up. Creating one now..."
    exit 1

    # Create virtual environment and confirm it was created successfully
    if ! python3 -m venv "$VENV_DIR"; then
      echo "Failed to create virtual environment. Exiting."
      exit 1
  fi
fi

# Activate virtual environment
echo "Activating virtual environment"
. "$VENV_DIR/bin/activate"

# Check if venv activation was successful
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Failed to activate virtual environment. Exiting"
    exit 1
fi

if ! command -v pip $>/dev/null; then
    echo "pip doesn't seem to be installed."
    echo "Run 'sudo apt install pip'"
    exit 1
fi

# Install requirements.txt dependencies with pip
if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "Requirements file found. Installing dependencies..."
    pip install --upgrade pip
    if ! pip install -r "$REQUIREMENTS_FILE"; then
        echo "Failed to install required dependencies. Exiting"
        exit 1
    fi
else
    echo "requirements.txt not found. Exiting..."
    exit 1
fi



# Print venv path
echo "Virtual environment activated: $VIRTUAL_ENV"

# Run app
echo "Running app"
python3 "${APP_DIR}/app.py"