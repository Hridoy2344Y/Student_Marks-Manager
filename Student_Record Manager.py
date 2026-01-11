import os
import json
task=input("Type: \n (A)-> Add \n (S)-> Search \n (D)-> Delelte \n (U)-> Update \n : ").upper()
if os.path.exists("E:\\Incomplete Projects\\Student Marks Manager"):
    pass
else:
    os.mkdir("E:\\Incomplete Projects\\Student Marks Manager")
match task:
    case "A":
            try:
              with open("E:\\Incomplete Projects\\Student Marks Manager\\Marks.json","r") as f:
                   x=json.load(f)
            except FileNotFoundError:
                with open("E:\\Incomplete Projects\\Student Marks Manager\\Marks.json","w") as f:
                     pass
            except json.JSONDecodeError:
                    x={}
            try:
                with open("E:\\Incomplete Projects\\Student Marks Manager\\Marks.json","r") as f:
                 x=json.load(f)
            except json.JSONDecodeError:
                    x={}
            try:
             roll_no=int(input("Enter Roll No. : "))
             if str(roll_no) in x:
                print("This Roll.No already Exist!!")
                exit()
             marks=int(input("Enter Marks: "))
            except ValueError:
                print("Give Proper Values(Numbers)")
                exit()
            x[str(roll_no)]=str(marks)
            with open("E:\\Incomplete Projects\\Student Marks Manager\\Marks.json","w") as m:
                 save=json.dump(x,m)
    case "S":
            try:
                with open("E:\\Incomplete Projects\\Student Marks Manager\\Marks.json","r") as f:
                    x=json.load(f)
            except FileNotFoundError:
                print("File Doesn't Exist\n You can't Search!! ")
                exit()
            try:
                roll_no=int(input("Enter Roll NO. : "))
            except ValueError :
                print("Give Valid Data(Number)")
                exit()
            if str(roll_no) in x:
                print(x[str(roll_no)])
            else:
                print("This Roll No. Doesn't Exist!!")
    case "D":
            try:
                with open("E:\\Incomplete Projects\\Student Marks Manager\\Marks.json","r") as m:
                    x=json.load(m)
            except FileNotFoundError:
                print("File doesn't Exist\n First Create a File!")
                exit()
            try:
                roll_no=int(input("Enter Roll NO. : "))
            except ValueError :
                print("Give Valid Data(Number)")
                exit()
            if str(roll_no) in x:
                del x[str(roll_no)]
                print(f"Roll No.{roll_no} Deleted!")
            else:
                print("This Roll NO. Doesn't Exist!!")
            with open("E:\\Incomplete Projects\\Student Marks Manager\\Marks.json","w") as m:
                json.dump(x,m)#Here was my main bug, I should have dumped like(x,m) but i did was (roll_no,m)-Which erased all data from file and saved the only Roll_no Given
    case "U":
            try:
                with open("E:\\Incomplete Projects\\Student Marks Manager\\Marks.json","r") as m:
                    x=json.load(m)
            except FileNotFoundError:
                print("File doesn't Exist\n First Make some new Contacts then only it could be Updated")
                exit()
            try:
                roll_no=int(input("Enter Roll NO. : "))
            except ValueError :
                print("Give Valid Data(Number)")
                exit()
            if str(roll_no) in x:
                old_mark=x[str(roll_no)]
                del x[str(roll_no)]
            else:
                print("This Roll.No Doesn't Exist!")
                exit()
            try:
                new_mark=int(input("Enter New Mark: "))
            except ValueError:
                print("Give Valid Data(Number)")
                exit()
            x[str(roll_no)]=str(new_mark)
            with open("E:\\Incomplete Projects\\Student Marks Manager\\Marks.json","w") as m:
                json.dump(x,m)
                print(f"Now its: Roll No. {roll_no}: Marks {new_mark} ")
    case _:
        print("Select from the Menu given above!")