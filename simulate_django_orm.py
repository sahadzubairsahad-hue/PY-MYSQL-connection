import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",password="root",database="DjangoORM")
cur=conn.cursor()
# cur.execute("CREATE DATABASE DjangoORM")
# print("database created")
# cur.execute('''create table employee(
#             id int primary key auto_increment,
#             name varchar(20),
#             designation varchar(30),
#             salary decimal(10,2)
#     )''')
# print("table created")

# conn.close()

import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",password="root",database="DjangoORM")
cur=conn.cursor()

# cur.execute("create database DjangoORM")
# print("database created")

# cur.execute('''create table employee(
#             id int primary key  auto_increment,
#             name   varchar(20),
#             designation    varchar(20),
#             salary      decimal(10,2)
#         )''')

# print("Table created")

class Employee:
    def create(self,*args,**kwargs):
        keys=""
        placeholder=""
        for key in kwargs.keys():
            if keys!="":
                keys+=','
                placeholder+=','
            keys+=key
            placeholder+="%s"
        value=tuple(kwargs.values())
        query=f"insert into employee({keys}) values({placeholder})"
        cur.execute(query,value)
        conn.commit()
        print("Employee created successfully!")

    def list(self,*args,**kwargs):
        cur.execute("select * from employee")
        # for emp in cur:
        #     print(emp)
        print(cur.fetchall())
    def retrieve(self,*args,**kwargs):
        for key in kwargs:
            cur.execute(f"select * from employee where {key}={kwargs.get(key)}")
            print(cur.fetchall())

    def update(self,*args,**kwargs):
        for key in kwargs:
            cur.execute(f"update employee set {key}='{kwargs.get(key)}' where id={args[0]}")
            conn.commit()
    def delete(self,*args,**kwargs):
        cur.execute(f"delete from employee where id={args[0]}")
        conn.commit()
    def filter(self,*args,**kwargs):
        for key in kwargs:
            cur.execute(f"select * from employee where {key}='{kwargs.get(key)}'")
            print(cur.fetchall())


employee=Employee()

while True:
    print("1. Create Employee")
    print("2. List all Employee")
    print("3. Employee detail view")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. filter Employee")
    print("7. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name=input("Enter the employee name : ")
        desig=input("Enter the designation : ")
        salary=float(input("Enter the salary amount : "))
        employee.create(name=name,designation=desig,salary=salary)

    elif choice == 2:
        employee.list()

    elif choice == 3:
        id=int(input("enter employee id :"))
        employee.retrieve(id=id)

    elif choice == 4:
        id=int(input("enter the id:"))
        print("1.name update")
        print("2.designation update")
        print("3.salary update")
        choice=int(input("enter your choice:"))

        if choice==1:
            new_name=input("enter new name:")
            employee.update(id,name=new_name)
        elif choice==2:
            desig=input("enter the new designation:")
            employee.update(id,designation=desig)
        elif choice==3:
            new_salary=float(input("enter the new salary:"))    
            employee.update(id,salary=new_salary)
        else:
            print("invalid choice")
        
    elif choice == 5:
        id=int(input("enter the id:"))
        employee.delete(id)

    elif choice == 6:
        print("1.filter by id")
        print("2.filter by name")
        print("3.filter by designation")
        print("4.filter by salary")
        choice=int(input("enter the choice:"))

        if choice==1:
            id=int(input("enter the id"))
            employee.filter(id=id)
        if choice==2:
            name=input("enter the name")
            employee.filter(name=name)
        if choice==3:
            design=input("enter the designation")
            employee.filter(designation=design)
        if choice==4:
            sal=int(input("enter the salary"))
            employee.filter(salary=sal)
    elif choice == 7:
        print("thank you")
        break
    else:
        print("Invalid Choice")










conn.close()
