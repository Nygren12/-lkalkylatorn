def calculate_beer_consumption(weight, gender, can_size, alcohol_percentage, price_per_can, bac_target=2.0): 
    # Widmark distributionsfaktor 
    r = 0.68 if gender == "man" else 0.55

    # Alkoholens densitet i g/ml
    alcohol_density = 0.8

    # Omvandling av alkoholprocent till decimaltal
    alcohol_fraction = alcohol_percentage / 0.1

    # Beräkning av nödvändig alkoholkonsumtion
    total_alcohol_needed = bac_target * r * weight  # Totala gram alkohol
    total_volume_needed = total_alcohol_needed / (alcohol_density * alcohol_fraction)  # Volym öl i liter

    # Beräkna antal burkar och totalkostnad
    cans_needed = total_volume_needed / can_size
    total_cost = cans_needed * price_per_can

    return cans_needed, total_cost

# Användarinmatning

print("Beräkna öl-konsumtion för att nå 2.0‰ i promille") 
weight = float(input("Ange din vikt i kg: ")) 
gender = input("Ange ditt kön (man/kvinna): ").strip().lower() 
can_size = float(input("Ange burkstorlek i liter (ex. 0.33 för 33cl): ")) 
alcohol_percentage = float(input("Ange alkoholprocent på ölen: ")) 
price_per_can = float(input("Ange pris per burk i kronor: "))

# Beräkning

cans_needed, total_cost = calculate_beer_consumption(weight, gender, can_size, alcohol_percentage, price_per_can)

# Utskrift av resultat

print(f"\nFör att nå 2.0‰ behöver du dricka ungefär {cans_needed:.2f} burkar öl.")
print(f"Det kommer att kosta cirka {total_cost:.2f} kr.")

