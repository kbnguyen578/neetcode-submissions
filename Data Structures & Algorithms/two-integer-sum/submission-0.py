class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # "return the smallest index first" -> no opposite sides closing in

        # target - nums[idx] = partner 
        # [partner: idx]

        partner = {}

        for i in range(len(nums)):
            if nums[i] in partner: 
                return [partner.get(nums[i]), i]
            
            p = target - nums[i]
            partner[p] = i
