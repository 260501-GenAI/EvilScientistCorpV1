from typing import Annotated

from pydantic import BaseModel, Field, SecretStr

# This MODEL class helps us MODEL data that we'll use throughout the app

# Notice the use of Annotated and Field
# They help us enforce constraints (or rules) on the data

class UserModel(BaseModel):
    # gt = 0: this value must be greater than 0
    # = None: this field is optional when creating a user (it gets overwritten anyway)
    id: Annotated[int, Field(gt=0)] = None
    # min_length = 8: this string must be at least 8 characters
    username: Annotated[str, Field(min_length=5, max_length=15)]
    password: Annotated[SecretStr, Field(min_length=8)]
    # pattern: allows us to define a regex pattern this string must follow
    # in this, just checking that the field looks like a valid email
    email: Annotated[str, Field(min_length=8, pattern=r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$')]
