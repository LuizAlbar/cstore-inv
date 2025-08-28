from .store_schema import BaseStore, CreateStore, UpdateStore, ReadStore, ReadAllStores, ReadDeletedStore, ReadAllEmployeesStore
from .phone_number_schema import BasePhoneNumber, CreatePhoneNumber, UpdatePhoneNumber, ReadPhoneNumber, ReadAllPhoneNumber, ReadDeletedPhoneNumber
from .address_schema import BaseAddress, CreateAddress, ReadAddress, ReadAllAddresses, UpdateAddress, ReadDeletedAddress, DeleteAddress
from .employee_schema import BaseEmployee, CreateEmployee, ReadEmployee, ReadAllEmployees, UpdateEmployee, DeleteEmployee, ReadDeletedEmployee

store_schema = [
    'BaseStore',
    'CreateStore',
    'UpdateStore',
    'ReadStore',
    'ReadAllStores',
    'ReadDeletedStore',
    'ReadAllEmployeesStore'
]

phone_number_schema = [
    'BasePhoneNumber',
    'CreatePhoneNumber',
    'UpdatePhoneNumber',
    'ReadPhoneNumber',
    'ReadAllPhoneNumber',
    'ReadDeletedPhoneNumber'
]

address_schema = [
    'BaseAddress',
    'CreateAddress',
    'ReadAddress',
    'ReadAllAddresses',
    'UpdateAddress',
    'ReadDeletedAddress',
    'DeleteAddress'
]

employee_schema = [
    'BaseEmployee',
    'CreateEmployee',
    'ReadEmployee',
    'ReadAllEmployees',
    'UpdateEmployee',
    'DeleteEmployee',
    'ReadDeletedEmployee'

]
__all__ = store_schema + phone_number_schema + address_schema + employee_schema
