from datetime import datetime
from server import app, db;
from flask import request, jsonify;
from models.Student import Student;
from dateutil.relativedelta import relativedelta

@app.post("/students/create")
def createStudent():
    data = request.get_json();

    name = data["name"];
    city = data["city"];
    state = data["state"];
    phone = data["phone"];
    address = data["address"];
    status = data["status"];


    if status == "Matriculado":
        registration_date = datetime.now();
        due_date = registration_date + relativedelta(months=1);
        termination_date = None;
    else:
        registration_date = None;
        due_date = None;
        termination_date = None;

    student = Student(
        name=name,
        city=city,
        state=state,
        phone=phone,
        address=address,
        status=status,
        registration_date=registration_date,
        termination_date=termination_date,
        due_date=due_date,
    );

    db.session.add(student);
    db.session.commit();

    return jsonify({"message": "Student created"});