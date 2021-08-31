class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float("Inf")
        max_prof = 0
        for i in prices:
            if i < min_val:
                min_val = i
            elif i - min_val > max_prof:
                max_prof = i - min_val
        return max_prof
#Find min val nd then max_prof
#suppose you have [4,6,9,2,1,7] as the input min_val will change from 4,2,1
#then if we encounter a value grater than min_val we try to find max_prof with that min val for example
#min val =4 max_prof will be 2, 5 then min_val=2 max_prof will be 5 nw min val =1 max_prof will be 6