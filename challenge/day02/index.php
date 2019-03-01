<?php
//temp.php
//Celsius to Fahrenheit ° F = 9/5 ( ° C) + 32
//Fahrenheit to Celsius ° C = 5/9 (° F - 32)
//Celsius to Kelvin K = ° C + 273.15
//Kelvin to Celsius ° C = K - 273.15
//Fahrenheit to Kelvin K = 5/9 (° F - 32) + 273.15
//Kelvin to Fahrenheit 	° F = 9/5 (K - 273.15) + 32
//Fahrenheit to celsius
function fahrenheit_to_celsius($given_value)
{
	$celsius=5/9*($given_value-32);
	return $celsius ;
}
//Fahrenheit to kelvin
function fahrenheit_to_kelvin($given_value)
{
	$kelvin=fahrenheit_to_celsius($given_value) + 273.15;
	return $kelvin ;
}
//Celsius to fahrenheit
function celsius_to_fahrenheit($given_value)
{
	$fahrenheit=$given_value*9/5+32;
	return $fahrenheit ;
}
//Celsius to kelvin 
function celsius_to_kelvin($given_value)
{
	$kelvin=$given_value+273.15;
	return $kelvin ;
}
//Kelvin to fahrenheit equation
function kelvin_to_fahrenheit($given_value)
{
	$fahrenheit=9/5*($given_value-273.15)+32;
	return $fahrenheit ;
}
//Kelvin to celsius equation
function kelvin_to_celsius($given_value)
{
	$celsius=$given_value-273.15;
	return $celsius ;
}
?>



<html>
<head>
	<title>Temp. Conv.</title>
</head>
<body>
	<form action="" method="post">
				<select name="first_temp_type_name">
					<option value="fahrenheit">Fahrenheit</option>
					<option value="celsius">Celsius</option>
					<option value="kelvin"> Kelvin</option>
				</select>
				<input type="text" name="given_value">
				<select name="second_temp_type_name">
					<option value="fahrenheit">Fahrenheit</option>
					<option value="celsius">Celsius</option>
					<option value="kelvin">Kelvin</option>
				</select>
				<input type="submit" name="btn" value="Convert">
<?php
if(isset($_POST['btn']))
{
    
    $first_temp_type_name=$_POST['first_temp_type_name'];
    $second_temp_type_name=$_POST['second_temp_type_name'];
    $given_value=$_POST['given_value'];
    
    //Fahrenheit to celsius and kelvin
    if ($first_temp_type_name=='fahrenheit') 
    {
        if ($second_temp_type_name=='celsius') 
        {
            $celsius=fahrenheit_to_celsius($given_value);
            echo "$given_value Fahrenheit = $celsius Celsius";
        }  elseif ($second_temp_type_name=='kelvin') 
        {
            $kelvin=fahrenheit_to_kelvin($given_value);
            echo "$given_value Fahrenheit = $kelvin Kelvin";
        }  else 
        {
            echo "$given_value Fahrenheit";
        }
    }
    //Celsius to fahrenheit and kelvin
    if ($first_temp_type_name=='celsius') 
    {
        if ($second_temp_type_name=='fahrenheit') 
        {
            $fahrenheit=celsius_to_fahrenheit($given_value);
	        echo "$given_value Celsius  = $fahrenheit Fahrenheit";
        }  elseif ($second_temp_type_name=='kelvin') 
        {
            $kelvin=celsius_to_kelvin($given_value);
            echo "$given_value Celsius   = $kelvin Kelvin";
        }  else 
        {
            echo "$given_value Celsius";
        }
    }
    //Kelvin to fahrenheit and celsius
    if ($first_temp_type_name=='kelvin') 
    {
        if ($second_temp_type_name=='fahrenheit') 
        {
            $fahrenheit=kelvin_to_fahrenheit($given_value);
            echo "$given_value Kelvin  = $fahrenheit Fahrenheit";
        }  elseif ($second_temp_type_name=='celsius') 
        {
            $celsius=kelvin_to_celsius($given_value);
            echo "$given_value Kelvin  = $celsius Celsius";
        }  else 
        {
            echo "$given_value Kelvin";
        }
    } 
}
?>
</form>
</body>
</html>