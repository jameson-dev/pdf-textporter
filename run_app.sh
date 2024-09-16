#!/bin/bash

# Define path to virtual environment
VENV_DIR="venv"

# Check if virtual environment exists
# shellcheck disable=SC1073
if [ ! -d "$VENV_DIR" ]; then
  echo "Virtual environment not yet set up. Creating on now..."




  # Create virtual environment and confirm it was created successfully
  if ! python3 -m venv "$VENV_DIR"; then
    echo "Failed to create virtual environment. Exiting."
    exit 1
  fi
fi

# Active virtual environment
source "$VENV_DIR/bin/activate"

# Run app
python3 app.py

# Deactivate virtual environment after app closes
deactivate