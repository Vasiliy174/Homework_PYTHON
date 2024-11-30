from Address import Address
from Mailing import Mailing

from_address = Address("456123", "Краснодар", "Сталина"," ""89", "12")

to_address = Address("148750", "Париж", "Ленина"," ""139", "45")

mailing = Mailing("89756910", from_address, to_address, "250")

print(mailing)
