# Stringman : String manipulation package
This package contains functions related to strings and regex so that I do not have to type them every time. Currently, there are not many functions but I am planning on adding more soon.

# Getting Started
```py
from stringman.strings import occurences

MESSAGE = "This is a string which contains a string which contains another string and string? Is it a string?"

print(occurences(MESSAGE, "string"))
```

Or, compress a string!

```py
from stringman.strings import compress_string
MESSAGE = "aaaaaaaaaaaaaaaaaabbbbeeebeeeeeeeeeeeeeeeeccccccccccccccccccc"

print(compress_string(MESSAGE))
```