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
        self.ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://192.168.1.80:11434")
        self.model_name = os.getenv("OLLAMA_DEFAULT_MODEL", "gpt-oss")  # Changed from default_model to model_name
        self.openai_api_key = os.getenv("OPENAI_API_KEY", "")
        self.log_level = os.getenv("LOG_LEVEL", "INFO")
        
        # Timeout settings for better connection handling
        self.request_timeout = int(os.getenv("OLLAMA_TIMEOUT", "120"))  # 2 minutes default
        self.connection_timeout = int(os.getenv("OLLAMA_CONNECTION_TIMEOUT", "60"))  # Increase for remote server
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
            "model": self.model_name,  # Changed from default_model to model_name
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