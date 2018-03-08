from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

cantProcs = comm.Get_size()

comm.Barrier()
tiempo_inicio = MPI.Wtime()
tamVec = 1000000

vect1 = []
vect2 = []

for x in range (0, tamVec):
    vect1.append(x)
    vect2.append(x+tamVec)

n = tamVec//cantProcs
a = rank * n
b = a+n
producto = 0.0

for x in range (a, b):
    producto += vect1[x] * vect2[x]


total = comm.reduce(producto, root=0, op=MPI.SUM)

comm.Barrier()

tiempo_diferencia = MPI.Wtime() - tiempo_inicio

if (rank == 0):
    print ("El total es ", total)
    print ("Tiempo total de ejecucion ", tiempo_diferencia)