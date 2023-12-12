using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Inheritance
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            Lecture lecture = new("Lecture", "Example lecture.", "1-1-2001", "12:00pm", new Address("123 Main ST", "Metropolis", "XX", "USA"), "John Doe", 50);

            Console.WriteLine(lecture.StandardDetails() + "\n");
            Console.WriteLine(lecture.ShortDescription() + "\n");
            Console.WriteLine(lecture.FullDetails() + "\n");

            Reception reception = new("Reception", "Example reception.", "1-1-2001", "12:00pm", new Address("123 Main ST", "Metropolis", "XX", "USA"), "JohnDoe@email.com");

            Console.WriteLine(reception.StandardDetails() + "\n");
            Console.WriteLine(reception.ShortDescription() + "\n");
            Console.WriteLine(reception.FullDetails() + "\n");

            OutdoorGathering outdoorGathering = new("Lecture", "Example lecture.", "1-1-2001", "12:00pm", new Address("123 Main ST", "Metropolis", "XX", "USA"), "Cloudy with a chance of rain.");

            Console.WriteLine(outdoorGathering.StandardDetails() + "\n");
            Console.WriteLine(outdoorGathering.ShortDescription() + "\n");
            Console.WriteLine(outdoorGathering.FullDetails() + "\n");
        }
    }
}
