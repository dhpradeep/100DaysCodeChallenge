<!DOCTYPE html>
<html lang="en">
<head>
   <title>Name Generator</title>
</head>
<body>
   <?php 
      //function to generate random name
      function name_generate(){
         $firstName= ["Raju","Pradeep","Pradip","Prabhu","Arjun","Saroj"];
         $lastName= ["Lamsal","Poudel","Dhakal","Gurung","Subedi","Tripathi"];

         $name= $firstName[array_rand($firstName)] . " " . $lastName[array_rand($lastName)];
         //returning name
         / return $name;
      }
      //display generated number
      if(isset($_POST['submit'])){
         echo(name_generate());
      }
   ?>
   <form action="index.php" method="POST">
      <!-- <label for="name">Enter Nam</label>
      <input type="text" name="etrname"/> -->
      <input type="submit" name="submit" value="Submit" />
   </form>
   
</body>
</html>