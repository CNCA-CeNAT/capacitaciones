from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
   datos = [(i+1)**2 for i in range(size)]
else:
   datos = None
datos = comm.scatter(datos, root=0)


print("Rank " + str(rank) + " --> datos: " + str(datos))