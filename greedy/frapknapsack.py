class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def fractionalKnapsack(W, arr, n):
    arr.sort(key=lambda x: (x.value / x.weight), reverse=True)

    curWeight = 0 
    finalvalue = 0.0 
    for i in range(n):
        if curWeight + arr[i].weight <= W:
            curWeight += arr[i].weight
            finalvalue += arr[i].value 
        else:
            remain = W - curWeight
            finalvalue += (arr[i].value / arr[i].weight) * remain
            break  
    return finalvalue
def main():
    n = 3
    weight = 50  
    arr = [Item(100, 20), Item(60, 10), Item(120, 30)]
    ans = fractionalKnapsack(weight, arr, n)
    print(f"The maximum value is: {ans:.2f}")
if __name__ == "__main__":
    main()