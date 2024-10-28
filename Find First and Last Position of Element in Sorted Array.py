import java.util.Scanner;
public class FirstLast{
    public static void main(String[] args){
        Scanner read = new Scanner(System.in);
        int size  = read.nextInt();
        int[] array = new int[size];
        for(int i = 0; i < size; i++){
            array[i] = read.nextInt();
        }
        int first = -1;
        int last = -1;
        int key = read.nextInt();
        for(int i = 0; i < size; i++){
            if(array[i] == key && first == -1){
                first = i;
                last = i;
            }
            else if(array[i] == key && last != -1){
                last = i;
            }
        }
        System.out.println(first+ " " + last);
    }
}