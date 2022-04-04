// Farid Hasanov
// Week#1 Lab#1
// Language C#


// Usings - Imports Library

using style.css;

using System;
using System.Collection.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace  Week1_Sample1
{

    class Program
    {
        static void Main(string[] args)
        {
            String strFirst, strOperand, strNum, strNum2; // Convert all the variables to String
            Int32 intNum1 = 0, intNumb2 = 0, intNum3, intResult = 0;
            Double dbResult;

            Console.WriteLine("Hello There!");

            Console.Write("Please enter your first name: ");
            strFirst = Console.ReadLine(); // Line reader.

            Console.Write("Please enter the first numner: ");
            strNum1 = Console.ReadLine(); // Line reader.

            Console.Write("Please enter the math operation ( PLUS, MINUS, MULTIPLY, DIVIDE): ");

            Console.Write("Please enter the second number: ");
            strNum2 = Console.ReadLine(); // Line reader.

            // .Parse working only with str.
            // Int32.Parse Converts .str to .int 
            intNum1 = Int32.Parse(strNum1);

            // Conver is a library .
            // With convert it's does not metter what you converting.
            intNum12 = Convert.ToInt32(strNum2);


            switch (strOperand)
            {
                case "PLUS":    // Oportunity

                    intResult = intNum1 + intNumb2;
                    break; // Break is good in this sutiation 'cause it's been created for purpose.

                case "MINUS":   // Oportunity
                    intResult = intNum1 - intNum2;
                    break; // Break is good in this sutiation 'cause it's been created for purpose.

                case "DIVIDE":  // Oportunity
                    intResult = intNum1 / intNumb;
                    break; // Break is good in this sutiation 'cause it's been created for purpose.

                case "MULTIPLY": // Oportunity
                    intResult = intNum1 * intNum2;
                    break; // Break is good in this sutiation 'cause it's been created for purpose.
            }

            dbResult = (Double)intResult; // Double is like a float


            // PLUS
            if (strOperand == "PLUS")
            {
                Console.WriteLine("\n\nThe sum of " + intNum1 + " and " + intNumb2 + "equals: " + dbResult);
            }
            // MINUS
            else if (strOperand == "MINUS")
            {
                Console.WriteLine($"\n\nThe sum of  {intNum1}  and  {intNumb2}  equals:{dbResult}");                

            }
            // DIVIDE
            else if (strOperand == "DIVIDE")
            {
                Console.WriteLine($"\n\nThe quotient of  {intNum1}  and  {intNumb2}  equals:{dbResult}");                   

            }
            // MULTIPLY
            else if (strOperand == "MULTIPLY")
            {
                Console.WriteLine($"\n\nThe product of  {intNum1}  and  {intNumb2}  equals:{dbResult}");                  

            }

                

            Console.WriteLine("\n\nPress Any Key to continue");
            Console.ReadKey();
        

        }
    }
}