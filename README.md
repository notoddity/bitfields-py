## Python alternative flags

### How to install
`pip install altflags`

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