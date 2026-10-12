student_grades = {
    "Elara": 86,
    "Kwame": 92,
    "Siobhan": 78,
    "Kai": 96,
    "Bella": 60
}

print(student_grades["Kwame"]) #92
print(student_grades.get("Aisha", "Not found")) #Not found

result = student_grades["Elara"]
print(result) # 85

print(student_grades.get ("Anna", "missing student")) #Error
print(student_grades["Bella"])