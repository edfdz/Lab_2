# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from timeit import default_timer as timer

def quicksort_stack(L,start,end): 
    #creates a temporary stack
    size = end - start + 1
    stack = [0] * (size) 
  
    #initiate stack
    top = -1
  
    #push start and end to stack
    top = top + 1
    stack[top] = start 
    top = top + 1
    stack[top] = end 
    
    #while stack is not empty keep popping
    while top >= 0: 
  
        #pop start and end
        end = stack[top] 
        top = top - 1
        start = stack[top] 
        top = top - 1
  
        p = partition( L, start, end-1 ) 
  
        #pushing left of stack
        if p-1 > start: 
            top = top + 1
            stack[top] = start 
            top = top + 1
            stack[top] = p - 1
            
        #pushing right of stack
        if p+1 < end: 
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = end                
            
            
        
def select_quickSort_Stack(L,k):
    quicksort_stack(L,0,len(L))
    return L[k]


def partition (L,l,h):
    x = L[h]
    i = (l-1)
    for j in range (l,h):
        if (L[j]) <= x:
            i += 1
            swap(L,i,j)
    swap(L,i+1,h)
    return (i + 1)

def swap (L,i,j):
    x = L[i]
    L[i] = L[j]
    L[j] = x


def quickSort(L,low,high): 
    if low < high: 
        p = partition(L,low,high) 
        quickSort(L, low, p-1) 
        quickSort(L, p+1, high)

def select_quick(L,k):
    quickSort(L,0,len(L) - 1)
    return L[k]
    
def bubbleSort (L,n):
    if n == 1:
        return L
    for i in range (n-1):
        if L[i] > L[i+1]:
            temp = L[i]
            L[i] = L[i+1]
            L[i+1] = temp
    bubbleSort(L,n-1)
    
def select_bubble(L,k):
    bubbleSort(L,len(L))
    return L[k]

def select_modified_quickSort(L,low,high,k):
    if low<high: 
        p = partition(L,low,high)
        if p == k:
            return L[p]
        elif k < p:
            return select_modified_quickSort(L, low, p-1,k)
        else:
            return select_modified_quickSort(L, p+1, high,k)

def select_modifiedWhile(L,low,high,k): 
    p = partition(L,low,high)
    while k == p:
        partition(L,low, p)
    
          
            
       
    
k = int(input('Enter index of K to find the Kth smallest element in the list: '))  
  
start = timer()
L1 = [55,11,33,66,44]
print (select_bubble(L1,k))
end = timer()
print('Runtime:',str(end-start))

start = timer()
L2 = [55,11,33,66,44]
print (select_quick(L2,k))
end = timer()
print('Runtime:',str(end-start))

start = timer()
L3 = [55,11,33,66,44]
print (select_modified_quickSort(L3,0,len(L3)-1,k))
end = timer()
print('Runtime:',str(end-start))

#start = timer()
#L5 = [55,11,33,66,44]
#print (select_modifiedWhile(L5,0,len(L5) - 1,k))
#end = timer()
#print('Runtime:',str(end-start))

start = timer()
L4 = [55,11,33,66,44]
print (select_quickSort_Stack(L4,k))
end = timer()
print('Runtime:',str(end-start))

