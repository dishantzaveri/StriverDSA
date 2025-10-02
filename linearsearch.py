def search(arr, n, num):
    for i in range(n):
        if arr[i]==num:
            return i
    return -1
        
def main():
    arr = [1, 2, 3, 4, 5]
    num = 1
    n = len(arr)
    val = search(arr, n, num)
    print(val)

if __name__ == "__main__":
    main()
