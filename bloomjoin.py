def bloom_join(student_table, course_table):
    # Create sets for student and course IDs
    student_ids = set()
    course_ids = set()

    # Set student IDs in the student set
    for row in student_table:
        student_id, _, _ = row.split(',')
        student_ids.add(int(student_id))

    # Set course IDs in the course set
    for row in course_table:
        course_id, _ = row.split(',')
        course_ids.add(int(course_id))

    # Perform join
    result = []
    for student_row in student_table:
        student_id, name, age = student_row.split(',')
        student_id = int(student_id)
        if student_id in student_ids and student_id in course_ids:
            for course_row in course_table:
                course_id, course_name = course_row.split(',')
                course_id = int(course_id)
                if student_id == course_id:
                    result.append(','.join([str(student_id), name.strip(), age.strip(), course_name.strip()]))
                    break

    return result

if __name__ == "__main__":
    student_table = [
        "1, Vijay, 20",
        "2, Ajay, 21",
        "3, Aman, 22",
        "4, Dilip, 23"]

    course_table = [
        "1, Math",
        "2, Science",
        "3, History",
        "4, English"]

    # Perform Bloom join
    result = bloom_join(student_table, course_table)

    # Print result
    print("Student ID, Name, Age, Course Name")
    for row in result:
        print(row)
