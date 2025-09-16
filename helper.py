import os

def get_openai_api_key():
    """Get OpenAI API key from environment variable."""
    return os.getenv('OPENAI_API_KEY', '')
