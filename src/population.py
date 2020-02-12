import individual



class Population:

    def __init__(self, populationSize, initialise):

        self.individuals = [None] * populationSize
        self.__populationSize = populationSize

        if initialise:
            for i in range(self.size()):
                newIndividual = individual.Individual()
                newIndividual.generateIndividual()
                self.saveIndividual(i, newIndividual)


    def getIndividual(self, index):
        return self.individuals[index]


    def getFittest(self):
        fittest = self.individuals[0]
        fitnessVal = self.individuals[0].getFitness()

        for i in range(self.size()):
            if fitnessVal <= self.getIndividual(i).getFitness():
                fittest = self.getIndividual(i)
                fitnessVal = fittest.getFitness()

        return fittest



    def saveIndividual(self, index, individual):
        self.individuals[index] = individual


    def size(self):
        return self.__populationSize


    def __str__(self):
        populationString = ""
        for i in range(self.size()):
            populationString += "\n" + str(i) + " ---- " + str(self.individuals[i])
        return populationString





'''
public class Population {

    Individual[] individuals;

    /*
     * Constructors
     */
    // Create a population
    public Population(int populationSize, boolean initialise) {
        individuals = new Individual[populationSize];
        // Initialise population
        if (initialise) {
            // Loop and create individuals
            for (int i = 0; i < size(); i++) {
                Individual newIndividual = new Individual();
                newIndividual.generateIndividual();
                saveIndividual(i, newIndividual);
            }
        }
    }

    /* Getters */
    public Individual getIndividual(int index) {
        return individuals[index];
    }

    public Individual getFittest() {
        Individual fittest = individuals[0];
        // Loop through individuals to find fittest
        for (int i = 0; i < size(); i++) {
            if (fittest.getFitness() <= getIndividual(i).getFitness()) {
                fittest = getIndividual(i);
            }
        }
        return fittest;
    }

    /* Public methods */
    // Get population size
    public int size() {
        return individuals.length;
    }

    // Save individual
    public void saveIndividual(int index, Individual indiv) {
        individuals[index] = indiv;
    }
}'''