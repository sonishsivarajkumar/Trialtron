#!/bin/bash

# Create main project directory
mkdir -p trialtron

# Backend structure
mkdir -p trialtron/backend/app/{models,routers,services,utils}
mkdir -p trialtron/backend/tests

# Create backend files
touch trialtron/backend/app/__init__.py
touch trialtron/backend/app/main.py
touch trialtron/backend/app/config.py

touch trialtron/backend/app/models/__init__.py
touch trialtron/backend/app/models/document.py
touch trialtron/backend/app/models/user.py

touch trialtron/backend/app/routers/__init__.py
touch trialtron/backend/app/routers/auth.py
touch trialtron/backend/app/routers/documents.py
touch trialtron/backend/app/routers/llm.py

touch trialtron/backend/app/services/__init__.py
touch trialtron/backend/app/services/document_service.py
touch trialtron/backend/app/services/llm_service.py
touch trialtron/backend/app/services/regulatory_service.py

touch trialtron/backend/app/utils/__init__.py
touch trialtron/backend/app/utils/helpers.py

touch trialtron/backend/tests/__init__.py
touch trialtron/backend/tests/test_documents.py
touch trialtron/backend/tests/test_llm.py

touch trialtron/backend/requirements.txt
touch trialtron/backend/Dockerfile

# Frontend structure
mkdir -p trialtron/frontend/{public,src/{components,services}}

# Create frontend files
touch trialtron/frontend/public/index.html

touch trialtron/frontend/src/components/Dashboard.js
touch trialtron/frontend/src/components/DocumentEditor.js
touch trialtron/frontend/src/components/RegulatoryChecker.js

touch trialtron/frontend/src/services/api.js
touch trialtron/frontend/src/services/auth.js

touch trialtron/frontend/src/App.js
touch trialtron/frontend/src/index.js

touch trialtron/frontend/package.json
touch trialtron/frontend/Dockerfile

# Root files
touch trialtron/docker-compose.yml
touch trialtron/README.md

echo "Trialtron project structure created successfully!"
