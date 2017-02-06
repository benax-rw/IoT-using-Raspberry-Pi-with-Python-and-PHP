<?php
/*
Created by BAZIRAMWABO GABRIEL from Rwanda, a country of Thousand Hills, on 2017-Feb-06.
This file is a part of basic IoT project. 
It is a contribution the community of coders which made me who I am now in matter of coding.
Use this code as your own. 
If you feel you need to contact me, my email is baziramwabo@gmail.com
*/

$file = "commands.txt";
$handle = fopen($file,'w+');

if (isset($_POST))
{
	
$timestamp = htmlspecialchars($_POST["timestamp"]);
$switch_status = htmlspecialchars($_POST["switch_status"]);
$client_ip = htmlspecialchars($_POST["client_ip"]);

/*

send to DB

*/


if ($switch_status=="ON"){fwrite($handle,"TurnOff");} 
elseif ($switch_status=="OFF"){fwrite($handle,"TurnOn");} 


fclose($handle);

}



?>

