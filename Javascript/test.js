/**
 * Created by matt on 10/2/14.
 */
var n = prompt("Check your number", "Type your number here");

n = parseInt(n);

if (n == 0)
{
    alert("The number is zero");
}
else if (n%2)
{
    alert("The number is odd");
}
else
{
    alert("The number is even");
}

