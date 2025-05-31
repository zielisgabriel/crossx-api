from server import app, db;
import controllers.list_students, controllers.create_student, controllers.delete_student, controllers.find_by_student_name;
from services.update_student_status import update_student_status;
from apscheduler.schedulers.background import BackgroundScheduler;

with app.app_context():
    db.create_all();

scheduler = BackgroundScheduler();
scheduler.add_job(func=update_student_status, trigger="interval", seconds=10);
scheduler.start();

if __name__ == "__main__":
    app.run(debug=True);