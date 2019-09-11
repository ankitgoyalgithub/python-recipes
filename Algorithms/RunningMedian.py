import heapq

class Solution:
    def __init__(self):
        self.lowers = []
        self.highers = []

    def add_number(self, n):
        if (len(self.lowers) == 0) or (-1*n > self.lowers[0]):
            heapq.heappush(self.lowers, -1*n)
        else:
            heapq.heappush(self.highers, n)
        
        print("-->", self.lowers, self.highers)
        
    
    def rebalance(self):
        if len(self.lowers) - len(self.highers) >=2:
            heapq.heappush(self.highers, heapq.heappop(self.lowers)*-1)
        
        elif len(self.highers) - len(self.lowers) >=2:
            heapq.heappush(self.lowers, heapq.heappop(self.highers)*-1)

    def get_median(self):
        if len(self.lowers) > len(self.highers):
            return self.lowers[0] * -1
        elif len(self.highers) > len(self.lowers):
            return self.highers[0]
        else:
            return ((self.lowers[0] * -1) + self.highers[0])/2 
    
    def get_medians(self, nums):
        medians = []

        for n in nums:
            self.add_number(n)
            self.rebalance()
            print(self.lowers, self.highers)
            medians.append(self.get_median())
        
        return medians

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    s = Solution()
    print(s.get_medians(nums))