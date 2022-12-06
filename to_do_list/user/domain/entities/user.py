import pydantic


class User(pydantic.BaseModel):

    user_id = int
    user_name = str
    user_lastname = str
    user_email = str
    user_password = str
