# grade = 0 to 100 inclusive
# grade<40 -> Fail
# if not failed and grade - x*5 < 3 then round up to x*5
# 84 -> 85
# 67 -> 67
# 29 -> 29

# Write code to automate rounding process
def gradingStudents(grades): 
    for i in range(len(grades)): 
        if grades[i] >= 38: 
            mod = grades[i]%5 
            if mod == 3 or mod == 4: 
                grades[i] = grades[i] + (5 - (grades[i]%5)) 
    return grades


