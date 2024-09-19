# controllers/principal_controller.py
from flask import request, jsonify
from models import Assignment

@principal_blueprint.route('/assignments', methods=['GET'])
def get_principal_assignments():
    assignments = Assignment.query.filter_by(state='SUBMITTED', grade=None).all()
    return jsonify({'data': [assignment.to_dict() for assignment in assignments]})

