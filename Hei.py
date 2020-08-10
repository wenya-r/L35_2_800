import pyalps
import numpy as np
import matplotlib.pyplot as plt
import pyalps.plot

parms = [ { 
       'LATTICE'                   : "open chain lattice", 
       'MODEL'                     : "spin",
       'CONSERVED_QUANTUMNUMBERS'  : 'N,Sz',
       'Sz_total'                  : 2,
       'local_S'                   : 1,
       'J'                         : 1,
       'SWEEPS'                    : 4,
       'NUMBER_EIGENVALUES'        : 1,
       'L'                         : 35,
       'MAXSTATES'                 : 800
      } ]

#write the input file and run the simulation
input_file = pyalps.writeInputFiles('parm_spin_one',parms)
res = pyalps.runApplication('/home/roweww/miniconda2/bin/dmrg',input_file,writexml=True)

#load all measurements for all states
data = pyalps.loadEigenstateMeasurements(pyalps.getResultFiles(prefix='parm_spin_one'))

# print properties of the eigenvector:
for s in data[0]:
    print s.props['observable'], ' : ', s.y[0]

# load and plot iteration history
iter = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parm_spin_one'),
                               what=['Iteration Energy','Iteration Truncation Error'])

plt.figure()
pyalps.plot.plot(iter[0][0])
plt.title('Iteration history of ground state energy (S=1)')
plt.ylim(-15,0)
plt.ylabel('$E_0$')
plt.xlabel('iteration')

plt.figure()
pyalps.plot.plot(iter[0][1])
plt.title('Iteration history of truncation error (S=1)')
plt.yscale('log')
plt.ylabel('error')
plt.xlabel('iteration')
plt.savefig('L22.pdf')
plt.show()
