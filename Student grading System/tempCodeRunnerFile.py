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

    # global defiend database for all student name : & marks
    