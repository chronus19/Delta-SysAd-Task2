<?PHP

$uname = "";
$pword = "";
$error = "";

if ($_SERVER['REQUEST_METHOD'] == 'POST'){
	$uname = $_POST['username'];
	$pword = $_POST['password'];
	$pword = md5($pword);				// Hash the password using md5

  $uname = htmlspecialchars($uname);


	//	Connect to the Database

	$user_name = "root";
	$pass_word = "password";
	$database = "delta";
	$server = "127.0.0.1";

    $db = mysqli_connect($server,$user_name,$pass_word,$database);
    
    if ($db) {

    $result = mysqli_query($db,"SELECT * from login where user = '$uname' and passwd = '$pword' ;");
    
    if($result != false)
    if (mysqli_num_rows($result)==1) {
  			// Load an image
  			header('Location: success.jpg');  
    	}
	
    else {
    	$error = "Invalid Credentials ";
    }

    
    mysqli_close($db);
    
    }
    else {
    	$error = "Could not connect to the database" ;
    }


}


?>


<html>
<head>
<title>Basic Login Script</title>
</head>
<body style='background-color:lightblue;'>

<center>
<h1>Delta System Administration - Task 2</h1>
<h3> <?PHP print $error ?> </h3><br/>
<br/>

<FORM NAME ="login" METHOD ="POST" ACTION ="login.php">

Username: <INPUT TYPE = 'TEXT' Name ='username'  value="<?PHP print $uname;?>" maxlength="20">
<br/><br/>
Password: <INPUT TYPE = 'PASSWORD' Name ='password'  value="" maxlength="16">
<br/><br/>

<INPUT TYPE = "Submit" Name = "Submit1"  VALUE = "Login">

</FORM>

</center>


</body>
</html>