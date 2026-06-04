# Quick Start Guide

## Prerequisites

- Python 3.8+
- Node.js 14+
- OpenAI API key (get it from https://platform.openai.com)

## 1-2-3 Quick Start

### Step 1: Backend Setup (5 minutes)

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file and add your OpenAI API key
copy .env.example .env
# Edit .env and add: OPENAI_API_KEY=sk-...

# Run the backend
python -m app.main
```

Backend runs on: `http://localhost:8000`
API Docs: `http://localhost:8000/docs`

### Step 2: Frontend Setup (5 minutes)

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

Frontend runs on: `http://localhost:3000`

### Step 3: Use the App

1. Open `http://localhost:3000` in your browser
2. Enter your health metrics
3. Get instant health analysis
4. Ask the AI health assistant questions

## API Examples

### Analyze Health Metrics

```bash
curl -X POST http://localhost:8000/api/health/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "heart_rate": 75,
    "blood_pressure": "120/80",
    "temperature": 37,
    "glucose_level": 95,
    "steps_count": 8000,
    "sleep_hours": 7.5,
    "water_intake": 2000
  }'
```

### Query Health Information

```bash
curl -X POST http://localhost:8000/api/health/query \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What is a normal blood pressure range?"
  }'
```

## Common Issues

| Issue | Solution |
|-------|----------|
| ModuleNotFoundError | Run `pip install -r requirements.txt` |
| OPENAI_API_KEY error | Add your API key to `.env` file |
| Port 8000 in use | Change port: `python -m app.main --port 8001` |
| CORS errors | Backend CORS is configured for all origins |
| npm dependencies error | Run `npm install` again or clear cache |

## Next Steps

- Customize the health knowledge base in `backend/app/data/health_knowledge.py`
- Add more health metrics and analysis rules
- Deploy to production (Vercel for frontend, Heroku/Railway for backend)
- Add user authentication
- Connect to real health data sources

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [OpenAI API Reference](https://platform.openai.com/docs/)
