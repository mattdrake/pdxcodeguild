/**
 * Created by matt on 10/2/14.
 */
var table_receipt = {chicken: 4.50, salad: 7.50, coffee: 3.50};
function total_bill() {
    table_receipt.total = 0;
    for (var price in table_receipt)
        table_receipt.total += (table_receipt.hasOwnProperty(price));
    alert("The table's total bill is " + table_receipt);
    console.log(table_receipt.total);
}
total_bill()