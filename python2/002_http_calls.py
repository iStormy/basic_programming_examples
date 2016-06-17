#!/bin/env python2.7

# Single line comment 
"""
Multiline 
comment.
"""

import requests

"""
This is an import. Python has a very large built-in library, providing hundreds of thousands of useful functions and objects. In Python,
you import "modules." Modules can have functions and variables defined within them directly or have sub objects inside them.  You can also download
and install additional modules, created by people other than the Python maintainers. Check out the Python Package Index (or pypi) for more info.
The "requests" is one of the modules used for making web/http requests. This module was built using python's builtin http/web reques modules.
"""

response = requests.get("https://google.com")
print("Response: %s" %s response.content) # response.text would work too.

"""
 I don't know how you're gonna explain the code above but try
 to use it as something to base it off of. Also I recommend, 
 guiding users through the process of setting up the environment
 in your readme.md
"""

# Incomplete. Next, we'll cover wtf the code above means.

# sorry if I rip'd what you were trying to do. I'll add more once I am home.
