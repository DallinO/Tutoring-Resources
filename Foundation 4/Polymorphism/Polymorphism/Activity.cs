using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Polymorphism
{
    internal abstract class Activity
    {
        protected string _date;
        protected double _length;

        public Activity(string date, double length)
        {
            _date = date;
            _length = length;
        }

        protected abstract double CalculateDistance();
        protected abstract double CalculateSpeed();
        protected abstract double CalculatePace();
        public void DisplaySummary()
        {
            Console.WriteLine($"{_date} Swimming ({_length} min)\n\tDistance: {Math.Round(CalculateDistance(), 2)} km\n\tSpeed: {Math.Round(CalculateSpeed(), 2)} Kph\n\tPace: {Math.Round(CalculatePace(), 2)} min per km");
        }
    }
}
