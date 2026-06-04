from typing import List, Optional
from app.models.health import HealthMetrics, HealthAlert
from datetime import datetime

class HealthAnalyzer:
    """Analyzes health metrics and generates alerts"""
    
    # Normal ranges for various metrics
    NORMAL_RANGES = {
        "heart_rate": (60, 100),
        "systolic_bp": (90, 120),
        "diastolic_bp": (60, 80),
        "temperature": (36.1, 37.2),
        "glucose_level": (70, 100),  # fasting
        "sleep_hours": (7, 9),
    }
    
    @staticmethod
    def analyze_metrics(metrics: HealthMetrics) -> List[HealthAlert]:
        """Analyze health metrics and return alerts"""
        alerts = []
        
        # Analyze heart rate
        if metrics.heart_rate < 60 or metrics.heart_rate > 100:
            alert_type = "warning" if 50 < metrics.heart_rate < 110 else "critical"
            alerts.append(HealthAlert(
                type=alert_type,
                message=f"Heart rate is {metrics.heart_rate} bpm. Consider resting or consulting a doctor.",
                metric="heart_rate",
                timestamp=datetime.now()
            ))
        
        # Analyze blood pressure
        try:
            systolic, diastolic = map(int, metrics.blood_pressure.split("/"))
            if systolic < 90 or systolic > 140 or diastolic < 60 or diastolic > 90:
                alert_type = "warning" if (80 < systolic < 160 and 50 < diastolic < 100) else "critical"
                alerts.append(HealthAlert(
                    type=alert_type,
                    message=f"Blood pressure is {metrics.blood_pressure}. Monitor closely.",
                    metric="blood_pressure",
                    timestamp=datetime.now()
                ))
        except:
            pass
        
        # Analyze temperature
        if metrics.temperature < 36.1 or metrics.temperature > 37.5:
            alert_type = "warning" if 35.5 < metrics.temperature < 38.5 else "critical"
            alerts.append(HealthAlert(
                type=alert_type,
                message=f"Body temperature is {metrics.temperature}°C. Keep an eye on this.",
                metric="temperature",
                timestamp=datetime.now()
            ))
        
        # Analyze glucose level
        if metrics.glucose_level < 70 or metrics.glucose_level > 125:
            alert_type = "warning" if 60 < metrics.glucose_level < 150 else "critical"
            alerts.append(HealthAlert(
                type=alert_type,
                message=f"Glucose level is {metrics.glucose_level} mg/dL. Check with your doctor if persistent.",
                metric="glucose_level",
                timestamp=datetime.now()
            ))
        
        # Analyze sleep
        if metrics.sleep_hours < 6 or metrics.sleep_hours > 10:
            alerts.append(HealthAlert(
                type="info",
                message=f"Sleep: {metrics.sleep_hours} hours. Aim for 7-9 hours for optimal health.",
                metric="sleep_hours",
                timestamp=datetime.now()
            ))
        
        # Analyze water intake
        if metrics.water_intake < 1500:
            alerts.append(HealthAlert(
                type="info",
                message=f"Water intake: {metrics.water_intake} ml. Consider drinking more water.",
                metric="water_intake",
                timestamp=datetime.now()
            ))
        
        return alerts
    
    @staticmethod
    def generate_health_summary(metrics: HealthMetrics) -> str:
        """Generate a health summary from metrics"""
        summary = f"""
        Health Summary:
        - Heart Rate: {metrics.heart_rate} bpm
        - Blood Pressure: {metrics.blood_pressure} mmHg
        - Temperature: {metrics.temperature}°C
        - Glucose Level: {metrics.glucose_level} mg/dL
        - Steps: {metrics.steps_count}
        - Sleep: {metrics.sleep_hours} hours
        - Water Intake: {metrics.water_intake} ml
        """
        return summary
