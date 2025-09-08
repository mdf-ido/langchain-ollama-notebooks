# Copilot Instructions for LangChain-Ollama-Notebooks

## Project Overview
This is a **self-hosted AI framework comparison repository** containing Jupyter notebooks for testing LangChain, Semantic Kernel, and future AI frameworks (CrewAI, DSPy, PydanticAI) with Ollama models. All notebooks use standard JSON `.ipynb` format for JupyterHub compatibility.

## Architecture Patterns
Each folder contains notebooks demonstrating framework-specific patterns for integrating with Ollama, using a shared configuration system.

### Framework Organization
- `langchain/` - Chain-based workflows, direct LLM invocation
- `semantic_kernel/` - Plugin-based architecture with `@kernel_function` decorators
- `setup/` - Environment validation and Ollama configuration notebooks
- `crewAi/` - Uses the CrewAI framework for advanced conversational agents
- `DSpy/` - Uses the DSpy framework for data science and analysis
- `PydanticAI/` - Uses PydanticAI for structured AI applications

### Configuration System
All notebooks share a **centralized configuration system** in `config.py` to manage Ollama connection settings, model selection, and timeouts.

**Centralized config pattern** in `config.py`:
```python
from config import config
# Access: config.ollama_base_url, config.model_name, config.temperature
```

Key settings controlled via `.env`:
- `OLLAMA_BASE_URL` (default: `http://192.168.1.81:11434` - note remote server setup)
- `OLLAMA_DEFAULT_MODEL` (commonly `gpt-oss`, `llama2`)
- Timeout configurations for remote server reliability

### Framework-Specific Patterns

**LangChain Pattern:**
```python
from langchain_ollama import ChatOllama
from langchain.schema import HumanMessage, SystemMessage

llm = ChatOllama(
    base_url=config.ollama_base_url,
    model=config.model_name,
    request_timeout=config.request_timeout  # Critical for remote Ollama
)
```

**Semantic Kernel Pattern:**
```python
import semantic_kernel as sk
from semantic_kernel.connectors.ai.ollama import OllamaChatCompletion

# Note: Use 'host' parameter, NOT 'base_url'
ollama_service = OllamaChatCompletion(
    ai_model_id=config.model_name,
    host=config.ollama_base_url,  # Different parameter name!
    service_id="service_name"
)
```

## Development Workflows

### Setup Sequence
1. **Always start with setup notebooks** before creating new examples
2. Run `setup/00_environment_setup.ipynb` to validate dependencies
3. Run `setup/01_ollama_configuration.ipynb` to test Ollama connectivity
4. Use `config.validate_ollama_connection()` for connection testing

### Notebook Conventions
- **Import pattern**: `sys.path.append('..')` to access shared config
- **Error handling**: Wrap Ollama calls in try/except with user-friendly messages
- **Timeout awareness**: Use config timeout settings for remote server stability
- **Model validation**: Check available models with `config.get_available_models()`

### Framework Comparison Notes
| Aspect | LangChain | Semantic Kernel |
|--------|-----------|----------------|
| **Memory** | Manual message arrays | `ChatHistory` class |
| **Functions** | Direct invocation | `@kernel_function` decorators |
| **Connection** | `base_url` parameter | `host` parameter |
| **Architecture** | Chain-based | Plugin-based |

## Key Integration Points

### Ollama Server Considerations
- **Remote server default** (`192.168.1.81:11434`) - not localhost
- **Network policies**: May require firewall/routing configuration
- **Timeout handling**: Connection and request timeouts configured separately
- **Model management**: Use `ollama pull model-name` on server

### Plugin Development (Semantic Kernel)
Follow the AI Learning Tutor pattern in `semantic_kernel/02_ai_learning_tutor_sk.ipynb`:
- Class-based plugins with multiple `@kernel_function` methods
- Async function signatures with typed parameters
- Structured prompts with clear formatting instructions
- Error handling for kernel function execution

## Common Issues & Solutions

### Connection Problems
```python
# Always validate before proceeding
if not config.validate_ollama_connection():
    print("❌ Ollama server not accessible")
    print(f"Check server at: {config.ollama_base_url}")
```

### Framework-Specific Errors
- **LangChain**: Check `base_url` parameter and timeout settings
- **Semantic Kernel**: Use `host` parameter, ensure service_id uniqueness
- **Model errors**: Verify model exists with `ollama list` on server

### JupyterHub Compatibility
- All notebooks use standard JSON format (no custom extensions)
- Shared config accessible via relative imports
- Environment variables loaded automatically via `python-dotenv`

## File Naming Conventions
- `01_`, `02_` prefixes for logical progression
- `_clean`, `_minimal` suffixes for complexity variants
- Framework name suffix for disambiguation (`_sk` for Semantic Kernel)
