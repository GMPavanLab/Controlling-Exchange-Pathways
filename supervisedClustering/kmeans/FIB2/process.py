# process.py
from __future__ import print_function
import numpy as np
import sys

M = np.loadtxt('all')
bins_x = 100
bins_y = 100
H, xedges, yedges = np.histogram2d(M[:,0], M[:,1], [bins_x, bins_y])

# output as 'nonuniform matrix' format, see gnuplot doc.
print(bins_x, end=' ')
np.savetxt(sys.stdout, xedges, newline=' ')
print()

for i in range(0, bins_y):
    print(yedges[i], end=' ')
    np.savetxt(sys.stdout, H[:,i], newline=' ')
    print(H[-1,i])

# print the last line twice, then 'pm3d corners2color' works correctly
print(yedges[-1], end=' ')
np.savetxt(sys.stdout, H[:,-1], newline=' ')
print(H[-1,-1])
