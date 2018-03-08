from mpi4py import MPI
from random import randint

comm = MPI.COMM_WORLD
rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()

dato = randint(0,100)

print("[%d] Dato generado: %d" % (rank, dato))

total = comm.reduce(dato, op=MPI.SUM, root = 0)

total = comm.bcast(total, root = 0)


print("[%d] Suma total: %d" % (rank,total))
