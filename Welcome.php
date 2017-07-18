
<html>
<?php session_start();
if(!isset($_COOKIE['cook_username']))
{
	header("Location: http://10.68.196.163/wp-login.php");
	$_SESSION['message'] = '<div class="alert alert-danger comments" style="text-align:center;"><strong>Please login to continue.</strong></div>';
	exit();
}


?>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" />
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

<script>

function startTimer()
{


 $(document).ready(function(){
     $("mytag").click(function(){
         $("mytag").fadeOut(2000);
     });
 });

}
</script>
<style type="text/css">
.question
{
	font-family : "Century Gothic";
	font-weight:600;
	color:#4286f4;
	font-size:14px;
}
.answer
{
	font-family : "Century Gothic";
	color:#8c5836;
	font-weight:300;
	
}
.divmid
{
	word-wrap: break-word;
}
.comments
{
	font-family : "Century Gothic";
	font-weight:600;
}
glyphicon:hover
{
	color:black;
}

</style>
<body>
<!--<div id="snackbar">Scroll Down to See More</div>-->

	<!--whole page div-->
	<div class="container" style="width: 100%;overflow:visible;">
		<nav class="navbar navbar-default">
		<div class="container-fluid">
			<div class="navbar-header">
			<a class="navbar-brand" href="Welcome.php"><strong class='comments'>Knowledge Level Survey</strong></a>
			</div>
		<ul class="nav navbar-nav">
			<li class="active"><a href="#"><p class='comments'>Home</p></a></li>
			<li><a href="http://10.68.196.163"><p class='comments'>Transmit</p></a></li>
			<!--<li><a href="#">Link</a></li>-->
		</ul>
			
			
			<button class="btn btn-danger navbar-btn pull-right comments" onclick="startTimer();" id='dashboard' name='dashboard' data-toggle="modal" data-target="#loginModal"><span class="glyphicon glyphicon-stats"></span>&nbsp;Dashboard</button>
			<button class="btn btn-danger navbar-btn pull-right comments" data-toggle="modal" data-target="#commentsModal" style="margin-right: 16px"><span class="glyphicon glyphicon-eye-open"></span>&nbsp;See what others want to learn</button>
			<button class="btn btn-danger navbar-btn pull-right comments" data-toggle="modal" data-target="#participantsModal" style="margin-right: 16px"><span class="glyphicon glyphicon-user"></span>&nbsp;See Participants</button>
		</div>
		</nav>
		<!-- Modal for  DASHBOARD STARTS HERE-->
	<div id="loginModal" class="modal fade" role="dialog">
		<div class="modal-dialog modal-lg">
			
    <!-- Modal content-->
			<div class="modal-content">
				<div class="modal-header">
					<button type="button" class="close" data-dismiss="modal">&times;</button>
					<h4 class="modal-title comments" style="text-align:center;font-size:34px;">Dashboard&nbsp;&nbsp;<span class="glyphicon glyphicon-stats"></span></h4>
				</div>
			<div class="modal-body">
			<mytag id='h'>
				
			
				<!--Code the login content here-->
				<div id="alert_message" class="alert alert-warning"><span><strong>Note:&nbsp;</strong> Please scroll down to view other plots.</span></div></mytag>
				<div class="divtop" style="display:inline-block;overflow:auto;"><?php $python=`python pie.py`; echo $python;?></div><br/>
				<div class="divmid" style="display:inline-block;overflow:visible;"><?php $python=`python hist.py`; echo $python;?></div><br/>
				<div class="divbottom" style="display:inline-block;overflow:hidden;"><?php $python=`python scatter.py`; echo $python;?></div>
				<!--div body for the graphs starts-->
				
				<!--div body for the graphs ends-->
			</div>
			<div class="modal-footer">
				<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
			</div>
			</div>

		</div>
	</div>
		<!-- Modal for  DASHBOARD ENDS HERE-->
		
		
		
		
	<!--Modal for See Parcipants starts here-->
	<!-- Modal -->
<div id="participantsModal" class="modal fade" role="dialog">
  <div class="modal-dialog">

    <!-- Modal content-->
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title comments" style="text-align:center;font-size:34px;">Participants&nbsp;&nbsp;<span class="glyphicon glyphicon-user"></span></h4>
      </div>
      <div class="modal-body">
        <!--php code to database querying-->
			<?php
			if($_COOKIE['cook_username']=="admin")
			{
			#session_start();
			$servername = "localhost";
			$username = "root";
			$password = "root";
			$dbname = "wordpress";
			//$tester="test string";
			// Create connection
			$conn = new mysqli($servername, $username, $password, $dbname);

			// Check connection
			if ($conn->connect_error) {
				die("Connection failed: " . $conn->connect_error);
			} 
			
			//db retrieve values
			$sql = "SELECT wp_users.display_name,wp_kmsurvey_comments.tval from wp_kmsurvey_comments inner join wp_users on wp_users.ID=wp_kmsurvey_comments.ID ";
			$result = $conn->query($sql);
			?>
			<table class="table table-striped">                     
				<div class="table responsive">
					<thead>
						<tr>
							<th>Name</th>
							<th>Date</th>
                        </tr>
					</thead>
			<tbody>
			<?php
			if ($result->num_rows > 0) {
			// output data of each row
			while($row = $result->fetch_assoc()) {
					
					echo '<tr>
						<td class="comments">' . $row["display_name"] .'</td>
						<td class="comments"> '.$row["tval"] .'</td></p>
						</tr>';
					
				}
				
			} 
			else 
			{
			echo "Sorry ! No users have taken the Survey yet";
			}
			$conn->close();	
			}
			else
			{
				echo("<p class='comments'>Sorry ! You're not allowed to view this page.Please contact System Administrator.</p>");
			}
			?>
			</tbody>
			</div>
			</table>
		
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
      </div>
    </div>

  </div>
</div>
	<!--Modal for See Parcipants ends here-->

	
	
	
	
	
<!--Modal for see what others want STARTS HERE-->
	<div id="commentsModal" class="modal fade" role="dialog">
		<div class="modal-dialog modal-lg">

    <!-- Modal content-->
			<div class="modal-content">
				<div class="modal-header">
					<button type="button" class="close" data-dismiss="modal">&times;</button>
					<h4 class="modal-title comments" style="text-align:center;font-size:34px;">See what your colleagues want to learn</h4>
				</div>
			<div class="modal-body">
				<!--Code the php content here-->
				
				<!--php for comments data starts here ============================================================-->
			<?php
			#session_start();
			$servername = "localhost";
			$username = "root";
			$password = "root";
			$dbname = "wordpress";
			$tester="test string";
			// Create connection
			$conn = new mysqli($servername, $username, $password, $dbname);

			// Check connection
			if ($conn->connect_error) {
				die("Connection failed: " . $conn->connect_error);
			} 
			
			
			//db retrieve values	
			$sql = "SELECT wp_users.display_name,wp_kmsurvey_comments.comment from wp_kmsurvey_comments inner join wp_users on wp_users.ID=wp_kmsurvey_comments.ID ";
			$result = $conn->query($sql);
			
			if ($result->num_rows > 0) {
			// output data of each row
				while($row = $result->fetch_assoc()) {
					?><p class="comments"><?php echo  $row["display_name"];
					echo  " left a comment:  " . $row["comment"]. "<br>";?></p><?php
					
				}
				
			} 
			else 
			{
			echo "No Comments Found";
			}
			$conn->close();
			?>				
				<!--php for comments data ends here==============================================================-->
			</div>
			<div class="modal-footer">
				<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
			</div>
			</div>

		</div>
	</div>	
		
<!--Modal for see what others want ENDS HERE-->
		
		
		
		
		<!--left div contains questions-->
		<div class="container-fluid" style="width: 600px; float: left;">
			
			<p class="lead bg-primary comments" style="text-align:center;">Welcome, <?php echo ($_COOKIE['cook_username']); #echo $_COOKIE['cook_id']?></p>
			<!--retrieve from databse here-->
			
			<?php
			
			$servername = "localhost";
			$username = "root";
			$password = "root";
			$dbname = "wordpress";

			// Create connection
			$conn = new mysqli($servername, $username, $password, $dbname);

			// Check connection
			if ($conn->connect_error) {
				die("Connection failed: " . $conn->connect_error);
			} 
			?>
			<form action="#" method="POST" class="ac-custom ac-checkbox ac-cross">
			<?php
			$x=1;
			//db retrieve values
			
			$sql = "SELECT question FROM wp_kmsurvey_questions";
			$result = $conn->query($sql);
			
			if ($result->num_rows > 0) {
			// output data of each row
				while($row = $result->fetch_assoc()) {
					echo  " <p class='question'>{$x}: " . $row["question"]. "</p>";
					#test plane for radio=========================================
					$radio="radio{$x}";
					$check=$x;
					$x++;
					
					?>
					<input type="radio" name=<?php echo $radio?> value="1" required autofocus><span class='answer'>Yes</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
					<input type="radio" name=<?php echo $radio?> value="0" required autofocus><span class='answer'>No</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
					<input type="checkbox" name="checkbox[]" value=<?php echo $check ?>><span class='answer'>Yes,I want to learn</span><br/><br/><br/>
					<?php
					#test plane ends==============================================
				}
				?>
			<?php	
			} 
			else 
			{
			echo "No Questions Found";
			}
			$conn->close();
			?>
			<p class="question">What else do you want to Learn?</p><textarea rows="3" cols="50" name='learnData' placeholder='Tell us what do you want to learn' required autofocus></textarea><br/><br/>
			<button type ="submit" name='submit' class="btn btn-info"  onclick="return confirm('Are you sure?')">Submit</button><br/><br/><br/><br/>
			</form>			
		</div>
		<!--left div contains questions ends here-->
		
		
		 <?php
		 if(isset($_POST['submit']))
		 {
			// #inset answers to db here
			$servername = "localhost";
			$username = "root";
			$password = "root";
			$dbname = "wordpress";
			$conn = new mysqli($servername, $username, $password, $dbname);

			// Check connection
			if ($conn->connect_error) {
				die("Connection failed: " . $conn->connect_error);
			} 
			
			#echo "connected successfully";
				$user=$_COOKIE['cook_id'];
				#echo $user;
				
				$answer1=$_POST['radio1'];
				$answer2=$_POST['radio2'];
				$answer3=$_POST['radio3'];
				$answer4=$_POST['radio4'];
				$answer5=$_POST['radio5'];
				$answer6=$_POST['radio6'];
				$answer7=$_POST['radio7'];
				$answer8=$_POST['radio8'];
				$answer9=$_POST['radio9'];
				$answer10=$_POST['radio10'];
				$id=[];
				$id[]=$user;
				#print_r($id);
				$date=date('n');
				if($answer1== '1'){$sq="update wp_kmsurvey_data set qA=qA+1 where ques_id=1;update wp_kmsurvey_month_data set q1=q1+1 where month_id=$date;";} 
				if($answer2== '1'){$sq.="update wp_kmsurvey_data set qA=qA+1 where ques_id=2;update wp_kmsurvey_month_data set q2=q2+1 where month_id=$date;";}
				if($answer3== '1'){$sq.="update wp_kmsurvey_data set qA=qA+1 where ques_id=3;update wp_kmsurvey_month_data set q3=q3+1 where month_id=$date;";} 
				if($answer4== '1'){$sq.="update wp_kmsurvey_data set qA=qA+1 where ques_id=4;update wp_kmsurvey_month_data set q4=q4+1 where month_id=$date;";} 
				if($answer5== '1'){$sq.="update wp_kmsurvey_data set qA=qA+1 where ques_id=5;update wp_kmsurvey_month_data set q5=q5+1 where month_id=$date;";} 
				if($answer6== '1'){$sq.="update wp_kmsurvey_data set qA=qA+1 where ques_id=6;update wp_kmsurvey_month_data set q6=q6+1 where month_id=$date;";} 
				if($answer7== '1'){$sq.="update wp_kmsurvey_data set qA=qA+1 where ques_id=7;update wp_kmsurvey_month_data set q7=q7+1 where month_id=$date;";} 
				if($answer8== '1'){$sq.="update wp_kmsurvey_data set qA=qA+1 where ques_id=8;update wp_kmsurvey_month_data set q8=q8+1 where month_id=$date;";} 
				if($answer9== '1'){$sq.="update wp_kmsurvey_data set qA=qA+1 where ques_id=9;update wp_kmsurvey_month_data set q9=q9+1 where month_id=$date;";} 
				if($answer10== '1'){$sq.="update wp_kmsurvey_data set qA=qA+1 where ques_id=10;update wp_kmsurvey_month_data set q10=q10+1 where month_id=$date;";}
				$msg=$_POST['learnData'];
				$query="Insert into `wp_kmsurvey_comments`(`ID`,`comment`) values ($user,'$msg');";
				mysqli_query($conn,$query);
				
				// if($conn->multi_query($sq))
				// {
					// echo ("data added successfully");
					
					
				// }
				// else
				// {
					// #echo ("Some error occured");
				// }
				
				if(!empty($_POST['checkbox']))
				{
					foreach($_POST['checkbox'] as $selected)
					{
						if($selected=='1'){$sq.="update wp_kmsurvey_data set qC=qC+1 where ques_id=1;";}
						if($selected=='2'){$sq.="update wp_kmsurvey_data set qC=qC+1 where ques_id=2;";}
						if($selected=='3'){$sq.="update wp_kmsurvey_data set qC=qC+1 where ques_id=3;";}
						if($selected=='4'){$sq.="update wp_kmsurvey_data set qC=qC+1 where ques_id=4;";}
						if($selected=='5'){$sq.="update wp_kmsurvey_data set qC=qC+1 where ques_id=5;";}
						if($selected=='6'){$sq.="update wp_kmsurvey_data set qC=qC+1 where ques_id=6;";}
						if($selected=='7'){$sq.="update wp_kmsurvey_data set qC=qC+1 where ques_id=7;";}
						if($selected=='8'){$sq.="update wp_kmsurvey_data set qC=qC+1 where ques_id=8;";}
						if($selected=='9'){$sq.="update wp_kmsurvey_data set qC=qC+1 where ques_id=9;";}
						if($selected=='10'){$sq.="update wp_kmsurvey_data set qC=qC+1 where ques_id=10;";}
						
					}
				}
					
					echo $q;
					if($conn->multi_query($sq))
					{
						#echo "success";
					}
					else
					{
						
						#echo "error";
						}
				
				session_start();
				$counter_name="counter.txt";
				if(!file_exists($counter_name))
				{
					$f=fopen($counter_name,"w");
					fwrite($f,"0");
					fclose($f);
				}
				$f=fopen($counter_name,"r");
				$counterval=fread($f,filesize($counter_name));
				fclose($f);
				if(!isset($_SESSION['hasVisited']))
				{
					$_SESSION['hasVisited']="yes";
					$counterval++;
					$f=fopen($counter_name,"w");
					fwrite($f,$counterval);
					fclose($f);
				}
				#echo ("You are visitor number $counterval");
				
				echo"<script type=\"text/javascript\">
				 document.location.href='success.html';
				 </script>";
				
				
		 }	
		
		
		 ?>
		
		<!--right div containing images-->
		<div style="margin-left: 620px;">
			<img src="background.jpg" class="img-circle pull-right" alt="Backgroung Image"/>
		</div>
		<!--right div containing images ends-->
		
		<!--div for FOOTER CONTENT STRATS HERE-->
		 <div class="navbar navbar-default navbar-fixed-bottom">
			<div class="container">
				<p class="navbar-text pull-left comments">&copy; Google Limited @
				<a href="https://www.google.com/" target="_blank" >Google</a>
				</p>
				<!--<a href="#" class="navbar-btn btn-danger btn pull-right comments" data-toggle="modal" data-target="#feedbackModal">
				<span class="glyphicon glyphicon-star"></span>&nbsp;Submit your Feedback</a>-->
			</div>
		</div>
		<!-- div for FOOTER CONTENTS ENDS HERE -->

		<!-- Modal for feedback STARTS HERE -->
	<div id="feedbackModal" class="modal fade" role="dialog">
		<div class="modal-dialog modal-lg">

    <!-- Modal content-->
			<div class="modal-content">
				<div class="modal-header">
					<button type="button" class="close" data-dismiss="modal">&times;</button>
					<h2 class="modal-title comments">Feedback</h2>
				</div>
			<div class="modal-body">
				<!--Code the feedback content here-->
				<form action="sendMail.php" method="POST"> 
					<h1><small>Enter your Name</small></h1><input type="text" size="45" name="inputName" required autofocus>
					<h1><small>Description</small></h1><textarea name="inputDescription" cols="50" rows="5" required autofocus></textarea>
				
			</div>
			<div class="modal-footer">
				<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
				<button type="button submit" class="btn btn-danger">Submit</button>
			</div>
			</form>
			</div>

		</div>
	</div>
	<!-- Modal for feedback ENDS HERE -->
	
	<!--whole page div ends here-->
	</div>

</body>
</html>