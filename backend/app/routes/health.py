from fastapi import APIRouter, HTTPException
from app.models.health import HealthMetrics, HealthQuery, HealthResponse, HealthAlert
from app.services.health_analyzer import HealthAnalyzer
from app.services.rag_service import RAGService
from datetime import datetime
from typing import List

router = APIRouter(prefix="/api/health", tags=["health"])

# Initialize services
rag_service = None
health_analyzer = HealthAnalyzer()

def init_rag_service(api_key: str):
    """Initialize RAG service"""
    global rag_service
    rag_service = RAGService(api_key)
    rag_service.initialize_vectorstore()
    rag_service.setup_qa_chain()

@router.post("/analyze", response_model=List[HealthAlert])
async def analyze_health(metrics: HealthMetrics):
    """Analyze health metrics and return alerts"""
    try:
        alerts = HealthAnalyzer.analyze_metrics(metrics)
        return alerts
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/query", response_model=HealthResponse)
async def query_health(health_query: HealthQuery):
    """Query the RAG system for health information"""
    try:
        if rag_service is None:
            raise HTTPException(status_code=500, detail="RAG service not initialized")
        
        answer, sources = rag_service.query(health_query.question)
        
        return HealthResponse(
            answer=answer,
            sources=sources,
            timestamp=datetime.now()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/summary")
async def get_health_summary(metrics: HealthMetrics):
    """Get a health summary from metrics"""
    try:
        summary = HealthAnalyzer.generate_health_summary(metrics)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
