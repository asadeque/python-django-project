function validateFormOnSubmit(theForm)
{
   error = "";
   var password = document.getElementById("password").value;
   var confirmPassword = document.getElementById("cpassword").value;

      if (password != confirmPassword)
      {
                document.getElementById("error_cpwd").innerHTML = "Password and confirm Password must be same";
                return false;
      }

     var re = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{7,}/;

    if(!(re.test(theForm.email.value)))
     {
        error = "One number\n One lowercase \n one uppercase letter \n six characters\n";
        fld.style.background = '#F5F5ED';
		document.getElementById("error_pwd").innerHTML = error;
		return false;
     }

      var emailfilter = /(([a-zA-Z0-9\-?\.?]+)@(([a-zA-Z0-9\-_]+\.)+)([a-z]{2,3}))+$/;

       if (!emailfilter.test(fld.value))
        {
           fld.style.background = '#F5F5ED';
           error = "Please enter a valid email address.\n";
           document.getElementById("error_email").innerHTML = error;
           return false;
        }


      if (error != "")
      {
        alert("Some fields need correction:\n" + reason);
        return false;
      }
  return true;
}

function validatePassword(fld,error_place)
{

    var error = "";
    var re = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{7,}/;

    if(!(re.test(fld.value)))
     {
        error = "One number\n One lowercase \n one uppercase letter \n six characters\n";
        fld.style.background = '#F5F5ED';
		document.getElementById(error_place).innerHTML = error;
     }
     else
     {
         document.getElementById(error_place).innerHTML = "";
         fld.style.background = 'White';
     }
   return error;
}


function validateEmail(fld,error_place)
{
    var error="";
    var emailfilter = /(([a-zA-Z0-9\-?\.?]+)@(([a-zA-Z0-9\-_]+\.)+)([a-z]{2,3}))+$/;

   if (!emailfilter.test(fld.value))
    {
       fld.style.background = '#F5F5ED';
       error = "Please enter a valid email address.\n";
	   document.getElementById(error_place).innerHTML = error;
    }
    else
    {
        fld.style.background = 'White';
		document.getElementById(error_place).innerHTML = "";
    }
    return error;
}


function validatecPassword(fld,error_place)
{
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("cpassword").value;

    if (password != confirmPassword)
    {
           document.getElementById("error_cpwd").innerHTML = "Password and confirm Password must be same";
           return false;
    }
    else
    {
        fld.style.background = 'White';
		document.getElementById(error_place).innerHTML = "";
    }
    return error;
}

function validateFormOnLogin(theForm)
{
   error = "";
     reason += validateEmail(theForm.emailid,'error_message_email');
  reason += validatePassword(theForm.pwd,'error_message_pwd');

      if (error != "")
      {
        //alert("Some fields need correction:\n" + reason);
        return false;
      }
  return true;
}
