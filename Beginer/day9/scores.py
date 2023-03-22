
d_scores = {}
end = False
while not end:
    name = input("Whats ur name? \n")
    score = int(input("how many scores did u get? \n"))

    if score in range(91,101):
        d_scores[name] = "Outstanding"
    elif score in range(81,91):
        d_scores[name] = "Exceeds Expectations"
    elif score in range(71,81):
        d_scores[name] = "Acceptable"
    else: 
        d_scores[name] = "Fail"
    print(d_scores) 

