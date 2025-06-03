from datetime import datetime
from server import app, db;
from flask import request, jsonify, Response;
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
    registration_date = None;
    termination_date = None;
    due_date = None;

    student = Student(
        name=name,
        city=city,
        state=state,
        phone=phone,
        address=address,
        registration_date=registration_date,
        termination_date=termination_date,
        due_date=due_date,
    );

    db.session.add(student);
    db.session.commit();

    return Response(status=201);