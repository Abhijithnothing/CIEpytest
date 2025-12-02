import pytest
def student_details(id,name,course,academic_year):
    result=(
        f"Student id: {id}\n"
        f"Student name: {name}\n"
        f"Student course: {course}\n"
        f"Academic year: {academic_year}\n"    )
    return result
    
if __name__=="__main__":
    id="101"
    name="ABhijith"
    course="BCA"
    academic_year="3"
    print(student_details(id,name,course,academic_year))    