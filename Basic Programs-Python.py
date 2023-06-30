def solve(t):
  return hash(t)

t=(1,2)
print(solve(t))







n=int(input())
int_list=tuple(map(int, input().split()))
print(hash(int_list))

if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))



















lb=int(input("enter lower bound"))
up=int(input("enter upper bound"))

for i in range(lb,up+1):
  sum=0
  temp=i
  pow=len(str(i))
  while temp>0:
       digit=temp%10
       sum+=digit ** pow
       temp//=10
  if i==sum:
     print(i)
       
