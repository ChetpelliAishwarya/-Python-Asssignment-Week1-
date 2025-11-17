# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 16:23:24 2025

@author: Hi
"""

 
#Exercise 3 : Student Marks Processor 

import numpy as np

# Grade assignment function
# -----------------------------
def assign_grade(mark):
    if mark >= 70:
        return 'A'
    elif mark >= 60:
        return 'B'
    elif mark >= 50:
        return 'C'
    elif mark >= 40:
        return 'D'
    else:
        return 'F'


# Main program
# -----------------------------
def process_student_marks(input_file, output_file):
    try:
        # 1. Read student data from file
        data = []
        with open(input_file, 'r') as f:
            for line in f:
                try:
                    reg, exam, cw = line.strip().split(',')
                    data.append((reg, float(exam), float(cw)))
                except:
                    print(f"Skipping invalid line: {line.strip()}")
        
        if not data:
            print("No valid data found in input file.")
            return

        # Convert to structured NumPy array
        student_dtype = np.dtype([
            ('reg', 'U20'),
            ('exam', 'f4'),
            ('cw', 'f4'),
            ('overall', 'f4'),
            ('grade', 'U2')
        ])

        structured_data = np.zeros(len(data), dtype=student_dtype)

        # 2. Compute overall marks (70% exam, 30% coursework)
        for i, (reg, exam, cw) in enumerate(data):
            overall = exam * 0.7 + cw * 0.3
            grade = assign_grade(overall)

            structured_data[i] = (reg, exam, cw, overall, grade)

        # 5. Sort students by overall mark (descending)
        sorted_students = np.sort(structured_data, order='overall')[::-1]

        # 6. Write results to output file
        with open(output_file, 'w') as f:
            f.write("Reg_No,Exam,Coursework,Overall,Grade\n")
            for s in sorted_students:
                f.write(f"{s['reg']},{s['exam']},{s['cw']},{s['overall']:.2f},{s['grade']}\n")

        print("\nResults saved to:", output_file)

        # 7. Display grade statistics
        print("\nGrade Statistics:")
        grades, counts = np.unique(sorted_students['grade'], return_counts=True)
        for g, c in zip(grades, counts):
            print(f"Grade {g}: {c}")

    except FileNotFoundError:
        print("Input file not found. Please check the filename.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")


# -----------------------------
# Run the program
# -----------------------------
input_file = r'C:\Users\Hi\Downloads\student_input.txt'     # Change file name if needed
output_file = r"C:\Users\Hi\Downloads\students_output.txt"

process_student_marks(input_file, output_file)

