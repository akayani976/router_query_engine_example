import os
from dotenv import load_dotenv

def get_openai_api_key():
    """Get OpenAI API key from environment variable."""
    # Load .env file if it exists
    load_dotenv()
    return os.getenv('OPENAI_API_KEY')
