/**
 * Created by matt on 11/12/14.
 */

 $(document).ready(function() {

     $curtainopen = false;

     $(".data_test").hide();

     $(".click-zone").click(function () {

         $(this).blur();
         $("#txtlzr-output").hide();
         $(".data_test").show();

         if ($curtainopen == false) {

             $(this).stop().animate({bottom: '20px' }, {queue: false, duration: 350, easing: 'easeOutBounce'});
             $(".leftcurtain").stop().animate({width: '60px'}, 2000);
             $(".rightcurtain").stop().animate({width: '60px'}, 2000);
             $curtainopen = true;

         } else {

             $(this).stop().animate({bottom: '20px' }, {queue: false, duration: 350, easing: 'easeOutBounce'});
             $(".leftcurtain").stop().animate({width: '50%'}, 2000);
             $(".rightcurtain").stop().animate({width: '51%'}, 2000);
             $curtainopen = false;
             $("#txtlzr-output").show();
             $(".data_test").hide();

         }

         return false;

     });

});



