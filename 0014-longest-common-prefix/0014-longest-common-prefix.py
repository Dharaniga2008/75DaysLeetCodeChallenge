class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        prefix = strs[0]   # take first string
        
        for word in strs[1:]:
            while word[:len(prefix)] != prefix:
                prefix = prefix[:-1]   # reduce prefix
                if prefix == "":
                    return ""
        
        return prefix