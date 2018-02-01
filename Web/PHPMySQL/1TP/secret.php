
<?php
echo $_POST['password'];
if(isset($_POST['password']) AND $_POST['password'] == 'kangourou')
{
        echo "Secret de la nasa";
}
else
{
        echo "Nein";
}







?>
