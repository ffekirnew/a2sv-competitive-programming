from typing import Dict, Generic, List, Tuple, TypeVar
T = TypeVar("T")


class DisjointSet(Generic[T]):
    def __init__(self):
        self._groups: Dict[T, T] = {}
        self._ranks: Dict[T, int] = {}
        self._sizes: Dict[T, int] = {}

    def insert(self, x: T) -> None:
        """Inserts a new node to the disjoint set if it didn't exist."""
        if x not in self._groups:
            self._groups[x] = x
            self._ranks[x] = 0
            self._sizes[x] = 1

    def insert_bulk(self, *nodes: List[T]) -> None:
        """Inserts any number of nodes to the disjoint set if they didn't exist."""
        for node in nodes:
            self.insert(node)

    def union(self, x: T, y: T) -> None:
        """Makes two nodes into a union."""
        self.insert_bulk(x, y)

        group_of_x = self.find(x)
        group_of_y = self.find(y)

        if group_of_x == group_of_y:
            return

        if self._ranks[group_of_x] > self._ranks[group_of_y]:
            self._groups[group_of_y] = group_of_x
            self._sizes[group_of_x] += 1
        elif self._ranks[group_of_y] > self._ranks[group_of_x]:
            self._groups[group_of_x] = group_of_y
            self._sizes[group_of_y] += 1
        else:
            self._groups[group_of_x] = group_of_y
            self._ranks[group_of_y] += 1
            self._sizes[group_of_y] += 1

    def find(self, x: T) -> bool:
        """Finds the parent of a node x."""
        group_of_x = x

        while group_of_x != self._groups[group_of_x]:
            group_of_x = self._groups[group_of_x]

        group_representative = group_of_x

        # path compression
        group_of_x = x
        while group_of_x != self._groups[group_of_x]:
            temp = self._groups[group_of_x]
            self._groups[group_of_x] = group_representative
            group_of_x = temp

        return group_representative

    def __getitem__(self, x: T) -> T:
        """Get the parent (representative) of the group to which element x belongs."""
        if x not in self._groups:
            raise ValueError("Element is not in the set.")
        return self.find(x)


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        disjoint_set = DisjointSet['str']()

        for i, str1 in enumerate(strs):
            disjoint_set.insert(str1)
            for j in range(i + 1, len(strs)):
                str2 = strs[j]
                
                disjoint_set.insert(str2)
                
                diff = 0
                for k in range(len(str1)):
                    diff += int(str1[k] != str2[k])
                    
                if diff <= 2:
                    disjoint_set.union(str1, str2)
        
        groups = set()
        for str_ in strs:
            groups.add(disjoint_set[str_])
        
        return len(groups)
                
                
            
            
        
        