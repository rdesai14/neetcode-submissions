class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointL = 0
        pointR = len(numbers) - 1

        while (pointL < pointR):
            if (numbers[pointL] + numbers[pointR] == target):
                return [pointL + 1 , pointR + 1]
            
            if (numbers[pointL] + numbers[pointR] > target):
                pointR -= 1
            elif(numbers[pointL] + numbers[pointR] < target):
                pointL += 1
            
        