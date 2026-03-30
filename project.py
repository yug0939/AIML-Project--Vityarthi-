import datetime
import statistics
import matplotlib.pyplot as plt
import numpy as np

def calculate_grade_point(marks):
    if marks >= 90:
        return 10
    elif marks >= 80:
        return 9
    elif marks >= 70:
        return 8
    elif marks >= 60:
        return 7
    elif marks >= 50:
        return 6
    elif marks >= 40:
        return 5
    else:
        return 0


def main():
    print("Student Performance Analysis System\n")

    print("Run Date:", datetime.datetime.now().strftime("%Y-%m-%d"))

    n = int(input("Enter number of subjects: "))

    subjects = []
    marks_list = []
    class_avg_list = []
    grade_points = []

    for i in range(n):
        print(f"\nSubject {i+1}")
        subject_name = input("Enter subject name: ")

        marks = float(input("Enter your marks: "))
        class_avg = float(input("Enter class average marks: "))

        gp = calculate_grade_point(marks)

        subjects.append(subject_name)
        marks_list.append(marks)
        class_avg_list.append(class_avg)
        grade_points.append(gp)

        print(f"Grade Point for {subject_name}: {gp}")

        if marks >= 90:
            print("Feedback: Excellent performance. Keep doing what you are doing.")
        elif marks >= 80:
            print("Feedback: Good performance. With a little more effort, you can reach excellence.")
        elif marks >= 70:+-+
            print("Feedback: Decent performance. Focus on practicing more questions.")
        elif marks >= 60:
            print("Feedback: Average performance. Revise concepts and practice regularly.")
        elif marks >= 50:
            print("Feedback: Below average. You need to work harder and strengthen basics.")
        else:
            print("Feedback: Poor performance. Focus seriously on understanding concepts.")

        if marks > class_avg:
            print("Comparison: You are performing above class average.")
        elif marks == class_avg:
            print("Comparison: You are at par with class average.")
        else:
            print("Comparison: You are below class average. Focus more on this subject.")

    cgpa = sum(grade_points) / n
    student_avg = statistics.mean(marks_list)
    class_avg_total = statistics.mean(class_avg_list)

    print("\nRESULTS")
    print("---------------------------")
    print(f"Your CGPA: {round(cgpa, 2)}")
    print(f"Your Average Marks: {round(student_avg, 2)}")
    print(f"Class Average Marks: {round(class_avg_total, 2)}")

    if student_avg > class_avg_total:
        print("Performance: Above Average")
    elif student_avg == class_avg_total:
        print("Performance: Average")
    else:
        print("Performance: Below Average")

    if student_avg >= 85:
        prediction = "Excellent Performance Expected"
    elif student_avg >= 70:
        prediction = "Good Performance Expected"
    elif student_avg >= 50:
        prediction = "Average Performance Expected"
    else:
        prediction = "Needs Improvement"

    print(f"Predicted Performance Level: {prediction}")

    weak_subjects = []
    for i in range(len(subjects)):
        if marks_list[i] < class_avg_list[i]:
            weak_subjects.append(subjects[i])

    if weak_subjects:
        print("Subjects to Focus More On:", ", ".join(weak_subjects))
    else:
        print("Great! You are performing well in all subjects.")

    x = np.arange(len(subjects))
    width = 0.35

    plt.figure()

    bars1 = plt.bar(x - width/2, marks_list, width)
    bars2 = plt.bar(x + width/2, class_avg_list, width)

    plt.xticks(x, subjects, rotation=20)
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title("Your Marks vs Class Average")

    plt.ylim(0, 100)
    plt.yticks(range(0, 101, 10))

    plt.legend(["Your Marks", "Class Average"])

    for bar in bars1:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, f'{height}', ha='center', va='bottom')

    for bar in bars2:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, f'{height}', ha='center', va='bottom')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
