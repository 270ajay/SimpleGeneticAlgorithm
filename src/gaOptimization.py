import fitnessCalc, population, algorithm, utilities, logging




if __name__ == "__main__":

    utilities.logger(logging)

    fitnessCalc.FitnessCalc.setSolutionStr("1111000000000000000000000000000000000000000000000000000000001111")
    myPop = population.Population(50, True)

    generationCount = 0
    maxFitness = fitnessCalc.FitnessCalc.getMaxFitness()
    fittest = myPop.getFittest()
    objectiveVal = fittest.getFitness()


    while (objectiveVal < maxFitness):
        generationCount += 1

        logging.info("Generation: " + str(generationCount) + " ObjectiveValue: " + str(objectiveVal))
        logging.debug("\nPopulation:" + str(myPop))
        logging.debug("Fittest in this population: " + str(fittest) + "\n")

        myPop = algorithm.Algorithm.evolvePopulation(myPop)
        fittest = myPop.getFittest()
        objectiveVal = fittest.getFitness()


    logging.info("\nReached optimal solution (that was provided in the beginning) in Generation: "+ str(generationCount + 1))
    logging.debug("\nPopulation:" + str(myPop))
    logging.info("Fittest in this population: " + str(fittest) + "\n")
    logging.info("-------------------------------------------------------------")





'''
public class GA {

    public static void main(String[] args) {

        // Set a candidate solution
        FitnessCalc.setSolution("1111000000000000000000000000000000000000000000000000000000001111");

        // Create an initial population
        Population myPop = new Population(50, true);
        
        // Evolve our population until we reach an optimum solution
        int generationCount = 0;
        while (myPop.getFittest().getFitness() < FitnessCalc.getMaxFitness()) {
            generationCount++;
            System.out.println("Generation: " + generationCount + " Fittest: " + myPop.getFittest().getFitness());
            myPop = Algorithm.evolvePopulation(myPop);
        }
        System.out.println("Solution found!");
        System.out.println("Generation: " + generationCount);
        System.out.println("Genes:");
        System.out.println(myPop.getFittest());

    }
}'''