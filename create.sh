#!/bin/bash 

# Backend structure
mkdir -p backend/app/{models,routers,services,utils}
mkdir -p backend/tests

# Create backend files
touch backend/app/__init__.py
touch backend/app/main.py
touch backend/app/config.py

touch backend/app/models/__init__.py
touch backend/app/models/document.py
touch backend/app/models/user.py

touch backend/app/routers/__init__.py
touch backend/app/routers/auth.py
touch backend/app/routers/documents.py
touch backend/app/routers/llm.py

touch backend/app/services/__init__.py
touch backend/app/services/document_service.py
touch backend/app/services/llm_service.py
touch backend/app/services/regulatory_service.py

touch backend/app/utils/__init__.py
touch backend/app/utils/helpers.py

touch backend/tests/__init__.py
touch backend/tests/test_documents.py
touch backend/tests/test_llm.py

touch backend/requirements.txt
touch backend/Dockerfile

# Frontend structure
mkdir -p frontend/{public,src/{components,services}}

# Create frontend files
touch frontend/public/index.html

touch frontend/src/components/Dashboard.js
touch frontend/src/components/DocumentEditor.js
touch frontend/src/components/RegulatoryChecker.js

touch frontend/src/services/api.js
touch frontend/src/services/auth.js

touch frontend/src/App.js
touch frontend/src/index.js

touch frontend/package.json
touch frontend/Dockerfile

# Root files
touch docker-compose.yml
touch README.md

echo "Trialtron project structure created successfully!"
#!/bin/bash

# Create main project directory
mkdir -p trialtron

# Create app structure
mkdir -p trialtron/app/{models,services,utils}
mkdir -p trialtron/data

# Create app files
touch trialtron/app/main.py
touch trialtron/app/config.py

touch trialtron/app/models/__init__.py
touch trialtron/app/models/document.py
touch trialtron/app/models/user.py

touch trialtron/app/services/__init__.py
touch trialtron/app/services/document_service.py
touch trialtron/app/services/llm_service.py
touch trialtron/app/services/regulatory_service.py

touch trialtron/app/utils/__init__.py
touch trialtron/app/utils/helpers.py

# Create data file
touch trialtron/data/documents.json

# Create root files
touch trialtron/requirements.txt
touch trialtron/README.md
touch trialtron/.env

# Add initial content to documents.json
echo "[]" > trialtron/data/documents.json

# Add initial content to .env
echo "OPENAI_API_KEY=your_api_key_here" > trialtron/.env

echo "Trialtron Streamlit project structure created successfully!"