from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = MPI.COMM_WORLD.Get_size()

datos = numpy.arange(int(rank)*int(size), int(rank)*int(size) + int(size))
recv = numpy.zeros(int(size)*int(size))
datos = comm.Gather(datos, recv, root=0)

print("Rank: " + str(rank) + "\n datos: " + str(datos) + " \n recv: " + str(recv))