'''
Given a sorted array with possibly duplicate elements, the task is to find indexes of first and last occurrences of an element x in the given array.

Note: If the number x is not found in the array just print '-1'.

Input:
The first line consists of an integer T i.e number of test cases. The first line of each test case contains two integers n and x. The second line contains n spaced integers.

Output:
Print index of the first and last occurrences of the number x with a space in between.

Constraints: 
1<=T<=100
1<=n,a[i]<=1000

'''


def Foccr(arr,ele):
    l,h = 0,len(arr)-1
    
    while l<=h:
        mid = (l+h)//2
        if arr[mid]>ele:
            h = mid -1
        elif arr[mid]<ele:
            l = mid+1
        else :
            if mid == 0 or arr[mid]!= arr[mid-1] :
                return mid
            else:
                h = mid-1
    return -1
                
def Loccr(arr,ele):
    l,h = 0,len(arr)-1
    while l<=h:
        mid = (l+h)//2
        if arr[mid]>ele:
            h = mid-1
        elif arr[mid]<ele:
            l = mid+1
        else :
            if mid == len(arr)-1 or arr[mid]!=arr[mid+1]:
                return mid
            else :
                l = mid+1
    return -1
    
def main():
    for _ in range(int(input())):
        n,k = map(int,input().split())
        arr = list(map(int,input().split()))
        if Foccr(arr,k) == -1 or Loccr(arr,k) == -1:
            print(-1)
        else :
            print(Foccr(arr,k),Loccr(arr,k))
        
if __name__ == "__main__":
    main()
