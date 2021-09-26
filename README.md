# bitfields-py
`bitfields-py` is a simple way to abstract away bitmasking bitfields used for things like permissions, flags, etc. I didn't want
to have to write another `1 >> n` or `1 << n` in my code ever again. I wanted to easily define a subclass and assign some properties
at certain bit locations to some name and have those be easily readable, editable and serializable. I finally wanted to build this
into marshmallow to help automatically parse bitfields over json passed by api's.

Automatically serialize and de-sserialize bitfields via marshmallow

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
