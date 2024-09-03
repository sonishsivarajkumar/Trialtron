# app/main.py
import streamlit as st
from models.document import Document
from services.document_service import DocumentService
from services.llm_service import LLMService
from services.regulatory_service import RegulatoryService
import os

# Initialize services
document_service = DocumentService()
llm_service = LLMService(api_key=os.environ.get("OPENAI_API_KEY"))
regulatory_service = RegulatoryService()

# Streamlit app
def main():
    st.title("Trialtron - FDA Submission Report Generator")

    # Sidebar for navigation
    page = st.sidebar.selectbox("Choose a page", ["Dashboard", "Document Editor", "Regulatory Checker"])

    if page == "Dashboard":
        show_dashboard()
    elif page == "Document Editor":
        show_document_editor()
    elif page == "Regulatory Checker":
        show_regulatory_checker()

def show_dashboard():
    st.header("Document Dashboard")

    # Ensure that DocumentService.get_all_documents() is implemented
    documents = document_service.get_all_documents()
    for doc in documents:
        if st.button(f"Edit: {doc.title}"):
            st.session_state.current_document = doc

    # Create new document
    if st.button("Create New Document"):
        new_doc = Document(title="New Document", content="")
        document_service.create_document(new_doc)
        st.success("New document created!")

def show_document_editor():
    st.header("Document Editor")

    # Get current document or create a new one
    current_doc = st.session_state.get("current_document", Document(title="New Document", content=""))

    # Document title
    current_doc.title = st.text_input("Document Title", current_doc.title)

    # Document content
    current_doc.content = st.text_area("Document Content", current_doc.content, height=300)

    # Ensure that DocumentService.update_document() is implemented
    if st.button("Save Document"):
        document_service.update_document(current_doc)
        st.success("Document saved successfully!")

    # Ensure that LLMService.generate_content() is implemented
    if st.button("Generate Content"):
        prompt = f"Generate FDA submission report content for {current_doc.title}"
        generated_content = llm_service.generate_content(prompt)
        current_doc.content += "\n\n" + generated_content
        st.success("Content generated and added to the document!")

def show_regulatory_checker():
    st.header("Regulatory Compliance Checker")

    # Text area for document content
    content = st.text_area("Enter document content to check", height=300)

    # Ensure that RegulatoryService.check_compliance() is implemented
    if st.button("Check Compliance"):
        issues = regulatory_service.check_compliance(content)
        if issues:
            st.warning("Compliance issues found:")
            for issue in issues:
                st.write(f"- {issue}")
        else:
            st.success("No compliance issues found!")

if __name__ == "__main__":
    main()

