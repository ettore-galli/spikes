from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from connection import Base


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    descr = Column(String)

    employees = relationship("Employee", back_populates="department")


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey("departments.id"))
    
    department = relationship("Department", back_populates="employees")
