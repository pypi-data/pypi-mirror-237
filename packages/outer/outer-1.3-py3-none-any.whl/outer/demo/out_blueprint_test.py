from outer import File, Dir


c = Dir('hello').sub_dir('hi').sub_dir('fsff')
d = c.sub_dir('123')
d.sub_dir('233')
aa = c.__str__()
x = d.sub_file('123.txt')
print(d)

