from typing import List

class Solution:
    def moveZeros(self, nums:List[int]) -> None:
        j=0
        for num in nums:
            if(num !=0):
                nums[j] = num
                j += 1

        for x in range(j,len(nums)):
            nums[x]=0
        print(nums)


if __name__ == "__main__":
    s= Solution()
    s.moveZeros([0,1,4,0,6,7,0,0,10,12,14])
