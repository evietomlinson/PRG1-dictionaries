exam_results = {
    "steve": [99, 98, 95],
    "violet": [56, 53, 88],
    "aqil": [100, 100, 100],
    "Adam": [65, 76, 92]
}

print(exam_results["steve"]) # [99, 98, 95]
print(exam_results["steve"][0]) # 99 
print(len(exam_results["steve"])) # 3
print(98 in exam_results["steve"]) # True 
print("hello" in exam_results["steve"]) # False

print(exam_results["aqil"][1])
print(sum(exam_results["violet"]))

print(len(exam_results))