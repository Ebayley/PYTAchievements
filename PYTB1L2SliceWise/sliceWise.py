#Haal de voornamen uit deze tekst op en maak gebruik van string slicing
tekst = "De Python lessen worden gegeven voor Erik, Erwin en ook door Hidde"

print("opdracht 1: \n" + tekst[37:41] + ", " + tekst[43:48] + ", " + tekst[61:66])

#Haal de namen van de vakken op uit deze tekst:
tekstEen = "SD vakken zijn Python, UXD, Frontend development en Backend development en nog veel meer ..."

print("opdracht 2: \n" + tekstEen[15:21] + ", " + tekstEen[23:26] + ", " + tekstEen[28:48] + ", " + tekstEen[52:72])

#Haal de laatste 6 letters op uit deze tekst:
tekstTwee = "Wat is hier het laatste woord?"

print("opdracht 3:\n" + tekstTwee[24:31])

#Haal de 5e tot en met de 8e letter op EN haal de 29e tot de 33e (dus tot niet MET de 33e) letters op uit deze tekst:
tekstDrie = "Het www is ontwikkeld vanaf 1989 door Tim Berners-Lee"

print("oprdacht 3:\n" + tekstDrie[4:7] + " " + tekstDrie[28:32])



