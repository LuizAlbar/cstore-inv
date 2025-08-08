from fastapi import HTTPException, status
from sqlalchemy.inspection import inspect

class ResponseHandler:
    @staticmethod
    def success(message, data=None):
        return {"message": message, "data": data}

    @staticmethod
    def get_single_success(name, id, data):
        message = f"Details for {name} with id {id}"
        return ResponseHandler.success(message, data)
    
    @staticmethod
    def get_all_success(object, data):
        message = f"Detais for all {object}s"
        return ResponseHandler.success(message, data)

    @staticmethod
    def create_success(name, id, data, response_schema=None):
        message = f"{name} with id {id} created successfully"
        response = {"message": message, "data": data}
    
        if response_schema:
            return response_schema(**response)  
    
        return response

    @staticmethod
    def update_success(name, id, data):
        message = f"{name} with id {id} updated successfully"
        return ResponseHandler.success(message, data)

    @staticmethod
    def delete_success(name, id, data):
        message = f"{name} with id {id} deleted successfully"
        return ResponseHandler.success(message, data)

    @staticmethod
    def not_found_error(name="", id=None):
        message = f"{name} With Id {id} Not Found!"
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)
    
    @staticmethod
    def db_not_populated_error(name = ""):
        message = f"{name} table is empty"
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)
    
    @staticmethod
    def value_already_exists_on_db(model, obj, db, exclude_id: int = None):

        mapper = inspect(model)
        unique_values = [
        c.name for c in mapper.columns
        if c.unique and not c.primary_key
    ]
        duplications = {}

        for value in unique_values:
            data = getattr(obj, value)
            if data is None:
                continue

            filter_query = db.query(model).filter(getattr(model, value) == data)

            if exclude_id:
 
                pk = mapper.primary_key[0].name
                filter_query = filter_query.filter(getattr(model, pk) != exclude_id)

            if filter_query.first():
                duplications[value] = f"{data} already exists"

        if duplications:
            raise HTTPException(status_code= status.HTTP_409_CONFLICT, detail= duplications)
        
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Database integrity error, but no unique constraint violation found."
            )

    @staticmethod
    def invalid_token(name=""):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid {name} token.",
            headers={"WWW-Authenticate": "Bearer"})