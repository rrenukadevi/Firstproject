<?php
include("db/config.php");
if(isset($_POST['submit']))
{
    $name=$_POST['name'];
    $email=$_POST['email'];
    $password=$_POST['password'];
    $number=$_POST['MobileNumber'];

    $result=mysqli_query($mysqli, "INSERT INTO  users value('','$name','$email','$password','$number')");
    if($result) {
        echo "User Registred Succesfully, You can login Now";
    }
    else {
        echo "Invalid Data";
    }

}
?>
