#!/usr/bin/env python

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename',help='tabulated power spectrum from GenPK')
parser.add_argument('boxsize',type=float)
args = parser.parse_args()

from plot import plot_genpk_power
import matplotlib.pyplot as plt
plt.figure()
plot_genpk_power(args.filename,args.boxsize)
plt.show()
#plt.savefig('powerspec.pdf')
