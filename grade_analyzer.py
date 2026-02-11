#Student Grade Analyzer
# 1. Ask use for grades
# 2. Store grades in a list
# 3. Calculate average grade
# 4. Find highest and lowest grade
# 5. Print results

def get_grades():
    grades = []
    while True:
        grade = input("Enter a grade (or 'done' to finish): ")

        if grade.lower() == "done":
            break

        try:
            grade = float(grade)
            grades.append(grade)
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

    return grades


def calculate_average(grades):
    if len(grades) == 0:
        return None
    return sum(grades) / len(grades)


def get_highest_lowest(grades):
    if len(grades) == 0:
        return None, None
    return max(grades), min(grades)


def main():
    grades = get_grades()

    average = calculate_average(grades)
    highest, lowest = get_highest_lowest(grades)

    print("\n--- Grade Summary ---")
    print(f"Grades: {grades}")
    print(f"Number of grades: {len(grades)}")

    if average is None:
        print("Average grade: N/A (no grades entered)")
        print("Highest grade: N/A")
        print("Lowest grade: N/A")
    else:
        print(f"Average grade: {average:.2f}")
        print(f"Highest grade: {highest}")
        print(f"Lowest grade: {lowest}")


if __name__ == "__main__":
    main()


