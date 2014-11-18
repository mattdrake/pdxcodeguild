/**
 * Created by matt on 10/14/14.
 */

var list = ['What are you in the mood for?', 'Click on one of the genres to get started!',];
var txt = $('#txtlzr');

var option = {
    duration: 1000,
    rearrangeDuration: 1000,
    effect: 'random',
    centered: true
};

txt.textualizer(list, options);
txt.textualizer('start');