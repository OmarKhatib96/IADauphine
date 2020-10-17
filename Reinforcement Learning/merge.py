'''
final_list=[]

def sort(temp):
    min=temp[0]
    n=len(temp)
    for element in range(0,n-2):
        min=element
        for j in range(element+1,n):
            if(temp[j]<temp[min]):
                min=j
        if(min!=element):
            temp_element=temp[element]
            temp[element]=temp[min]
            temp[min]=temp_element
            
      

def n_ways_ms(L):
    n=len(L)
    temp=[]
    for i in range(0,n):
        for j in range(len(L[i])):
            temp.append(L[i][j])
    
    sort(temp)
    return temp
    
print(n_ways_ms([[1,2,3,4],[1,5,6,7,8]]))
'''

final_list=[]

def get_min(min_list):
    my_index=min_list.index(min(min_list))
    return my_index

def check_empty_list(L):
    sum=0
    for i in range(0,len(L)):
        sum=+len(L[i])
    if(sum==0):
       return True

def n_ways_ms(L):

    if(check_empty_list(L)):
        return final_list

    min_list=[]

    for i in range(0,len(L)):
        if(len(L[i])!=0):
            min_list.append(L[i][0])
        else:
            min_list.append(float('inf'))

    min_index=get_min(min_list)
    element=L[min_index].pop(0)#On le retire de la liste
    final_list.append(element)
    n_ways_ms(L)#Appel récursif



n_ways_ms([[1,2,3,4,5],[1,8,10,387],[0,386,390]])
print(final_list)
