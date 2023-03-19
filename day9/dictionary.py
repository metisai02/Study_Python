programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                           "Function": "A piece of code that you can easily call over and over again."}

print(programming_dictionary["Bug"])

for key, value in programming_dictionary.items():
    print(key,value)

programming_dictionary[123] = "dcmm"

print(programming_dictionary[123])
