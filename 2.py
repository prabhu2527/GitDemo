from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 3, "maxLength": 25,"pattern":"^[A-Z][a-z]+$" },
        "surname": {"type": "string", "minLength": 3,"pattern":"^[A-Z][a-z]+$" },
        "age": {"type": "number", "minimum": 0, "maximum": 120},
        "status": {"type": "string", "enum": ["ACTIVE", "NOT ACTIVE"]},
        "dependencies": {"age": ["status"]},

        },
    
    
}

# validate(instance={"people": [
#     {
#       "name": "Adam",
#       "surname": "Bacon",
#       "age": 26,
#       "status": "ACTIVE"
#     },
#     {
#       "name": "Elizabeth",
#       "surname": "Corny",
#       "age": 55,
#       "status": "NOT ACTIVE"
#     },
#     {
#       "name": "Tommy",
#       "surname": "Freizer"
#     }
#   ]
# }, schema=schema)

validate(instance={
  "people": [
    {
      "name": "A", # name too short
      "surname": "Bacon",
      "age": 26,
      "status": "ACTIVE"
    },
    {
      "name": "Elizabeth",
      # missing surname
      "age": 55,
      "status": "UNKNOWN"
    },
    {
      "name": "Tommy",
      "surname": "Freizer",
      "age": 222
         }
  ]
},schema=schema)


