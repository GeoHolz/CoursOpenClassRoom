<?php
// On démarre la session AVANT d'écrire du code HTML
session_start();
// On s'amuse à créer quelques variables de session dans $_SESSION
//$_SESSION['SessionPseudo'] = 'Jean';
?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Mini-chat</title>
    </head>
    <style>
    form
    {
        text-align:center;
    }
    </style>
    <body>
    <form action="minichat_post.php" method="post">

        <p>

        <label for="pseudo">Pseudo</label> : <input type="text" name="pseudo" id="pseudo" value="<?php echo $_SESSION['SessionPseudo']?>" /><br />

        <label for="message">Message</label> :  <input type="text" name="message" id="message" /><br />


        <input type="submit" value="Envoyer" />

    </p>

    </form>
   
<?php

// Connexion à la base de données

try

{

    $bdd = new PDO('mysql:host=localhost;dbname=CoursOCR;charset=utf8', 'CoursOCR', 'open');

}

catch(Exception $e)

{

        die('Erreur : '.$e->getMessage());

}


// Récupération des 10 derniers messages

$reponse = $bdd->query("SELECT pseudo, message, DATE_FORMAT(date_creation, '%Hh%imin%ss %d/%m/%Y') as date FROM minichat ORDER BY ID DESC LIMIT 0, 10");


// Affichage de chaque message (toutes les données sont protégées par htmlspecialchars)

while ($donnees = $reponse->fetch())

{

    echo '<p>'. htmlspecialchars($donnees['date']) .' <strong>' . htmlspecialchars($donnees['pseudo']) . '</strong> : ' . htmlspecialchars($donnees['message']) . '</p>';

}


$reponse->closeCursor();


?>

    </body>

</html>
