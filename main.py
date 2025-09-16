# Import helper function to get OpenAI API key from environment variables
from helper import get_openai_api_key
# Import text splitter to break documents into smaller chunks
from llama_index.core.node_parser import SentenceSplitter
# Import settings and AI models
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
# Import document reader to load PDF files
from llama_index.core import SimpleDirectoryReader
# Enable nested asyncio event loops (required for some async operations)
import nest_asyncio
# Import index types for different query strategies
from llama_index.core import VectorStoreIndex, SummaryIndex
from llama_index.core.tools import QueryEngineTool
from llama_index.core.query_engine.router_query_engine import RouterQueryEngine
from llama_index.core.selectors import LLMSingleSelector

# Get and store the OpenAI API key
OPENAI_API_KEY = get_openai_api_key()

nest_asyncio.apply()

# Load documents from PDF file
# This reads the PDF and converts it into a format that can be processed
documents = SimpleDirectoryReader(input_files=["metagpt.pdf"]).load_data()

# Create a text splitter that breaks documents into chunks of 512 characters
# with 10 characters of overlap between chunks to maintain context
splitter = SentenceSplitter(chunk_size=512, chunk_overlap=10)
# Split the loaded documents into smaller nodes/chunks
nodes = splitter.get_nodes_from_documents(documents)

# Configure the AI models to use:
# - GPT-3.5-turbo for text generation and question answering
# - text-embedding-ada-002 for creating vector embeddings of text
Settings.llm = OpenAI(model="gpt-3.5-turbo")
Settings.embed_model = OpenAIEmbedding(model="text-embedding-ada-002")

# Create two different types of indexes from the document chunks:
# - SummaryIndex: Good for summarization and high-level overview queries
# - VectorStoreIndex: Good for semantic search and similarity-based queries
summary_index = SummaryIndex(nodes)
vector_index = VectorStoreIndex(nodes)

summary_query_engine = summary_index.as_query_engine(
    response_mode="tree_summarize",
    use_async=True,
)
vector_query_engine = vector_index.as_query_engine()

summary_tool = QueryEngineTool.from_defaults(
    query_engine=summary_query_engine,
    name="summary_query_engine",
    description="Useful for summarization queries of the metaGPT document",
)
vector_tool = QueryEngineTool.from_defaults(
    query_engine=vector_query_engine,
    name="vector_query_engine",
    description="Useful for specific context search queries of the metaGPT document",
)

query_engine = RouterQueryEngine(
    selector=LLMSingleSelector.from_defaults(),
    query_engine_tools=[summary_tool, vector_tool],
    verbose=True,
)

response = query_engine.query("What is the main idea of the metaGPT document?")
print(response)