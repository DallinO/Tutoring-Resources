using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Encapsulation
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            List<Product> products1 = new()
            {
                new Product("Product1", "001", 2.50f, 2),
                new Product("Product2", "002", 6.15f, 1),
                new Product("Product3", "003", 15.70f, 1)
            };
            Order order1 = new(products1, new Customer("John Doe", new Address("123 Main St", "City", "State", "USA")));

            Console.WriteLine(order1.ShippingLabel());
            Console.WriteLine(order1.ProductLabel());
        }
    }
}
