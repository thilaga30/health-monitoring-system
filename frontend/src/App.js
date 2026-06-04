import React, { useState } from 'react';
import './App.css';
import HealthMetricsForm from './components/HealthMetricsForm';
import HealthAnalysis from './components/HealthAnalysis';
import RAGQuery from './components/RAGQuery';

function App() {
  const [metrics, setMetrics] = useState(null);
  const [alerts, setAlerts] = useState([]);
  const [activeTab, setActiveTab] = useState('metrics');

  const handleMetricsSubmit = async (formMetrics) => {
    setMetrics(formMetrics);
    try {
      const response = await fetch('http://localhost:8000/api/health/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formMetrics),
      });
      const data = await response.json();
      setAlerts(data);
    } catch (error) {
      console.error('Error analyzing metrics:', error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>💚 Health Monitoring RAG System</h1>
        <p>AI-Powered Health Insights with Real-Time Analysis</p>
      </header>

      <div className="tabs">
        <button 
          className={`tab-button ${activeTab === 'metrics' ? 'active' : ''}`}
          onClick={() => setActiveTab('metrics')}
        >
          📊 Health Metrics
        </button>
        <button 
          className={`tab-button ${activeTab === 'query' ? 'active' : ''}`}
          onClick={() => setActiveTab('query')}
        >
          🤖 AI Assistant
        </button>
      </div>

      <div className="content">
        {activeTab === 'metrics' && (
          <div className="metrics-section">
            <HealthMetricsForm onSubmit={handleMetricsSubmit} />
            {alerts.length > 0 && <HealthAnalysis alerts={alerts} metrics={metrics} />}
          </div>
        )}
        {activeTab === 'query' && <RAGQuery metrics={metrics} />}
      </div>
    </div>
  );
}

export default App;
