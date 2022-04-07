from flask import request, jsonify, current_app
from app.models.vaccined_people_model import Vacinned
from  datetime import date, timedelta
from app.exc import NotFoundKey, InvalidKeyValue, InvalidCpf, CpfAlrealyExists


def new_vaccinated_people_controller():
    valid_keys = ["cpf", "name", "vaccine_name", "health_unit_name"]
    data  = request.get_json()
    new_data = dict()
    invalid_values = list()

    for key in data.keys():
        if key in valid_keys and type(data[key]) == str:
            new_data[key] = (data[key]).lower()
        elif key in valid_keys:
            invalid_values.append(key)

    not_found_keys = [
        key for key in valid_keys
         if key not in new_data.keys()
         ]
    
    search_old_vaccined_people = Vacinned.query.get(new_data['cpf'])
    
    try: 
        if search_old_vaccined_people:
            raise CpfAlrealyExists

        if len(invalid_values) > 0:
            raise InvalidKeyValue(invalid_values)

        if len(not_found_keys) > 0:
            raise NotFoundKey(valid_keys, not_found_keys)  

        if len(data["cpf"]) !=11:
            raise InvalidCpf(data["cpf"])
   
        date_today = date.today()
        next_date = date_today+timedelta(40)

        new_data["first_shot_data"] = date_today
        new_data["second_shot_data"] = next_date
        vaccined_people = Vacinned(**new_data)

        current_app.db.session.add(vaccined_people)
        current_app.db.session.commit()

        return jsonify(vaccined_people), 201


    except InvalidCpf as err:
        return err.message

    except NotFoundKey as err:
        return err.message

    except InvalidKeyValue as err:
        return err.message

    except CpfAlrealyExists as err:
        return err.message
    
    
