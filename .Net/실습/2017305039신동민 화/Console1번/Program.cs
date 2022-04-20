using System;

namespace Console1번
{
    class Program
    {
        enum Color {Red, Green, Blue};
        static void Main()
        {
            Color c = Color.Red;
            int[] color = new int[3];
            for (int i = 0; i < 3; i++)
            {
                color[i] = (int)c;
                c++;
            }
            c = 0;
            foreach (int s in color) {
                Console.WriteLine("color of "+ c + " = " + s);
                c++;
            }
        }
    
    }
}
