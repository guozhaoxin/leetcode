#encoding:utf8
__author__ = 'gold'

strs = ["nozzle","punjabi","waterlogged","imprison","crux","numismatists","sultans","rambles","deprecating"]
nstrs = map(lambda x:''.join(sorted(x)),strs)
print(nstrs)
for s in nstrs:
    print(s)