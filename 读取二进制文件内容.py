import pickle as p

shoplistfile='shoplist.data'

shoplist=['apple','carrot','peach']

# because the dump operation is using binary, so 'b' is needed.
# also for read file.
f=open(shoplistfile,'wb')
p.dump(shoplist,f)
f.close

del shoplist

f=open(shoplistfile,'rb')
storedlist=p.load(f)
print(storedlist)
