
from info2000_package import info_logger
from info2000_package import student_details

import argparse

def get_user_info():
    name = input("Enter name: ")
    major = input("Major: ")
    student = student_details.Student(name,major)
    return student

def main():
    # create the parser object
    parser = argparse.ArgumentParser(description="Gets information about students and saves it to file")
    # add arguments to parser
    parser.add_argument('filename')
    # parser.add_argument('--filename','-f', type=str, help="destination file", default="student_log.txt", required=True)
    parser.add_argument('--times','-t', type=int, help = "how many students you want to capture", required=True)

    #parse the arguments that the user enters

    args = parser.parse_args()

    #we have access to the arguments through this pobject
    # args.filename
    # args.times



    # do the majority of work here
    for _ in range(args.times):
            my_student = get_user_info()
            #print(f"Hey {my_student.name} I hope you're enjoying your {my_student.major} major")              
            my_logger = info_logger.Logger(args.filename)
            my_logger.LogRow(f"{my_student.name} {my_student.major}") 

if __name__ == '__main__':
    main()