function pcheck(){
    let password = document.getElementById("password").value;
    let cpassord = document.getElementById("cpassword").value;
    if(password==cpassord){
        document.getElementById('password').style.border = "3px solid green";
        document.getElementById('cpassword').style.border = "3px solid green";
    }
    else{
        document.getElementById('password').style.border = "3px solid red";
        document.getElementById('cpassword').style.border = "3px solid red";
    }
}
function pcheck2(){
    let password = document.getElementById("password").value;
    let cpassord = document.getElementById("cpassword").value;
    if(password==cpassord){
        return true;
    }
    else{
        document.getElementById('error').innerHTML = "Password didn't match!!!";
        return false;
    }
}