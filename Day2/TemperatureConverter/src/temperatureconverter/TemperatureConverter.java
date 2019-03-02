/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package temperatureconverter;

import java.util.Scanner;

/**
 *
 * @author sbdar
 */
public class TemperatureConverter {
double cels,fahr;

TemperatureConverter(int temptype, double temp){
    switch (temptype){
        case 1:
            celstofahr(temp);
            break;
        case 2:
            fahrtocels(temp);
            break;
        default:
            System.out.println("Invalid Choice!");           
    }
    
}
void celstofahr(double cels){
fahr = ((cels * 9) / 5) +  32;
System.out.println("Fahrenheit:" +fahr);
}

void fahrtocels(double fahr){
    cels = ((fahr - 32)* 5)/9;
    System.out.println("Celsius:"+cels);
}
    /**
     * @param args the command line arguments
     */


    public static void main(String[] args) {
        int option;
        double temp;
        // TODO code application logic here
         Scanner input = new Scanner(System.in);
         System.out.println("1 : Celsius to fahrenheit \n2 : Fahrenheit to Celsius");
         System.out.println("Enter your choice:");
         option = Integer.parseInt(input.nextLine());
         System.out.println("Enter temperature Value:");
         temp = Double.parseDouble(input.nextLine());
         new TemperatureConverter(option,temp);
    }
}


         
       