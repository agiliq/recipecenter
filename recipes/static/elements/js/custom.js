$(document).ready(function()
{
	  // Just cleaning up here
	  $('#top-nav ul li:last a').css('background', 'none');
	  $('#sidebar .box:last-child').css('padding-bottom', '0');
	  $('#sidebar .box li:last-child a').css('margin-bottom', '0').css('border', 'none');
      $('.post:last').css('border', 'none').css('padding-bottom', '0px');
	  
	  $('#page .post').css('margin-bottom', '0');
	  
	  // Pans, Just for show :)
      if (screen.width <= 1024)
	  {
		    $('#pans').css('right', '0%');
	  }
	  
});

function myFocus(element) 
{
	  if (element.value == element.defaultValue) 
	  {
		    element.value = '';
      }
}
function myBlur(element) 
{
      if (element.value == '') 
	  {
            element.value = element.defaultValue;
      }
}

