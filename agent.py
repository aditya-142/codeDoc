import openai
import os
from llama_index.llms.openai import OpenAI
from llama_index.agent.openai import OpenAIAgent
from llama_index.tools.code_interpreter.base import CodeInterpreterToolSpec
import streamlit as st

def return_agent():
    # API config
    openai.api_type = "azure"
    openai.api_base = st.secrets['AZURE_API_BASE']  
    openai.api_version = st.secrets['AZURE_OPENAI_API_VERSION']  
    openai.api_key = st.secrets['AZURE_API_KEY']  

    code_spec = CodeInterpreterToolSpec()
    tools = code_spec.to_tool_list()
    agent = OpenAIAgent.from_tools(
        tools,
        llm=OpenAI(temperature=0, model="gpt-4o"),  
        verbose=True
    )
    return agent
