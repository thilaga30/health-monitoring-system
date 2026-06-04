import React, { useState } from 'react';

function HealthMetricsForm({ onSubmit }) {
  const [formData, setFormData] = useState({
    heart_rate: 72,
    blood_pressure: '120/80',
    temperature: 37,
    glucose_level: 100,
    steps_count: 8000,
    sleep_hours: 7.5,
    water_intake: 2000,
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: name === 'heart_rate' || name === 'glucose_level' || name === 'steps_count' 
        ? parseInt(value) 
        : name === 'temperature' || name === 'sleep_hours'
        ? parseFloat(value)
        : value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <div className="form-container">
      <h2>Enter Your Health Metrics</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>❤️ Heart Rate (bpm)</label>
          <input
            type="number"
            name="heart_rate"
            value={formData.heart_rate}
            onChange={handleChange}
            min="40"
            max="150"
          />
          <span className="range-info">Normal: 60-100 bpm</span>
        </div>

        <div className="form-group">
          <label>🩸 Blood Pressure (mmHg)</label>
          <input
            type="text"
            name="blood_pressure"
            value={formData.blood_pressure}
            onChange={handleChange}
            placeholder="120/80"
          />
          <span className="range-info">Normal: &lt;120/80 mmHg</span>
        </div>

        <div className="form-group">
          <label>🌡️ Temperature (°C)</label>
          <input
            type="number"
            name="temperature"
            value={formData.temperature}
            onChange={handleChange}
            step="0.1"
            min="35"
            max="40"
          />
          <span className="range-info">Normal: 36.1-37.2°C</span>
        </div>

        <div className="form-group">
          <label>🍬 Glucose Level (mg/dL)</label>
          <input
            type="number"
            name="glucose_level"
            value={formData.glucose_level}
            onChange={handleChange}
            min="50"
            max="300"
          />
          <span className="range-info">Normal (Fasting): 70-100 mg/dL</span>
        </div>

        <div className="form-group">
          <label>👟 Steps Today</label>
          <input
            type="number"
            name="steps_count"
            value={formData.steps_count}
            onChange={handleChange}
            min="0"
            max="50000"
          />
          <span className="range-info">Target: 8000-10000 steps</span>
        </div>

        <div className="form-group">
          <label>😴 Sleep Hours</label>
          <input
            type="number"
            name="sleep_hours"
            value={formData.sleep_hours}
            onChange={handleChange}
            step="0.5"
            min="0"
            max="12"
          />
          <span className="range-info">Target: 7-9 hours</span>
        </div>

        <div className="form-group">
          <label>💧 Water Intake (ml)</label>
          <input
            type="number"
            name="water_intake"
            value={formData.water_intake}
            onChange={handleChange}
            step="100"
            min="0"
            max="5000"
          />
          <span className="range-info">Target: 2000-3000 ml per day</span>
        </div>

        <button type="submit" className="submit-button">
          Analyze Metrics
        </button>
      </form>
    </div>
  );
}

export default HealthMetricsForm;
