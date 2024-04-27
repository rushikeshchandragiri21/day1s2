#include <iostream>
#include <vector>
#include <sstream>
#include <bitset>
#include <unordered_map>

using namespace std;

vector<string> bloomJoin(vector<string> &studentTable, vector<string> &courseTable)
{
    // Create bitsets for student and course IDs
    bitset<10> studentBits;
    bitset<10> courseBits;

    // Set bits for student IDs in the student bitset
    for (auto &row : studentTable)
    {
        stringstream ss(row);
        string studentId;
        getline(ss, studentId, ',');
        int id = stoi(studentId);
        studentBits.set(id);
    }
    cout<<studentBits<<endl;

    // Set bits for course IDs in the course bitset
    for (auto &row : courseTable)
    {
        stringstream ss(row);
        string studentId;
        getline(ss, studentId, ',');
        int id = stoi(studentId);
        courseBits.set(id);
    }

    // Perform join
    vector<string> result;
    for (auto &row : studentTable)
    {
        stringstream ss(row);
        string studentId, name, age;
        getline(ss, studentId, ',');
        getline(ss, name, ',');
        getline(ss, age, ',');

        int id = stoi(studentId);
        if (studentBits.test(id) && courseBits.test(id))
        {
            for (auto &courseRow : courseTable)
            {
                stringstream css(courseRow);
                string courseId, courseName;
                getline(css, courseId, ',');
                if (id == stoi(courseId))
                {
                    getline(css, courseName, ',');
                    result.push_back(studentId + "," + name + "," + age + "," + courseName);
                    break;
                }
            }
        }
    }

    return result;
}

int main()
{

    vector<string> studentTable = {
        "1, Vijay, 20",
        "2, Ajay, 21",
        "3, Aman, 22",
        "4, Dilip, 23"};

    vector<string> courseTable = {
        "1, Math",
        "2, Science",
        "3, History",
        "4, English"};

    // Perform Bloom join
    vector<string> result = bloomJoin(studentTable, courseTable);

    // Print result
    cout << "Student ID, Name, Age, Course Name" << endl;
    for (auto &row : result)
    {
        cout << row << endl;
    }

    return 0;
}
