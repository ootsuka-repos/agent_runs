import os
from dotenv import load_dotenv
from smolagents import CodeAgent, OpenAIServerModel

def load_api_key():
    load_dotenv()
    return os.environ.get("OPENAI_API_KEY")

def create_model(model_id):
    api_key = load_api_key()
    return OpenAIServerModel(
        model_id=model_id,
        api_base="https://api.openai.com/v1",
        api_key=api_key,
    )

def create_agent(tools, additional_authorized_imports, model_id):
    model = create_model(model_id)
    return CodeAgent(
        tools=tools,
        model=model,
        additional_authorized_imports=additional_authorized_imports
    )

def is_valid_result(result):
    if not result or "エラー" in str(result) or "error" in str(result).lower():
        return False
    return True