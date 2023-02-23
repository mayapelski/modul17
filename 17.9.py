def insertionSort(arr):
	for i in range(1, len(arr)):
		x=arr[i]
		idx=i
		while idx>0 and arr[idx-1]>x:
			arr[idx]=arr[idx-1]
			idx-=1
		arr[idx]=x
		
def binSearch(arr, value):
	k = len(arr)//2
	l= 0
	h = len(arr) - 1
 
	while arr[k] != value and l <= h:
 	   if value > arr[k]:
 	       l = k+1
 	   else:
 	       h = k-1
 	   k = (l + h)//2
 
	if l> h:
		return -1
	else:
	    return k
	    
def isInteger(value):
	k=0
	if value[0]=='-':
		k=1
	for i in range(len(value)-k):
		if ((value[i+k]>='0' and value[i+k]<='9')==False):
			return False
	return True

valueList=[]		
a=input("Введите последовательность чисел через пробел: ").split()
value=input("Введите одно число из последовательности: ")
state=0;

for i in range(len(a)):
	if(a[i]==' '):
		continue
	if(isInteger(a[i])==False):
		state=1
		break
	else:
		valueList.append(int(a[i]))
if(isInteger(value)==False):		
	state=2;
	
if(state==0):
	print("Список до  сортировки:")
	print(valueList)
	print("Отсортированный список:")
	insertionSort(valueList)
	print(valueList)
	print("Результат поиска позиции числа:")
	bsResult=binSearch(valueList, int(value))
	if(bsResult==-1):
		print("Число ",value," не найдено в последовательности")
	else:
		print("Число ",value," найдено на позиции ",bsResult)
		
if(state==1):
	print("Неправильно введена числовая последовательность")
if(state==2):
	print("Неправильно введено число")