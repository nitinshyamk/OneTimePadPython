OneTimePadPython
================

a simple set of files that convert a string to a cipher text using the one time pad.
NOT intended to be secure yet, simply an exercise in converting character strings
to bit strings using the  xor operation and mapping from one space to another. 
I will attempt to add a more secure pseudo random
generator later (though implemented, linear congruential generator has an extremely predictable output. e.g. one result produced 1110010111 repeating, hardly random at all).
Could use the os.random function, but would limit my ability to create a decrpyt.py file - will wait to develop further