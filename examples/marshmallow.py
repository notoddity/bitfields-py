# Import bitfields class and property
from bitfields import Fields, field

# Create your Fields class maping field's to bits
class Permissions(Fields):
    kick = field(0)
    ban = field(1)
    mute = field(2)

# import marshmallow schema and bitfields bitfield class
from marshmallow import Schema
from bitfields.marshmallow import BitField

# create marshmallow schema
class User(Schema):
    
    # use bitfield to assign a schema field to a bit field.
    # pass your bitfield class type as the first arg
    permissions = BitField(Permissions)

# simple json example
json_example = \
'''
{
    "permissions": 5
}
'''

# loads json data into python dict
user = User().loads(json_example)

# lets check the fields of our bitfields object
print(user["permissions"].kick)
print(user["permissions"].ban)
print(user["permissions"].mute)
# >>> True
# >>> False
# >>> True