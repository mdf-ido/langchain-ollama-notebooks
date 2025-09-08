# LangChain & Semantic Kernel Ollama Notebooks

A comprehensive collection of Jupyter notebooks for testing and exploring **LangChain** and **Microsoft Semantic Kernel** with self-hosted Ollama GPT-OSS models. All notebooks are in standard JSON `.ipynb` format for full compatibility with JupyterHub and other Jupyter environments.

## 🎯 Overview

This repository provides practical examples and templates for:
- **LangChain integration** with self-hosted Ollama models
- **Microsoft Semantic Kernel** integration with Ollama 
- **Plugin architecture** and kernel function development
- **AI Learning Tutor** system with comprehensive educational features
- **Prompt engineering** techniques and best practices
- **Advanced workflows** including RAG, agents, and chains
- **Performance testing** and model comparison
- **Real-world use cases** and applications

## 🏗️ Self-Hosted Architecture

This setup is designed for **completely self-hosted AI workflows**:
- **Local Ollama server** - Run models on your own hardware
- **Standard Jupyter notebooks** - All `.ipynb` files use JSON format for universal compatibility
- **JupyterHub ready** - Works seamlessly with JupyterHub deployments
- **No external API dependencies** - Everything runs on your infrastructure
- **Privacy-first** - All data stays on your servers

## 📋 Prerequisites

- **Python 3.8+**
- **Self-hosted Ollama server** with at least one model downloaded
- **JupyterHub or Jupyter environment** (notebooks use standard JSON format)
- **Network access** to your Ollama server (local or remote)
- Basic knowledge of Python and Jupyter notebooks

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mdf-ido/langchain-ollama-notebooks.git
   cd langchain-ollama-notebooks
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *Note: Includes both LangChain and Semantic Kernel dependencies*

3. **Set up environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your Ollama settings
   ```

4. **Start with setup notebooks:**
   - Open `setup/00_environment_setup.ipynb`
   - Then `setup/01_ollama_configuration.ipynb`
   - Try LangChain examples in `langchain/` folder
   - Explore Semantic Kernel examples in `semantic_kernel/` folder

## 📁 Repository Structure

```
├── README.md
├── requirements.txt           # Both LangChain & Semantic Kernel deps
├── config.py                 # Shared configuration for both frameworks  
├── setup/
│   ├── 00_environment_setup.ipynb
│   └── 01_ollama_configuration.ipynb
├── langchain/                # LangChain Examples
│   ├── 01_simple_chat.ipynb
│   ├── 01_simple_chat_clean.ipynb
│   ├── 01_simple_chat_minimal.ipynb
│   ├── 02_basic_prompts.ipynb
│   ├── 03_model_testing.ipynb
│   └── 01_prompt_engineering.ipynb
└── semantic_kernel/          # Microsoft Semantic Kernel Examples
    ├── 01_simple_chat_sk.ipynb
    └── 02_ai_learning_tutor_sk.ipynb
```

### 🧠 Semantic Kernel Features

The `semantic_kernel/` folder includes advanced AI orchestration examples:

**01_simple_chat_sk.ipynb**
- Basic Semantic Kernel setup with Ollama
- Plugin architecture demonstration
- Chat history management
- Kernel function examples

**02_ai_learning_tutor_sk.ipynb** 
- Comprehensive AI Learning Tutor system
- 5 specialized tutoring functions:
  - `find_facts` - Discover related facts and context
  - `create_examples` - Generate examples and analogies  
  - `build_mnemonics` - Create memory aids and mnemonics
  - `explore_contradictions` - Present alternative perspectives
  - `comprehensive_tutor` - All-in-one learning expansion
- Educational workflow automation
- Critical thinking enhancement tools

## 🔧 Configuration

1. **Self-Hosted Ollama Setup:** 
   - Can run locally on `http://localhost:11434` 
   - Or on remote server (e.g., `http://192.168.1.81:11434`)
   - Configure in `config.py` for both LangChain and Semantic Kernel
2. **Models:** Download your preferred models (e.g., `ollama pull llama2`, `ollama pull gpt-oss`)
3. **JupyterHub Compatibility:** All notebooks use standard JSON `.ipynb` format for seamless deployment

## 💡 Framework Comparison

| Feature | LangChain | Semantic Kernel |
|---------|-----------|----------------|
| **Architecture** | Chain-based workflows | Plugin-based kernel functions |
| **Memory Management** | Manual message arrays | Built-in ChatHistory class |
| **Function Calling** | Direct LLM invocation | @kernel_function decorators |
| **Ecosystem** | Extensive community tools | Microsoft enterprise focus |
| **Use Case** | Rapid prototyping, chains | Structured AI applications |

## 📚 Usage Examples

### LangChain Basic Chat
```python
from langchain_ollama import ChatOllama
llm = ChatOllama(model="gpt-oss", base_url="http://localhost:11434")
response = llm.invoke("Hello, how are you?")
```

### Semantic Kernel Setup
```python
import semantic_kernel as sk
from semantic_kernel.connectors.ai.ollama import OllamaChatCompletion

kernel = sk.Kernel()
ollama_service = OllamaChatCompletion(
    ai_model_id="gpt-oss",
    host="http://localhost:11434",
    service_id="ollama_chat"
)
kernel.add_service(ollama_service)
```

### AI Learning Tutor Example
```python
# Using Semantic Kernel's AI Learning Tutor
insight = "Spaced repetition improves long-term memory"
source = "Cognitive psychology textbook"

# Get comprehensive learning expansion
tutor_function = kernel.get_function("LearningTutor", "comprehensive_tutor")
result = await tutor_function.invoke(kernel, KernelArguments(
    insight=insight, source=source
))
```

## 🛠️ Troubleshooting

- **Ollama not responding:** Check if Ollama service is running on your server
- **Model not found:** Ensure the model is pulled locally (`ollama pull model-name`)
- **Memory issues:** Consider using smaller models for testing
- **JupyterHub compatibility:** All notebooks use standard JSON `.ipynb` format - fully compatible
- **Network issues:** For remote Ollama servers, check firewall and network policies
- **Semantic Kernel errors:** Ensure `host` parameter is used instead of `base_url`

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for improvements!

## 📄 License

MIT License - feel free to use and modify as needed.