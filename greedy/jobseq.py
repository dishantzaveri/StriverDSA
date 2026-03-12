class Job:
    def __init__(self, id, dead, profit):
        self.id = id      
        self.dead = dead  
        self.profit = profit  


def JobScheduling(arr, n):
    arr.sort(key=lambda x: x.profit, reverse=True)
    maxi = arr[0].dead
    for i in range(1, n):
        maxi = max(maxi, arr[i].dead)  
    slot = [-1] * (maxi + 1)

    countJobs = 0
    jobProfit = 0
    for i in range(n):
        for j in range(arr[i].dead, 0, -1):
            if slot[j] == -1:  
                slot[j] = i  
                countJobs += 1  
                jobProfit += arr[i].profit  
                break 
    return countJobs, jobProfit

if __name__ == "__main__":
    n = 4
    arr = [Job(1, 4, 20), Job(2, 1, 10), Job(3, 2, 40), Job(4, 2, 30)]
    ans = JobScheduling(arr, n)
    print(ans[0], ans[1])