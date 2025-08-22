from .store import BaseStore, CreateStore, UpdateStore, ReadStore, ReadAllStores, ReadDeletedStore
from .phone_number import BasePhoneNumber, CreatePhoneNumber, UpdatePhoneNumber, ReadPhoneNumber, ReadAllPhoneNumber, ReadDeletedPhoneNumber
from .address import BaseAddress, CreateAddress, ReadAddress, ReadAllAddresses, UpdateAddress, ReadDeletedAddress, DeleteAddress
from .employee import BaseEmployee, CreateEmployee, ReadEmployee, ReadAllEmployees, UpdateEmployee, DeleteEmployee, ReadDeletedEmployee

store = [
    'BaseStore',
    'CreateStore',
    'UpdateStore',
    'ReadStore',
    'ReadAllStores',
    'ReadDeletedStore'
]

phone_number = [
    'BasePhoneNumber',
    'CreatePhoneNumber',
    'UpdatePhoneNumber',
    'ReadPhoneNumber',
    'ReadAllPhoneNumber',
    'ReadDeletedPhoneNumber'
]

address = [
    'BaseAddress',
    'CreateAddress',
    'ReadAddress',
    'ReadAllAddresses',
    'UpdateAddress',
    'ReadDeletedAddress',
    'DeleteAddress'
]

employee = [
    'BaseEmployee',
    'CreateEmployee',
    'ReadEmployee',
    'ReadAllEmployees',
    'UpdateEmployee',
    'DeleteEmployee',
    'ReadDeletedEmployee'

]
__all__ = store + phone_number + address + employee
