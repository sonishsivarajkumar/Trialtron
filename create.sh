#!/bin/bash


# Create app structure
mkdir -p app/{models,services,utils}
mkdir -p data

# Create app files
touch app/main.py
touch app/config.py

touch app/models/document.py
touch app/models/user.py

touch app/services/document_service.py
touch app/services/llm_service.py
touch app/services/regulatory_service.py

touch app/utils/helpers.py

# Create data file
touch data/documents.json

# Create root files
touch requirements.txt
touch README.md

# Add initial content to documents.json
echo "[]" > data/documents.json

echo "Trialtron Streamlit project structure created successfully!"