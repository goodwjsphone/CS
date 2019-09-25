using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Playground
{
    class Program
    {
        static void Main(string[] args)
        {

            /* This is where the code goes*/
            Console.WriteLine("Enter number for operation");
           int num = Convert.ToInt32( Console.ReadLine());
            Console.WriteLine("add?");
            int x = Convert.ToInt32(  Console.ReadLine());
            Console.WriteLine("subtract?");
            int y = Convert.ToInt32( Console.ReadLine());

            if (x == 1)
            { num += 1; }

            if (y == 1)
            { num -= 1; }



            Console.WriteLine("ans = " + num);
            Console.ReadKey();

        }
    }
}
