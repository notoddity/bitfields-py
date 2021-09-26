# bitfields-py
`bitfields-py` is a simple way to abstract away bitmasking bitfields used for things like permissions, flags, etc.

## Why?
1. I don't want to have to manually bitmask a interger in code so abstract that away
2. I wanted to sort these "fields" as properties under a python class so they could be easily callable like `my_obj.my_field = True/False`
1. Easily parse bitfields passed to me over json with marshmallow
2. Easily create and parse bitfields to and from integers without writing any bit-masking in any situation

## Quick Start
### 1. Install with pip from PyPi
`python -m pip install altflags`
### 2. Create altflags, Flags class
```
from altflags import Flags, flag

class Permissions(Flags):
    create_message = flag(0)
    delete_message = flag(1)
    edit_message = flag(2)

user_permissions = Permissions()
```
### 3. Edit your flags
```
# Set create_message and edit_message flags to true
user_permissions.create_message = True
user_permissions.edit_message = True

# print flags as binary
print("{:0b}".format(user_permissions.flags))
# >>> 101
# all flags are False (0) from initialization

# print flags as integer
print({:0n}.format(user_permissions.flags))
# >>> 5
```
### 4. Compare flags
```
user2_permissions = Permission()
user2_permissions.create_message = True
user2_permissions.edit_message = True

print(user_permissions == user2_permissions)
# >>> True

user2_permissions.create_message = False
print(user_permissions == user2_permissions)
# >>> False
```

### 5. Extend altflags with class methods that return pre-formatted flag objects
```
class Permissions(Flags):
    create_message = flag(0)
    delete_message = flag(1)
    edit_message = flag(2)

    @classmethod
    def all(cls):
        new_cls = cls()
        new_cls.create_message = True
        new_cls.delete_message = True
        new_cls.edit_message = True
        return new_cls

user_permissions = Permissions.all()

print({:0b}.format(user_permissions))
# >>> 111

print({:0n}.format(user_permissions))
# >>> 7
```

### Notes
+ `flags(n: int)` n argument specifies the bit position of your flag (Warning: These can be overwritten).
