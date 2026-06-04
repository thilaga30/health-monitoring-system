import React, { useState } from 'react';

function RAGQuery({ metrics }) {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!query.trim()) return;

    setLoading(true);
    setError(null);
    try {
      const response = await fetch('http://localhost:8000/api/health/query', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          question: query,
          metrics: metrics,
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to get response');
      }

      const data = await response.json();
      setResponse(data);
    } catch (err) {
      setError(err.message);
      console.error('Error querying RAG:', err);
    } finally {
      setLoading(false);
    }
  };

  const suggestedQuestions = [
    'What is a normal blood pressure range?',
    'How many hours of sleep do I need?',
    'What should my water intake be?',
    'How often should I exercise?',
    'What are signs of high blood sugar?',
  ];

  return (
    <div className="rag-container">
      <h2>🤖 AI Health Assistant</h2>
      <p>Ask questions about health, fitness, and wellness. Our AI will provide evidence-based answers.</p>

      <form onSubmit={handleSubmit} className="query-form">
        <div className="input-group">
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Ask a health question..."
            className="query-input"
          />
          <button type="submit" disabled={loading} className="query-button">
            {loading ? 'Thinking...' : 'Ask'}
          </button>
        </div>
      </form>

      <div className="suggested-questions">
        <p>Suggested questions:</p>
        <div className="question-chips">
          {suggestedQuestions.map((q, idx) => (
            <button
              key={idx}
              className="question-chip"
              onClick={() => {
                setQuery(q);
                // Auto-submit
                setTimeout(() => {
                  document.querySelector('.query-form').dispatchEvent(new Event('submit', { bubbles: true }));
                }, 100);
              }}
            >
              {q}
            </button>
          ))}
        </div>
      </div>

      {error && (
        <div className="error-message">
          ❌ Error: {error}
        </div>
      )}

      {response && (
        <div className="response-container">
          <div className="response-card">
            <h3>💡 Answer</h3>
            <p className="response-text">{response.answer}</p>
            
            {response.sources && response.sources.length > 0 && (
              <div className="sources">
                <h4>📚 Sources:</h4>
                <ul>
                  {response.sources.map((source, idx) => (
                    <li key={idx}>{source}...</li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}

export default RAGQuery;
