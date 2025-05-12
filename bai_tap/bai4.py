def tach_chan_le(infile, outfile):
    with open(infile, 'r') as f:
        numbers = list(map(int, f.readline().strip().split()))
    chan = [str(x) for x in numbers if x % 2 == 0]
    le = [str(x) for x in numbers if x % 2 == 1]
    with open(outfile, 'w') as f:
        f.write(" ".join(chan) + '\n')
        f.write(" ".join(le) + '\n')

tach_chan_le(r"bai_tap\f_in.dat",'f_out.dat')