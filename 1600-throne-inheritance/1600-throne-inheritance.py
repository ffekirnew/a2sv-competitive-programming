class ThroneInheritance:

    def __init__(self, kingName: str):
        self.live = defaultdict(int)
        self.throne = {
            kingName: []
        }
        self.live[kingName] = 1
        self.king = kingName
        

    def birth(self, parentName: str, childName: str) -> None:
        self.throne[parentName].append(childName)
        self.throne[childName] = []
        self.live[childName] = 1

    def death(self, name: str) -> None:
        self.live[name] = 0        

    def getInheritanceOrder(self) -> List[str]:
        order = []
        
        fringe = [self.king]
        while fringe:
            curr_person = fringe.pop()
            
            if self.live[curr_person]:
                order.append(curr_person)
            
            for child in reversed(self.throne[curr_person]):
                fringe.append(child)
        
        return order
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()