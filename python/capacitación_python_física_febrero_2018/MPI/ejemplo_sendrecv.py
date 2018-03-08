from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()

mi_dato = random.randint(0,50)
otro_dato = comm.sendrecv(mi_dato, dest=(rank+1)%size, source=(rank +size -1)%size)

print("Soy el rank %d, generé el dato %d y recibí el dato %d" % (rank, mi_dato, otro_dato))