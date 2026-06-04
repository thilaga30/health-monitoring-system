import React from 'react';

function HealthAnalysis({ alerts, metrics }) {
  const getAlertIcon = (type) => {
    switch (type) {
      case 'critical':
        return '🚨';
      case 'warning':
        return '⚠️';
      case 'info':
        return 'ℹ️';
      default:
        return '📌';
    }
  };

  const getAlertClass = (type) => {
    return `alert alert-${type}`;
  };

  return (
    <div className="analysis-container">
      <h2>Health Analysis Results</h2>
      
      {metrics && (
        <div className="metrics-summary">
          <h3>Your Metrics Summary</h3>
          <div className="summary-grid">
            <div className="metric-item">
              <span className="metric-label">❤️ Heart Rate</span>
              <span className="metric-value">{metrics.heart_rate} bpm</span>
            </div>
            <div className="metric-item">
              <span className="metric-label">🩸 Blood Pressure</span>
              <span className="metric-value">{metrics.blood_pressure}</span>
            </div>
            <div className="metric-item">
              <span className="metric-label">🌡️ Temperature</span>
              <span className="metric-value">{metrics.temperature}°C</span>
            </div>
            <div className="metric-item">
              <span className="metric-label">🍬 Glucose</span>
              <span className="metric-value">{metrics.glucose_level} mg/dL</span>
            </div>
            <div className="metric-item">
              <span className="metric-label">👟 Steps</span>
              <span className="metric-value">{metrics.steps_count}</span>
            </div>
            <div className="metric-item">
              <span className="metric-label">😴 Sleep</span>
              <span className="metric-value">{metrics.sleep_hours} hrs</span>
            </div>
          </div>
        </div>
      )}

      <div className="alerts-section">
        <h3>Health Alerts & Recommendations</h3>
        {alerts.length === 0 ? (
          <div className="alert alert-success">
            ✅ All metrics look good! Keep up your healthy habits.
          </div>
        ) : (
          <div className="alerts-list">
            {alerts.map((alert, index) => (
              <div key={index} className={getAlertClass(alert.type)}>
                <span className="alert-icon">{getAlertIcon(alert.type)}</span>
                <div className="alert-content">
                  <h4>{alert.metric.replace(/_/g, ' ').toUpperCase()}</h4>
                  <p>{alert.message}</p>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default HealthAnalysis;
