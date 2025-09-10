class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        height = 0
        for i in range(len(gain)):
            height += gain[i]
            max_alt = max(max_alt, height)
        return max_alt
        