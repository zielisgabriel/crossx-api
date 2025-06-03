from dataclasses import dataclass
from server import db;
from sqlalchemy import Integer, String, Date;
from sqlalchemy.orm import Mapped, mapped_column;
from datetime import datetime;

@dataclass
class Student(db.Model):
    __tablename__ = "students";

    student_id: Mapped[int] = mapped_column(Integer, primary_key=True);
    name: Mapped[str] = mapped_column(String(100), nullable=False);
    status: Mapped[str] = mapped_column(String(15), nullable=False, default="Não Matriculado");
    city: Mapped[str] = mapped_column(String(20), nullable=False);
    address: Mapped[str] = mapped_column(String(180), nullable=False);
    state: Mapped[str] = mapped_column(String(20), nullable=False);
    phone: Mapped[str] = mapped_column(String(12), nullable=False);
    registration_date: Mapped[datetime | None] = mapped_column(Date, nullable=True);
    termination_date: Mapped[datetime | None] = mapped_column(Date, nullable=True);
    due_date: Mapped[datetime | None] = mapped_column(Date, nullable=True);

    @property
    def update_status(self):
        if self.status == "Matriculado" and self.due_date and self.due_date < datetime.now():
            self.status = "Pendente";
            db.session.commit();
        return self.status;