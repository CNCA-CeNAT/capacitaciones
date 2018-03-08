from mpi4py import MPI
import math

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

def f(x):
    return 4/(1+math.pow(x,2))

cantidad_trapecios = 10000
l_interv = float(1/size)
inicio = float(rank * l_interv)
final = float(inicio + l_interv)
ancho_trapecios = float((l_interv)/ cantidad_trapecios)

suma = 0
total= 0

for x in range(0, cantidad_trapecios):
    altura = float(f(inicio + float(x/cantidad_trapecios)) + f(inicio + float((x+1)/cantidad_trapecios)))/2
    suma += altura*(ancho_trapecios)
    
    
total = comm.reduce(suma, op=MPI.SUM, root=0)

if rank == 0:
    print("La aproximación dio ", total)