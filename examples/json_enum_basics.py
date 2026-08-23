import json
from enum import StrEnum

text = """
{
    "job": {
        "title": "Python Engineer",
        "requirements": [
            {
                "name": "Python",
                "level": "required"
            }
        ]
    },
    "candidate": {
        "skills": ["Python", "Java"]
    }
}
"""

raw = json.loads(text)

print(type(raw))
print(type(raw["job"]))
print(type(raw["job"]["title"]))
print(type(raw["job"]["requirements"]))
print(type(raw["job"]["requirements"][0]))
print(type(raw["candidate"]["skills"]))


class RequirementLevel(StrEnum):
    REQUIRED = "required"
    PREFERRED = "preferred"


a = RequirementLevel("required")
b = RequirementLevel.REQUIRED

print(a)
print(b)

print(a == b)

print(RequirementLevel.REQUIRED.name)
print(RequirementLevel.REQUIRED.value)

print(a.name)  # REQUIRED
print(a.value)  # required
print(repr(a))  # <RequirementLevel.REQUIRED: 'required'>
