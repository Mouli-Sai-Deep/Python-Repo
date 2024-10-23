import java.util.Scanner;
public class weights{
    public static void main(String[] args){
        Scanner read = new Scanner(System.in);
        int x = read.nextInt();
        int y = read.nextInt();
        int z = read.nextInt();
        int answer = 3 * x -(y + z);
        System.out.println(answer);
    }
}