from smartphone import Smartphone

catalog = []
phone_1 = Smartphone("Realme", "C55", "+7967652135")
phone_2 = Smartphone("Samsung", "GalaxyA24", "+7932652135")
phone_3 = Smartphone("POCO", "X5", "+739865135")
phone_4 = Smartphone("Tecno", "Camon 20 Pro", "+7963152135")
phone_5 = Smartphone("Honor", "X7b", "+7943652135")

catalog.append(phone_1)
catalog.append(phone_2)
catalog.append(phone_3)
catalog.append(phone_4)
catalog.append(phone_5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model} . {phone.phone_number}")
