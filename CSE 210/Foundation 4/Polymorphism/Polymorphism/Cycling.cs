using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace Polymorphism
{
    internal class Cycling : Activity
    {
        private double _speed;

        public Cycling(string date, double length, double speed) : base(date, length)
        {
            _speed = speed;
            _date = date;
            _length = length;
        }

        protected override double CalculateDistance()
        {
            double distance = _speed * (_length / 60);
            return distance;
        }

        protected override double CalculateSpeed()
        {
            return _speed;
        }

        protected override double CalculatePace()
        {
            return 60 / _speed;
        }
    }
}
