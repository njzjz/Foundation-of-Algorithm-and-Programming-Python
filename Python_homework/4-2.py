#2 试编写程序计算
#S=1-1/2+1/3-1/4+1/5-…+1/99-1/100
s=0
for i in range(1,101):s+=-1/i*(-1)**i
print(s)
