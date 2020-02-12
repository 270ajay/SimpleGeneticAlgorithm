import random, fitnessCalc


class Individual:

    __defaultGeneLength = 64

    def __init__(self):
        self.__fitness = 0
        self.__genes = [None] * Individual.__defaultGeneLength


    def generateIndividual(self):
        for i in range(self.size()):
            gene = round(random.random())
            self.__genes[i] = gene


    @staticmethod
    def setDefaultGeneLength(length):
        Individual.__defaultGeneLength = length


    def getGene(self, index):
        return self.__genes[index]


    def setGene(self, index, value):
        self.__genes[index] = value


    def setFitness(self, value):
        self.__fitness = value


    def getFitness(self):
        if self.__fitness == 0:
            self.__fitness = fitnessCalc.FitnessCalc.getFitness(self)
        return self.__fitness


    def size(self):
        return Individual.__defaultGeneLength


    def __str__(self):
        geneString = ""
        for i in range(self.size()):
            geneString += str(self.getGene(i))
        return geneString


'''
public class Individual {

    static int defaultGeneLength = 64;
    private byte[] genes = new byte[defaultGeneLength];
    // Cache
    private int fitness = 0;

    // Create a random individual
    public void generateIndividual() {
        for (int i = 0; i < size(); i++) {
            byte gene = (byte) Math.round(Math.random());
            genes[i] = gene;
        }
    }

    /* Getters and setters */
    // Use this if you want to create individuals with different gene lengths
    public static void setDefaultGeneLength(int length) {
        defaultGeneLength = length;
    }
    
    public byte getGene(int index) {
        return genes[index];
    }

    public void setGene(int index, byte value) {
        genes[index] = value;
        fitness = 0;
    }

    /* Public methods */
    public int size() {
        return genes.length;
    }

    public int getFitness() {
        if (fitness == 0) {
            fitness = FitnessCalc.getFitness(this);
        }
        return fitness;
    }

    @Override
    public String toString() {
        String geneString = "";
        for (int i = 0; i < size(); i++) {
            geneString += getGene(i);
        }
        return geneString;
    }
}'''