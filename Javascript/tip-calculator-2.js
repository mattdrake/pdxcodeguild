/**
 * Created by matt on 10/2/14.
 */
    //Define the variables and calculate the tip multiplier//
var people = prompt("How many people are in your party? ");
var bill = prompt("How much was your bill? ");
var tip = prompt("How much would you like tip? 15, 20, or 25 %? ")
tip = tip / 100;

    //if else to change tip multiplier based on party size. More than 6 people requires a greater tip.//
if (people < 6) {
    alert("Your total tip is $" + bill * tip + ". Press return for your individual total. ");
    new_bill = (bill * (1 + tip)) / people;
    new_bill = new_bill.toFixed(2);
    alert("Your individual bill is $" + new_bill);
}
    //Because tip must be at least 18% the 15% choice doesn't apply and user must choose a higher one.//
else {
    if(tip === .15) {
        alert("Hey cheapskate, the minimum is 18%! Press return to choose a more suitable amount. ")
        var larger_tip = prompt("Would you like to do 18, 20 or 25%? ")
        larger_tip = larger_tip / 100
        alert("Your total tip is $" + bill * larger_tip + ". Press return for your individual total. ");
        new_bill = (bill * (1 + larger_tip)) / people;
        new_bill = new_bill.toFixed(2);
        alert("Your individual bill is $" + new_bill);
    }
    else {
        alert("<hey big tipper, your gratuity is $" + bill * tip + ". Press return for your individual total. ");
        new_bill = (bill * (1 + tip)) / people;
        new_bill = new_bill.toFixed(2);
        alert("Your individual bill is $" + new_bill);
    }
}