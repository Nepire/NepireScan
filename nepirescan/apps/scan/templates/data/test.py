
f = open('bilibili/acg.tv.txt')
domain=[]
for i in range(20):
    tmp = f.readline()[:-1].replace(' ','')
    domain.append(tmp[:tmp.index('\t')])

print(domain)
