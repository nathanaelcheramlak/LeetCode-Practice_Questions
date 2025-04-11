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
        emp = defaultdict(list)
        for employee in employees:
            emp[employee.id] = employee.subordinates
            emp[employee.id].append(employee.importance)

        def dfs(id):
            if len(emp[id]) == 1:
                return emp[id][-1]

            current = emp[id][-1]
            for i in range(len(emp[id]) - 1):
                current += dfs(emp[id][i])
            return current
            
        return dfs(id)