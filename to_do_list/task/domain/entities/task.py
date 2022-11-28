import pydantic


class Task(pydantic.BaseModel):
    task_id = int
    task_name = str
    task_description = str
    task_state = str
    list_id = int
