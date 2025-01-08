import openai
import os
from llama_index.llms.openai import OpenAI
from llama_index.agent.openai.base import OpenAIAgent
from llama_index.tools.code_interpreter.base import CodeInterpreterToolSpec
import streamlit as st

def return_agent(key, endpoint, deployment_name):
    openai.api_key = key
    openai.api_base = endpoint

    code_spec = CodeInterpreterToolSpec()
    tools = code_spec.to_tool_list()
    agent = OpenAIAgent.from_tools(
        tools,
        llm=OpenAI(temperature=0, model=deployment_name),
        verbose=True
    )
    return agent
