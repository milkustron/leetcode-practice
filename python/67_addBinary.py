class Solution:
    def addBinary(self, a: str, b: str) -> str:

        i = 1
        result = []
        memory = 0

        while i <= min(len(a),len(b)):
            if int(a[-i]) + int(b[-i]) + memory > 1:
                if int(a[-i]) + int(b[-i]) + memory == 2:
                    result.append("0")
                else: 
                    result.append("1")
                memory = 1
            else:
                result.append(str(int(a[-i]) + int(b[-i]) + memory))
                memory = 0
            i += 1

        if len(a) > len(b):
            j = len(a)-len(b)-1
            while j >= 0:
                if int(a[j]) + memory > 1:
                    result.append("0")

                else:
                    result.append(str(int(a[j])+memory))
                    memory = 0
                j -= 1
        elif len(a) < len(b):
            j = len(b)-len(a)-1
            while j >= 0:
                if int(b[j]) + memory > 1:
                    result.append("0")
                else:
                    result.append(str(int(b[j])+memory))
                    memory = 0
                j -= 1

        if memory > 0:
            result.append("1")

        result.reverse()
        return "".join(result)

