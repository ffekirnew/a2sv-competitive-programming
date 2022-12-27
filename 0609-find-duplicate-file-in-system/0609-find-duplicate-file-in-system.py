class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # create a container
        container = defaultdict(list)
        # iterate over the paths
        for path in paths:
            path_unpacked = path.split()
            root, files = path_unpacked[:1][0], path_unpacked[1:]
            for file in files:
                text_contained = ""
                for i in range(len(file) - 1, -1, -1):
                    if file[i] == "(":
                        break
                text_contained = file[i:len(file) - 1]
                container[text_contained].append(root + "/" + "".join(file[:i]))
        answer = []
        for value in container.values():
            if len(value) > 1:
                answer.append(value)
        return answer
        