## Python alternative flags

### Quick Start
1. Install with pip from PyPi
    + `python -m pip install altflags`
1. Create your `myapplication.py` file
1. Import `Flags` and `flag` from altflags
    + `from altflags import Flags, flag`
1. Create a new Flags class (i.e. `Permissions`)
``` class Permissions(Flags):
create_message = flag(0)
delete_message = flag(1)
edit_message = flag(2)
```
1. Update your flags

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