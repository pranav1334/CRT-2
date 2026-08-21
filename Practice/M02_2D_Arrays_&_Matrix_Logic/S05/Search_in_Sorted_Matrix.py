from typing import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        arr =[]
        for row in matrix:
            arr+=row
        left,right=0,len(arr)-1
        while left <=right:
            mid=(left+right)//2
            if target == arr[mid]:
                return True
            elif target < arr[mid]:
                right=mid-1
            else:
                left =mid+1
        return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix,target))                