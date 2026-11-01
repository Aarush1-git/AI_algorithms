import math 

def ab(depth, node, is_max, a, b):
    if depth == max_depth:
        return values[node]

    best = -math.inf if is_max else math.inf

    for i in range(2):
        val = ab(depth + 1, node*2 + i, not is_max, a, b)
        if is_max:
            best = max(best, val)
            a = max(best, a)
        else:
            best = min(best, val)
            b = min(best, b)

        if b <= a:
            break

    return best

if __name__ == "__main__":
    values = list(map(int, input("Enter the leaf nodes of binary tree: ").split()))
    max_depth = int(math.log2(len(values)))

    print("Optimal value", ab(0, 0, True, -math.inf, math.inf))