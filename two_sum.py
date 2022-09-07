def twoSum(nums, target):
    hashmap = dict()
    for i, v in enumerate(nums):
        if target-v in hashmap and hashmap[target-v] != i:
            return [hashmap[target-v], i]
        hashmap[v] = i
    return
