from fastapi import HTTPException, status

class PhoneNumberHandler:

    @staticmethod
    def phone_numbers_limit_exceeded(obj, name, id):

        message = f'{obj} called {name} with id {id} has reached the maximum number of phone numbers'
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= message)