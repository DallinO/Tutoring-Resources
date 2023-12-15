using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Encapsulation
{
    internal class Order
    {
        private List<Product> _products;
        private Customer _customer;

        public Order(List<Product> products, Customer customer)
        {
            _products = products;
            _customer = customer;
        }

        private float CalculateTotalCost()
        {
            float totalCost = 0;
            foreach (Product x in _products)
            {
                totalCost += x.GetPrice();
            }
            if (_customer.GetAddress().IsInUSA())
                totalCost += 5;
            else
                totalCost += 35;
            return totalCost;
        }

        public string ProductLabel()
        {
            string label = ("-------Products-------\n");
            foreach (Product p in _products)
            {
                label += $"{p.GetName()} {p.GetID()} @ {p.GetPrice().ToString("C")} x {p.GetQuantity()}\n";
            }
            label += $"Total: ${(CalculateTotalCost().ToString("C"), 2)}";
            return label;
        }


        public string ShippingLabel()
        {

            return $"Name: {_customer.GetName()}\n" 
                + $"Address: {_customer.GetAddress().GetAddressString()}";
        }
    }
}
