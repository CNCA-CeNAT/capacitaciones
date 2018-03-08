from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

datos = (int(rank)+1)**2 

datos = comm.gather(datos, root=0)


print("Rank " + str(rank) + " --> datos: " + str(datos))