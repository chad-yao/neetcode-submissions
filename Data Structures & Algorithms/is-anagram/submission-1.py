class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()
        t_dict = dict()
        for ch in s:
            s_dict[ch] = 1 + s_dict.get(ch, 0)
        for ch in t:
            t_dict[ch] = 1 + t_dict.get(ch, 0)

        if len(s_dict.keys()) != len(t_dict.keys()):
            return False

        for key, value in s_dict.items():
            if key not in t_dict.keys():
                return False
            else:
                if value != t_dict[key]:
                    return False

        return True