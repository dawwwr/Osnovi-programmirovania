student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10

print('Первый символ:', student[0])         #1
print('Последний символ:', student[-1])

print(student[:4])      #2
print(student[5:])

print(student.upper())     #3
print(student.lower())

print(student[0] + '.' + student[5] + '.')   #4

print(course[::-1])      #5

print('%s - %s: %d/%d (%.1f%%)' % (student, course, completed, total, completed / total * 100))     #6
print('{} - {}: {}/{} ({:.1f}%)'.format(student, course, completed, total, completed / total * 100))
print(f'{student} - {course}: {completed}/{total} ({completed / total * 100:.1f}%)')

symbol = "Я"        #7
print(symbol)
print(ord(symbol))
print(chr(ord(symbol)))
print(symbol.encode('utf-8'))
print(len(symbol.encode('utf-8')))

#student[0] = 'О' 8
#print(student)
