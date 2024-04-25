a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

r1 = a
r2 = b
s1 = 1
s2 = 0
t1 = 0
t2 = 1
def gcdExtended(a, b):
	global r2,r1,s1,s2,t1,t2
	if a == 0:
		return b, 0, 1

	while(r2>0):
		q = r1//r2
		r = r1 - q*r2
		r1 = r2
		r2 = r
		s = s1 - q*s2
		s1 = s2
		s2 = s
		t = t1 - q*t2
		t1 = t2
		t2 = t

gcdExtended(a, b) 
s = s1
t = t1

print("\ngcd(", a, ",", b, ") = ", r1, "\ns = ", s1, ", t = ", t1)
print(f"({s}*{a}) + ({t}*{b}) = {(s*a)+(t*b)}")