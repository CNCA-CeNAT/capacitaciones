import numpy as np
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()

comm.Barrier()
tiempo_inicio = MPI.Wtime()

data = np.zeros(5)


for i in range(rank, len(data), size):
    data[i] = i

print ('[%i]'%rank, data)
comm.Barrier()

if rank==0:
    total = np.zeros_like(data)
    
else:
    total = None

comm.Reduce([data, MPI.DOUBLE], [total, MPI.DOUBLE], op = MPI.SUM, root = 0)

print ('[%i]'%rank, total)

comm.Barrier()

tiempo_diferencia = MPI.Wtime() - tiempo_inicio

if rank == 0: 
    print ("Tiempo total de ejecucion ", tiempo_diferencia)
