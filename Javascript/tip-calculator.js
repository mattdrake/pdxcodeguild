/**
 * Created by matt on 10/2/14.
 */
var people = prompt("How many people are in your party? ");
var bill = prompt("How much was your bill? ");

if (people < 6) {
    alert("Your total tip is $" + bill * tip + ". Press return for your individual total. ");
    new_bill = (bill * (1 + tip)) / people;
    new_bill = new_bill.toFixed(2);
    alert("Your individual bill is $" + new_bill);
}

else {
    alert("Because your party is larger than 6, your gratuity is automatically 18%, totaling $" + bill * .18 + ". Press return for your individual total. ");
    new_bill = (bill*1.18 ) / people;
    new_bill = new_bill.toFixed(2);
    alert("Your individual bill is $" + new_bill);
}