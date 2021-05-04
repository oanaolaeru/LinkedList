import os
import shutil


class Students:
    def __init__(self, name, f_name, id_num, math_grade, programming_grade, year, prep):
        self.name = name
        self.f_name = f_name
        self.id_num = id_num
        self.math_grade = math_grade
        self.programming_grade = programming_grade
        self.year = year
        self.prep = prep

    def __str__(self):
        return str(self.name + "," + self.f_name + "," + self.id_num + "," + self.math_grade + "," +
                   self.programming_grade + "," + self.year + self.prep)


class Node:
    def __init__(self, data=None, next=0):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def add_node_end(self, data):
        iter = self.head

        while iter.next:
            iter = iter.next
        iter.next = Node(data)

    def add_head(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp

    def count_nodes(self):
        counter = 1
        iter = self.head

        while iter.next:
            iter += 1
            iter = iter.next

        return counter

    def print_list(self):
        iter = self.head

        while iter:
            print(iter)
            iter = iter.next

    def find_in_list(self, data):
        iter = self.head

        while iter:
            if iter.data == data:
                return iter
            iter = iter.next

        return None

    def remove_node(self, data):
        iter = self.head

        # if we need to remove the first Node
        if iter.data == data:
            self.head = self.head.next

        # find the object to remove and remove it: if found&deleted return 1 else 0
        while iter:
            if iter.next and iter.next.data == data:
                iter.next = iter.next.next
                return 1

            iter = iter.next

        return 0

    def remove_node_by_id(self):
        id_to_remove = input("Enter id number you want to remove: ")
        iter = self.head

        # if the id number we need to remove the first Node
        if iter.data.id_num == id_to_remove:
            self.head = self.head.next
        # if the list from which we want to remove is empty
        elif self.head is None:
            raise Exception("The list is empty")
        # find the object to remove and remove it: if found&deleted return 1 else 0
        while iter:
            if iter.next and iter.next.data.id_num == id_to_remove:
                iter.next = iter.next.next
                print("Student removed")
                return

            iter = iter.next

        print("Student not removed")

    def __str__(self):
        # initialize
        to_print = ""
        iter = self.head

        # add data to to_print
        while iter:
            to_print = to_print + str(iter.data) + "\n"
            iter = iter.next

        # return string representing Linked List
        return to_print


# this function can be called only once at the startup
def load_csv_file(ll, file_path):
    if os.path.isfile(file_path):
        line_count = 0
        with open(file_path, 'r') as fd:
            print("Loading file...")
            # Read the first student
            line = fd.readline()
            line = line.strip()
            line = line.split(",")
            line_count += 1

            # Create new LinkedList
            ll = LinkedList(Students(line[0], line[1], line[2], line[3], line[4], line[5], line[6]))

            # Read line by line and add all students
            for line in fd:
                line = line.strip()
                line = line.split(",")
                ll.add_head(Students(line[0], line[1], line[2], line[3], line[4], line[5], line[6]))

            print("Done")
            return ll
    else:
        print("Error!\nFile do not exist - Student LinkedList not created")


def load_csv_file_to_existing_ll(ll):
    file_path = input("Enter file name\n")

    if ll is None:
        load_csv_file(ll, file_path)
        return

    if os.path.isfile(file_path):
        with open(file_path, 'r') as fd:
            print("Loading file...")

            # Read line by line and add all students
            for line in fd:
                line = line.strip()
                line = line.split(",")
                ll.add_head(Students(line[0], line[1], line[2], line[3], line[4], line[5], line[6]))

            print("Done")
            return ll
    else:
        print("Error!\nFile do not exist - Student LinkedList not created")


def export_to_csv(ll):

    # Check if the list is empty
    if ll is None:
        print("The list is empty")
        return

    fd = open("Students_new.csv", 'w')
    # Set iterator
    iter_ll = ll.head

    # Iterate all the list

    while iter_ll:
        fd.write(iter_ll.data.name + "," + iter_ll.data.f_name + "," + iter_ll.data.id_num + "," + iter_ll.data.year +
                 "," + iter_ll.data.math_grade + "," + iter_ll.data.programming_grade + "," + iter_ll.data.prep + "\n")
        iter_ll = iter_ll.next

    fd.close()
    return


def create_student():
    sname = input("Enter name\n")
    if len(sname) == 0:
        print("Wrong input")
        return
    sf_name = input("Enter family name\n")
    if len(sname) == 0:
        print("Wrong input")
        return
    sid_num = input("Enter id number\n")
    if len(sid_num) != 9 or sid_num.isdigit():
        print("Wrong input")
        return

    try:
        smath_grade = int(input("Enter math grade\n"))
    except:
        print("Wrong input!")
        return
    if not 0 < smath_grade > 100:
        print("Wrong input!")
        return

    try:
        sprogramming_grade = int(input("Enter programming grade\n"))
    except:
        print("Wrong input!")
        return
    if not 0 < sprogramming_grade > 100:
        print("Wrong input!")
        return

    try:
        syear = int(input("Enter year\n"))

    except:
        print("Wrong input!")
        return
    if not (syear == 2016 or syear == 2017 or syear == 2018 or syear == 2019 or syear == 2020):
        print("Wrong value")
        return

    sprep = input("Enter 1 if the student did prep or 0 for if not\n")

    return Students(sname, sf_name, sid_num, smath_grade, sprogramming_grade, syear, sprep)


def create_parent_dir():
    path_to_reports = r"\reports\\"
    try:
        os.mkdir("reports")
    except:
        pass


def remove_all_data():
    shutil.rmtree("reports")
    create_parent_dir()


def all_students_report(ll, folder_path):
    with open(folder_path + "all_students.txt", 'w') as fd:
        ll_iter = ll.head
        while ll_iter:
            fd.write(ll_iter.data.name + "," + ll_iter.data.f_name + "," + ll_iter.data.id_num + "," +
                    ll_iter.data.year + "," + ll_iter.data.math_grade + "," + ll_iter.data.programming_grade + ","
                     + ll_iter.data.prep + "\n")
            ll_iter = ll_iter.next


def years_reports(ll, folder_path):

    fd2016 = open(folder_path + "Students2016.txt", 'w')
    fd2017 = open(folder_path + "Students2017.txt", 'w')
    fd2018 = open(folder_path + "Students2018.txt", 'w')
    fd2019 = open(folder_path + "Students2019.txt", 'w')
    fd2020 = open(folder_path + "Students2020.txt", 'w')

    ll_iter = ll.head

    while ll_iter:
        count2016 = 0
        count2017 = 0
        count2018 = 0
        count2019 = 0
        count2020 = 0
        math_g = int(ll_iter.data.math_grade)
        programming_g = int(ll_iter.data.programming_grade)
        avg = (math_g + programming_g) / 2

        to_write = ll_iter.data.name + "," + ll_iter.data.f_name + "," + ll_iter.data.id_num + "," + ll_iter.data.year +"," + ll_iter.data.math_grade + "," + ll_iter.data.programming_grade + "," + ll_iter.data.prep + "\n"

        if ll_iter.data.year == "2016":
            count2016 += 1
            fd2016.write(to_write)

        elif ll_iter.data.year == "2017":
            count2017 += 1
            fd2017.write(to_write)
        elif ll_iter.data.year == "2018":
            count2018 += 1
            fd2018.write(to_write)
        elif ll_iter.data.year == "2019":
            count2019 += 1
            fd2019.write(to_write)
        elif ll_iter.data.year == "2020":
            count2020 += 1
            fd2020.write(to_write)

        ll_iter = ll_iter.next

    fd2016.close()
    fd2017.close()
    fd2018.close()
    fd2019.close()
    fd2020.close()


def excellent_students_reports(ll, folder_path):

    with open(folder_path + "Excellent_students_report.txt", 'w') as fd:
        ll_iter = ll.head

        while ll_iter:
            math_g = int(ll_iter.data.math_grade)
            programming_g = int(ll_iter.data.programming_grade)
            avg = (math_g + programming_g) / 2
            if programming_g >= 90 and avg > 85:
                to_write = ll_iter.data.name + "," + ll_iter.data.f_name + "," + str(avg) + "\n"
                fd.write(to_write)

            ll_iter = ll_iter.next


def average_students_reports(ll, folder_path):
    with open(folder_path + "Average_students_report.txt", 'w') as fd:
        ll_iter = ll.head

        while ll_iter:
            math_g = int(ll_iter.data.math_grade)
            programming_g = int(ll_iter.data.programming_grade)
            avg = (math_g + programming_g) / 2
            if avg <= 70 and math_g < 60 and programming_g < 70:

                to_write = ll_iter.data.name + "," + ll_iter.data.f_name + "," + str(avg) + "\n"
                fd.write(to_write)
            ll_iter = ll_iter.next


def report_menu(ll, folder_path):
    user_choice = input("Reports menu:\n1)"
                        " All students report\n2)"
                        " Report by year\n3)"
                        " Excellent student report\n4)"
                        " Average students report\n")

    if user_choice == "1":
        all_students_report(ll, folder_path)
    if user_choice == "2":
        years_reports(ll, folder_path)
    if user_choice == "3":
        excellent_students_reports(ll, folder_path)
    if user_choice == "4":
        average_students_reports(ll, folder_path)


create_parent_dir()
studentLinkedList = None
path_to_reports = r"reports\\"

# Load student from file
"""user_input = input("Load students from csv?\ny\\n")
if user_input == "y" or user_input == "Y":
    file_path = input("Enter your file name or path: \nThe default student file is students.csv\n")
    studentLinkedList = load_csv_file(studentLinkedList, file_path)
"""
studentLinkedList = load_csv_file(studentLinkedList, "students.csv")
# Welcome
print("Welcome to INT College!")

while True:
    user_input = input("Menu:\n1)"
                       " Add student\n2)"
                       " Delete student by id number\n3)"
                       " Delete all students\n4)"
                       " Delete all data\n5)"
                       " Report menu\n6)"
                       " Import from csv\n7)"
                       " Export from csv\n8)"
                       " Print all data\n9)"
                       " Exit\n")

    # Add student
    if user_input == "1":
        new_student = create_student()
        if new_student is not None:
            if studentLinkedList is None:
                studentLinkedList = LinkedList(new_student)
            else:
                studentLinkedList.add_node_end(new_student)

    # Delete student
    elif user_input == "2":
        studentLinkedList.remove_node_by_id()

    # Delete all information
    elif user_input == "3":
        studentLinkedList = None
        print("All students from the list removed")

    # Delete all students log
    elif user_input == "4":
        remove_all_data()

    # Report menu
    elif user_input == "5":
        report_menu(studentLinkedList, path_to_reports)

    # Import from csv
    elif user_input == "6":
        studentLinkedList = None
        load_csv_file_to_existing_ll(studentLinkedList)

    # Export from csv
    elif user_input == "7":
        export_to_csv(studentLinkedList)

    # Print all students
    elif user_input == "8":
        if studentLinkedList is not None:
            studentLinkedList.print_list()

    # Exit
    elif user_input == "9":
        user_input = input("Do you want to backup your data?\n")
        if user_input == "y" or user_input == "Y":
            export_to_csv(studentLinkedList)
        print("Goodbye")