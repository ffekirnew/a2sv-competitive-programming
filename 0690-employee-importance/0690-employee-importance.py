"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:        
        visited = set()
        def dfs_importance(employee: Employee):
            employee_importance = employee.importance
            
            for subordinate in employee.subordinates:
                if subordinate not in visited:
                    visited.add(subordinate)
                    employee_importance += dfs_importance(employees[subordinate])
            
            return employee_importance
        
        
        employees = { employee.id: employee for employee in employees }
        return dfs_importance(employees[id])
        
        
            
            
        