import mysql.connector as c
con = c.connect(host = 'localhost',
                user = 'root',
                password = 'Saud12345',
                database = 'bank_management')

cursor = con.cursor()

print("Welcome to the Bank Management system\n")
while True:

    print("Press 1 ---> Open bank account")
    print("Press 2 ---> Cash deposit")
    print("Press 3 ---> Cash withdrawl")
    print("Press 4 ---> Account details")
    print("Press 5 ---> Account close")
    print("Press 0 ---> Exit ")
    option = int(input("Enter option "))

    if option == 1:
        name = input("Enter your name ")
        account_no = input("Enter your account no ")
        age =  input("Enter your age ")
        mobile = int(input("Enter your mobile number "))
        city = input("Enter city name ")

        query1 = "insert into account values ('{}','{}','{}',{},'{}','{}')".format(name,account_no,age,mobile,city,0)
        cursor.execute(query1)
        con.commit()
        print("Account created successfully")

    elif option == 2:

        acntno = int(input("Enter your account no "))
        deposit = int(input("Enter amount to be deposited:"))
        getbalanceQuery = "SELECT balance FROM account WHERE account_no ='{}'".format(acntno)
        cursor.execute(getbalanceQuery)
        balance = list(cursor.fetchone()).pop()
        query2 = "UPDATE account SET balance = {} WHERE account_no ='{}'".format(deposit + balance, acntno)
        cursor.execute(query2)
        print("Rs.",deposit,"has been deposited successfully in account no:",acntno)
        con.commit()

    elif option == 3:

        acntno = int(input("Enter your account no "))
        withdraw = int(input("Enter amount to be withdraw "))
        getbalanceQuery ="SELECT balance FROM account WHERE account_no = '{}'".format(acntno)
        cursor.execute(getbalanceQuery)
        balance = list(cursor.fetchone()).pop()

        if balance < withdraw:
            print("Can't withdraw money.Insufficient balance!")
        else:
             query3 = "UPDATE account SET balance = {} WHERE account_no = '{}'".format(balance - withdraw, acntno)
             cursor.execute(query3)
             print("Rs.",withdraw,"has been withdrawn successfully from account no:",acntno)
             con.commit()

    elif option == 4:

          acntno = int(input("Enter your account number"))
          query4 = "SELECT * FROM account WHERE account_no ='{}'".format(acntno)
          cursor.execute(query4)
          data = cursor.fetchone()
          if data is None:
              print("bank account not found")
          print(data)
          con.commit()

    elif option == 5:

         acntno = int(input("Enter your account number"))
         query5 = "DELETE FROM account WHERE account_no ='{}'".format(acntno)
         cursor.execute(query5)
         print("your account has been successfully deleted.")
         con.commit()

    else:
         print("Thank you for using our service.")
         break
