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


if (isset($_GET['command'])){

fwrite($handle,$_GET['command']);
fclose($handle);
goto MAIN;

}

MAIN:
?>




<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width,initial-scale=1">
		<title>IoT Example</title>
		<link rel="stylesheet" href="style.css">
		<link rel="stylesheet" href="http://code.jquery.com/mobile/1.4.0/jquery.mobile.structure-1.4.0.min.css" />
		<link rel="stylesheet" href="themes/jquery.mobile.icons.min.css" />
		<script src="http://code.jquery.com/jquery-1.8.2.min.js"></script>
		<script src="http://code.jquery.com/mobile/1.4.0/jquery.mobile-1.4.0.min.js"></script>
	</head>
	
	
	<body>
		<div data-role="page" data-theme="a">
			<div data-role="header" data-position="inline">
				<h1>IoT Example</h1>

			</div>
			
			
			<div data-role="content" data-theme="a">


				
				
				

				<form action="" method="GET">


					
					

					<div class="ui-body ui-body-b">
						<fieldset class="ui-grid-a">
						
						
						<?php
						//initializing by reading the current command

						$command = file_get_contents("commands.txt");
						if ($command=="TurnOn"){
						?>
						
													
							<div class="ui-block">
							<button type="submit" name ="command"  value = "TurnOff" data-theme="a">TURN OFF</button>
							</div>
						<?php
						}else{	
						?>	

					
						
							<div class="ui-block">
							<button type="submit" name ="command"  value = "TurnOn" data-theme="d">TURN ON</button>
							</div>
							
						<?php
						}
						?>
							
							
					    </fieldset>
					</div>
				</form>

			</div>
		</div>
	</body>
</html>