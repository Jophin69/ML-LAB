# FIND S
import csv
hypo=['%']*6
data=[]

print("The training example are ")

with open('finds.csv') as csv_file:
    read_csv=csv.reader(csv_file,delimiter=',')
    next(read_csv)
    for row in read_csv:
        print(row)
        if(row[-1]=="Yes"):
            data.append(row)
            
            
            
print("The positive examples are:")
for row in data:
    print(row)
    
    
for i in range(len(data)):
    for j in range(len(data[i])-1):
        if hypo[j]=='%':
            hypo[j]=data[i][j]
        elif hypo[j]!=data[i][j]:
            hypo[j]='?'
    print(hypo)
    
    
    
print("The maximum specified hypothesis is:")
print([h for h in hypo if h!='%'])                        
            
            

        
        