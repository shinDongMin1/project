using System;

namespace Console3번
{
    /*
    class Frac
    {
        int number;
        int denominator;
        public Frac(int x = 0, int y = 0)
        {
            number = x;
            denominator = y;
        }
        public static Frac operator +(Frac x, Frac y)
        {
            Frac e = new Frac();
            if (x.denominator != y.denominator)
                e.number = (x.number * y.denominator) + (y.number * x.denominator);
            else
                e.number = x.number + y.number;
            if (x.denominator != y.denominator)
                e.denominator = x.denominator * y.denominator;
            else
                e.denominator = x.denominator;
            return e;
        }

        public void Print()
        {
            Console.WriteLine("Number= " + number + "/" + denominator);
        }
    
    }

    class Cmain {
        static void Main()
        {
            Frac sum = new Frac();
            Frac n1 = new Frac(1, 5);
            Frac n2 = new Frac(3, 4);

            Frac sum1 = new Frac();
            Frac n3 = new Frac(1, 4);
            Frac n4 = new Frac(2, 4);

            sum = n1 + n2;
            sum.Print();

            sum1 = n3 + n4;
            sum1.Print();

        }
    }
    */
    class Program {
        static int i;
        static Program() {
           i = 1000;
        }
        public static void print() {
            Console.WriteLine("{0}",i);
        }

    }
    class CmainP
    {
        static void Main() {

            Program.print();
        }

    }
}
