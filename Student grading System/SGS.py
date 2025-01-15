from prettytable import PrettyTable
def main():
    # here i am written the basic code for printing hello world msg and taking the name of all the stu
    #student whom we need to create the marksit....
    print("\n Enter Your Good Name: \n") 
    while True:
          name=input().title().split()
          name=' '.join(name)
          if check(name):
                    print(f'''Welcom You {name} ! In This Greading Software :\n ''')
                    break
          else:
               print("Enter Valid Name :\n ")

    l=["Math","hindi","english","science","Art","computer"]
    name_list=[]
    all_data=[]

    # taking student name from the teacher from
    print("Enter All Student's Name :\n")
    print("Note : If The ALL Student's Name Is Entered , Then Enter 'Done'  \n")
    while True:
        name= get_name()
        if name=='Done':
             break
        else:
             name_list.append(name)
    
    for i in name_list:
        mark_sum=0
        t1=[]
        t1.append(i)
        t2=[]
        print(f'''Enter ! {i}'s Marks :''')
        for i in l:
                temp= get_subject_mark(i)
                t2.append(temp)
                mark_sum+=temp
        t1.append(t2)
        grade=get_grade(mark_sum/6)
        t1.append(grade)
        all_data.append(t1)

    printGrade(all_data)
                
def printGrade(data):
     result=PrettyTable(["Name","Math","hindi","english","science","Art","computer","Gread"])
     for i in data:
          result.add_row([i[0],i[1][0],i[1][1],i[1][2],i[1][3],i[1][4],i[1][5],i[2]])
     print("RESULT OF ALL THE STUDENT: ")
     print(result)
     

# this method retun the grade
def get_grade(avg):

    if avg>90:
         return "A"
    elif avg>80:
         return "B"
    elif avg>70:
         return "C"
    elif avg>60:
         return "D"
    else :
         return "Fail"




# this function return the valid name taking form the user and return after checking
def get_name():
    
    while True:
        name=input( "\n").title()
        if name =='Done':
            return name
        #check function check the name is write of note
        elif check(name):
             return name
        else:
             print("Enter valid name ! ")


#return the true of false after checking the name 
def check(name):
    # this function return the valide name or not of 
    name=name.title().split()
    def checkx(name):
        count=0
        for i in range(len(name)):
            if (ord(name[i])>=65 and ord(name[i])<=90) or (ord(name[i])>=97 and ord(name[i])<=122) or (ord(name[i])==32):
                count=count+1
        if count==len(name):
            return True
        return False
    for i in name:
        if not checkx(i): 
            return False
    return True

          
        
# return the subject marks form the user
def  get_subject_mark(s):
    while True:
        try:
            mark=int(input(f'''{s} :'''))
            if mark<0 or mark>101:
                print("Enter positive marks : ")
            else:
                return mark
        except ValueError:
                print("Enter Valid marks :")

main()

