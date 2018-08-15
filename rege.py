import re
str=raw_input("Enter your password! ")
flag=0
if len(str)>=6:
    match1=re.search(r'[A-Z]',str)
    flag+=1
    if match1:
        match2=re.search(r'[0-9]',str)
        flag+=1
        if match2:
            flag+=1
            match3=re.search(r'[!@#$%^&*.-_]',str)
            if match3:
                flag+=1;
                match4=re.search(r'[a-z]',str)
if flag==4:
    print("Password Accepted!")
else:
    print("Your password does not meet the required contraints!")
