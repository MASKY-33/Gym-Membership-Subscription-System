from sqlalchemy import Column, Integer, String, Boolean
from motorForDB import Base







class GymMemberDB(Base):

    """
    Het database-model voor sportschoolleden.
    Strikte constraints op database-niveau garanderen absolute data-integriteit.
    """

    __tablename__ = "gym_members"


    id = Column(Integer, primary_key=True, index=True)


    # Een naam is verplicht (nullable=False) en mag maximaal 50 tekens lang zijn
    name = Column(String(50), nullable=False)


    # Leeftijd is verplicht
    age = Column(Integer, nullable=False)


    # De status is verplicht en staat standaard op True (active)
    is_active = Column(Boolean, default=True, nullable=False)