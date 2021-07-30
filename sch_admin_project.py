import csv
def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact Number", "Email ID"])

        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True
    student_num = 1

    while(condition):
        student_info = input("Enter student informaton in the following format (Name, Age, Contact_Number, Email_ID): ".format(student_num))
        print("Entered information: " + student_info)

        #split
        student_info_list = student_info.split(' ')
        print("Entered split up information is: " + str(student_info_list))

        write_into_csv(student_info_list)

        condition_check = input("Enter (yes/no) if you want to enter information for another student: ")
        if condition_check == "yes":
            condition = True
            student_num = student_num + 1
        elif condition_check == "no":
            condition = False
