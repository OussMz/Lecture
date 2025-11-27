from collections import defaultdict
student_records = []
stats = {"highest": None, "lowest": None, "average": None}
unique_grades= set()
grade_dist = defaultdict(int)

def data_entry(n):
    total = 0
    for i in range(n):
        name = input("Enter name: ")
        score = input("Enter score: ")
        while not score.isdigit():
            print("Invalid score. Please enter a numeric value.")
            score = input("Enter score: ")
        score = int(score)
        student_records.append((name, score))
        total += score
        if not stats["highest"] or score > stats["highest"]:
            stats["highest"] = score
        if not stats["lowest"] or score < stats["lowest"]:
            stats["lowest"] = score
        if score not in unique_grades:
            unique_grades.add(score)
    for name, score in student_records:
            grade_dist[score] += 1

    stats["average"] = total / n


def display_results():
    print("=== STUDENT RECORDS ===")
    index = 1
    for name, score in student_records:
        print(f"{index}.{name}: {score}")
        index += 1
    print("=== CLASS STATISTICS ===")
    print(f"Highest Score: {stats['highest']}")
    print(f"Lowest Score: {stats['lowest']}")
    print(f"Average Score: {stats['average']:.2f}")
    print("=== UNIQUE SCORES ===")
    print(unique_grades)
    print(f"Total unique scores: {len(unique_grades)}")
    print("=== GRADE DISTRIBUTION ===")
    for grade, count in grade_dist.items():
        print(f"score {grade}: {count} student(s)")
data_entry(6)
display_results()