from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = MPI.COMM_WORLD.Get_size()

if size != 2:
    print("La cantidad de ranks debe de ser exactamente 2")
    exit(1)

if rank == 0:
   datos = numpy.arange(100, dtype=numpy.float64)
   datos[88] = 5.666
   comm.Send(datos, dest=1, tag=13)
elif rank == 1:
   datos = numpy.empty(100, dtype=numpy.float64)
   comm.Recv(datos, source=0, tag=13)
    
print("Rank: " + str(rank) + " --> datos: " + str(datos))