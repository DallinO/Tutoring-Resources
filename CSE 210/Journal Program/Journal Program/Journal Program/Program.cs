public class Program
{
    static void Main(string[] args)
    {
        // Faciliate overall logic of program
        int age = 24;
        Job job1 = new Job();
        job1._positionTitle = "Software Engineer";
        job1._company = "Microsoft";
        job1._description = "...";
        job1.SetSalary(50000);
        Console.WriteLine(job1.Display());



        Job job2 = new Job();
        job2._positionTitle = "System Architect";
        job2._company = "Apple";
        job2._description = "...";
        job2.SetSalary(90000);
        Console.WriteLine(job2.Display());
    }
}