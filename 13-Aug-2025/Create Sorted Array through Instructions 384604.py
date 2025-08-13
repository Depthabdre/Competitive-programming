# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        min_value = min(instructions)
        range_of_numbers = (max(instructions) - min_value) + 1

        bucket_count = ceil(pow(range_of_numbers, 0.5))
        single_bucket_size = ceil(range_of_numbers / bucket_count)

        all_items_count_in_bucket = [[0] * single_bucket_size for _ in range(bucket_count)]
        each_bucket_count = [0] * bucket_count
        ans = 0

        for num in instructions:
            bucket = (num - min_value) // single_bucket_size
            item_index_in_bucket = (num - min_value) % single_bucket_size

            less_items_count = 0
            greater_items_count = 0

            # Count less than current
            for i in range(bucket):
                less_items_count += each_bucket_count[i]
            for i in range(item_index_in_bucket):
                less_items_count += all_items_count_in_bucket[bucket][i]

            # Count greater than current
            for i in range(bucket + 1, bucket_count):
                greater_items_count += each_bucket_count[i]
            for i in range(item_index_in_bucket + 1, single_bucket_size):
                greater_items_count += all_items_count_in_bucket[bucket][i]

            ans += min(greater_items_count, less_items_count) % (10**9 + 7)

            all_items_count_in_bucket[bucket][item_index_in_bucket] += 1
            each_bucket_count[bucket] += 1

        return ans % (10**9 + 7)
