from fastapi import APIRouter, status, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import CreateEmployee, ReadEmployee, ReadAllEmployees, UpdateEmployee, ReadDeletedEmployee
from app.services import EmployeeService

router = APIRouter()

@router.post('/', status_code= status.HTTP_201_CREATED, response_model= ReadEmployee)
async def create_employee(
    employee : CreateEmployee,
    db : Session = Depends(get_db)):

    return EmployeeService.create(db, employee)

@router.get('/{employee_id}', status_code= status.HTTP_200_OK, response_model= ReadEmployee)
async def read_employee(employee_id : int, db : Session = Depends(get_db)):

    return EmployeeService.read(db , employee_id)

@router.get('/', status_code= status.HTTP_200_OK, response_model= ReadAllEmployees)
async def read_all_employees(search : str | None = Query("", description= ""), db : Session = Depends(get_db)):

    return EmployeeService.read_all(db, search)

@router.put('/{employee_id}', status_code= status.HTTP_200_OK, response_model= ReadEmployee)
async def update_employee(employee_id : int, updated_employee : UpdateEmployee, db : Session = Depends(get_db)):

    return EmployeeService.update(db, employee_id, updated_employee)

@router.delete('/{employee_id}', status_code= status.HTTP_200_OK, response_model= ReadDeletedEmployee)
async def delete_employee(employee_id : int, db : Session = Depends(get_db)):

    return EmployeeService.delete(db, employee_id)
