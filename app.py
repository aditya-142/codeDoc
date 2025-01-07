import streamlit as st
import os
import logging
from agent import return_agent

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Streamlit app setup
st.set_page_config(page_title="Code Product Documentation", layout="wide")
st.title("Code Product Documentation Generator")
st.markdown("Generate comprehensive documentation for your Python projects with ease using Hugging Face's Inference API.")

# Function to generate documentation using Hugging Face API
def generate_documentation(agent, project_info: str, template: str) -> str:
    prompt = f"""
    Generate comprehensive documentation for the following Python project:
    
    Project Information:
    {project_info}

    Use this template for the structure:
    {template}

    Ensure detailed coverage of the project's purpose, components, and usage.
    """
    try:
        payload = {"inputs": prompt}
        response = agent.query(payload)
        return response[0]["generated_text"]
    except Exception as e:
        logger.error(f"Error generating documentation: {e}")
        return "Failed to generate documentation. Please check your inputs or API configuration."

# Main app logic
def main():
    # User input for GitHub repo or local directory path
    input_path = st.text_input(
        "Enter the directory path or GitHub repository URL:",
        help="You can enter a local directory path or a GitHub repository URL (e.g., https://github.com/username/repository)."
    )

    # Template input
    template = st.text_area(
        "Enter the documentation template structure:",
        value="# Project Overview\n## Installation\n## Usage\n## API Reference\n## Contributing",
        help="Provide a Markdown-formatted template for your documentation."
    )

    # Initialize Hugging Face agent
    agent = return_agent()

    if input_path and st.button("Generate Documentation"):
        # Placeholder project information for simplicity
        project_info = f"Analyzing project from: {input_path}."
        
        with st.spinner("Generating documentation..."):
            documentation = generate_documentation(agent, project_info, template)
            st.markdown("## Generated Documentation")
            st.markdown(documentation)

if __name__ == "__main__":
    main()
