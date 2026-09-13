class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1

        sorted_items = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)

        
        top_k_elements = [item[0] for item in sorted_items[:k]]

        return top_k_elements
