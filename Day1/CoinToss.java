/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package cointoss;

import java.util.Scanner;

public class CoinToss
    {   
       public void toss()
                {
             
                    Scanner take = new Scanner(System.in);
                 
                    System.out.println("Enter the number of runs (1 - 10):" );
                    int r = take.nextInt();
                 
                    System.out.println("Enter the number of toss per run (1 - 5): ");
                    int t = take.nextInt();
                     
                    if(r<=10 && t<=5)
                        {
                            for (int run = 0; run < r; run++) 
                                {
                                    for (int toss = 0; toss < t; toss++)
                                        System.out.print(Math.random() < 0.5 ? "H " : "T ");//This fragment generates a random value between 0.0 and 1.0; if the random value is below 0.5, then it prints ``heads.''
                                        System.out.println();
                                }
                        } 
                    else
                        System.out.println("Please check your entry and try again.");
                         
                }
                 
        public static void main(String[] args)
            {
                CoinToss coin = new CoinToss();
                 
                coin.toss();
            }
 
    }
