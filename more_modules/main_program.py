# import info_logger
# import student_details

from info2000_package import info_logger
from info2000_package import student_details

# from info2000_package import info_logger, student_details

import sys

# print ("In the main program" + __name__)


def get_user_info():
    name = input("Enter name: ")
    major = input("Major: ")
    student = student_details.Student(name,major)
    return student

def main():
    # do all the work here
    if len(sys.argv) == 3:
        times = int(sys.argv[1])   

        for _ in range(times):
            my_student = get_user_info()
            #print(f"Hey {my_student.name} I hope you're enjoying your {my_student.major} major")              
            my_logger = info_logger.Logger(sys.argv[2])
            my_logger.LogRow(f"{my_student.name} {my_student.major}") 
    else:
        print(f"usage: {sys.argv[0]} times file_to_log")


# define the logger object


if __name__ == '__main__': # called from the command line as the main program

    main()
    # for arg in  sys.argv: # gives you access to commandline args. it's a list
    #     print(arg)

   



