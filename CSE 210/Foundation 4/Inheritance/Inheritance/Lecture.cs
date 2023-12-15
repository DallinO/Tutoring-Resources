using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace Inheritance
{
    internal class Lecture : Event
    {
        private string _speaker;
        private int _capacity;

        public Lecture(string title, string description, string date, string time, Address address, string speaker, int capacity) : base(title, description, date, time, address)
        {
            _type = "Lecture";
            _speaker = speaker;
            _capacity = capacity;
        }

        public string FullDetails()
        {
            return $"{StandardDetails()}\nSpeaker: {_speaker}\nCapacity: {_capacity}";
        }
    }
}
