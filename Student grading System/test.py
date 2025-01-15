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

name=input("Enter your  name :")
print(check(name))

