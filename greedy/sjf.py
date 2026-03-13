class SJF:
    def wait(self,jobs):
        jobs.sort()
        wt = 0
        tt = 0
        n = len(jobs)
        for job in jobs:
            wt +=tt
            tt +=job
        return wt/n
    
if __name__ == "__main__":
    jobs = [4,3,7,1,2]
    print(jobs)
    sjf = SJF()
    ans = sjf.wait(jobs)
    print(ans)
    