from flask import Blueprint 
from app.controllers.post_vaccinated_people_controller import new_vaccinated_people_controller
from app.controllers.get_all_controller import get_all_controller

bp_vaccine = Blueprint("bp_vaccine", __name__, url_prefix="/vaccinations")

bp_vaccine.get("")(get_all_controller)
bp_vaccine.post("")(new_vaccinated_people_controller)
