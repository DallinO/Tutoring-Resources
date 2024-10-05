public class Journal
{

    public void AddEntry()
    {
        // response = Console.ReadLine()
        Entry entry = new Entry("Date", "My prompt...", "..");
        entry.Date = "...";
        Console.WriteLine(entry.Date);


    }

}
