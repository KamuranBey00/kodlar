#numbers = [1,2,3,4,5,6,7,8,9]
#list2=[]
##for number in numbers:
##    list2.append(number)
#print(list2)  
#list3 =[number for number in numbers] 
#print(list3) 

#list2= []
#for number in numbers:
#    list2.append(number*number)
#print(list2)
#list3=[number * number for number in numbers]
#print(list3)

#list2 =list()
#for number in numbers:
#    if number %2==0:
#        list2.append(number)
#print(list2)
#list3=[number for number in numbers if number%2==0]
#print(list3)

#list2=list()
#for number in numbers:
#        if number%2==0:
#            list2.append(number*number)
#print(list2)
#list3=[number*number for number in numbers if number%2==0]

#list2=[]
#for number in numbers:
#    if number>4 and number%2==0:
#        list2.append(number**2)
#print(list2)
#
#list3=[nubmer**2 for nubmer in numbers if number>4 and number%2==0]
#print(list3)
#numbers=[1,2,3,4]
#letters="abcd"
#list2=[]
#for number in numbers:
#    for letter in letters:
#        list2.append((number,letter))
#print(list2)

#list3=[(number,letter) for number in numbers for letter in letters]

#list1=[1,2,3,4,5,6,7,8,9]
#list2=[2,3,6,9,5]

#list3=[] 
#for i in list1:
#    if i not in list2:
#        list3.append(i*i)
#print(list3)        
#list4 =[i*i for i in list1 if not i in list2]
#print(list4)
#list_= [[1,2,3],[4,5,6,7],[8,9,10,11,12]]
#list2=[]
#for i in list_:
#    for j in i:
#        list2.append(j)
#print(list2)        
#
#list3 =[j for i in list_ for j in i]

#list_methods = []
#
#for method in dir(list):
#    if method.startswith("__"):
#        continue
#    list_methods.append(method)
#print(list_methods)

#liste=[method for method in dir(list) if not method.startswith("__")]
#print(liste)