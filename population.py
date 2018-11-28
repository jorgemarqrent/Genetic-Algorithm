from dna import dna
from random import randrange,randint,random

class population:
    def __init__(self,num, max_population, mutationR):
        self.population=[dna(num) for i in range(max_population)]
        self.parents=[]
        self.generations=0
        self.finished=False
        self.mutation_rate=mutationR
        self.perfect_score=sum([i for i in range(num)])
        self.best=None
        self.calculate_fitness()
        self.mutations=0


    def calculate_fitness(self):
        for individual in self.population:
            individual.set_fitness()
        # print("newpop",len(self.population),"\npop",[(n.fitness,n.genes) for n in self.population])

    def selection(self,percentage):
       self.population.sort(key=lambda n:n.fitness,reverse=True)
    #    print([n.fitness for n in self.population])
       selected=int(len(self.population)*(percentage/100))
       if selected<=1:
           selected=5
       top=selected
       self.parents=self.population[:top]
       
 
    def pick(self,parents,sum_):
        index=0
        r=randint(0,sum_)
        while r>0:
            r=r-parents[index].fitness
            index+=1
        return parents[index-1]

    def generate_childs(self):
        hundred_percent=sum([n.fitness for n in self.parents])
        offspring=[]
        self.mutations=0
        for _ in range(len(self.population)):
            parent_a=self.pick(self.parents,hundred_percent)
            parent_b=self.pick(self.parents,hundred_percent)
            child=parent_a.crossover(parent_b)
            if random()<self.mutation_rate:
                child.mutate()
                self.mutations+=1
            # self.population[i]=child
            offspring.append(child)
        self.population=offspring
        
        self.generations+=1
    # def mutation(self):
    #     if random()<self.mutation_rate:
            

    def evaluation(self):
        self.population.sort(key= lambda n: n.fitness,reverse=True)
        self.best=self.population[0]
        avg_fitness=sum([n.fitness for n in self.population])//len(self.population)
        print("Mejor :",[n for n in self.best.genes],"   Generaciones:",self.generations,"    Mutaciones:",self.mutations,"   Promedio de idoneidad:",avg_fitness,flush=True)
        if self.best.fitness==self.perfect_score:
            self.finished=True
        return self.finished
    
     

# p=population(8,20,.1)
# print("inicial",[(n.fitness,n.genes) for n in p.population])
# p.selection(5)
# p.generate_childs()
# print("hijos",[(n.fitness,n.genes) for n in p.population])