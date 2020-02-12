import population, individual, random

class Algorithm:

    _uniformRate = 0.5
    _mutationRate = 0.015
    _tournamentSize = 5
    _elitism = True


    @staticmethod
    def evolvePopulation(pop):

        elitismOffset = 0
        newPopulation = population.Population(pop.size(), False)

        if Algorithm._elitism:
            newPopulation.saveIndividual(0, pop.getFittest())
            elitismOffset = 1

        for i in range(elitismOffset, pop.size()):
            individual1 = Algorithm.tournamentSelection(pop)
            individual2 = Algorithm.tournamentSelection(pop)
            newIndividual = Algorithm.crossover(individual1, individual2)
            newPopulation.saveIndividual(i, newIndividual)

        for i in range(elitismOffset, newPopulation.size()):
            Algorithm.mutate(newPopulation.getIndividual(i))

        return newPopulation



    @staticmethod
    def crossover(individual1, individual2):

        newSol = individual.Individual()

        for i in range(individual1.size()):
            if random.random() <= Algorithm._uniformRate:
                newSol.setGene(i, individual1.getGene(i))
            else:
                newSol.setGene(i, individual2.getGene(i))

        return newSol



    @staticmethod
    def mutate(individual):
        for i in range(individual.size()):
            if random.random() <= Algorithm._mutationRate:
                gene = round(random.random())
                individual.setGene(i, gene)



    @staticmethod
    def tournamentSelection(pop):
        tournament = population.Population(Algorithm._tournamentSize, False)

        for i in range(Algorithm._tournamentSize):
            randomIndex = int(random.random() * pop.size())
            tournament.saveIndividual(i, pop.getIndividual(randomIndex))

        fittest = tournament.getFittest()
        return fittest




'''
public class Algorithm {

    /* GA parameters */
    private static final double uniformRate = 0.5;
    private static final double mutationRate = 0.015;
    private static final int tournamentSize = 5;
    private static final boolean elitism = true;

    /* Public methods */
    
    // Evolve a population
    public static Population evolvePopulation(Population pop) {
        Population newPopulation = new Population(pop.size(), false);

        // Keep our best individual
        if (elitism) {
            newPopulation.saveIndividual(0, pop.getFittest());
        }

        // Crossover population
        int elitismOffset;
        if (elitism) {
            elitismOffset = 1;
        } else {
            elitismOffset = 0;
        }
        // Loop over the population size and create new individuals with
        // crossover
        for (int i = elitismOffset; i < pop.size(); i++) {
            Individual indiv1 = tournamentSelection(pop);
            Individual indiv2 = tournamentSelection(pop);
            Individual newIndiv = crossover(indiv1, indiv2);
            newPopulation.saveIndividual(i, newIndiv);
        }

        // Mutate population
        for (int i = elitismOffset; i < newPopulation.size(); i++) {
            mutate(newPopulation.getIndividual(i));
        }

        return newPopulation;
    }

    // Crossover individuals
    private static Individual crossover(Individual indiv1, Individual indiv2) {
        Individual newSol = new Individual();
        // Loop through genes
        for (int i = 0; i < indiv1.size(); i++) {
            // Crossover
            if (Math.random() <= uniformRate) {
                newSol.setGene(i, indiv1.getGene(i));
            } else {
                newSol.setGene(i, indiv2.getGene(i));
            }
        }
        return newSol;
    }

    // Mutate an individual
    private static void mutate(Individual indiv) {
        // Loop through genes
        for (int i = 0; i < indiv.size(); i++) {
            if (Math.random() <= mutationRate) {
                // Create random gene
                byte gene = (byte) Math.round(Math.random());
                indiv.setGene(i, gene);
            }
        }
    }

    // Select individuals for crossover
    private static Individual tournamentSelection(Population pop) {
        // Create a tournament population
        Population tournament = new Population(tournamentSize, false);
        // For each place in the tournament get a random individual
        for (int i = 0; i < tournamentSize; i++) {
            int randomId = (int) (Math.random() * pop.size());
            tournament.saveIndividual(i, pop.getIndividual(randomId));
        }
        // Get the fittest
        Individual fittest = tournament.getFittest();
        return fittest;
    }
}'''