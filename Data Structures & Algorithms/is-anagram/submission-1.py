class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_list1 = [char for char in s]
        char_list2 = [char for char in t]

        if len(s) != len(t):
            return False

        char_list1.sort()
        char_list2.sort()

        if char_list1 == char_list2:
            return True
        else:
            return False
