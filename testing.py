__author__ = 'shawn.wang'

def candy(ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # initialize the candy list
        candys = [1]*len(ratings)

        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                candys[i] += 1

        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1] and candys[i] <= candys[i+1]:
                candys[i] += 1
        res = 0
        for i in candys:
            res+=i

        return res

print candy([1, 2, 5])