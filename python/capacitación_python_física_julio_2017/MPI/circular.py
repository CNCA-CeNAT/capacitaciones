# Tomado del material del profesor Esteban Meneses:
# University of Pittsburgh
# Center for Simulation and Modeling (SaM)
# Introduction to MPI with MPI4Py
# Esteban Meneses, PhD
# Description: ring exchange of messages between ranks. Each rank circulates its random value until it reaches all the ranks.

from mpi4py import MPI
from random import randint


comm = MPI.COMM_WORLD
rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()
name = MPI.Get_processor_name()

# intercambio entre ranks
contador = 0
dato = randint(0,100)
for x in range(size):
    comm.send(dato, dest=(rank+1)%size, tag=7)
    dato = comm.recv(source=(rank+size-1)%size, tag=7)
    contador += dato

print("[%d] Suma total: %d" % (rank,contador))
