
def twoSum(self, nums: List[int], target: int) -> List[int]:
    pointerA = 0        #Defining this variable at zero allows us to use it at the zero index
    pointerB = 1        #Defining this at one follows the same principle

    for pointerA in range(len(nums)):
        currentInd = nums[pointerA] #defines actual zero index
        
        pointerB = pointerA + 1     #if the pointer reaches the end of the array, reset
        while pointerB < len(nums):     #go until the pointer reaches the end of the array
            currentIndexPlusOne = nums[pointerB] #defines first index
            desNum = currentInd + currentIndexPlusOne
            if target == desNum:
                return pointerA, pointerB #returns the indices of the numbers that equal the target
            else:
                pointerB+=1 #increments the pointer 

        pointerA+=1 #If the target is not found with the zero index, increment and check remaining indices using the same process