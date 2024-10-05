public class Job
{
    // Attributes (Class Variables, Class Members)
    public string _positionTitle;
    public string _company;
    private double _salary;
    public DateTime _startDate;
    public DateTime _endDate;
    public string _description;

    // Constructors (Special Methods For Initializing A Class)
    public Job()
    { }

    // Methods (Class Function, Behaviours)
    //[ACCESS TYPE] [RETURN TYPE] [NAME]([PARAMETERS])
    public string Display()
    {
        string display = 
            $"Title: {_positionTitle}\n" +
            $"Company: {_company}\n" +
            $"Salary: {_salary}\n" +
            $"Description: {_description}\n";

        return display;
    }

    public void SetSalary(int value)
    {
        _salary = value; 
    }

}