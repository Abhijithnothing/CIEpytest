from student import student_details
def test_student_details():
    expected_output=(
    "Student id: 101\n"           
    "Student name: Abhijith\n"
    "Student course: BCA\n"
    "Academic year: 3\n"
    )
    assert student_details("101","Abhijith","BCA","3") == expected_output
