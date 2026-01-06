from typing import Annotated

from pydantic import BaseModel, Field, StringConstraints, constr

# This MODEL class helps us MODEL data that we'll use throughout the app

# Notice the use of data types conint and constr
# They help us enforce constraints (or rules) on the data

class UserModel(BaseModel):
    id: Annotated[int, Field(gt=0)] # gt = 0: this value must be greater than 0
    username: Annotated[str, Field(min_length=8)] # min_length = 8: this string must be at least 8 characters
    password: Annotated[str, Field(min_length=8)]
    email: Annotated[str, Field(min_length=8)]

    # TODO: better constraints, particularly for email