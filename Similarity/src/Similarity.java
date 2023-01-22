import com.google.common.net.InternetDomainName;

import java.io.*;
import java.net.URI;
import java.net.URISyntaxException;
import java.util.Arrays;
import java.util.Scanner;

public class Similarity {

    public static void main(String[] args) throws IOException, URISyntaxException {

        Scanner scan = new Scanner(System.in);
        String link = scan.nextLine();
        scan.close();

        System.out.println(check(getDomain(link)));

    }

    public static String getDomain(String link) throws URISyntaxException {
        if (!(link.contains("://")))
            link = "https://" + link;
        String urlString = link;
        URI uri = new URI(urlString);
        String host = uri.getHost();

        InternetDomainName internetDomainName = InternetDomainName.from(host).topPrivateDomain();
        String domainName = internetDomainName.toString();

        String publicSuffix = internetDomainName.publicSuffix().toString();
        String name = domainName.substring(0, domainName.lastIndexOf("." + publicSuffix));

        return name;
    }

    public static double similarity(String s1, String s2) {
        String longer = s1, shorter = s2;
        if (s1.length() < s2.length()) { // longer should always have greater length
            longer = s2; shorter = s1;
        }
        int longerLength = longer.length();
        if (longerLength == 0) { return 1.0; }
        return (longerLength - editDistance(longer, shorter)) / (double) longerLength;

    }

    public static int editDistance(String s1, String s2) {
        s1 = s1.toLowerCase();
        s2 = s2.toLowerCase();

        int[] costs = new int[s2.length() + 1];
        for (int i = 0; i <= s1.length(); i++) {
            int lastValue = i;
            for (int j = 0; j <= s2.length(); j++) {
                if (i == 0)
                    costs[j] = j;
                else {
                    if (j > 0) {
                        int newValue = costs[j - 1];
                        if (s1.charAt(i - 1) != s2.charAt(j - 1))
                            newValue = Math.min(Math.min(newValue, lastValue),
                                    costs[j]) + 1;
                        costs[j - 1] = lastValue;
                        lastValue = newValue;
                    }
                }
            }
            if (i > 0)
                costs[s2.length()] = lastValue;
        }
        return costs[s2.length()];
    }

    public static double getSimilarity(String s, String t) {
//        System.out.println(String.format(
//                "%.3f  \"%s\" ~ \"%s\"", similarity(s, t), s, t));
        return similarity(s, t)*100;
    }

    public static double check(String domain) {
        String data = "";
        int counter = 0;

        try {
            File file = new File("verifiedD.txt");
            Scanner scan = new Scanner(file);
            while (scan.hasNextLine()) {
                data += scan.nextLine()+"\n";
                counter++;
            }
            scan.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

        String[] verifiedD = data.split("\n");
        double[] similarity = new double[verifiedD.length];

        for (int i = 0; i < verifiedD.length; i++) {
            similarity[i] = getSimilarity(domain, verifiedD[i]);
        }

        double maxValue = Arrays.stream(similarity).max().getAsDouble();
//        int maxIndex;

//        for (int i = 0; i < verifiedD.length; i++) {
//            if (similarity[i] == Arrays.stream(similarity).max().getAsDouble()) {
//                maxIndex = i;
//            }
//        }

        if (Arrays.stream(similarity).max().getAsDouble() < 100.0)
            return Arrays.stream(similarity).max().getAsDouble();
        else
            return 0.0;
    }

}