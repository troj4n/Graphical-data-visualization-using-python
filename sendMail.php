<?php
ini_set('SMTP','localhost');
ini_set('smtp_port',25);
         $to = "abc@123.com";
         $subject = "Hey!!Someone Left a Feedback";
         $name=$_POST['inputName'];
         $message = $_POST['inputDescription'];
         //$message .= "<h1>This is headline.</h1>";
		 $header  = "From: user";
         //$header   .= $_POST['inputName'];
         //$header = "From:abc@somedomain.com \r\n";
         //$header .= "Cc:afgh@somedomain.com \r\n";
         $header .= "MIME-Version: 1.0\r\n";
         $header .= "Content-type: text/html\r\n";
         
         $retval = mail ($to,$subject,$message,$header);
         
         if( $retval == true ) {
            echo "Message sent successfully...";
         }else {
            echo "Message could not be sent...";
         }
?>