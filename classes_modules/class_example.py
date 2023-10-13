
import student_info 
import info_logger


#internal variable __main__ == '__main__'
#otherwise name of the module

def get_user_info():
    
    name = input("Enter name: ")
    major = input("Major: ")
    student = student_info.Student(name,major)
    return student

# define the logger object
my_logger = info_logger.Logger('student_data.txt')

for _ in range(5):
    my_student = get_user_info()
    #print(f"Hey {my_student.name} I hope you're enjoying your {my_student.major} major")  
    my_logger.LogRow(f"{my_student.name} {my_student.major}") 
