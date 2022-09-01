t0 = 0
t1 = 1
n = 5000
count = 0
seq = [t0, t1]

if(n > 1):
    while(count < n):
        new = t0+t1
        seq.append(new)
        t0 = t1
        t1 = new
        count += 1
print(len(seq))