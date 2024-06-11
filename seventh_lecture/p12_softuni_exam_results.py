command = input()
exam_results = {"Submissions": {}}
while command != "exam finished":
    if "banned" in command.split("-"):
        del exam_results[name]
    else:
        command = command.split("-")
        name = command[0]
        language = command[1]
        points = command[2]
        exam_results["Submissions"][language] = exam_results["Submissions"].get(language, 0)
        exam_results["Submissions"][language] += 1
        exam_results[name] = exam_results.get(name, {})
        exam_results[name][language] = exam_results[name].get(language, points)
        if exam_results[name][language] < points:
            exam_results[name][language] = points

    command = input()

print("Results:")
for user in exam_results:
    if user != "Submissions":
        for k, v in exam_results[user].items():
            print(f"{user} | {v}")
print("Submissions:")
for lang, count in exam_results["Submissions"].items():
    print(f"{lang} - {count}")