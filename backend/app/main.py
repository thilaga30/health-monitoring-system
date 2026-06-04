from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import health
from app.data.health_knowledge import HEALTH_DOCUMENTS
from app.services.rag_service import RAGService
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Health Monitoring RAG System",
    description="A RAG-based health monitoring system with LangChain",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize RAG service and load documents
@app.on_event("startup")
async def startup_event():
    """Initialize services on startup"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Warning: OPENAI_API_KEY not set")
    
    # Initialize RAG service
    rag_service = RAGService(api_key)
    rag_service.initialize_vectorstore("./chroma_db")
    rag_service.add_documents(HEALTH_DOCUMENTS)
    rag_service.setup_qa_chain()
    
    # Store in app state
    app.state.rag_service = rag_service
    print("RAG service initialized with health knowledge base")

# Include routes
app.include_router(health.router)

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Health Monitoring RAG System",
        "docs": "/docs",
        "health": "/api/health"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
