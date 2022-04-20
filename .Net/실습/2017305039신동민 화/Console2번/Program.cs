using System;

namespace Console2번
{
    class Program
    {
        static void Main()
        {
            int sum;
            for (int i = 1; i <= 500; i++)
            {
                sum = 0;
                for (int j = 1; j < i; j++)
                {
                    if (i % j == 0)
                    {
                        sum += j;
                    }
                }
                if (sum == i)
                {
                    Console.WriteLine("완전수: "+ i);
                }
            }
        }
    }
}
