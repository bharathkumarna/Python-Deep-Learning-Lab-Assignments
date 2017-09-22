class Person:
    def __init__(self,name,email):
        self.name = name
        self.email = email
    def display(self):
        print("Name: ", self.name)
        print("Email: ", self.email)

class Student(Person):
    StudentCount = 0
    def __init__(self,name,email,student_id):
        Person.__init__(self,name,email)
        self.student_id = student_id
        Student.StudentCount +=1
    def displayCount(self):
        print("Total Number of Students:", Student.StudentCount)
    def display(self):
        print("Student Details:")
        Person.display(self)
        print("Student Id: ",self.student_id)

class Librarian(Person):
    StudentCount = 0
    def __init__(self,name,email,employee_id):
        super().__init__(name,email)
        self.employee_id = employee_id
    def display(self):
        print("Employee Details:")
        Person.display(self)
        print("Employee Id: ",self.employee_id)

class Book():
    def __init__(self,book_name,author,book_id):
        self.book_name = book_name
        self.author = author
        self.book_id = book_id
    def display(self):
        print("Book Details")
        print("Book_Name: ", self.book_name)
        print("Author: ", self.author)
        print("Book_ID: ", self.book_id)

class Borrow_Book(Student,Book):
    def __init__(self,name,email,student_id,book_name,author,book_id):
        Student.__init__(self,name,email,student_id)
        Book.__init__(self,book_name,author,book_id)
    def display(self):
        print("Borrowed Book Details:")
        Student.display(self)
        Book.display(self)

Records = []
Records.append(Student('Sneha','xyz@gmail.com',123))
Records.append(Librarian('Bharath','xyz@gmail.com',789))
Records.append(Book('davinci code','leo',123456))
Records.append(Borrow_Book('Sibi','pqr@gmail.com',456,'wings of fire','kalam',67890))

for obj, item in enumerate(Records):
    item.display()
    print("\n")
    if obj == len(Records)-1:
        item.displayCount()