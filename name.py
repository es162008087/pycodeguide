# Álvaro Toriz
# python3
# name.py
# Some methods to transform basically names and concatenate them:
# title, upper, lower
# plus sign: "+" to conacatenate
# syntax for tab and new line

name = "ada lovelace"
print(name.title())
name = "Ada Lovelace"
print(name.upper())
print(name.lower())
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")
message = "Hello, " + full_name.title() + "!"
print(message)
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
favorite_language = 'python '
print("'"+favorite_language+"'")
favorite_language = favorite_language.rstrip()
print("'"+favorite_language+"'")
favorite_language = ' python '
favorite_language = favorite_language.rstrip()
print("'"+favorite_language+"'")
favorite_language = ' python '
favorite_language = favorite_language.lstrip()
print("'"+favorite_language+"'")
favorite_language = ' python '
favorite_language = favorite_language.strip()
print("'"+favorite_language+"'")

