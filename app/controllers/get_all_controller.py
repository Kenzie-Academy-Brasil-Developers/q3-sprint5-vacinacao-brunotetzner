from app.models.vaccined_people_model import Vacinned
from flask import jsonify
def get_all_controller():
    all_vacinneds = Vacinned.query.all()
    return jsonify(all_vacinneds)
