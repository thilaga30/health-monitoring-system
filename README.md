# Health Monitoring RAG System

A modern, AI-powered health monitoring system built with:
- **LangChain** - For RAG (Retrieval-Augmented Generation)
- **FastAPI** - High-performance Python web framework
- **React** - Modern frontend with Vite
- **OpenAI GPT** - For intelligent health insights
- **Chroma** - Vector database for document retrieval

## Features

✨ **Health Metrics Analysis**
- Track heart rate, blood pressure, temperature, glucose, sleep, steps, and water intake
- Real-time health alerts and recommendations
- Visual dashboard with metric summaries

🤖 **AI Health Assistant**
- Ask health-related questions using natural language
- RAG-powered responses using a curated health knowledge base
- Evidence-based answers with source citations

📊 **Real-Time Monitoring**
- Instant health analysis with threshold-based alerts
- Critical, warning, and info level notifications
- Personalized health recommendations

## Tech Stack

**Backend:**
- Python 3.8+
- FastAPI
- LangChain
- Chroma
- OpenAI API

**Frontend:**
- React 18
- Axios for API calls
- CSS Grid for responsive design

## Installation

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

5. Run the backend:
```bash
python -m app.main
# or use uvicorn directly:
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The frontend will be available at `http://localhost:3000`

## API Endpoints

### Health Metrics Analysis
- **POST** `/api/health/analyze` - Analyze health metrics and get alerts

### Health Query (RAG)
- **POST** `/api/health/query` - Query the AI health assistant

### Health Summary
- **POST** `/api/health/summary` - Generate a health summary

### Documentation
- **GET** `/docs` - Interactive API documentation (Swagger UI)

## Project Structure

```
health-monitoring-rag/
├── backend/
│   ├── app/
│   │   ├── models/
│   │   │   └── health.py          # Data models
│   │   ├── routes/
│   │   │   └── health.py          # API routes
│   │   ├── services/
│   │   │   ├── rag_service.py     # RAG service with LangChain
│   │   │   └── health_analyzer.py # Health analysis logic
│   │   ├── data/
│   │   │   └── health_knowledge.py # Health knowledge base
│   │   └── main.py                 # FastAPI app setup
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── HealthMetricsForm.js   # Metrics input form
│   │   │   ├── HealthAnalysis.js      # Analysis results display
│   │   │   └── RAGQuery.js            # AI query interface
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   └── index.css
│   ├── public/
│   │   └── index.html
│   └── package.json
└── README.md
```

## Usage

1. **Enter Health Metrics:**
   - Fill in your current health metrics
   - Click "Analyze Metrics"
   - View alerts and recommendations

2. **Ask Health Questions:**
   - Switch to AI Assistant tab
   - Ask a health-related question
   - Get AI-powered responses with sources

3. **View Results:**
   - See personalized recommendations
   - Track your health metrics over time
   - Follow health guidance from the AI

## Health Metrics Explained

- **Heart Rate**: Beats per minute (60-100 bpm is normal)
- **Blood Pressure**: Systolic/Diastolic (120/80 mmHg is normal)
- **Temperature**: Body temperature (36.1-37.2°C is normal)
- **Glucose Level**: Blood sugar (70-100 mg/dL fasting is normal)
- **Steps**: Daily physical activity target (8,000-10,000)
- **Sleep**: Hours of sleep needed (7-9 hours recommended)
- **Water Intake**: Daily hydration (2-3 liters recommended)

## Knowledge Base

The system includes a curated knowledge base covering:
- Heart health and cardiovascular wellness
- Blood pressure management
- Temperature regulation
- Blood glucose monitoring
- Sleep quality and importance
- Hydration guidelines
- Physical activity recommendations
- Stress management
- Nutrition basics
- When to seek medical help

## Configuration

### LangChain Configuration
- LLM: GPT-3.5-Turbo
- Temperature: 0.7 (balanced creativity/consistency)
- Embeddings: OpenAI embeddings
- Retriever: Top 3 documents

### Vector Store
- Type: Chroma (persistent local storage)
- Location: `./chroma_db`
- Auto-persists changes

## Environment Variables

```
OPENAI_API_KEY=your_openai_api_key
```

Get your API key from: https://platform.openai.com/api-keys

## Future Enhancements

- User authentication and data persistence
- Historical health data tracking
- Personalized health goals
- Integration with wearable devices
- Multi-language support
- Advanced analytics and reporting
- Predictive health insights
- Medication tracking

## Troubleshooting

**Backend won't start:**
- Ensure Python 3.8+ is installed
- Check that OPENAI_API_KEY is set in .env
- Run `pip install -r requirements.txt` again

**Frontend won't load:**
- Clear node_modules: `rm -rf node_modules && npm install`
- Clear browser cache
- Make sure backend is running on port 8000

**API connection issues:**
- Check CORS configuration in backend
- Verify backend is running on localhost:8000
- Check browser console for errors

## License

MIT

## Support

For issues or questions, please check the documentation or create an issue in the repository.
