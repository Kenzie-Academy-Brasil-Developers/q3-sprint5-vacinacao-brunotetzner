from email.policy import default
from sqlalchemy import DateTime, String, Column
from app.configs.database import db
from dataclasses import dataclass
from  datetime import date, timedelta

@dataclass
class Vacinned(db.Model):
    cpf: str
    name: str
    vaccine_name: str
    health_unit_name: str
    first_shot_data: DateTime
    second_shot_data: DateTime

    __tablename__ = "vaccine_cards"
   
    cpf =              Column(String, primary_key=True, unique=True)
    name =             Column(String,  nullable=False)
    vaccine_name =     Column(String, nullable=False)
    health_unit_name = Column(String)
    first_shot_data  = Column(DateTime, default = date.today())
    second_shot_data = Column(DateTime, default =  date.today()+timedelta(90))


