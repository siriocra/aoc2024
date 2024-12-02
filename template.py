def one():
    pass

def two():
    pass

fin = open('d_in.txt', 'r')
fout = open('d_out.txt', 'w')

lines = fin.readlines()

fout.write(str(one()))

fin.close()
fout.close()
