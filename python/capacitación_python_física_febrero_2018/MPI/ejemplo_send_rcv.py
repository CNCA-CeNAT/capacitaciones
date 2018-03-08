from mpi4py import MPI
import random


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if size != 2: 
    print("La cantidad de procesos debe de ser exactamente 2")
    exit(1)
    


if rank == 0:
    var = random.randint(0, 50)
    comm.send(var, dest=1)
    print("Hola, soy el proceso %d y le envié el dato %d al otro proceso" % (rank, var))
    
else:
    var = comm.recv(source=0)
    print("Hola, soy el proceso %d y recibí el dato %d desde el otro proceso" % (rank, var))