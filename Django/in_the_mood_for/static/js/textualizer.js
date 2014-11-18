/**
 * Created by matt on 11/13/14.
 */
 $(document).ready(function() {

     var list = ['What are you in the mood for?', 'Click on a genre to get started!'];
     var output = $("#txtlzr-output");
     var options = {
         duration: 1000,          // Time (ms) each blurb will remain on screen
         rearrangeDuration: 250, // Time (ms) a character takes to reach its position
         effect: 'random',        // <a href="http://www.jqueryscript.net/animation/">Animation</a> effect the characters use to appear
         centered: true           // Centers the text relative to its container
     };
     output.textualizer(list, options);
     output.textualizer('start');
 });