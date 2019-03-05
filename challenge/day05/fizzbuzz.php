<?php
/**
 * @author:Raju Lamsal
 * @copyright 2019
 * 
*/ 
for($i=1;$i<=100;$i++){
    if($i%15==0 and $i%5==0){
        echo "<br/> Fizzbuzz";
    }elseif($i%3==0){
        echo "<br/> Fizz";
    }elseif($i%5==0){
        echo "<br/> Buzz";
    }else{
        echo "<br/>" . $i;
    }
}
?>