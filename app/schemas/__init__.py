from .store import BaseStore, CreateStore, UpdateStore, ReadStore, ReadAllStores, ReadDeletedStore
from .phone_number import BasePhoneNumber, CreatePhoneNumber, UpdatePhoneNumber, ReadPhoneNumber, ReadAllPhoneNumber, ReadDeletedPhoneNumber
from .address import BaseAddress, CreateAddress, ReadAddress, ReadAllAddresses, UpdateAddress, ReadDeletedAddress, DeleteAddress

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

__all__ = store + phone_number + address
