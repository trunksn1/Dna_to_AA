#Programma che converte una sequenza di DNA nella proteina 
#corrispondente
#scritto e ideato dal Dr. Taurino Jacopo specializzando esaurito
#in genetica medica.

#PROTEINA A 1 LETTERA
#CORREZIONE POSIZIONE DUP

#Solo per giocare con sequenze casuali
from random import randint
import os

#Le quattro lettere della vita
Nucleotidi = ['T', 'C', 'A', 'G']

#Dizionario che traduce le triplette nucleotidiche in aminoacidi
Dna_to_AA = {
"TTT": "Phe", "TTC": "Phe", "TTA": "Leu", "TTG": "Leu", "CTT": "Leu", 
"CTC": "Leu", "CTA": "Leu", "CTG": "Leu", "ATT": "Ile", "ATC": "Ile", 
"ATA": "Ile", "ATG": "Met", "GTT": "Val", "GTC": "Val", "GTA": "Val", 
"GTG": "Val", "TCT": "Ser", "TCC": "Ser", "TCA": "Ser", "TCG": "Ser", 
"CCT": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro", "ACT": "Thr", 
"ACC": "Thr", "ACA": "Thr", "ACG": "Thr", "GCT": "Ala", "GCC": "Ala", 
"GCA": "Ala", "GCG": "Ala", "TAT": "Tyr", "TAC": "Tyr", "TAA": "STOP", 
"TAG": "STOP", "CAT": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln", 
"AAT": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys", "GAT": "Asp", 
"GAC": "Asp", "GAA": "Glu", "GAG": "Glu", "TGT": "Cys", "TGC": "Cys", 
"TGA": "STOP", "TGG": "Trp", "CGT": "Arg", "CGC": "Arg", "CGA": "Arg", 
"CGG": "Arg", "AGT": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg", 
"GGT": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
}

#Dizionario degli AA: scritti in 3 e 1 lettera
AA1to3 = {
"Ala": "A", "Gly": "G", "Ile": "I", "Leu": "L", "Pro": "P", "Val": "V",
"Phe": "F", "Trp": "W", "Tyr": "Y", "Asp": "D", "Glu": "E", "Arg": "R",
"His": "H", "Lys": "K", "Ser": "S", "Thr": "T", "Cys": "C", "Met": "M",
"Asn": "N", "Gln": "Q",
}	

def main():
	scelta = ""

	while not scelta:
		
		scelta = input("""\nSe vuoi giocare con una sequenza casuale scrivi 1, se hai un gene da tradurre scrivi 2: """)
		if scelta == "1":
			print("Hai scelto di giocare con la sequenza casuale!")
			x = crea_gene()
			print ("-".join(traduzione(x)))
			continue		
		elif scelta == "2":
			print("Hai scelto di tradurre un gene!")
			inizio()
			continue		
		else:
			scelta = ""


def crea_gene ():
	sequenza_casuale = []
	lunghezza_DNA = int(input("quanti nucleotidi?\n"))
	for x in range (0, lunghezza_DNA):
		base = Nucleotidi[randint(0, 3)]
		sequenza_casuale.append(base)
	print (str(sequenza_casuale))
	global scelta
	scelta = ""
	return sequenza_casuale

#Accetta il gene che sia espresso come Lista che come stringa!
def traduzione(gene):
	proteina = []
	prot1 = []
	tripletta = ""
	y = len(gene)
	for x in range(y):
		if gene[x] == "!":
			y -= 1
			continue
		tripletta = tripletta + gene[x] 
		if len(tripletta) == 3:
			print ("Tripletta: ", tripletta, "--->>", Dna_to_AA[tripletta])
			if Dna_to_AA[tripletta] == "STOP":
				print("Incontrato codone di STOP")
				prot1.append('***')
				break

			#Dicitura a 3 lettere
			proteina.append(Dna_to_AA[tripletta])
			#Dicitura a 1 lettera
			popaa= proteina.pop()
			prot1.append(AA1to3[popaa])
			
			tripletta = ""
	if type(gene) == list:
		return prot1
	else:
		prot1 = "-".join(prot1)
		return prot1
			
def inizio():
	nome_gene = input("Come si chiama il gene che vuoi tradurre?\n")
#Crea la cartella col nome del gene nella CWD (cioè cartella da dove
#viene lanciato questo script
	cartella = os.path.join(os.getcwd(), nome_gene)
#Error Checking con exist_ok=True, se la cartella già esiste non crasha
#il programma
	os.makedirs(cartella, exist_ok=True)
#entriamo nella cartella creata
	os.chdir(cartella)
#Crea il file nome_gene.txt nella cartella appena creata
	gene = input("""Incolla la sequenza del gene\n\n\n""").upper().replace(" ","")	#si può provare a fargli leggere la sequenza da un file già esistente
	miofile = (os.path.join(nome_gene + ".txt"))
	x = open(miofile, 'a')
	x.write('Sequenza di DNA del gene: ' + str(nome_gene) + ':\n\n')
	x.write(gene)
	x.write('\n\n')
	x.write('Proteina corrispettiva:\n\n')
	x.write(traduzione(gene))
	cnv = "x"
	while cnv:
		cnv = input("MUTAZIONE: scegli tra: 'del', 'dup', 'scambio' [lascia vuoto per terminare il programma]\n")
		if cnv.lower() == "dup":
			#chiamo la funzione dup che restituisce un gene_mutato che 
			#viene tradotto dalla funzione traduzione() e quindi scritto
			# nel file nome_gene.txt
			x.write(traduzione(dup(gene, x)))
			x.close()
			os.startfile(miofile)
			return 2
		elif cnv.lower() == "del":
			x.write(traduzione(dlz(gene, x)))
			x.close()
			os.startfile(miofile)
			return 3
		elif cnv.lower() == "scambio":
			x.write(traduzione(scambio(gene, x)))
			x.close()
			os.startfile(miofile)
			return 4
		else:
			return 1
			
		
def dup(gene, filetxt):
	dove = int(input("posizione della dup\n"))
	
	#DOMANDA, la dup può essere anche più grande di un solo nucleotidie? il mio codice funziona anche per dup più grandi.
	cosa = input("Inserisci la sequenza duplicata\n").upper()
	
	#Controllo che effettivamente la sequenza aggiunta sia composta da nucleotidi di DNA e non da cazzate
	while not cosa:
		for x in range(len(cosa)):
			if cosa[x] not in Nucleotidi:
				print ("Non hai inserito un nucleotide corretto: 'T', 'C', 'A', 'G'") 
				cosa = ""
				
	#Scrittura del gene una volta mutato, la dup viene messa DOPO il nucleotide indicato
	#es: scelta la posizione 5, i primi cinque nucleotidi saranno uguali, poi ci sarà la dup, e poi tutto il resto
	gene_mutato = gene[:(dove-1)] + "!" + cosa + "!" + gene[(dove-1):]
	
	filetxt.write('\n\n\n\nMUTAZIONE!!!! : c.' + str(dove) + 'dup' + str(cosa) + '\n\nNuova Sequenza del Gene:\n\n')
	filetxt.write(gene_mutato)
	filetxt.write('\n\nNuova proteina\n\n')
	return gene_mutato
	
#chiedere a MT come vengono scritte le DEL e cosa si intente: dove parte la del e dove finisce
def dlz(gene, filetxt):
	inizio = int(input("inizio della del\n"))
	fine = int(input("ultimo nucleotide deleto\n"))
	if inizio == fine:
		fine += 1
		gene_mutato = gene[: (inizio)] + "!" + gene[(fine):]
	else:
		gene_mutato = gene[: (inizio-1)] + gene[fine:]
	
	#MODIFICARE
	filetxt.write('\n\n\n\nDELEZIONE!!!!\n\n')
	filetxt.write(gene_mutato)
	filetxt.write('\n\nNuova proteina\n\n')
	return gene_mutato
	
#scambio tra due nucleotidi e basta
def scambio(gene, filetxt):
	posizione = int(input("Posizione del nucleotide da scambiare!\n"))
	originale = gene[(posizione-1)]
	
	nuovo = input("nuovo nucleotide\n").upper()
	
	gene_mutato = gene[:(posizione-1)] + "!" + nuovo + "!" + gene[posizione:]
	
	filetxt.write('\n\n\n\nMUTAZIONE!!!! : c.' + str(posizione) + str(originale) + '>' + str(nuovo) + '\n\nNuova Sequenza del Gene:\n\n')
	filetxt.write(gene_mutato)
	filetxt.write('\n\nNuova proteina\n\n')
	return gene_mutato
	
if __name__ == "__main__":
	inizio() #bypassa il giochino casuale direttamente
	scazzo()
	#main()
