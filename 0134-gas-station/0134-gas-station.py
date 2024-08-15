class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_gas = 0
        total_cost = 0
        tank = 0
        start_position = 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            tank += gas[i] - cost[i]
            
            # If tank is negative, this means we cannot reach the next station
            if tank < 0:
                start_position = i + 1
                tank = 0

        if total_gas < total_cost:
            return -1

        return start_position
