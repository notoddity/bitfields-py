# Python alternative (binary) flags

## How to install altflags
`pip install altflags`

## How to use altflags
```
from altflags import Flags, flag

class Permissions(Flags)
    view_page = flag(0)
    add_message = flag(1)

user = Permission()

user.view_page = True

print(user.view_page)
# >>> True

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
```

## flag method
The n argument should me to bit position of the flag you are setting