from random  import randint,random

class dna:
    def __init__(self,num):
        self.genes=[randint(1,num) for n in range(num) ]
        self.fitness=0

    def set_fitness(self):
        no_attacking=0    
        max_pair=sum(range(len(self.genes)))
        # print("maxpair",max_pair)
        for i in range(len(self.genes)):
            for j in range(len(self.genes)):
                if i!=j:
                    x=abs(i-j)
                    y=abs(self.genes[i]-self.genes[j])
                    if x==y:
                        no_attacking+=1
        no_attacking//=2
        unique = []
        [unique.append(item) for item in self.genes if item not in unique]
        no_attacking+=(abs(len(self.genes)-len(unique)))
        # print("atacandose: ",no_attacking)
        self.fitness= (max_pair-no_attacking)
        # print("fitness: ",self.fitness)

    
    def crossover(self,parent):
        child=dna(len(self.genes))
        midpoint=randint(1,len(self.genes)-1)
        # print("midpoint: ",midpoint)
        child.genes=self.genes[:midpoint]+parent.genes[midpoint:]
        # print(child.genes)
        return child

    # def mutate(self,mutationRate):
    #     for i in range(len(self.genes)):
    #         if random()<mutationRate:
    #             # print("antes de mutar:",self.genes)
    #             self.genes[i]=randint(1,len(self.genes))
    #             # print("Despues de mutar:",self.genes)

    def mutate(self):
        index=randint(0,len(self.genes)-1)
        self.genes[index]=randint(1,len(self.genes))
             
        
# obj=dna(4)
# obj.genes=[2,4,7,4,8,5,5,2]
# obj1=dna(4)
# obj1.genes=[3,2,5,4,3,2,1,3]
# obj.set_fitness()
# obj1.set_fitness()
# obj.crossover(obj1)
# obj1.crossover(obj)
# obj.mutate(.1)