using System.Diagnostics;

Console.WriteLine("Hello, Please enter the maximum number you need to add");

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


//maximumNumber = Convert.ToInt32(maximumNumberFromUser);

Console.WriteLine($"Are you sure you need to get the addition up to {maximumNumberFromUser}?");
Stopwatch stopwatch1 = Stopwatch.StartNew();
int sum = 0;
for (int iterator = 1; iterator <= maximumNumber; iterator++)
{
    //Console.WriteLine($"iterator = {iterator}, old sum = {sum}");

    sum = sum + iterator;

    //Console.WriteLine($"new sum = {sum}");
}
stopwatch1.Stop();

Stopwatch stopwatch2 = Stopwatch.StartNew();
int seriesSum = maximumNumber * (maximumNumber + 1) / 2;
stopwatch2.Stop();
Console.WriteLine($"The sum of numbers from 1 to {maximumNumber} = {sum}  || Elapsed Seconds = {stopwatch1.Elapsed.TotalMilliseconds} ms");
Console.WriteLine($"The sum of numbers from 1 to {maximumNumber} = {seriesSum} using series form || Elapsed Seconds = {stopwatch2.Elapsed.TotalMilliseconds} ms");




