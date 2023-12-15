using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Polymorphism
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<Activity> list = new()
            {
                new Running("1-1-20XX", 60, 1),
                new Cycling("1-1-20XX", 60, 60),
                new Swimming("1-1-20XX", 60, 20)
            };

            foreach (Activity x in list)
            {
                x.DisplaySummary();
            }
        }
    }
}
