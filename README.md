# Anfis-From-Matlab-To-Python
Reads .fis file generated by matlab's anfis and returns it as simpful's fuzzy system.

Requires simpful library.
Requires product as AndMethod to work properly, which is not default in matlab (simpful doesn't work with min method).
Example usage in example.py.
Don't change anything in .fis file manually.
Handles generalized bell and gauss bell by default, you can add your own input function in place pointed in code.

May 2022