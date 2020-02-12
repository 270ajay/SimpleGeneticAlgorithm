import logging


class FitnessCalc:

    solution = [None] * 64

    @staticmethod
    def setSolution(newSolution):
        FitnessCalc.solution = newSolution
        logging.info("Optimal solution to reach: " + str(newSolution) + "\n")


    @staticmethod
    def setSolutionStr(newSolutionStr):
        logging.info("Optimal solution to reach: " + newSolutionStr + "\n")
        FitnessCalc.solution = [None] * len(newSolutionStr)

        for i in range(len(newSolutionStr)):
            character = newSolutionStr[i]
            if character == "1" or character == "0":
                FitnessCalc.solution[i] = int(character)
            else:
                FitnessCalc.solution[i] = 0



    @staticmethod
    def getFitness(individual):
        fitness = 0
        for i in range(individual.size()):
            if i < len(FitnessCalc.solution):
                if individual.getGene(i) == FitnessCalc.solution[i]:
                    fitness += 1

        return fitness


    @staticmethod
    def getMaxFitness():
        maxFitness = len(FitnessCalc.solution)
        return maxFitness





'''
public class FitnessCalc {

    static byte[] solution = new byte[64];

    /* Public methods */
    // Set a candidate solution as a byte array
    public static void setSolution(byte[] newSolution) {
        solution = newSolution;
    }

    // To make it easier we can use this method to set our candidate solution
    // with string of 0s and 1s
    static void setSolution(String newSolution) {
        solution = new byte[newSolution.length()];
        // Loop through each character of our string and save it in our byte
        // array
        for (int i = 0; i < newSolution.length(); i++) {
            String character = newSolution.substring(i, i + 1);
            if (character.contains("0") || character.contains("1")) {
                solution[i] = Byte.parseByte(character);
            } else {
                solution[i] = 0;
            }
        }
    }

    // Calculate inidividuals fittness by comparing it to our candidate solution
    static int getFitness(Individual individual) {
        int fitness = 0;
        // Loop through our individuals genes and compare them to our cadidates
        for (int i = 0; i < individual.size() && i < solution.length; i++) {
            if (individual.getGene(i) == solution[i]) {
                fitness++;
            }
        }
        return fitness;
    }
    
    // Get optimum fitness
    static int getMaxFitness() {
        int maxFitness = solution.length;
        return maxFitness;
    }
}'''