from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class HealthMetrics(BaseModel):
    heart_rate: int
    blood_pressure: str  # e.g., "120/80"
    temperature: float
    glucose_level: int
    steps_count: int
    sleep_hours: float
    water_intake: int  # in ml
    timestamp: Optional[datetime] = None

class HealthQuery(BaseModel):
    question: str
    metrics: Optional[HealthMetrics] = None

class HealthResponse(BaseModel):
    answer: str
    sources: List[str]
    timestamp: datetime

class HealthAlert(BaseModel):
    type: str  # warning, critical, info
    message: str
    metric: str
    timestamp: datetime
