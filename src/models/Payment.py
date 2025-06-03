from server import db;
from dataclasses import dataclass;
from datetime import datetime;
from sqlalchemy import ForeignKey, Integer, DECIMAL, Date, String;
from sqlalchemy.orm import Mapped, mapped_column;
from decimal import Decimal;

@dataclass
class Payment(db.Model):
    __tablename__ = "payments";

    payment_id: Mapped[int] = mapped_column(Integer, primary_key=True);
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("students.student_id"));
    amount: Mapped[Decimal] = mapped_column(DECIMAL, nullable=False);
    payment_method: Mapped[str] = mapped_column(String(20), nullable=False);
    payment_date: Mapped[datetime] = mapped_column(Date, nullable=False, default=datetime.now());