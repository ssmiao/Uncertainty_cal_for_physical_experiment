import math

#m = []

i =input("请输入初始变量的个数：\n")

for n in range(int(i)):  
    #name ='v'+str(n)  
    locals()['v'+str(n+1)]=float(i)

#print(v0)

#var = [0]
#deviation = [0]
unc = 0.0
function = [input("请输入各变量原始公式f，变量使用v1,v2,v3...而且使用pow代替^号\n")]

#n = 1
for n in range(int(i)):
	locals()['v'+str(n+1)] = float(input("请输入第" +str(n+1)+"个变量的平均值\n"))
	locals()['deviation'+str(n+1)] = float(input("请输入第" +str(n+1)+"个变量的偏差值\n"))
	#deviation.append(input("请输入第" +"n"+"个变量的偏差值"))

for n in range(int(i)):
	function.append(input("请输入与第"+str(n+1)+"个变量相关的df/dx公式，使用v1,v2,v3...作为变量，使用pow代替^号\n"))
	print(function[n+1])
	a = eval(function[n+1])
	unc = float(unc) + pow(a*locals()['deviation'+str(n+1)],2)
	print("目前为止的公式和为："+ str(unc))

unc = pow(unc,1/2)
ave_v0=float(eval(function[0]))

uv0 = float(eval(function[0]))*unc


print("\n"+"Answer is")
print(ave_v0)
print("+-")
print(uv0)
