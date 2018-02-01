<?php
// On démarre la session AVANT d'écrire du code HTML
session_start();
// On s'amuse à créer quelques variables de session dans $_SESSION
$_SESSION['SessionPseudo'] = $_POST['pseudo'];
?>
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

if(!empty($_POST['pseudo']) AND !empty($_POST['message']))
{
        // Insertion du message à l'aide d'une requête préparée
        $req = $bdd->prepare('INSERT INTO minichat (pseudo, message, date_creation) VALUES(?, ?, NOW())');
        $req->execute(array($_POST['pseudo'], $_POST['message']));
}


// Redirection du visiteur vers la page du minichat

header('Location: minichat.php');

?>
