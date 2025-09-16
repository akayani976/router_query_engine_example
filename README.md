# Router Query Engine Example

A sophisticated RAG (Retrieval-Augmented Generation) system that intelligently routes queries to the most appropriate retrieval strategy using LlamaIndex's Router Query Engine.

## 🎯 Purpose

This project demonstrates how to build an intelligent document query system that automatically selects the best retrieval strategy based on the nature of your question. Instead of using a single approach, the router analyzes your query and chooses between:

- **Summary Index**: For high-level overviews and summarization queries
- **Vector Store Index**: For specific context search and similarity-based queries

## 🚀 Features

- **Intelligent Query Routing**: Automatically selects the best retrieval strategy
- **Multi-Strategy RAG**: Combines summarization and semantic search capabilities
- **PDF Document Processing**: Loads and processes PDF documents for querying
- **OpenAI Integration**: Uses GPT-3.5-turbo and text-embedding-ada-002 models
- **Async Support**: Handles asynchronous operations efficiently

## 📋 Prerequisites

- Python 3.9+
- OpenAI API key
- Virtual environment (recommended)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/akayani976/router_query_engine_example.git
   cd router_query_engine_example
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install llama-index
   ```

4. **Set up environment variables**
   ```bash
   # Create a .env file in the project root
   echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
   ```

## 🏃‍♂️ Usage

1. **Place your PDF document** in the project directory (e.g., `metagpt.pdf`)

2. **Update the file path** in `main.py` if needed:
   ```python
   documents = SimpleDirectoryReader(input_files=["your_document.pdf"]).load_data()
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

4. **Example queries**:
   - "What is the main idea of the document?"
   - "Summarize the key concepts"
   - "Find specific information about [topic]"
   - "What are the main benefits mentioned?"

## 🏗️ Architecture

```
Query → Router Query Engine → Strategy Selection
                                ├── Summary Index (for overviews)
                                └── Vector Store Index (for specific search)
```

### Components

- **Document Loader**: Reads PDF files using SimpleDirectoryReader
- **Text Splitter**: Breaks documents into 512-character chunks with 10-character overlap
- **Embedding Model**: text-embedding-ada-002 for vector representations
- **LLM**: GPT-3.5-turbo for text generation and query routing
- **Router**: LLMSingleSelector for intelligent strategy selection

## 📁 Project Structure

```
router_query_engine/
├── main.py              # Main application logic
├── helper.py            # Utility functions for API key management
├── .env                 # Environment variables (not tracked)
├── .gitignore          # Git ignore rules
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## 🔧 Configuration

### Chunk Settings
- **Chunk Size**: 512 characters
- **Chunk Overlap**: 10 characters
- **Model**: GPT-3.5-turbo for LLM, text-embedding-ada-002 for embeddings

### Query Engine Tools
- **Summary Tool**: Optimized for summarization and overview queries
- **Vector Tool**: Optimized for specific context and similarity search

## 🎓 Learning Outcomes

This project demonstrates:
- **Multi-strategy RAG**: How to combine different retrieval approaches
- **Query Routing**: Intelligent selection of retrieval strategies
- **Document Processing**: PDF loading and text chunking
- **Async Operations**: Handling asynchronous AI model calls
- **Environment Management**: Secure API key handling

## 🔒 Security

- API keys are stored in `.env` files (not committed to git)
- `.env` is included in `.gitignore` to prevent accidental exposure
- Use environment variables for production deployments

## 🤝 Contributing

This is a learning project, but suggestions and improvements are welcome!

## 📚 Next Steps

- [ ] Add support for multiple document types
- [ ] Implement custom query routing logic
- [ ] Add query result caching
- [ ] Create a web interface
- [ ] Add more sophisticated chunking strategies

## 📄 License

This project is for educational purposes.