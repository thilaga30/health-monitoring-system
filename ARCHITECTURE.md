# Architecture Overview

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                       Frontend (React)                       │
│  - Health Metrics Form Component                             │
│  - Health Analysis Display                                   │
│  - RAG Query Interface                                       │
└─────────────────┬───────────────────────────────────────────┘
                  │ HTTP/REST API
                  │ (CORS enabled)
┌─────────────────▼───────────────────────────────────────────┐
│                   Backend (FastAPI)                          │
│  ┌───────────────┐  ┌──────────────┐  ┌───────────────┐    │
│  │  API Routes   │  │   Services   │  │   Models      │    │
│  │               │  │              │  │               │    │
│  │ /api/health   │→ │ RAG Service  │  │ HealthMetrics │    │
│  │ /analyze      │  │ Health       │  │ HealthQuery   │    │
│  │ /query        │  │ Analyzer     │  │ HealthAlert   │    │
│  │ /summary      │  │              │  │               │    │
│  └───────────────┘  └──────────────┘  └───────────────┘    │
└────────┬─────────────────┬─────────────────┬────────────────┘
         │                 │                 │
         │                 │                 │
    ┌────▼─────┐   ┌──────▼──────┐   ┌─────▼───────┐
    │  OpenAI  │   │  Chroma DB  │   │  Knowledge  │
    │   API    │   │ (Embeddings)│   │   Base      │
    │ (GPT)    │   │             │   │ (Health     │
    │          │   │  Vector     │   │  Docs)      │
    │          │   │  Store      │   │             │
    └──────────┘   └─────────────┘   └─────────────┘
```

## Data Flow

### 1. Health Metrics Analysis Flow

```
User Input Form
    ↓
HealthMetrics Model
    ↓
POST /api/health/analyze
    ↓
HealthAnalyzer Service
    ↓
Rule-based Analysis
    ↓
Alert Generation
    ↓
JSON Response with Alerts
    ↓
Frontend Display
```

### 2. RAG Query Flow

```
User Question
    ↓
HealthQuery Model
    ↓
POST /api/health/query
    ↓
RAG Service
    ├─ Query Embeddings (OpenAI)
    ├─ Vector Search (Chroma)
    ├─ Retrieve Top-K Docs
    ├─ Pass to LLM
    └─ Generate Response
    ↓
LLM Response + Sources
    ↓
Frontend Display
```

## Component Interaction

```
App (Main Router)
├── HealthMetricsForm
│   └── calls handleMetricsSubmit()
│       └── POST /api/health/analyze
│           └── HealthAnalyzer
├── HealthAnalysis
│   └── displays alerts
│       └── from analyze endpoint
└── RAGQuery
    └── calls handleSubmit()
        └── POST /api/health/query
            └── RAGService
                ├── LangChain
                └── Chroma + OpenAI
```

## RAG (Retrieval-Augmented Generation) Pipeline

```
Knowledge Base (Text Documents)
    ↓
Text Chunking (RecursiveCharacterTextSplitter)
    ↓
Embedding Generation (OpenAI Embeddings)
    ↓
Vector Storage (Chroma)
    ↓
[User Query]
    ↓
Query Embedding
    ↓
Similarity Search (Top-K Retrieval)
    ↓
Retrieved Documents + Query
    ↓
LLM Prompt Construction
    ↓
GPT-3.5-Turbo Response
    ↓
Response + Sources to Frontend
```

## Key Services

### RAGService
- Manages vector store and LLM
- Handles document ingestion
- Performs similarity search
- Generates contextual responses

### HealthAnalyzer
- Analyzes metrics against thresholds
- Generates health alerts
- Provides recommendations
- Creates health summaries

## Technology Choices

| Layer | Technology | Why |
|-------|-----------|-----|
| Frontend | React | Modern, component-based, great for dashboards |
| Backend | FastAPI | High performance, async support, auto API docs |
| RAG | LangChain | Comprehensive, well-maintained, easy integration |
| Vector DB | Chroma | Lightweight, embedded, great for small-to-medium apps |
| LLM | GPT-3.5-Turbo | Cost-effective, high quality, reliable |
| Embeddings | OpenAI | High quality, consistent with LLM |

## Scalability Considerations

For production:
- Replace Chroma with PostgreSQL + pgvector
- Use Redis for caching
- Add API rate limiting
- Implement user authentication
- Use message queues for async jobs
- Deploy on Kubernetes
- Set up monitoring and logging

## Security Considerations

Current (Development):
- CORS open to all origins
- No authentication

Production:
- Restrict CORS origins
- Add JWT authentication
- Encrypt sensitive data
- Use HTTPS
- Implement rate limiting
- Sanitize user inputs
- Regular security audits
