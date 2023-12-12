using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Encapsulation
{
    internal class Product
    {
        private string _name;
        private string _productID;
        private float _price;
        private int _quantity;

        public Product(string name, string productID, float price, int quantity)
        {
            _name = name;
            _productID = productID;
            _price = price;
            _quantity = quantity;
        }

        public float GetPrice() { return _price * _quantity; }
        public string GetName() { return _name; }
        public string GetID() { return _productID; }
        public int GetQuantity() { return _quantity; }
    }
}
