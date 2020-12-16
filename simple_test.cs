using System;
using System.Collections.Generic;
using System.Diagnostics;

class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("\nGet ready to play... Press any key when ready.");
        Console.ReadLine();
        var random = new Random();
        var list = new List<string> { "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" };
        int index = random.Next(list.Count);

        Stopwatch stopWatch = new Stopwatch();
        stopWatch.Start();

        Console.WriteLine(list[index]);
        var randomChosen = (list[index]);

        string answer = Console.ReadLine();
        if (answer == null || answer != randomChosen)
            {
                Console.WriteLine("\nYour answer is incorrect. Please play again.");
            }
        if (answer == randomChosen)
        {
            Console.WriteLine("Congratulations! You are not an idiot. Thanks for playing. Here is your time- \n");
        }

        TimeSpan ts = stopWatch.Elapsed;
        string elapsedTime = String.Format("{0:00}:{1:00}.{2:00}", ts.Minutes, ts.Seconds, ts.Milliseconds / 10);

        Console.WriteLine("\nRunTime " + elapsedTime);
    }
}