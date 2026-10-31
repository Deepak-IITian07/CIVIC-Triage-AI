from pydantic import BaseModel, ConfigDict


class IncidentReport(BaseModel):
    model_config = ConfigDict(extra="forbid")

    incident_id: str
    location: str
    severity: int
