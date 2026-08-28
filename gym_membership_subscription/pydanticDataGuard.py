from pydantic import BaseModel, Field







# Wat er BINNEN komt bij een inschrijving
# Pydantic BaseModel
class MembershipCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, json_schema_extra={"example": "MASKY MASK"})
    age: int = Field(..., ge=16, le=100, json_schema_extra={"example": 25})  # Alleen leden tussen 16 en 100 jaar


# Wat er wordt teruggestuurd naar de frontend/klant
class MembershipResponse(BaseModel):
    id: int
    name: str
    age: int
    is_active: bool


    # Dit zorgt ervoor dat Pydantic data uit de SQLAlchemy ORM-modellen kan lezen
    class Config:
        from_attributes = True