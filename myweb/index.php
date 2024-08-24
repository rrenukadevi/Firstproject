<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First PHP and MySQL Database Project</title>
    <script>
        function validateForm() {
            var name = document.forms["registrationForm"]["name"].value;
            var email = document.forms["registrationForm"]["email"].value;
            var password = document.forms["registrationForm"]["password"].value;
            var mobileNumber = document.forms["registrationForm"]["MobileNumber"].value;

            if (name == "") {
                alert("Name must be filled out");
                return false;
            }
            if (email == "") {
                alert("Email must be filled out");
                return false;
            }
            if (password == "") {
                alert("Password must be filled out");
                return false;
            }
            if (mobileNumber == "") {
                alert("Mobile Number must be filled out");
                return false;
            }
            if (!/^\d{10}$/.test(mobileNumber)) {
                alert("Mobile Number must be 10 digits");
                return false;
            }
            return true;
        }
    </script>
</head>
<body style="background-color:lightgreen;">
<center>
<form name="registrationForm" action="Register.php" onsubmit="return validateForm()" method="post">
    <h1 style="text-align :center;">Registration Form</h1>
    <p style="text-align:center; font-size: 20px;"><br>
        <label for="name">Name:&ensp;&ensp;&ensp;&ensp;</label>
        <input style="padding: 10px 20px" type="text" name="name" placeholder="Enter your name">
    </p>
    <p style="text-align:center; font-size: 20px;"><br>
        <label for="email">Email:&ensp;&ensp;&ensp;&ensp;</label>
        <input style="padding: 10px 20px" type="email" name="email" placeholder="Enter your email-id">
    </p>
    <p style="text-align:center; font-size: 20px;"><br>
        <label for="password">Password:&ensp;&ensp;&ensp;</label>
        <input style="padding: 10px 20px" type="password" name="password" placeholder="Enter your password">
    </p>
    <p style="text-align:center; font-size: 20px;"><br>
        <label for="number">MobNo:&ensp;&ensp;&ensp;&ensp;</label>
        <input style="padding: 10px 20px" type="number" name="MobileNumber" placeholder="Enter your mobile number">
    </p>
    <input type="submit" name="submit" value="Create Account">
</form>
</center>
</body>
</html>
