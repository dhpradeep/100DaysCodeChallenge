/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package agetoseconds;

import java.util.Scanner;

/**
 *
 * @author sbdar
 */
public class AgetoSeconds {
public static void main(String[] args) {
   int age;
    Scanner in =new Scanner(System.in);
   
    System.out.println("Enter your age:");
    int a =in.nextInt();
    
    age = a * 365 * 24 * 60 * 60; 

    System.out.println("Your age is:" +age);
//    age = Integer.parseInt(in.nextLine());

    /**
     * @param args the command line arguments
     */
    
        // TODO code application logic here
    }
    
}
