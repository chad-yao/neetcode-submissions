class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x_dict = defaultdict(list)

        for string in strs:
            table = [0] * 26
            for s in string:
                table[ord(s) - ord('a')] += 1
            key = tuple(table)
            x_dict[key].append(string)
        
        return list(x_dict.values())
        