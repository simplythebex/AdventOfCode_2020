with open("day_4.txt", "r") as passports:
    passports = passports.read()

def clean_passports(data):
    cleaned_passports = []
    raw_passports = data.strip().split("\n\n")

    for raw_passport in raw_passports:
        passport_list = raw_passport.replace("\n", " ").split(" ")
        passport_dict = {}

        for item in passport_list:
            key, value = item.split(":")
            passport_dict[key] = value
        cleaned_passports.append(passport_dict)
    return cleaned_passports

def count_valid_passports(data):
    passports = clean_passports(data)
    valid_passports = []
    valid_key = {
    "byr",
	"iyr",
	"eyr",
	"hgt",
	"hcl",
	"ecl",
	"pid"
    }
    for passport in passports:
        passport_keys = set(passport.keys())
        valid_passports.append(valid_key.issubset(passport_keys))
    count = 0
    for passport in valid_passports:
        if passport == True:
            count += 1
    return count


print(count_valid_passports(passports))   
