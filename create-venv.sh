#!/bin/bash

echo "Setting up venv"
python3 -m venv venv

ACTIVATE_FILE="`pwd`/venv/bin/activate"

echo "file location: $ACTIVATE_FILE"

if [ -f "$ACTIVATE_FILE" ]; then
echo "File exists"
fi

source "$ACTIVATE_FILE"

echo "Installing requirements"
pip install -r requirements.txt

echo "Deactivating setup venv, ready for development"
deactivate
