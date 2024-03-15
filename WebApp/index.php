<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" type='text/css' href="styles.css">
	<title>Time-Lapse - Raspberry Pi</title>
</head>

<body>
	<div id="wrapper">
		<header>
		</header>

		<section>
			<h1>Réglages du time-lapse</h1>
			<p>Les réglages suivant sont nécessaires avant de lancer le time-lapse. Après validation, la liste des réglages sera affichée et une confirmation sera demandée avant de lancer la séquence. Ensuite, un bouton permettra l'annulation en cours de réalisation.</p>
			<form method="POST" action="confirmation.php">
				<div>
					<label for="nom">Nom du time-lapse</label>
					<input type="text" id="nom" name="nom" placeholder="nom" required>
				</div>
				<div>
					<label for="nombre">Nombre de photos</label>
					<input type="number" id="nombre" name="nombre" required>
				</div>
				<div>
					<label for="periode">Intervalle entre deux photos</label>
					<input type="number" id="periode" name="periode" required>
				</div>
				<div>
					<label for="nomphoto">Nom des photos ("exemple" donnera exemple1.jpg, exemple2.jpg etc.)</label>
					<input type="text" id="nomphoto" name="nomphoto" placeholder="nom photo" required>
				</div>
				<div>
					<label for="typephoto">Type des fichiers-photo (jpg ou png)</label>
					<select name="select">
  						<option>jpeg</option>
  						<option>png</option>
					</select>
				</div>
				<div>
					<label for="log">Nom du fichier de suivi</label>
					<input type="text" id="log" name="log" placeholder="log" required><p>.log</p>
				</div>
				<input type="submit" name="Valider">
			</form>
		</section>
	</div>
</body>

</html>