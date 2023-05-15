class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1

        freq = [(count, i) for i, count in counts.items()]

        freq.sort(reverse=True)

        top_k = [i for _, i in freq[:k]]

        return top_k