# ==========================================
# Codomax AI/ML Internship - Day 7
# Topic: File Handling in Python
# Author: Akash Kumar Jha
# ==========================================

FILE_NAME = "students.txt"

print("=" * 60)
print("         FILE HANDLING - DAY 7")
print("=" * 60)

# Write student records
with open(FILE_NAME, "w") as file:
    file.write("Akash Kumar Jha,AIML,85\n")
    file.write("Rahul Sharma,CSE,78\n")
    file.write("Priya Singh,IT,91\n")

print("\nStudent records saved successfully.")

# Read records
print("\nReading Student Records:\n")

with open(FILE_NAME, "r") as file:
    records = file.readlines()

for record in records:
    print(record.strip())

# Append new record
with open(FILE_NAME, "a") as file:
    file.write("Neha Verma,ECE,88\n")

print("\nNew student record added.")

# Display updated records
print("\nUpdated Student Records:\n")

with open(FILE_NAME, "r") as file:
    updated_records = file.readlines()

for record in updated_records:
    print(record.strip())

print("\nTotal Student Records:", len(updated_records))

print("\nProgram Executed Successfully ✅")
print("=" * 60)
