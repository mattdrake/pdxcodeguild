/**
 * Created by matt on 10/9/14.
 */
$(document).ready(function(){
    $("ul").hover(function() {
        $(this).fadeOut(100);
        $(this).fadeIn(200);
    });
    $("ul").mouseenter(function(){
        $(this).css('color','red');
    });
    $("ul").mouseleave(function(){
        $(this).css('color', 'black');
    });
});