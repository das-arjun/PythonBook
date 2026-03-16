family = ["Ketaki", "Suman", "Mihika", "Madhu", "Ashish"]  # This is a list.
rainbow = ("red","orange","yellow","green","blue(azure)","indigo(blue)","violet(purple)")  # This is a tuple.
print(family[1])  # Prints 'Suman'
family.append("Arjun")  # Adds me
print(family)  # Prints the modified list
print(family[2:4])  # Prints 'Mihika' to 'Ashish'
print(rainbow)  # Prints the colours of the rainbow.
if False:
 rainbow.append("magenta")
else:
    print("You can't \"append\" to a tuple!")