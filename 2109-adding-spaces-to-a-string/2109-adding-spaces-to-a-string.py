class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # create the object to be returned
        answer = []
        # iterate over the string and add the spaces
        space_ctr = 0
        for str_index, char in enumerate(s):
            if space_ctr < len(spaces) and str_index == spaces[space_ctr]:
                answer.append(" ")
                space_ctr += 1
            answer.append(char)
        # return the solution
        return "".join(answer)
        