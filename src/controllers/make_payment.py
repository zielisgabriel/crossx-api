from datetime import datetime
from server import app, db;
from flask import jsonify, request, Response;
from models.Payment import Payment;
from models.Student import Student;
from decimal import Decimal;
from dateutil.relativedelta import relativedelta;

from exceptions.StudentNotFoundException import StudentNotFoundException;

@app.post("/payments/make/<int:student_id>")
def make_payment(student_id):
    try:
        student = Student.query.filter_by(student_id=student_id).first();

        if student is None:
            raise StudentNotFoundException();

        if student.status == "Matriculado":
            raise Exception("O aluno já esta matriculado.");

        data = request.get_json();
    
        payment = Payment(
            student_id=student_id,
            amount=Decimal(data["amount"]),
            payment_method=data["payment_method"],
            payment_date=datetime.now()
        );
    
        student.status = "Matriculado";
        student.registration_date = datetime.now();
        student.due_date = datetime.now() + relativedelta(months=1);
    
        db.session.add(payment);
        db.session.commit();
    
        return Response(status=200);
    except (Exception) as e:
        if isinstance(e, StudentNotFoundException):
            return jsonify({"message": str(e)}), 404;
        elif isinstance(e, Exception):
            return jsonify({"message": str(e)}), 400;
        return jsonify({"message": "Unhandled error"}), 500;
    