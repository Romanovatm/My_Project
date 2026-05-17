from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date

get_mask_card_number("23523423523423")
get_mask_account("23523423523423")

print(mask_account_card("Visa Platinum 1234567891023456"))
print(mask_account_card("Счет 12345678910234560000"))
print(mask_account_card("Visa 1234567891023456"))

print(get_date("2024-03-11T02:26:18.671407"))
