<?php 
// simple encryption without user input
$txt="rajusoft";
$enc=base64_encode($txt);
echo $enc;
//description
$dc=base64_decode($enc);
echo '<br/><br/>';
echo $dc;

?>
