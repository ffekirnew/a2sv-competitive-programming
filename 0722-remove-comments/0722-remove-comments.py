class Solution:
    def removeComments(self, source: List[str]) -> List[str]:        
        # object to be returned
        out_put = []
        
        # create a flag to know if in comment
        in_comment = False
        
        # iterate the source code
        for line in source:
            if not in_comment:
                out_put.append([])
            i = 0
            while i < len(line):
                char = line[i]
                if in_comment:
                    if char == '*' and i + 1 < len(line) and line[i + 1] == '/':
                        in_comment = False
                        i += 1
                    i += 1
                else:
                    if char == '/' and i + 1 < len(line) and line[i + 1] == '*':
                        in_comment = True
                        i += 1
                    elif char == '/' and i + 1 < len(line) and line[i + 1] == '/':
                        break
                    else:
                        out_put[-1].append(char)
                    i += 1
            if not in_comment:
                new_line = "".join(out_put.pop())
                if new_line:
                    out_put.append(new_line)
                    
        return out_put
                    