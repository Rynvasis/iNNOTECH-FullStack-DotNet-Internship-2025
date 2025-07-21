using System.Diagnostics;
using System.Text;

Console.WriteLine("Hello, Please enter the maximum number you need to write");
string? maximumNumberFromUser;
int maximumNumber;

#region add Validation For The maximumNumber
while (true)
{
    maximumNumberFromUser = Console.ReadLine();
    //TODO:: add validation for the maximumNumber

    if (int.TryParse(maximumNumberFromUser, out maximumNumber))
    {
        if (maximumNumber > 0)
        {
            break;
        }
        else
        {
            Console.WriteLine("Please enter a number greater than 0:");
        }
    }
    else
    {
        Console.WriteLine("Invalid input. Please enter a valid integer:");
    }
}
#endregion

maximumNumber = Convert.ToInt32(maximumNumberFromUser);

//string numbers = string.Empty;

Stopwatch stopwatch = Stopwatch.StartNew();

//for (int i = 1; i <= maximumNumber; i++)
//    numbers = $"{numbers}{i},";

//stopwatch.Stop();
//Console.WriteLine(numbers);
//Console.WriteLine($"Old approach, Elapsed Seconds = {stopwatch.Elapsed.TotalSeconds}");


#region String & StringBuilder & Time Complexity
/*************************     Time Complexity(String)     *******************************
Time Complexity with using string instead of StringBuilder is O(n^2) becasue string is immutable
The old content is copied every time
*/

/*************************      StringBuilder      ********************************
 StringBuilder is built using a dynamic character array , it is mutable, adds characters 
 without creating a new object and Time Complexity is O(n)
 */ 
#endregion


stopwatch.Start();
StringBuilder numbersNewApproach = new();

for (int i = 1; i <= maximumNumber; i++)
{
    numbersNewApproach.Append(i);
    if (i != maximumNumber)
        numbersNewApproach.Append(',');
}
    


stopwatch.Stop();

Console.WriteLine(numbersNewApproach);
Console.WriteLine($"New approach, Elapsed Seconds = {stopwatch.Elapsed.TotalSeconds}");
