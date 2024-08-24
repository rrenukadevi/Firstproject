<?php
include("db/config.php");
if(isset($_POST['submit']))
{
    $name=$_POST['name'];
    $emailid=$_POST['email'];
    $password=$_POST['password'];
    $MobileNumber=$_POST['MobileNo'];
    $result=mysqli_query($mysqli, "INSERT INTO users value('','$name','$emailid','$password','$MobileNumber')");
    if($result) {
        echo "User Succesfullly Registered";
    }
    else {
        echo "Invalid Data";
    }

}
?>