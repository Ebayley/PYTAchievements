verzekering_per_maand = 23
benzine_kosten_per_liter = 1.54
liter_per_kilometer = 0.2

#maandkosten = (km_per_maand x liter_per_kilometer x benzine_kosten_per_liter) + verzekering_per_maand

invoer = 0
while not isinstance(invoer, float):
	
	def bereken_maandkosten():
		maandkosten = ((km_per_maand * liter_per_kilometer) * benzine_kosten_per_liter) + verzekering_per_maand
		print("je scooter kost jou €", maandkosten, " per maand")	

	try:
		km_per_maand = input("hoeveel km rijd jij per maand? ")
		km_per_maand = float(km_per_maand)
		bereken_maandkosten()
		break
	
	except ValueError:
		print(km_per_maand + " is geen geldig getal!")
