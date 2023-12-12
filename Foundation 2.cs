using System;

class Program
{
    static void Main(string[] args)
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
        
        //Add more...
        

class Address
{
    private string _streetAddress;
    private string _city;
    private string _state;
    private string _country;

    public Address(string streetAddress, string city, string state, string country)
    {
        _streetAddress = streetAddress;
        _city = city;
        _state = state;
        _country = country;
    } 

    public bool IsInUSA()
    {
        if (_country.ToUpper() == "USA"|| _country.ToUpper() == "UNITED STATES"){

            return true;
        }
        return false;
    }

    public string GetAddressString()
    {
        return $"Street Address : {_streetAddress}\n" 
            + "City : {_city}\n"
            + "State : {_state}\n"
            + "Country : {_country}";
    }
}



class Customer
{
    private string _name;
    private Address _address;

    public Customer(string name, Address address)
    {
         _name = name;
         _address = address;
    }

    public string GetName()
    {
        return _name;
    }

    public Address GetAddress()
    {
        return _address;
    }
}



class Product
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

    public float TotalPrice()   {return _price * _quantity;}
    public string GetName()     {return _name;}
    public string GetID()       {return _productID;}
    public int GetQuantity()    {return _quantity;}
}



class Order
{
    private List<Product> _products;
    private Customer _customer;

    public Order(List<Product> products, Customer customer)
    {
        _products = products;
        _customer = customer;
    }

    private int CalculateTotalCost()
    {
        int totalCost = 0;
        foreach (Product x in _products)
        {
            totalCost = totalCost + x.TotalPrice();
        }
        if (_customer.GetAddress().IsInUSA())
            totalCost = totalCost + 5;
        else
            totalCost = totalCost + 35;
        return totalCost;
    }

    public string ProductLabel()
    {
        string label = ("-------Products-------\n");
        foreach(Product p in _products)
        {
            label += "{p.GetName()} {p.GetID()} @ {p.GetPrice()} x {p.GetQuantity()}\n";
        }
        label += "Total: {CalculateTotalCost()}"; 
        return label;
    }


    public string ShippingLabel(){

        return $"Name: {_customer.GetName()}\n" 
            + "Address: {_customer.GetAddress().GetAddressString()};
    }
}



