from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            d[key].append(s)
        return list(d.values())


if __name__ == "__main__":
    tests = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(tests))
