import sys
move = [[0,1],[0,-1],[1,0],[-1,0]]
def solution(board):
   n = len(board)
   new_board = [[1 for _ in range(n+2)] for _ in range(n+2)]
   cost = [[sys.maxsize for _ in range(n+2)] for _ in range(n+2)]
   for i in range(1,n+1):
      for j in range(1,n+1):
         new_board[i][j] = board[i-1][j-1]

   cost[1][1] = 0
   #ele[1] -> 0: init, 1: parallel, 2: vertical
   stack = [[(1,1),0,0]]
   ans = sys.maxsize
   while len(stack)>0:
      idx,shape,val = stack.pop()
      
      if idx == (n,n):      
         ans = min(ans,val)
         continue
      
      for m in move:
         if new_board[idx[0]+m[0]][idx[1]+m[1]]==0:
            money = calc((idx[0]+m[0],idx[1]+m[1]),idx,shape)
            new_s = 1
            if m[0]!=0: new_s=2
            if val+money<=cost[idx[0]+m[0]][idx[1]+m[1]]:
               cost[idx[0]+m[0]][idx[1]+m[1]] = val+money
               stack.append([(idx[0]+m[0],idx[1]+m[1]),new_s,val+money])

   return ans

def calc(idx,prev,shape):
   if shape==0:
      return 100
   elif shape==1:
      if abs(idx[0]-prev[0])==1 and idx[1]==idx[1]:
         return 600
      else:
         return 100
   else:
      if abs(idx[0]-prev[0])==1 and idx[1]==idx[1]:
         return 100
      else:
         return 600

test = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]

print(solution(test))
