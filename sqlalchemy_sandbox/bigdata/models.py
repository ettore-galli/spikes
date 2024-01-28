from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from bigdata.base import Base


# pylint: disable=too-few-public-methods
class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    descr = Column(String(50))

    employees = relationship("Employee", back_populates="department")


# pylint: disable=too-few-public-methods
class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    department_id = Column(Integer, ForeignKey("departments.id"))

    department = relationship("Department", back_populates="employees")
