
$(".dropdown-button").dropdown();
$(".button-collapse").sideNav();

 $('.carousel.carousel-slider').carousel({full_width: false,indicators:true,dist:0,padding:-2});

 function x(){$('.carousel').carousel('next');
} setInterval(x,2000);

$(document).ready(function(){



 $("#hpcontent").click(function(){
        $("#panel1").toggle();

    });

 $("#chpcl").click(function(){
        $("#chklstPanel").toggle();

    });

    $("#flip").click(function(){
        $("#panel").toggle();
            if ($(this).find('#myicondown').text() == 'keyboard_arrow_down')
            {
                $(this).find('#myicondown').text('keyboard_arrow_up');
            }
            else
             {
                 $(this).find('#myicondown').text('keyboard_arrow_down');
             }
    });



});
if(screen.width>480) {
   for(var x=0;x< $(".setrow").length;x++){
        $(".setrow").attr("class","col m4 l4");
    }
}
if(screen.width<=480){

 for(var x=0;x< $(".setrow").length;x++){
            $(".setrow").attr("class","setrow");
            if(x%2==0)
            $(".setrow").eq(x).attr("style","float:left;");
            else  $(".setrow").eq(x).attr("style","float:right;");
     }
}



$(document).ready(function(){
      $('.slider').slider({full_width: true});
    });

$('.carousel.carousel-slider').carousel({full_width: true});


$('#modal1').modal('open');

$('#modal1').modal('close');

$('.modal').modal({
      dismissible: true, // Modal can be dismissed by clicking outside of the modal
      opacity: .5, // Opacity of modal background
      in_duration: 300, // Transition in duration
      out_duration: 200, // Transition out duration
      starting_top: '4%', // Starting top style attribute
      ending_top: '10%', // Ending top style attribute
      ready: function(modal, trigger) { // Callback for Modal open. Modal and trigger parameters available.
         console.log(modal, trigger);
      },
      complete: function() {  } // Callback for Modal close
    }
  );

 $('.chips-initial').material_chip({
    data: [{
      tag: 'FPIC',
    }],
  });

  $('.chips-placeholder').material_chip({
   placeholder: 'Enter a tag',
    secondaryPlaceholder: '+Tag',
  });

  $('.collapsible').collapsible();


 $('.chips').on('chip.add', function(e, chip){
    var keywordForSearch = document.getElementById("keywordForSearch");
   if(keywordForSearch.value == '')
    {
       keywordForSearch.value = chip.tag;
    }
    else
    {
     keywordForSearch.value = keywordForSearch.value+","+chip.tag;
    }
  });


  function Switch_Activate_Content(id,field)
  {
     var topicForContent = document.getElementById("ContentForSearch");
     if(field.checked)
     {
          if(topicForContent.value == '')
            {
               topicForContent.value = id;
            }
            else
            {
             topicForContent.value = topicForContent.value+","+id;
            }
     }
    else
     {
        var n = topicForContent.value.indexOf(id);
        if(n > -1)
        {
           var value = topicForContent.value.split(",");
           y = jQuery.grep(value, function(value) {
              return value != id;
            });
           topicForContent.value = y;
        }

     }

  }
 function Switch_Activate_Topic(id,field)
  {
     var topicForSearch = document.getElementById("topicForSearch");
     if(field.checked)
        {
           if(topicForSearch.value == '')
            {
               topicForSearch.value = id;
            }
            else
            {
             topicForSearch.value = topicForSearch.value+","+id;
            }
        }
        else
         {
            var n = topicForSearch.value.indexOf(id);
            if(n > -1)
            {
               var value = topicForSearch.value.split(",");
               y = jQuery.grep(value, function(value) {
                  return value != id;
                });
               topicForSearch.value = y;
            }

         }
  }

 function Switch_Activate_complexity(id,field)
  {
     var complexityForSearch = document.getElementById("complexityForSearch");

        if(field.checked)
        {
           if(complexityForSearch.value == '')
            {
               complexityForSearch.value = id;
            }
            else
            {
             complexityForSearch.value = complexityForSearch.value+","+id;
            }
         }
         else
         {
            var n = complexityForSearch.value.indexOf(id);
            if(n > -1)
            {
               var value = complexityForSearch.value.split(",");
               y = jQuery.grep(value, function(value) {
                  return value != id;
                });
               complexityForSearch.value = y;
            }
         }
  }

  function Switch_Activate_WritternFor(id,field)
  {
     var writternforForSearch = document.getElementById("writternforForSearch");
     if(field.checked)
       {

           if(writternforForSearch.value == '')
            {
               writternforForSearch.value = id;
            }
            else
            {
             writternforForSearch.value = writternforForSearch.value+","+id;
            }
       }
       else
         {
            var n = writternforForSearch.value.indexOf(id);
            if(n > -1)
            {
               var value = writternforForSearch.value.split(",");
               y = jQuery.grep(value, function(value) {
                  return value != id;
                });
               writternforForSearch.value = y;
            }
         }
  }

   function Switch_Activate_WritternBy(id,field)
  {
     var writternbyForSearch = document.getElementById("writternbyForSearch");
     if(field.checked)
       {
           if(writternbyForSearch.value == '')
            {
               writternbyForSearch.value = id;
            }
            else
            {
             writternbyForSearch.value = writternbyForSearch.value+","+id;
            }
        }
        else
         {
            var n = writternbyForSearch.value.indexOf(id);
            if(n > -1)
            {
               var value = writternbyForSearch.value.split(",");
               y = jQuery.grep(value, function(value) {
                   return value != id;
                });
               writternbyForSearch.value = y;
            }
         }
  }
