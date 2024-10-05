public class Entry
{
    private string _date; //0x0023453
    private string _prompt;
    private string _response;

    public string Date
    { 
        get { return _date; } 
        set { _date = value; }
    }

    public string Prompt { get; set; }
    public string Response { get; set; }


    public Entry()
    {
    }

    public Entry(Entry entry)
    {
        _date = entry.GetDate();
        _prompt = entry.GetPrompt();
        _response = entry.GetResponse();
    }

    public Entry(string date, string prompt, string response)
    {
        _date = date;
        _prompt = prompt;
        _response = response;
    }

    public void Display()
    {
        Console.WriteLine(_date);
        Console.WriteLine(_prompt);
        Console.WriteLine(_response);
    }
}
