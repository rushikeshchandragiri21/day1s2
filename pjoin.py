import threading
from prettytable import PrettyTable

# Sample data for students and their performance
students_data = [
    ["PRN NO.", "Name", "Class", "Branch"],
    [101, "Aarav Sharma", "FY", "Computer Engineering"],
    [102, "Aditi Singh", "SY", "Information Technology"],
    [103, "Vivek Patel", "TY", "Electronics Engineering"],
    [104, "Sneha Krishnan", "FY", "Mechanical Engineering"],
    [105, "Rohan Gupta", "SY", "Civil Engineering"],
    [106, "Pooja Desai", "TY", "Electrical Engineering"],
    [107, "Nikhil Joshi", "FY", "Chemical Engineering"],
    [108, "Meera Nair", "SY", "Biotechnology"]
]

performance_data = [
    ["PRN NO.", "Attendance", "Grade"],
    [101, "90%", "A"],
    [102, "85%", "B"],
    [103, "92%", "A"],
    [104, "88%", "B"],
    [105, "95%", "A"],
    [106, "80%", "C"],
    [107, "75%", "D"],
    [108, "98%", "A"]
]

# Function to perform join operation for a range of rows
def parallel_join(result, start, end):
    for i in range(start, end):
        for j in range(1, len(students_data)):
            if students_data[j][0] == performance_data[i][0]:
                result.append([students_data[j][0], students_data[j][1], students_data[j][2], students_data[j][3], performance_data[i][1], performance_data[i][2]])

# Number of threads
num_threads = 4
result = []

# Lock for thread-safe appending to result
lock = threading.Lock()

# Split data range for each thread
chunk_size = len(performance_data) // num_threads
ranges = [(i * chunk_size, (i + 1) * chunk_size) for i in range(num_threads - 1)]
ranges.append(((num_threads - 1) * chunk_size, len(performance_data)))

# Create and start threads
threads = []
for start, end in ranges:
    thread = threading.Thread(target=parallel_join, args=(result, start, end))
    thread.start()3
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Display the result in a table format
students_table = PrettyTable(students_data[0])
for row in students_data[1:]:
    students_table.add_row(row)

performance_table = PrettyTable(performance_data[0])
for row in performance_data[1:]:
    performance_table.add_row(row)

result_table = PrettyTable(["PRN NO.", "Name", "Class", "Branch", "Attendance", "Grade"])
for row in sorted(result):  # Sort results by PRN NO. for readability
    result_table.add_row(row)

print("Students Table:")
print(students_table)
print("\nPerformance Table:")
print(performance_table)
print("\nJoin Result:")
print(result_table)
