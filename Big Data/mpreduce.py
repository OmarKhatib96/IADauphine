
import csv


import csv

target_row = 3
target_col = 4
def get_element_row( row):
    with open('yourfile.db.csb', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        n = 0
        for row in reader:
            if row == target_row:
                data = row.split()[target_col]
                break




def get_data(filename):
    f=open(filename,"r")
    contents=f.read()
    f.close()
    return contents

def map(k,v):
    for element in v:
        return "("+str(element)+",1)"
    
def reduce(k,v):
    print(v)
    c=0
    for x in v:
        c=c+1
    return "("+str(k)+","+str(c)+")"

content=get_data("db.csv")
mapped=map(1,content)
print(reduce(1,mapped))

