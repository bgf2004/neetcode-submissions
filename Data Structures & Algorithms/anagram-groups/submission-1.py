class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_List = {}

        for str in strs:
            str_count = Counter(str)
            hashed_str = tuple(sorted(str_count.items()))
            if hashed_str not in anagrams_List:
                anagrams_List[hashed_str] = []
            anagrams_List[hashed_str].append(str)
        return list(anagrams_List.values())