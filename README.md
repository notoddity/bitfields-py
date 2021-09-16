## Python alternative flags

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
# >>> 
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
+ `flags(n: int)` n argument specifies the bit position of your flag (Warning: These can be overwritten)

### How to use
```
from altflags import Flags, flag

class Permissions(Flags)
    view_page = flag(0)
    add_message = flag(1)

user = Permission()

user.view_page = True

print(user.view_page)
# 

print(user.flags)
# >>> 1

user.add_message = True

print(user.add_message)
# >>> True

print(user.flags)
# >>> 3

user.view_page = False

print(user.view_page)
# >>> False

print(user.flags)
# >>> 2

print("{:0b}".format(user.flags))
# >>> 10
```

### Flag method arguments
The `n` argument in `altflags.flag(n)` is the bit position of the flag