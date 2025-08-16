"""
Configuration helper functions for LangChain Ollama notebooks.
"""

import os
import logging
from dotenv import load_dotenv
from typing import Dict, Any, Optional

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for Ollama and LangChain settings."""
    
    def __init__(self):
        self.ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        self.default_model = os.getenv("OLLAMA_DEFAULT_MODEL", "llama2")
        self.openai_api_key = os.getenv("OPENAI_API_KEY", "")
        self.log_level = os.getenv("LOG_LEVEL", "INFO")
        self.max_tokens = int(os.getenv("MAX_TOKENS", "2048"))
        self.temperature = float(os.getenv("TEMPERATURE", "0.7"))
        
        # Set up logging
        self.setup_logging()
    
    def setup_logging(self):
        """Set up logging configuration."""
        logging.basicConfig(
            level=getattr(logging, self.log_level.upper()),
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    
    def get_ollama_config(self) -> Dict[str, Any]:
        """Get Ollama configuration dictionary."""
        return {
            "base_url": self.ollama_base_url,
            "model": self.default_model,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens
        }
    
    def validate_ollama_connection(self) -> bool:
        """Validate connection to Ollama server."""
        import requests
        try:
            response = requests.get(f"{self.ollama_base_url}/api/tags", timeout=5)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False
    
    def get_available_models(self) -> Optional[list]:
        """Get list of available Ollama models."""
        import requests
        try:
            response = requests.get(f"{self.ollama_base_url}/api/tags", timeout=5)
            if response.status_code == 200:
                data = response.json()
                return [model['name'] for model in data.get('models', [])]
        except requests.exceptions.RequestException:
            pass
        return None

# Global config instance
config = Config()