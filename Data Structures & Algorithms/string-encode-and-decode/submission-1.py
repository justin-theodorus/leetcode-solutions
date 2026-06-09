class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append("#")
            encoded.append(s)
        return "".join(encoded)


    def decode(self, s: str) -> List[str]:
        print(s)
        decoded = []
        is_length = True
        cur_length = 0
        cur_string = []
        idx = 0
        while idx < len(s):
            if is_length:
                if s[idx] == "#":
                    is_length = False
                    if cur_length == 0:
                        decoded.append("")
                        is_length = True
                else:
                    cur_length = 10 * cur_length + int(s[idx])
            else:
                if cur_length != 0:
                    cur_string.append(s[idx])
                    cur_length -= 1

                if cur_length == 0: 
                    decoded.append("".join(cur_string))
                    cur_string = []
                    is_length = True
            idx += 1
        return decoded
        

"""
Don't need a separator not in ASCII, just use length to capture string info

length#string

5#Hello5#World

###
3####
"""
