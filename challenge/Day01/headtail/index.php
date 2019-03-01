<?php 
$coin1= rand(1,2);
function ranMsg(){
    $msg_arr=['head','tail'];
    $msg=$msg_arr[array_rand($msg_arr)];
    //return $msg
    return $msg;
}
if(isset($_POST['submit'])){
    $coin1=$_POST['num'];
    if($coin1==1){
        echo(ranMsg());
    }else if($coin1==2){
        echo(ranMsg());
    }else{
        echo "wrong number enter";
    }
}
?>
<html>
    <form action="index.php" method="POST">
        <label for="num">Enter Number</label>
        <input type="number" name="num" />
        <button type="submit" name="submit">Submit</button>
    </form>
</html>
