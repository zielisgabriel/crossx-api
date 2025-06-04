from server import app, db

import controllers.list_students_controller, controllers.create_student_controller, controllers.delete_student_controller, controllers.update_student_controller, controllers.find_student_by_name_controller, controllers.list_student_payment_history_controller, controllers.make_payment_controller

from services.update_student_status import update_student_status
from apscheduler.schedulers.background import BackgroundScheduler

with app.app_context():
    db.create_all()

scheduler = BackgroundScheduler()
scheduler.add_job(func=update_student_status, trigger="interval", seconds=10)
scheduler.start()

if __name__ == "__main__":
    app.run(debug=True)