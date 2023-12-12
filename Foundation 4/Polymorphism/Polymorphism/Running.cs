using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace Polymorphism
{
    internal class Running : Activity
    {
        private double _distance;

        public Running(string date, double length, double distance) : base(date, length)
        {
            _distance = distance;
        }

        protected override double CalculateDistance()
        {
            return _distance;
        }

        protected override double CalculateSpeed()
        {
            return (_distance / _length) * 60;
        }

        protected override double CalculatePace()
        {
            return 60 / CalculateSpeed();
        }
    }
}
