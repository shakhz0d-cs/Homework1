N = int(input())
s = input()

if len(s) > N:
    s = s[len(s)-N:]
elif len(s) < N:
    s = "." * (N - len(s)) + s

print(s)

N1 = int(input())
N2 = int(input())
s1 = input()
s2 = input()

print(s1[:N1] + s2[-N2:])
