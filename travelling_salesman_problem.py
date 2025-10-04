# Travelling Salesman Problem (TSP) using Memoization + Bitmasking
# Finds both the minimum cost and the route

def totalCost(mask, curr, n, cost, memo, parent):
    # Base case: if all cities are visited, return cost back to start
    if mask == (1 << n) - 1:
        return cost[curr][0]

    # If already computed, return from memo
    if memo[curr][mask] != -1:
        return memo[curr][mask]

    ans = float('inf')
    next_city = -1

    # Try visiting every city not visited yet
    for i in range(n):
        if (mask & (1 << i)) == 0:   # If city i not visited
            new_cost = cost[curr][i] + totalCost(mask | (1 << i), i, n, cost, memo, parent)
            if new_cost < ans:
                ans = new_cost
                next_city = i   # remember best city to go next

    # Save result and next step for path reconstruction
    memo[curr][mask] = ans
    parent[curr][mask] = next_city
    return ans


def tsp(cost):
    n = len(cost)
    memo = [[-1] * (1 << n) for _ in range(n)]    # DP memo table
    parent = [[-1] * (1 << n) for _ in range(n)]  # For path reconstruction

    min_cost = totalCost(1, 0, n, cost, memo, parent)

    # Reconstruct route from parent table
    mask = 1
    curr = 0
    route = [0]
    while True:
        next_city = parent[curr][mask]
        if next_city == -1:  # no further city
            break
        route.append(next_city)
        mask |= (1 << next_city)
        curr = next_city
    route.append(0)  # return to starting city

    return min_cost, route


# ------------------ Run Example -------------------
cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

min_cost, route = tsp(cost)

print("Minimum Cost:", min_cost)
print("Route:", " -> ".join(map(str, route)))
