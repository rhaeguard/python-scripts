import json
from typing import List
from dataclasses import dataclass

@dataclass
class Class:
    id: str
    name: str


@dataclass
class Student:
    name: str
    school: str
    classes: List[Class]


student = Student(name='Ellie', school='UofT', classes=[
    Class(1, 'Sociology'),
    Class(2, 'Philosophy')
])

# this 'default' parameter helps converting the object to dict which makes it possible
# to be converted to json
# indent is for pretty print
# sort_keys is just there for...sorting keys
print(json.dumps(student, default=lambda x: x.__dict__, indent=4, sort_keys=True))
