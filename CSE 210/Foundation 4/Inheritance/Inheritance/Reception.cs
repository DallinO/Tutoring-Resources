using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace Inheritance
{
    internal class Reception : Event
    {
        private string _email;

        public Reception(string title, string description, string date, string time, Address address, string email) : base(title, description, date, time, address)
        {
            _type = "Reception";
            _email = email;
        }
        public string FullDetails()
        {
            return $"{StandardDetails()}\nEmail: {_email}";
        }
    }
}
