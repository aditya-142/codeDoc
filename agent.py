import openai
import os
from llama_index.llms.openai import OpenAI
from llama_index.agent.openai import OpenAIAgent
from llama_index.tools.code_interpreter.base import CodeInterpreterToolSpec
import streamlit as st

def return_agent():
    # Azure OpenAI configuration
    openai.api_type = "azure"
    openai.api_base = st.secrets['AZURE_API_BASE']  # Add this to Streamlit secrets
    openai.api_version = "2023-05-15"  # Use the correct version for your Azure OpenAI resource
    openai.api_key = st.secrets['AZURE_API_KEY']  # Add your API key to Streamlit secrets

    code_spec = CodeInterpreterToolSpec()
    tools = code_spec.to_tool_list()
    agent = OpenAIAgent.from_tools(
        tools,
        llm=OpenAI(temperature=0, model="gpt-4"),  # Replace "gpt-4" with your Azure deployment name
        verbose=True
    )
    return agent
