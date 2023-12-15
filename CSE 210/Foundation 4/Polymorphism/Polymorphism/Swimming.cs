using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace Polymorphism
{
    internal class Swimming : Activity
    {
        private double _laps;

        public Swimming(string date, double length, double laps) : base(date, length)
        {
            _laps = laps;
        }

        protected override double CalculateDistance()
        {
            double distance = ((_laps * 50) / 1000);
            return distance;
        }

        protected override double CalculateSpeed()
        {
            return (CalculateDistance() / _length) * 60;
        }

        protected override double CalculatePace()
        {
            return 60 / CalculateSpeed();
        }
    }
}
