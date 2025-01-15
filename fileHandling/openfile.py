import os
def Write():
    try:
        file=open("hello.txt",'a')
        add=input("Enter new data")+"\n"
        file.write(add)
        file.close()
    except IOError:
      print("file not present")

def Read():
    file=open("hello.txt",'r')
    data=file.readline()
    print(data.split())
    file.close()
Write()
Read()
