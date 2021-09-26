
# Import bitfields class and property
from bitfields import Fields, field

# Create your Fields class maping field's to bits
class Permissions(Fields):
    kick = field(0)
    ban = field(1)
    mute = field(2)

# Create a new permissions field
user_perms = Permissions()
print(user_perms)
# >>> 0

# Update user permissions
user_perms.kick = True
user_perms.mute = True
print(user_perms)
# >>> 5