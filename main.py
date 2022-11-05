import phonenumbers
from phonenumbers import carrier, geocoder
UserPhoneNumber = input("Enter Your Phone Number: ")
PhoneNumber = phonenumbers.parse(UserPhoneNumber)
print("Carrier:" + carrier.name_for_number(PhoneNumber, 'en'))
print("Region:" + geocoder.description_for_number(PhoneNumber, 'en'))
validity = phonenumbers.is_valid_number(PhoneNumber)
if validity:
    print("The Given Number is Valid")
else:
    print("The Given Number is Invalid")
