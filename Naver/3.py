dp = [[-1 for i in range(151)] for j in range(151)]

def solution(n, m, k):
   answer = 0
   total = int(m/2)
   div1, div2 = 0, 0

   if n%2==1:
      div1, div2 = int(n/2)+1, int(n/2)
   else:
      div1, div2 = int(n/2), int(n/2)

   answer += (((partition(total, div1, k)%1000000007)*(partition(total, div2, k)%1000000007))*2)
   
   return answer%1000000007

def partition(num, cnt,limit):
   global dp
   if dp[num][cnt]!=-1: return dp[num][cnt]

   if cnt==1: 
      if limit>=num:
         dp[num][cnt]=1
         return 1
      else:
         dp[num][cnt]=0
         return 0
   else:
      ret=0
      upper = min(num-cnt+2,limit+1)
      for i in range(1,upper):
         ret+=partition(num-i,cnt-1,limit)
         
      dp[num][cnt] = ret
      return ret

print(solution(   50, 150, 20))