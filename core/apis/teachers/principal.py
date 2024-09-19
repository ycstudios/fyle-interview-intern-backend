# controllers/principal_controller.py
from flask import request, jsonify
from models import Teacher

@principal_blueprint.route('/teachers', methods=['GET'])
def get_principal_teachers():
    teachers = Teacher.query.all()
    return jsonify({'data': [teacher.to_dict() for teacher in teachers]})
