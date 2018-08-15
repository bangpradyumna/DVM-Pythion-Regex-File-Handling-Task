import csv
import re

path=open('messy_data.csv')
csv_f=csv.reader(path)
data=[]
for row in csv_f:
    for column in row:
       match1=re.search(r'\b\d+\w\d\w+\d+\b',column)
       if(match1):
           id=column
       else:
           match2=re.search(r'\d+',column)
           if(match2):
               age=column
           else:
                match3=re.search(r'\b\w\b',column)
                if(match3):
                    gender=column
                else:
                    name=column    
    data.append([id,name,age,gender])
finalfile=open('clean_data.csv','w+')
with finalfile:
    writer=csv.writer(finalfile)
    writer.writerows(data)        
                    
           
            