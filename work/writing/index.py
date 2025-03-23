import get as g
n=0
with open("now.txt","r") as f:
	n=int(f.read())
x=n
while x-n>100000:
	g.get_hotComments(str(x))
	x=x+1
with open("now.txt","w") as f:
	f.write(x)
