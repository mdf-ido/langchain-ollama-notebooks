# LangChain Ollama Notebooks

A comprehensive collection of Jupyter notebooks for testing and exploring LangChain with local Ollama GPT-OSS models. Designed for use with JupyterHub environments.

## 🎯 Overview

This repository provides practical examples and templates for:
- **LangChain integration** with Ollama models
- **Prompt engineering** techniques and best practices
- **Advanced workflows** including RAG, agents, and chains
- **Performance testing** and model comparison
- **Real-world use cases** and applications

## 📋 Prerequisites

- **Python 3.8+**
- **Ollama installed locally** with at least one model downloaded
- **JupyterHub server** (you mentioned you already have this)
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

3. **Set up environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your Ollama settings
   ```

4. **Start with setup notebooks:**
   - Open `setup/00_environment_setup.ipynb`
   - Then `setup/01_ollama_configuration.ipynb`

## 📁 Repository Structure

```
├── README.md
├── requirements.txt
├── .env.example
├── config.py
├── setup/
│   ├── 00_environment_setup.ipynb
│   └── 01_ollama_configuration.ipynb
├── basic_examples/
│   ├── 01_simple_chat.ipynb
│   ├── 02_basic_prompts.ipynb
│   └── 03_model_testing.ipynb
├── advanced_examples/
│   ├── 01_prompt_engineering.ipynb
│   ├── 02_chains_and_workflows.ipynb
│   ├── 03_memory_and_conversation.ipynb
│   ├── 04_rag_document_processing.ipynb
│   └── 05_agents_and_tools.ipynb
├── utilities/
│   ├── model_comparison.ipynb
│   ├── performance_testing.ipynb
│   └── debugging_tools.ipynb
└── docs/
    ├── best_practices.md
    └── troubleshooting.md
```

## 🔧 Configuration

1. **Ollama Setup:** Ensure Ollama is running locally on `http://localhost:11434`
2. **Models:** Download your preferred models (e.g., `ollama pull llama2`, `ollama pull codellama`)
3. **Environment:** Copy `.env.example` to `.env` and configure your settings

## 📚 Usage Examples

### Basic Chat
```python
from langchain_ollama import ChatOllama
llm = ChatOllama(model="llama2", base_url="http://localhost:11434")
response = llm.invoke("Hello, how are you?")
```

### Prompt Templates
```python
from langchain.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("human", "{input}")
])
```

## 🛠️ Troubleshooting

- **Ollama not responding:** Check if Ollama service is running
- **Model not found:** Ensure the model is pulled locally
- **Memory issues:** Consider using smaller models for testing
- **JupyterHub compatibility:** All notebooks tested with standard JupyterHub setups

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for improvements!

## 📄 License

MIT License - feel free to use and modify as needed.