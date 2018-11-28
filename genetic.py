from random import randint
# from dna import
from population import *
def get_value(request):
    try:
        return int(input(request))
    except ValueError :
        print("Ingrese solo valores numericos")
        return get_value(request)

def main():
    size=get_value("Ingrese el tamaño del tablero: ")
    max_pop=get_value("Ingrese el tamaño de la poblacion: ")
    mutation=get_value("Ingrese la probabilidad de mutacion: ")
    mutation/=100
    select=get_value("Ingrese el porcentaje de selección para el crossover")
    p=population(size,max_pop,mutation)
    iteration=0
    while p.finished!=True and iteration<10000: 
        p.selection(select)
        p.generate_childs()
        p.calculate_fitness()
        p.evaluation()
        iteration+=1
if __name__=="__main__":
    main()
