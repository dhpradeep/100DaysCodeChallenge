<?php
 $text=$_POST['txt'];
//ecryption
if(isset($_POST['enc'])){
    $enc= base64_encode($text); 
    //display chiper text
    echo $enc;
}
//decryption


?>
<html>
    <form action="crypto.php" method="POST">
    <label for="txt">Enter your text:</label>
    <input type="text" name="txt" />
    <br/><br/>
    <button type="submit" name="enc">Encrypt Text</button>
    <button type="submit" name="dc">Decrypt Text</button>
    </form>

</html>
