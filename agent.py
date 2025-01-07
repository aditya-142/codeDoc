import requests
import streamlit as st

class HuggingFaceAgent:
    def __init__(self, model_name: str, api_key: str):
        self.api_url = f"https://api-inference.huggingface.co/models/{model_name}"
        self.api_key = api_key

    def query(self, payload: dict) -> dict:
        """Send a request to the Hugging Face API."""
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.post(self.api_url, headers=headers, json=payload)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")

def return_agent(model_name: str = "gpt2") -> HuggingFaceAgent:
    """Factory function to initialize the HuggingFaceAgent."""
    api_key = st.secrets["HF_API_KEY"]  # Ensure your API key is in Streamlit secrets
    return HuggingFaceAgent(model_name=model_name, api_key=api_key)
