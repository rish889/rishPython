course = 'Python course for Beginners'
print(len(course))  # function
print(course.upper())  # method
print(course)

print(course.find('P'))
print(course.find('o'))
print(course.find('O'))
print(course.find('Beginner'))

print(course.replace('Beginners', 'Absolute Beginners'))
print(course.replace('beginners', 'Absolute Beginners'))
print(course.replace('P', 'J'))

print('Python' in course)
print('python' in course)

# 27
# PYTHON COURSE FOR BEGINNERS
# Python course for Beginners
# 0
# 4
# -1
# 18
# Python course for Absolute Beginners
# Python course for Beginners
# Jython course for Beginners
# True
# False