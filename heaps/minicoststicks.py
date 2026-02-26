import heapq

def minCostConnectSticks(sticks):
    heapq.heapify(sticks) 
    total_cost = 0

    while len(sticks) > 1:
        first = heapq.heappop(sticks)   # smallest
        second = heapq.heappop(sticks)  # second smallest
        cost = first + second
        total_cost += cost
        heapq.heappush(sticks, cost)    # push merged stick back

    return total_cost

# Example 1
print(minCostConnectSticks([2, 4, 3]))    # Output: 14

# Example 2
print(minCostConnectSticks([1, 8, 3, 5])) # Output: 30
