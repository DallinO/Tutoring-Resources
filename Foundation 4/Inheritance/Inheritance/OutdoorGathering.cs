using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace Inheritance
{
    internal class OutdoorGathering : Event
    {
        private string _weather;

        public OutdoorGathering(string title, string description, string date, string time, Address address, string weather) : base(title, description, date, time, address)
        {
            _type = "Outdoor Gathering";
            _weather = weather;
        }

        public string FullDetails()
        {
            return $"{StandardDetails()}\nWeather: {_weather}";
        }
    }
}
