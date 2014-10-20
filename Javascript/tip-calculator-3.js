/**
 * Created by matt on 10/3/14.
 */

var itemArray = [];
var receipt = {
    chicken: 8.00,
    salad: 2.00,
    soda: 1.00
}

function name() {
    var name = prompt("Please tell us your name. ");
    var name = itemArray;
    createList();
}

function createList() {
    var item = prompt("Tell us what you had. ");
    itemArray.push(item);
    var anymore = prompt("Anymore items? ");
    if (anymore === "yes") {
        createList();
    }
    else {
        alert(itemArray);

    }
}

//function individualTotal() {
//    for (item in name);
//    {
//        for (name in receipt);
//        {
//            return receipt(0, 1);
//        }
//    }
//}
name();
