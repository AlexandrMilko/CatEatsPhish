import java.io.*;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {

        String dir;
        Scanner scan = new Scanner(System.in);
        dir = scan.nextLine();
        scan.close();

        Reader spam = new FileReader("spam.txt");
        Reader ham = new FileReader("ham.txt");
        Reader content = new FileReader(dir);

        BayesianAnalyzer analyzer = new BayesianAnalyzer();

        analyzer.addSpam(spam);
        analyzer.addHam(ham);
        analyzer.buildCorpus();

        double probability = analyzer.computeSpamProbability(content);

        System.out.println(probability * 100);

    }

}