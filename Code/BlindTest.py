#coding:utf-8
#Importation des bibliothèques
from tkinter import*
#import tkinter
import random
import pygame

#Initialisation de pygame
pygame.init()

qt = []
score = 0
l = False
qt = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]
q =random.randint(0,13)
qt[q] = True


#Initialise les variables à  chaque lancement de jeu-------------------------------------------------------------------------------------
def init():

#Création des questions

	global questions10_1, questions00_1, questions10_2, questions00_2, questions80_fr, questions80_us, questions19_fr, questions19_us, choix_reponses10_1, choix_reponses00_1, choix_reponses10_2, choix_reponses00_2, choix_reponses80_fr, choix_reponses80_us, choix_reponses19_fr, choix_reponses19_us, q, l, qt, sons10_1, sons00_1, sons10_2, sons00_2, sons80_fr, sons80_us, sons19_fr, sons19_us, reponses10_1, reponses00_1, reponses10_2, reponses00_2, reponses80_fr, reponses80_us, reponses19_fr, reponses19_us, rsp_du_keum, indexes,score, questions_order, ques
	questions10_1 = [
		"Quel est le titre de ce morceau ?",
		"Avec qui Jenifer Lopez interprète-t-elle On the floor en duo ?",
		"En quelle année est sortie Chandelier de Sia  ?",
		"Quel est le titre exact de cette chanson ?",
		"Qui est l'interprète de cette chanson (I Knew you where trouble) ?",
		"De quel album est extrait Bella\nde Maitre Gims ?",
		"Avec quel  humoriste Stromae réalise la video promotion de 'Alors on Danse'?",
		"Quel est le titre de ce célèbre morceau de Sexion d'Assaut?",
		"Quel est le nom du groupe qui interprète le tube 'Party Rock Anthem'?",
		"Quel est le titre de cette musique de Colonel Reyel ?",
		"De quel album d'Adèle ce titre provient-il ?",
		"Quel est record est detenu par ce titre ?",
		"Quel est le titre qui a rendu populaire le groupe Daft Punk ?",
		"De la bande originale de quel film la musique cette musique provient-elle ?",
		]


	questions00_1 = [
		"Quel est le titre de cette musique d'Amel Bent ?",
		"Quelle est l'origine du groupe O-Zone, connu notamment grâce à ce titre (Dragostea din tei) ?",
		"Accompagné de quel artiste Magic System chante la chanson\n'Bouger bouger' ?",
		"En quelle année est sortie 'Hey Oh' du groupe Tragédie  ?",
		"De quelle chansion Yannick s'est-il inspire en 2003 pour obtenir le tube 'Ces soirées - là' ?",
		"Quel rappeur marseillais interprète cette musique ?",
		"Qui est l'auteur de la chanson 'Qui est l'exemple' ?",
		"Qui interprète ce célèbre titre 'J'aimerais tellement' ?",
		"Quel duo est à l'origine de 'Confessions Nocturnes' ?",
		"Quel est le titre de ce tube de Sheryfa Luna ?",
		"Quel est le titre de cette musique de Sexion d'Assaut ?",
		"Quel est le titre de cette musique de Booba ?",
		"Qui est l'auteur du titre de 'Gravé dans la roche' ?",
		"Quel est le nom de ce titre de La Fouine ?",
		]


	questions10_2 = [
		"Avec qui Rihanna intreprète-t-elle ce titre ?",
		"Quel est le titre de cette musique ?",
		"Qui est l'interprète de 'Shape of You' ?",
		"Avec quel artiste Luis Fonsi interprète l'énorme succès 'Despacito' ?",
		"Quel est le titre de ce single d'Ariana Grande ?",
		"Quel artiste est en featuring avec Camila Cabello sur le titre 'Havana' ?",
		"Quel est le titre de cette chanson en duo entre Charlie Puth et Selena Gomez  ?",
		"Quel est le titre de ce tube de l'été 2015 d'OMI ?",
		"Avec qui Maitre Gims interprète-t-il le titre 'La même'?",
		"Quel est le titre de cette collaboration entre DJ Sanke Major Lazer et MO ? ",
		"Avec qui Mark Ronson réalise ce titre ?",
		"Combien de vues a realisé PNL en seulement 48h sur la chanson 'Au DD' ?",
		"Quel est le titre de ce single de Niska ?",
		"Quel est le nom de l'artiste qui chante le hit 'Ramenez la coupe a la maison'? ",
		]


	questions00_2 = [
		"Quel est le titre de cette musique d'Usher en collaboration avec Lil Jon et Ludacris ?",
		"Dans quel film peut-on retrouver ce titre d'Eminem intitulé 'Lose yourself' ?",
		"Quel artiste accompagne Alicia Keys sur la chanson 'Empire State Of Mind ?",
		"Quel est le titre de ce son d'Akon ?",
		"Quel est le groupe à l'origine de ce titre nommé 'Pump it' ?",
		"Qui chante ce tire en duo avec 50 cent ?",
		"Qui est chante le célèbre titre 'Single Ladies' ?",
		"Quel est le titre de ce tube qui a rendu populaire les Black Eyed Peas ?",
		"Quel rappeur interprète le titre 'Stronger' ?",
		"Qui est le duo qui interprète cette musique ?",
		"Quelle artiste interprète ce son ?",
		"Quel est le titre de cette musique de Bruno Mars et B.o.B ?",
		"Quel est le titre de ce son de Jason Derulo ?",
		"Quelle artiste d'origine sud-americaine interprète\n'Hips don't lie' en featuring avec\n Wyclef Jean ?",
		]


	questions80_fr = [
		"Comment se nomme cette chanson de Johnny ?",
		"Quel est le titre de cette chanson\nde Celine Dion ?",
		"Quel est le titre exact de cette chanson ?",
		"Qui chante la chanson\n'Partenaire particulier' ?",
		"Quel est le nom de cette chanson\ninterprète par Daniel Balavoine ?",
		"Quel est le nom de ce tube\nde Jean-Luc Lahaye ?",
		"Quel est le nom du groupe qui interprète 'Nuit De Folie' ?",
		"Quel est le titre exact de cette chanson ?",
		"Comment se nomme la chanteuse qui interprète cette chanson ?",
		"Comment se nomme la chanteuse qui interprète cette chanson ?",
		"Comment se nomme la chanteuse qui interprète cette chanson ?",
		"Laquelle de cette chanson correspond à l'extrait diffusé ?",
		"Lequel de cet artiste chante cette chanson ?",
		"Comment se nomme cette chanson\ndu groupe Indochine ?",
		]


	questions80_us = [
		"A quel titre de Michael Jackson l'extrait\ndiffusé correspond-t-il ?",
		"Quel est le nom du groupe d'artistes formé par\nMichael Jackson qui enregistre en 1985\nWe are the world ?",
		"Quel artiste interprète\nle tube de disco 'Daddy Cool' en\n1976 ?",
		"Quel est le titre de ce succès\nde Bonnie Taylor ?",
		"Quel artiste interprète\n'Part Time A Lover' en\n1985 ?",
		"De quelle origine est le duo 'Modern Talking'\nintérpretant cette chanson ?",
		"De quel film cette bande originale\nest-elle tirée ?",
		"De quel film cette bande originale\nest-elle tirée ?",
		"Quelle artiste interprète cette chanson ?",
		"A quelle chanson cet extrait\nappartient-il ?",
		"De quel film cette chanson est-elle\nla bande originale ?",
		"Quelle chanteuse interprète 'All I Want For Christmas Is You' ?",
		"A quel thème se rapporte la chanson\nde George Michael ?",
		"Quel artiste interprète cette chanson ?",
		]


	questions19_fr = [
		"Quel est la suite de 'J'suis une moula, t'es une moula ... ?",
		"De quel album cette chanson est extraite ?",
		"Quels artistes interprètent cette chanson ?",
		"Quel est le bon refrain ?",
		"Que se passe t-i-il à  la fin? Qu'en est-il de la décision de Ninho ?",
		"Quel âge a Koba LaD ?",
		"Qui est l'auteur de cette musique ?",
		"De quel album cette chanson est-elle extraite ?",
		"Avec quel artiste Maës interprète la chanson'Madrina' ?",
		"Quel est le titre de l'album ?",
		"Quel est le titre de cette musique ?",
		"Quel est la suite de Et moi je me repete ... ?",
		"Quels artistes interprètent ce son ?",
		"De quelle origine est Angèle ?",
		]



	questions19_us = [
		"Quel est le titre de cette musique ?",
		"Le(s) chanteur(s) ?",
		"Que y a t-il avant le refrain de 'Thank you, next' ?",
		"Qui est le chanteur manquant : Selena Gomez, J Balvin, Benny Blanco et...?",
		"Qui est l'auteur de cette musique ?",
		"Quel est le titre de cette musique ?",
		"Quel est la bonne version de cette musique ?",
		"Quel est le titre de cette musique ?",
		"Quelle chaine présente cette musique ?",
		"Qui est le chanteur de cette musique ?",
		"Quel est l'âge de Lil Mosey ?",
		"A quoi référe Butterfly Doors ?",
		"Quel est le titre de cette musique ?",
		"De quel film Disney cette chanson est-elle la bande originale ?",
		]







	c = 0
	qt = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]
	q =random.randint(0,13)
	qt[q] = True
	l = False




	#Liste des sons
	sons10_1 = ["EG-B.wav", "JL-OTF.wav", "S-C.wav", "BM-SMR.wav", "TS-IKYWT.wav", "MG-B.wav","ST-AD.wav","SA-DS.wav","LM-PR.wav","CR-CL.wav","AD-SL.wav","ST-PP.wav","DP-GL.wav","PW-HA.wav"
	]

	sons00_1 = ["AB-MP.wav", "OZ-DDT.wav", "MS-BB.wav", "T-HO.wav", "Y-CSL.wav", "SO-AB.wav","RO-QL.wav","JL-JA.wav","DI-CN.wav","SL-IL.wav","SA-WB.wav","BO-PT.wav","SN-GR.wav","LF-DF.wav"
	]

	sons10_2 = ["RI-WK.wav","DR-OD.wav","ES-SY.wav","LF-DS.wav","AG-7R.wav","CC-HV.wav","CP-WDTA.wav","OM-CL.wav","MG-LM.wav","ML-LO.wav","MR-UF.wav","PN-DD.wav","NK-RS.wav","VD-CM.wav"
	]

	sons00_2 = ["US-YE.wav", "EM-LY.wav", "AK-ESOM.wav", "AK-LO.wav", "TB-PI.wav", "50-CS.wav", "BE-SL.wav", "TB-IG.wav", "KW-S.wav", "R-U.wav", "BS-T.wav", "BM-NO.wav", "JD-WS.wav", "SH-HI.wav"
	]

	sons80_fr = ["JH-L.wav", "CD-PQTME.wav", "I-LDDM.wav", "PP-PP.wav", "DB-L.wav", "JLL-FQJ.wav", "DDS-NDF.wav", "D-VV.wav", "FG-ELEL.wav", "VP-JLT.wav", "MF-D.wav", "GM-SDT.wav", "R-MG.wav", "I-L.wav"
	]

	sons80_us = ["MJ-T.wav", "USAFA-WATW.wav", "BM-DC.wav", "BT-TEOTH.wav", "SW-PTL.wav", "MT-BL.wav", "CD-MHWGO.wav", "WH-IWALY.wav", "CL-GJWTHF.wav", "MJ-BJ.wav", "S-EOTT.wav", "MC-AIWFCIY.wav", "GM-CW.wav", "RA-NGGYU.wav"
	]

	sons19_fr = ["H-K.wav", "PNL-DD.wav", "N-M.wav", "A-P.wav", "N-P.wav", "K-A.wav", "LD-M.wav", "MD-B.wav", "MB-M.wav", "BB-S.wav", "Kaza-H.wav", "DD-P.wav", "GM-H.wav", "A-B.wav"
	]

	sons19_us = ["K-T.wav", "JB-S.wav", "A-T.wav", "BTSJ-I.wav", "CB-P.wav", "AS-D.wav", "P-W.wav", "A-Lp.wav", "J-R.wav", "L-I.wav", "L-G.wav", "L-B.wav", "L-E.wav", "ZZ-A.wav"
	]







	#Creation des reponses
	choix_reponses10_1 = [
		["To the word", "World", "Burn", "Sky"],
		["Jason Derulo", "Pitbull", "Justin Bieber", "Usher"],
		["2016", "2014", "2012", "2013"],
		["Lefa - Sur ma route", "Back M - Sur ma route", "Black M - Sur ma route", "Blac M - Ma roots"],
		["Britney Spears", "Taylor Swift", "Katy Perry", "Elie Goulding"],
		["Subliminal", "Ceinture noire", "L'apogée", "Mon coeur avait raison"],
		["Gad Elmaleh", "Thomas N'Gijol", "Fabrice Eboué", "Jamel Debbouze"],
		["Pavéééé", "Sorry", "Merci", "Désolé"],
		["OMG", "LOL", "LMFAO", "GTY"],
		["Lui", "Laisse moi être celui", "Moi", "Celui"],
		["21", "Someone Like You", "Adele", "Me"],
		["Clip le plus visionné en 24h", "Plus grand nombre de vues pour une chanson francophone", "Chanson la plus populaire de 2013", "Rien"],
		["Unlucky", "Lucky", "Get Lucky", "We're up all night to Get Lucky"],
		["Moi, Moche et Méchant 2", "Raiponce", "Les Minions", "Aucun"],
	]

	choix_reponses00_1 = [
		["Viser la lune","Ma philosophie","Ca me fait pas peur","J'y crois encore et encore"],
		["Moldavie", "Roumanie", "Serbie","Russie"],
		["Mokobé", "Fally Ipupa", "Khaled", "Shawki"],
		["2000", "2001", "2005", "2003"],
		["Michel Sardou - L'année 60", "Claude François - Cette année - là", "Johnny Hallyday - Le bon vieux temps ", "Khaled - Aïcha"],
		["Soprano", "Alonzo", "Jul", "Naps"],
		["Booba", "La Fouine", "Rohff", "Stromae"],
		["Mary Lee", "Jena Lee", "Lisa Lee", "Lee Lee"],
		["Diam's et Soprano", "Vitaa et Diam's", "Soprano et Vitaa", "Maitre Gims et Vitaa"],
		["Il avait les mots", "Je l'aimais", "Mots", "Accro"],
		["Wati Son", "Wati Bon Son", "Wati Music", "Wati Beau Son"],
		["Pitbull", "Boulbi", "Chien", "92i"],
		["Sniper", "113", "Psy 4 De La Rime", "La Fouine"],
		["Cocaïne dans le jean", "Ferme", "Du Ferme", "La Fouine"],
	]

	choix_reponses10_2 = [
		["Drake", "Snake", "Snoop Dogg", "Usher"],
		["One Dance", "Last Chance", "Last Dance", "One Chance"],
		["Ed Sheeran", "Ed Fraangipan", "Ed Sheren", "Edy Sheeran"],
		["Mammy Yankee", "Daddy Pipi", "Daddy Yankee", "6ix9ine"],
		["6 rings", "8 rings", "7 kings", "7 rings"],
		["Young Thug", "Drake", "6ix9ine", "Tory Lanez"],
		["We Need To Talk", "Why Don't We Talk Anymore ?", "We Don't Talk Anymore", "Talk"],
		["Cheerleader", "Pom-pom girl", "Chez Lidl", "Leader"],
		["Vianno", "Slimane", "Mika", "Vianney"],
		["Lean off", "Leak", "Lean On", "Lean"],
		["Bruno Mars", "Pharell Williams", "Mackelemore", "Migos"],
		["20 millions", "12 millions", "7 millions", "16 millions"],
		["Twitter", "Follow", "Réseaux", "Pouloulou"],
		["Vegeteaux", "Vegedream", "Franglish", "Dadju"],
	]

	choix_reponses00_2 = [
		["Waouh!", "Yes!", "Okey!", "Yeah!"],
		["8Mile", "Lose yourself", "Empire", "Fight"],
		["JAY-Z", "40 Cent", "50 Cent", "Tupac"],
		["So lonely", "I'm sorry", "So sorry", "Lonely"],
		["The White Eyed Peas", "The Black Aie Peas", "The Black Eyed Peas", "Will.i.am"],
		["Olivia", "Olivine", "Olive et Tom", "Beyoncé"],
		["Rihanna", "Jessy J", "Nicki Minaj", "Beyoncé"],
		["Feel", "I Gotta Feeling", "Got The Feeling", "Feeling"],
		["JAY-Z", "Nelly", "Kanye West", "Diddy"],
		["JAY-Z & Beyoncé", "JAY-Z & Rihanna", "JAY-Z & Alicia Keys", "50 Cent & Alicia Keys"],
		["Britney Spears", "Lady Gaga", "Katy Perry", "Nelly Furtado"],
		["Girls", "Beautiful Girl", "Nothin On You", "Baby"],
		["What to say", "What you say", "Whatcha Say", "Say It"],
		["Selena Gomez", "Jenifer Lopez", "Shakira", "Camila Cabello"],
	]


	choix_reponses80_fr = [
		["L'Envie", "Allumer le feu", "J'en parlerai au diable", "Requiem pour un fou"],
		["Sous le vent", "Pour que tu m'aimes encore", "S'il suffisait d'aimer", "Parler a  mon pere"],
		["Peter Et Sloane - Besoin de rien envie de toi", "Desirless - Voyage, Voyage", "Images - Les démons de minuit", "Laroche Valmont - T'as le look coco"],
		["Jean-Pierre Mader", "Partenaire particulier", "Jean-Luc Lahaye", "Francis Cabrel"],
		["Mon Fils Ma Bataille", "L'aziza", "Je Ne Suis Pas Un Héros", "Tous les cris les S.O.S."],
		["Femme que t'aimes", "Femme qu'il aime", "Femme", "Femme que j'aime"],
		["Debut de soirée","Debut de journée","Debut de matinée","Debut d'après-midi"],
		["Peter Et Sloane - Besoin de rien envie de toi", "Desirless - Voyage, Voyage", "Images - Les démons de minuit", "Laroche Valmont - T'as le look coco"],
		["Corynne Charby", "France Gaal", "Mylène Farmer", "Vanessa Paradis"],
		["Corynne Charby", "France Gaal", "Mylène Farmer", "Vanessa Paradis"],
		["Corynne Charby", "France Gaal", "Mylène Farmer", "Vanessa Paradis"],
		["On va s'aimer", "Les sunlights des tropiques", "L'amour se raconte en musique", "On a toute la vie pour s'aimer"],
		["Renaud", "Michel Sardou", "Johnny Hallyday", "Jean-Jacques Goldman"],
		["Trois nuits par semaine", "La vie est belle", "L'aventurier", "J'ai demande à  la lune"],
	]

	choix_reponses80_us = [
		["Smooth Criminal", "Beat It", "Thriller", "Billie Jean"],
		["U.S.A. For Womens", "U.S.A. For Orphelins", "U.S.A For Africa", "U.S.A For Haïti"],
		["Boney S", "Boney K", "Boney M", "Boney D"],
		["Total Eclipse Of The Hearth", "I Will Always Love You", "My Hearth Will Go One", "Whenevher "],
		["Lionel Richie", "Stevie Wonder", "Eddie Murphy", "Michael Douglas"],
		["Suédois", "Anglais", "Français", "Allemand"],
		["Bodyguard", "The Green Mile ", "The Lion King", "Titanic"],
		["Bodyguard", "The Green Mile ", "The Lion King", "Titanic"],
		["Cyndi Lauper","Mariah Carey","Whitney Houston","Céline Dion"],
		["Thriller", "Billie Jean", "Beat It", "They Don't Really Care About Us"],
		["Rambo", "Creed II", "Rocky", "Walker, Texas Rangers"],
		["Cyndi Lauper", "Mariah Carey", "Whitney Houston", "Céline Dion"],
		["L'amour", "L'infidélité", "La malbouffe", "Le racisme"],
		["Kenny Loggins", "Toto", "a-ha", "Rick Astley"],
	]

	choix_reponses19_fr = [
		["T'es en esprit", "Y a un esprit", "T'es l'esprit", "T'es un esprit"],
		["Les deux reufs", "Les deux freres", "Les freres", "Les frelons"],
		["Booba, Vegedream et Niska", "Niska", "MHD, Niska et Vegedream", "Niska et Booba"],
		["J'suis bang, hors gang Boy ne joue pas, gang, gang, gang", "J'suis gang, hors game Boy ne joue pas, bang, bang, bang", "J'suis game, hors gang Boy ne joue pas, bang, bang, bang", "Chui game, hors gang Hoy ne joue pas, bang, bang, bang "],
		["C'est mort parce qu'elle est tombe sur un bandit", "C'est bon il prendra soin d'elle", "C'est mort son pote lui a dit que les meufs sont toutes comme ca", "C'est bon, mais elle est morte"],
		["18 ans", "22 ans", "19 ans", "20 ans"],
		["T2R","Dadju","Damso","Landy"],
		["IX","XIX","MHD","XVI"],
		["Une femme respectueuse","Une mere","Une femme sanguinaire et redoutee","Une drogue"],
		["Brams", "Trone", "Or noir 3", "aucune des 3"],
		["HRTBRK", "HRTBRK4", "HRTBRK2", "HRTBRK3"],
		["De faire attention a  mes potes","Qu'il y a des braves","De jamais baisser les bras","Que le respect c'est pas dans les poches"],
		["Alonzo, Daddy Yankee, Gims", "J Balvin, Landy, Gims", "Maluma, Gims", "Maluma, Gims, DJ Snake"],
		["Francaise", "Bretonne", "Belge", "Suisse"],
	]

	choix_reponses19_us = [
		["Can you just","Talk","Just talk","Can you"],
		["Joe","Nick","Kevin","Jonas Brothers"],
		["I'm so fuckin'","And one tought me pain", "And for that way", "And for that, I say"],
		["Tainy", "Post Malone", "Ozuna", "Khalid "],
		["Bruno Mars", "Cardi B", "Chris Brown", "Daft Punk"],
		["Diva", "I'm a Diva", "I'm", "Ain't no Diva"],
		["Get more bottles, got em sayin',wow,wow,wow","It's a moment when i show up, got em sayin',wow,wow,wow","Hunnid bands on my pocket, got em sayin',wow,wow,wow","It's a moment, got em sayin',wow,wow,wow"],
		["Back","Look at it","Look back at it","Tra ta ta ta"],
		["Juice Wrld","Sony","Lyrical Lemonade","Millenium"],
		["Swae Lee","Lil Mosey","Juice Wrld","Lil Skies"],
		["19 ans", "17 ans", "15 ans", "18 ans"],
		["Drogue","Basket","Voiture","Jet privÃ©"],
		["Our Home","Earth","We love the earth","It's our planet"],
		["Le roi lion","La belle et la bete","Aladdin","Vaiana"],
	]




	#Bonnes réponses
	reponses00_1 = [1 ,0, 0, 3, 1, 0, 2, 1, 1, 0, 1, 0, 0, 3]
	reponses00_2 = [3, 0, 0, 3, 2, 2, 3, 1, 2, 1, 0, 2, 2, 2]
	reponses10_1 = [2, 1, 1, 2, 1, 0, 3, 3, 2, 3, 0, 1, 2, 0]
	reponses10_2 = [0 ,0 ,0 ,2 ,3 ,0 ,2 ,0 ,3 ,2 ,0 ,1 ,2 ,1]
	reponses80_fr = [0, 1, 2, 1, 1, 3, 0, 1, 1, 3, 2, 1, 0, 2]
	reponses80_us = [2, 2, 2, 0, 1, 3, 3, 0, 0, 1, 2, 1, 1, 3]
	reponses19_fr = [0, 2, 3, 1, 1, 2, 3, 1, 2, 3, 2, 2, 2, 2]
	reponses19_us = [1, 3, 3, 0, 1, 0, 1, 2, 2, 3, 1, 2, 1, 2]


	rsp_du_keum = []

	indexes = []
	questions_order = []
	ques = 1
	pygame.mixer.stop() #Pour que le son s'arrête lorsque le quiz est fini


global labelscoretext
#Création résultat quizz----------------------------------------------------------------------------------------------------------------
def montrer_resulat(score):
	lblQuestion.destroy()
	r1.destroy()
	r2.destroy()
	r3.destroy()
	r4.destroy()
	labelimage = Label(
		fen,
		background = "#4065A4",
		border = 0)

	labelimage.pack(pady=(50, 30))
	labelresulttext = Label(
		fen,
		font = ("Consolas", 20),
		background = "#4065A4")

	labelscoretext = Label(
		fen,
		font = ("Consolas", 30),
		background = "#4065A4")

	labelresulttext.pack()
	labelscoretext.pack()

	if score >= 11:
		img = PhotoImage(file="Victoire.png")
		labelimage.configure(image=img)
		labelimage.image = img
		labelscoretext.configure(text="Score :"+ str(score) + "/14 !")
		labelresulttext.configure(text="T'es plutôt bon !\nEssaye une autre catégorie voir")

	elif (score >= 6 and score < 10):
		img = PhotoImage(file="Bof.png")
		labelimage.configure(image=img)
		labelimage.image = img
		labelscoretext.configure(text="Score :"+ str(score) + "/14")
		labelresulttext.configure(text="Pas mal")

	else:
		img = PhotoImage(file="Fail.png")
		labelimage.configure(image=img)
		labelimage.image = img
		labelscoretext.configure(text="Score :"+ str(score) + "/14")
		labelresulttext.configure(text="Essaye une autre catégorie\nc'est pas ton point fort on dirait...")


	# Bouton restart
	btnRestart = Button(
		fen,
		text = "Essayer une autre catégorie",
		relief = FLAT,
		font = ("Times", 20),
		command = lambda : btn_restart_enclenche(labelresulttext, labelscoretext, btnRestart, labelimage),
		background = "#000000",
		foreground = "#ffffff")
	btnRestart.pack(pady=5)



#Action bouton restart
def btn_restart_enclenche(labelresulttext, labelscoretext, btnRestart, labelimage):
	labelimage.destroy()
	labelresulttext.destroy()
	labelscoretext.destroy()
	btnRestart.destroy()
	choix_categories()
	init()


#Calcul du score-------------------------------------------------------------------------------------------------------------------------
def calc():
	if c == 0:
	   global indexes,rsp_du_keum, reponses10_1,reponses00_1, reponses10_2, reponses00_2, reponses80_fr, reponses80_us, reponses19_fr, reponses19_us, questions_order, calc
	   x = 0
	   bonnes_reponses = [reponses10_1[i] for i in questions_order]
	   # Score est égal au nombre de bonnes reponses mutliplié par 5 (Score max = 70/70)
	   score = 1*sum([bonnes_reponses[i] == rsp_du_keum[i] for i in range(len(reponses10_1))])
	   montrer_resulat(score)
	if c == 1:
	   global indexes,rsp_du_keum, reponses10_1, reponses00_1, reponses10_2, reponses00_2, reponses80_fr, reponses80_us, reponses19_fr, reponses19_us, questions_order, calc
	   x = 0
	   bonnes_reponses = [reponses00_1[i] for i in questions_order]
	   # Score est égal au nombre de bonnes reponses mutliplié par 5 (Score max = 70/70)
	   score = 1*sum([bonnes_reponses[i] == rsp_du_keum[i] for i in range(len(reponses00_1))])
	   montrer_resulat(score)
	if c == 2:
	   global indexes, rsp_du_keum, reponses10_1, reponses00_1, reponses10_2, reponses00_2, reponses80_fr, reponses80_us, reponses19_fr, reponses19_us, questions_order, calc
	   x = 0
	   bonnes_reponses = [reponses10_2[i] for i in questions_order]
	   # Score est égal au nombre de bonnes reponses mutliplié par 5 (Score max = 70/70)
	   score = 1*sum([bonnes_reponses[i] == rsp_du_keum[i] for i in range(len(reponses10_2))])
	   montrer_resulat(score)
	if c == 3:
		global indexes, rsp_du_keum, reponses10_1, reponses00_1, reponses10_2, reponses00_2, reponses80_fr, reponses80_us, reponses19_fr, reponses19_us, questions_order, calc
		x = 0
		bonnes_reponses = [reponses00_2[i] for i in questions_order]
		# Score est égal au nombre de bonnes reponses mutliplié par 5 (Score max = 70/70)
		score = 1*sum([bonnes_reponses[i] == rsp_du_keum[i] for i in range(len(reponses00_2))])
		montrer_resulat(score)
	if c == 4:
		global indexes, rsp_du_keum, reponses10_1, reponses00_1, reponses10_2, reponses00_2, reponses80_fr, reponses80_us, reponses19_fr, reponses19_us, questions_order, calc
		x = 0
		bonnes_reponses = [reponses80_fr[i] for i in questions_order]
		# Score est égal au nombre de bonnes reponses mutliplié par 5 (Score max = 70/70)
		score = 1*sum([bonnes_reponses[i] == rsp_du_keum[i] for i in range(len(reponses80_fr))])
		montrer_resulat(score)
	if c == 5:
		global indexes, rsp_du_keum, reponses10_1, reponses00_1, reponses10_2, reponses00_2, reponses80_fr, reponses80_us, reponses19_fr, reponses19_us, questions_order, calc
		x = 0
		bonnes_reponses = [reponses80_us[i] for i in questions_order]
		# Score est égal au nombre de bonnes reponses mutliplié par 5 (Score max = 70/70)
		score = 1*sum([bonnes_reponses[i] == rsp_du_keum[i] for i in range(len(reponses80_us))])
		montrer_resulat(score)
	if c == 6:
		global indexes, rsp_du_keum, reponses10_1, reponses00_1, reponses10_2, reponses00_2, reponses80_fr, reponses80_us, reponses19_fr, reponses19_us, questions_order, calc
		x = 0
		bonnes_reponses = [reponses19_fr[i] for i in questions_order]
		# Score est égal au nombre de bonnes reponses mutliplié par 5 (Score max = 70/70)
		score = 1*sum([bonnes_reponses[i] == rsp_du_keum[i] for i in range(len(reponses19_fr))])
		montrer_resulat(score)
	if c == 7:
		global indexes, rsp_du_keum, reponses10_1, reponses00_1, reponses10_2, reponses00_2, reponses80_fr, reponses80_us, reponses19_fr, reponses19_us, questions_order, calc
		x = 0
		bonnes_reponses = [reponses19_us[i] for i in questions_order]
		# Score est égal au nombre de bonnes reponses mutliplié par 5 (Score max = 70/70)
		score = 1*sum([bonnes_reponses[i] == rsp_du_keum[i] for i in range(len(reponses19_us))])
		montrer_resulat(score)


questions_order = []
ques = 1
def rps_cochee():
	q = 0
	m = 0
	l = False
	while q < 13:
		if qt[q] == True:
			m += 1
		else:
			m = m
		if m == 13:
			l = True
		else:
			m == True
		q+= 1

	while qt[q] == True and l == False:
		q =random.randint(0,13)

	global questions_order
	questions_order.append(q)
	global radiovar,rsp_du_keum
	global lblQuestion,r1,r2,r3,r4
	global ques
	x = radiovar.get()
	rsp_du_keum.append(x)
	radiovar.set(-1)
	if ques <= 13:
		if c == 0:
			pygame.mixer.stop()
			son = pygame.mixer.Sound(sons10_1[q])
			son.play()
			lblQuestion.config(text= questions10_1[q])
			r1['text'] = choix_reponses10_1[q][0]
			r2['text'] = choix_reponses10_1[q][1]
			r3['text'] = choix_reponses10_1[q][2]
			r4['text'] = choix_reponses10_1[q][3]
		if c == 1:
			pygame.mixer.stop()
			son = pygame.mixer.Sound(sons00_1[q])
			son.play()
			lblQuestion.config(text= questions00_1[q])
			r1['text'] = choix_reponses00_1[q][0]
			r2['text'] = choix_reponses00_1[q][1]
			r3['text'] = choix_reponses00_1[q][2]
			r4['text'] = choix_reponses00_1[q][3]
		if c == 2:
			pygame.mixer.stop()
			son = pygame.mixer.Sound(sons10_2[q])
			son.play()
			lblQuestion.config(text= questions10_2[q])
			r1['text'] = choix_reponses10_2[q][0]
			r2['text'] = choix_reponses10_2[q][1]
			r3['text'] = choix_reponses10_2[q][2]
			r4['text'] = choix_reponses10_2[q][3]
		if c == 3:
			pygame.mixer.stop()
			son = pygame.mixer.Sound(sons00_2[q])
			son.play()
			lblQuestion.config(text= questions00_2[q])
			r1['text'] = choix_reponses00_2[q][0]
			r2['text'] = choix_reponses00_2[q][1]
			r3['text'] = choix_reponses00_2[q][2]
			r4['text'] = choix_reponses00_2[q][3]
		if c == 4:
			pygame.mixer.stop()
			son = pygame.mixer.Sound(sons80_fr[q])
			son.play()
			lblQuestion.config(text= questions80_fr[q])
			r1['text'] = choix_reponses80_fr[q][0]
			r2['text'] = choix_reponses80_fr[q][1]
			r3['text'] = choix_reponses80_fr[q][2]
			r4['text'] = choix_reponses80_fr[q][3]
		if c == 5:
			pygame.mixer.stop()
			son = pygame.mixer.Sound(sons80_us[q])
			son.play()
			lblQuestion.config(text= questions80_us[q])
			r1['text'] = choix_reponses80_us[q][0]
			r2['text'] = choix_reponses80_us[q][1]
			r3['text'] = choix_reponses80_us[q][2]
			r4['text'] = choix_reponses80_us[q][3]
		if c == 6:
			pygame.mixer.stop()
			son = pygame.mixer.Sound(sons19_fr[q])
			son.play()
			lblQuestion.config(text= questions19_fr[q])
			r1['text'] = choix_reponses19_fr[q][0]
			r2['text'] = choix_reponses19_fr[q][1]
			r3['text'] = choix_reponses19_fr[q][2]
			r4['text'] = choix_reponses19_fr[q][3]
		if c == 7:
			pygame.mixer.stop()
			son = pygame.mixer.Sound(sons19_us[q])
			son.play()
			lblQuestion.config(text= questions19_us[q])
			r1['text'] = choix_reponses19_us[q][0]
			r2['text'] = choix_reponses19_us[q][1]
			r3['text'] = choix_reponses19_us[q][2]
			r4['text'] = choix_reponses19_us[q][3]
		ques += 1
		qt[q] = True
	else:
		  calc()

#Création page quizz--------------------------------------------------------------------------------------------------------------------
def commence_quiz10_1():
	global questions_order
	questions_order.append(q)
	global lblQuestion,r1,r2,r3,r4
	lblQuestion = Label(
		fen,
		text = questions10_1[q],
		font = ("Consolas", 20, "bold"),
		width = 500,
		justify = "center",
		wraplength = 400,
		background = "#ffffff",)
	son = pygame.mixer.Sound (sons10_1[q])
	son.play()
	lblQuestion.pack(pady=(100,30))

	global radiovar
	radiovar = IntVar()
	radiovar.set(-1)

	r1 = Radiobutton(
		fen,
		text = choix_reponses10_1[q][0],
		font = ("Times New Roman", 15),
		value = 0,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r1.pack(pady=5)

	r2 = Radiobutton(
		fen,
		text = choix_reponses10_1[q][1],
		font = ("Times New Roman", 15),
		value = 1,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r2.pack(pady=5)

	r3 = Radiobutton(
		fen,
		text = choix_reponses10_1[q][2],
		font = ("Times New Roman", 15),
		value = 2,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r3.pack(pady=5)

	r4 = Radiobutton(
		fen,
		text = choix_reponses10_1[q][3],
		font = ("Times New Roman", 15),
		value = 3,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r4.pack(pady=5)


def commence_quiz00_1():
	global questions_order
	questions_order.append(q)
	global lblQuestion,r1,r2,r3,r4
	lblQuestion = Label(
		fen,
		text = questions00_1[q],
		font = ("Consolas", 20, "bold"),
		width = 500,
		justify = "center",
		wraplength = 400,
		background = "#ffffff",)
	son = pygame.mixer.Sound (sons00_1[q])
	son.play()
	lblQuestion.pack(pady=(100,30))

	global radiovar
	radiovar = IntVar()
	radiovar.set(-1)

	r1 = Radiobutton(
		fen,
		text = choix_reponses00_1[q][0],
		font = ("Times New Roman", 15),
		value = 0,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r1.pack(pady=5)

	r2 = Radiobutton(
		fen,
		text = choix_reponses00_1[q][1],
		font = ("Times New Roman", 15),
		value = 1,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r2.pack(pady=5)

	r3 = Radiobutton(
		fen,
		text = choix_reponses00_1[q][2],
		font = ("Times New Roman", 15),
		value = 2,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r3.pack(pady=5)

	r4 = Radiobutton(
		fen,
		text = choix_reponses00_1[q][3],
		font = ("Times New Roman", 15),
		value = 3,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r4.pack(pady=5)


def commence_quiz10_2():
	global questions_order
	questions_order.append(q)
	global lblQuestion,r1,r2,r3,r4
	lblQuestion = Label(
		fen,
		text = questions10_2[q],
		font = ("Consolas", 20, "bold"),
		width = 500,
		justify = "center",
		wraplength = 400,
		background = "#ffffff",)
	son = pygame.mixer.Sound (sons10_2[q])
	son.play()
	lblQuestion.pack(pady=(100,30))

	global radiovar
	radiovar = IntVar()
	radiovar.set(-1)

	r1 = Radiobutton(
		fen,
		text = choix_reponses10_2[q][0],
		font = ("Times New Roman", 15),
		value = 0,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r1.pack(pady=5)

	r2 = Radiobutton(
		fen,
		text = choix_reponses10_2[q][1],
		font = ("Times New Roman", 15),
		value = 1,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r2.pack(pady=5)

	r3 = Radiobutton(
		fen,
		text = choix_reponses10_2[q][2],
		font = ("Times New Roman", 15),
		value = 2,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r3.pack(pady=5)

	r4 = Radiobutton(
		fen,
		text = choix_reponses10_2[q][3],
		font = ("Times New Roman", 15),
		value = 3,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r4.pack(pady=5)


def commence_quiz00_2():
	global questions_order
	questions_order.append(q)
	global lblQuestion,r1,r2,r3,r4
	lblQuestion = Label(
		fen,
		text = questions00_2[q],
		font = ("Consolas", 20, "bold"),
		width = 500,
		justify = "center",
		wraplength = 400,
		background = "#ffffff",)
	son = pygame.mixer.Sound (sons00_2[q])
	son.play()
	lblQuestion.pack(pady=(100,30))

	global radiovar
	radiovar = IntVar()
	radiovar.set(-1)

	r1 = Radiobutton(
		fen,
		text = choix_reponses00_2[q][0],
		font = ("Times New Roman", 15),
		value = 0,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r1.pack(pady=5)

	r2 = Radiobutton(
		fen,
		text = choix_reponses00_2[q][1],
		font = ("Times New Roman", 15),
		value = 1,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r2.pack(pady=5)

	r3 = Radiobutton(
		fen,
		text = choix_reponses00_2[q][2],
		font = ("Times New Roman", 15),
		value = 2,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r3.pack(pady=5)

	r4 = Radiobutton(
		fen,
		text = choix_reponses00_2[q][3],
		font = ("Times New Roman", 15),
		value = 3,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r4.pack(pady=5)


def commence_quiz80_fr():
	global questions_order
	questions_order.append(q)
	global lblQuestion,r1,r2,r3,r4
	lblQuestion = Label(
		fen,
		text = questions80_fr[q],
		font = ("Consolas", 20, "bold"),
		width = 500,
		justify = "center",
		wraplength = 400,
		background = "#ffffff",)
	son = pygame.mixer.Sound (sons80_fr[q])
	son.play()
	lblQuestion.pack(pady=(100,30))

	global radiovar
	radiovar = IntVar()
	radiovar.set(-1)

	r1 = Radiobutton(
		fen,
		text = choix_reponses80_fr[q][0],
		font = ("Times New Roman", 15),
		value = 0,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r1.pack(pady=5)

	r2 = Radiobutton(
		fen,
		text = choix_reponses80_fr[q][1],
		font = ("Times New Roman", 15),
		value = 1,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r2.pack(pady=5)

	r3 = Radiobutton(
		fen,
		text = choix_reponses80_fr[q][2],
		font = ("Times New Roman", 15),
		value = 2,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r3.pack(pady=5)

	r4 = Radiobutton(
		fen,
		text = choix_reponses80_fr[q][3],
		font = ("Times New Roman", 15),
		value = 3,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r4.pack(pady=5)


def commence_quiz80_us():
	global questions_order
	questions_order.append(q)
	global lblQuestion,r1,r2,r3,r4
	lblQuestion = Label(
		fen,
		text = questions80_us[q],
		font = ("Consolas", 20, "bold"),
		width = 500,
		justify = "center",
		wraplength = 400,
		background = "#ffffff",)
	son = pygame.mixer.Sound (sons80_us[q])
	son.play()
	lblQuestion.pack(pady=(100,30))

	global radiovar
	radiovar = IntVar()
	radiovar.set(-1)

	r1 = Radiobutton(
		fen,
		text = choix_reponses80_us[q][0],
		font = ("Times New Roman", 15),
		value = 0,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r1.pack(pady=5)

	r2 = Radiobutton(
		fen,
		text = choix_reponses80_us[q][1],
		font = ("Times New Roman", 15),
		value = 1,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r2.pack(pady=5)

	r3 = Radiobutton(
		fen,
		text = choix_reponses80_us[q][2],
		font = ("Times New Roman", 15),
		value = 2,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r3.pack(pady=5)

	r4 = Radiobutton(
		fen,
		text = choix_reponses80_us[q][3],
		font = ("Times New Roman", 15),
		value = 3,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r4.pack(pady=5)


def commence_quiz19_fr():
	global questions_order
	questions_order.append(q)
	global lblQuestion,r1,r2,r3,r4
	lblQuestion = Label(
		fen,
		text = questions19_fr[q],
		font = ("Consolas", 20, "bold"),
		width = 500,
		justify = "center",
		wraplength = 400,
		background = "#ffffff",)
	son = pygame.mixer.Sound (sons19_fr[q])
	son.play()
	lblQuestion.pack(pady=(100,30))

	global radiovar
	radiovar = IntVar()
	radiovar.set(-1)

	r1 = Radiobutton(
		fen,
		text = choix_reponses19_fr[q][0],
		font = ("Times New Roman", 15),
		value = 0,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r1.pack(pady=5)

	r2 = Radiobutton(
		fen,
		text = choix_reponses19_fr[q][1],
		font = ("Times New Roman", 15),
		value = 1,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r2.pack(pady=5)

	r3 = Radiobutton(
		fen,
		text = choix_reponses19_fr[q][2],
		font = ("Times New Roman", 15),
		value = 2,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r3.pack(pady=5)

	r4 = Radiobutton(
		fen,
		text = choix_reponses19_fr[q][3],
		font = ("Times New Roman", 15),
		value = 3,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r4.pack(pady=5)


def commence_quiz19_us():
	global questions_order
	questions_order.append(q)
	global lblQuestion,r1,r2,r3,r4
	lblQuestion = Label(
		fen,
		text = questions19_us[q],
		font = ("Consolas", 20, "bold"),
		width = 500,
		justify = "center",
		wraplength = 400,
		background = "#ffffff",)
	son = pygame.mixer.Sound (sons19_us[q])
	son.play()
	lblQuestion.pack(pady=(100,30))

	global radiovar
	radiovar = IntVar()
	radiovar.set(-1)

	r1 = Radiobutton(
		fen,
		text = choix_reponses19_us[q][0],
		font = ("Times New Roman", 15),
		value = 0,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r1.pack(pady=5)

	r2 = Radiobutton(
		fen,
		text = choix_reponses19_us[q][1],
		font = ("Times New Roman", 15),
		value = 1,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r2.pack(pady=5)

	r3 = Radiobutton(
		fen,
		text = choix_reponses19_us[q][2],
		font = ("Times New Roman", 15),
		value = 2,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r3.pack(pady=5)

	r4 = Radiobutton(
		fen,
		text = choix_reponses19_us[q][3],
		font = ("Times New Roman", 15),
		value = 3,
		variable = radiovar,
		command = rps_cochee,
		background = "#000000",
		foreground = "#ffffff")
	r4.pack(pady=5)




#Action dÃƒÂ©clanchÃƒÂ©e lorsqu'on appuie sur un des boutons catÃƒÂ©gories--------------------------------------------------------------------------------------------------------------
def btn_quiz_10_1():
	global btn_10_1s, btn_00_1, btn_10_2s, btn_00_2s, btn_80_frs, btn_80_uss, btn_19_frs, btn_19_uss, lbl_titreCTG, c
	btn_10_1s.destroy()
	btn_00_1.destroy()
	btn_10_2s.destroy()
	btn_00_2s.destroy()
	btn_80_frs.destroy()
	btn_80_uss.destroy()
	btn_19_frs.destroy()
	btn_19_uss.destroy()
	lbl_titreCTG.destroy()
	c = 0
	commence_quiz10_1()

def btn_quiz_00_1():
	global btn_10_1s, btn_00_1, btn_10_2s, btn_00_2s, btn_80_frs, btn_80_uss, btn_19_frs, btn_19_uss, lbl_titreCTG, c
	btn_10_1s.destroy()
	btn_00_1.destroy()
	btn_10_2s.destroy()
	btn_00_2s.destroy()
	btn_80_frs.destroy()
	btn_80_uss.destroy()
	btn_19_frs.destroy()
	btn_19_uss.destroy()
	lbl_titreCTG.destroy()
	c = 1
	commence_quiz00_1()

def btn_quiz_10_2():
	global btn_10_1s, btn_00_1, btn_10_2s, btn_00_2s, btn_80_frs, btn_80_uss, btn_19_frs, btn_19_uss, lbl_titreCTG, c
	btn_10_1s.destroy()
	btn_00_1.destroy()
	btn_10_2s.destroy()
	btn_00_2s.destroy()
	btn_80_frs.destroy()
	btn_80_uss.destroy()
	btn_19_frs.destroy()
	btn_19_uss.destroy()
	lbl_titreCTG.destroy()
	c = 2
	commence_quiz10_2()


def btn_quiz_00_2():
	global btn_10_1s, btn_00_1, btn_10_2s, btn_00_2s, btn_80_frs, btn_80_uss, btn_19_frs, btn_19_uss, lbl_titreCTG, c
	btn_10_1s.destroy()
	btn_00_1.destroy()
	btn_10_2s.destroy()
	btn_00_2s.destroy()
	btn_80_frs.destroy()
	btn_80_uss.destroy()
	btn_19_frs.destroy()
	btn_19_uss.destroy()
	lbl_titreCTG.destroy()
	c = 3
	commence_quiz00_2()


def btn_quiz_80_fr():
	global btn_10_1s, btn_00_1, btn_10_2s, btn_00_2s, btn_80_frs, btn_80_uss, btn_19_frs, btn_19_uss, lbl_titreCTG, c
	btn_10_1s.destroy()
	btn_00_1.destroy()
	btn_10_2s.destroy()
	btn_00_2s.destroy()
	btn_80_frs.destroy()
	btn_80_uss.destroy()
	btn_19_frs.destroy()
	btn_19_uss.destroy()
	lbl_titreCTG.destroy()
	c = 4
	commence_quiz80_fr()


def btn_quiz_80_us():
	global btn_10_1s, btn_00_1, btn_10_2s, btn_00_2s, btn_80_frs, btn_80_uss, btn_19_frs, btn_19_uss, lbl_titreCTG, c
	btn_10_1s.destroy()
	btn_00_1.destroy()
	btn_10_2s.destroy()
	btn_00_2s.destroy()
	btn_80_frs.destroy()
	btn_80_uss.destroy()
	btn_19_frs.destroy()
	btn_19_uss.destroy()
	lbl_titreCTG.destroy()
	c = 5
	commence_quiz80_us()

def btn_quiz_19_fr():
	global btn_10_1s, btn_00_1, btn_10_2s, btn_00_2s, btn_80_frs, btn_80_uss, btn_19_frs, btn_19_uss, lbl_titreCTG, c
	btn_10_1s.destroy()
	btn_00_1.destroy()
	btn_10_2s.destroy()
	btn_00_2s.destroy()
	btn_80_frs.destroy()
	btn_80_uss.destroy()
	btn_19_frs.destroy()
	btn_19_uss.destroy()
	lbl_titreCTG.destroy()
	c = 6
	commence_quiz19_fr()

def btn_quiz_19_us():
	global btn_10_1s, btn_00_1, btn_10_2s, btn_00_2s, btn_80_frs, btn_80_uss, btn_19_frs, btn_19_uss, lbl_titreCTG, c
	btn_10_1s.destroy()
	btn_00_1.destroy()
	btn_10_2s.destroy()
	btn_00_2s.destroy()
	btn_80_frs.destroy()
	btn_80_uss.destroy()
	btn_19_frs.destroy()
	btn_19_uss.destroy()
	lbl_titreCTG.destroy()
	c = 7
	commence_quiz19_us()


#Creation de la page categorie-----------------------------------------------------------------------------------------------------------
def choix_categories():
	global btn_10_1s, btn_00_1, btn_10_2s, btn_00_2s, btn_80_frs, btn_80_uss, btn_19_frs, btn_19_uss, lbl_titreCTG
	btn_10_1s = Button (fen,
		text = "Années 2010 (Partie 1)",
		command = btn_quiz_10_1,
		font = ("Broadway 20"),
		bg ="#1E90FF",
		fg = "white",
		width = 25,
		height = 1)
	btn_10_1s.pack(pady = 5)


	btn_10_2s = Button (fen,
		text = "Années 2010 (Partie 2)",
		font = ("Broadway 20"),
		command = btn_quiz_10_2,
		bg ="#1E90FF",
		fg = "white",
		width = 25,
		height = 1)
	btn_10_2s.pack(pady = 5)


	btn_00_1 = Button (fen,
		text = "Années 2000, en France",
		command = btn_quiz_00_1,
		font = ("Broadway 20"),
		bg ="#800080",
		fg = "white",
		width = 25,
		height = 1,)
	btn_00_1.pack(pady = 5)


	btn_00_2s = Button (fen,
		text = "Années 2000, US",
		command = btn_quiz_00_2,
		font = ("Broadway 20"),
		bg ="#800080",
		fg = "white",
		width = 25,
		height = 1)
	btn_00_2s.pack(pady = 5)


	btn_80_frs = Button (fen,
		text = "Années 80 - 90, en France",
		font = ("Broadway 20"),
		command = btn_quiz_80_fr,
		bg ="#00FF00",
		fg = "white",
		width = 25,
		height = 1)
	btn_80_frs.pack(pady = 5)


	btn_80_uss = Button (fen,
		text = "Annees 80 - 90, US",
		font = ("Broadway 20"),
		command = btn_quiz_80_us,
		bg ="#00FF00",
		fg = "white",
		width = 25,
		height = 1)
	btn_80_uss.pack(pady = 5)


	btn_19_frs = Button (fen,
		text = "Titres récents, en France",
		font = ("Broadway 20"),
		command = btn_quiz_19_fr,
		bg ="#FF0000",
		fg = "white",
		width = 25,
		height = 1)
	btn_19_frs.pack(pady = 5)


	btn_19_uss = Button (fen,
		text = "Titres récents, dans le monde",
		font = ("Broadway 20"),
		command = btn_quiz_19_us,
		bg ="#FF0000",
		fg = "white",
		width = 25,
		height = 1)
	btn_19_uss.pack(pady = 5)


	lbl_titreCTG = Label(fen,
		text = "Choisis une catégorie de chansons",
		font = ("Times", "35", "bold italic"),
		bg = "#4065A4",
		fg = "#FFD700",
		width = 110,
		height = 4)
	lbl_titreCTG.pack()

#Création première page---------------------------------------------------------------------------------------------------------------------
#Création du bouton start
def btn_start_enclenche():
	labelimage.destroy()
	lblInstruction.destroy()
	lblRegles.destroy()
	btnStart.destroy()
	choix_categories()
	init()

#Création fenetre
fen = Tk()
fen.title("Blind Test")
fen.geometry("820x690")
fen.config(background="#4065A4")
fen.iconbitmap("BTSMRL.ico")
fen.resizable(0,0)

#Image principale
img1 = PhotoImage(file="BTSMRL.png")
labelimage = Label(
	fen,
	image = img1,
	background = "#4065A4")
labelimage.pack(pady=(0,0))

#Création du bouton start
img2 = PhotoImage(file="btn_Start.png")
btnStart = Button(
	fen,
	image = img2,
	relief = FLAT,
	background = "#4065A4",
	border = 0,
	command = btn_start_enclenche)
btnStart.pack()

#Instructions du quizz
lblInstruction = Label(
	fen,
	text = "Lis les règles juste au-dessous\nLorsque tu es prêt, appuies sur start\n Amuse toi bien !",
	background = "#4065A4",
	font = ("Consolas",14),
	justify = "center")
lblInstruction.pack(pady=(0,40))

#Règles du quizz
lblRegles = Label(
	fen,
	text = "Choisis une catégorie de chansons\nLe Blind Test se lancera tout de suite après que tu aies choisi.\nAttention, l'extrait de la musique ne dure que 10 secondes\nUne catégorie comporte 6 questions, 1 bonne réponse compte pour 5 points.\nOn verra bien qui possède la meilleure culture musicale !",
	width = 100,
	height = 130,
	font = ("University Roman", 16),
	background = "#000000",
	foreground = "#FACA2F")
lblRegles.pack()

#Boucle fenetre(fin du code)------------------------------------------------------------------------------------------------------------
fen.mainloop()
pygame.quit()