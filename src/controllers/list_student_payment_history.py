from exceptions.StudentNotFoundException import StudentNotFoundException
from server import app;
from flask import jsonify;
from models.Payment import Payment;
from models.Student import Student;


@app.get("/payments/list/<int:student_id>")
def list_student_payment_history(student_id):
    try:
        student = Student.query.filter_by(student_id=student_id).first();

        if student is None:
            raise StudentNotFoundException();
            
        payment = Payment.query.filter_by(student_id=student_id).order_by(Payment.payment_date).all();
    
        return jsonify({"payments": payment});
    except Exception as e:
        return jsonify({"message": str(e)}), 400;