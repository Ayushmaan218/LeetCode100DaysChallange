class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_map = Counter(arr)
        s = set()
        for v in count_map.values():
            if v in s:
                return False
            else:
                s.add(v)
        return True
