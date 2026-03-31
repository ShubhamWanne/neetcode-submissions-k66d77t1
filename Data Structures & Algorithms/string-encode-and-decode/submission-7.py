class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        str_enc = []
        for str_ in strs:
            if str_ == "":
                str_enc.append(chr(9998))
                continue
            str_enc.append(str_)
        delimiter = chr(9999)
        return delimiter.join(str_enc)
            

    def decode(self, s: str) -> List[str]:
        print(f"s before {s}")
        if s == "":
            return []
        dec_str = []
        for c in s:
            if c == chr(9998):
                dec_str.append("")
                continue
            dec_str.append(c)

        s = "".join(dec_str)

        print(f"s after {s}")
                                       
        return s.split(chr(9999))
