
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()
name = MPI.Get_processor_name()

if size != 2:
    print("La cantidad de ranks debe de ser exactamente 2")
    exit(1)

# ping-pong entre dos ranks
contador = 0
for x in range(1000):
    if rank == 0:
        comm.send(contador, dest=1)
        contador = comm.recv(source=1)
    else:
        contador = comm.recv(source=0)
        contador += 1
        comm.send(contador, dest=0)
        
if rank == 0:
    print("El número total de intercambio de mensajes es: %d" % contador)
