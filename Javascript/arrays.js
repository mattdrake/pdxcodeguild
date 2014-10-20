/**
 * Created by matt on 10/3/14.
 */


var receipt = {'chicken': 8, 'salad': 6, 'soda': 3};
var name = ['chicken', 'salad', 'soda'];
var nameCosts = [];
for (var i = 0; i < name.length; i++) {
    if (name[i] === receipt) {
        nameCosts.push(receipt[name[i]]);
        }
    }
    else {
        alert(nameCosts);
    }

alert(nameCosts);