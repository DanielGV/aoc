import re
import sys

mandatory = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
#optional = set(['cid'])
optional = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])

year_pattern = re.compile(r'^\d{4}$')
def valid_byr(value):
    return year_pattern.match(value) and 1920 <= int(value) <= 2002

def valid_iyr(value):
    return year_pattern.match(value) and 2010 <= int(value) <= 2020

def valid_eyr(value):
    return year_pattern.match(value) and 2020 <= int(value) <= 2030

hgt_pattern = re.compile(r'^\d+((cm)|(in))$')
def valid_hgt(value):
    return bool(hgt_pattern.match(value)) and (((150 <= int(value[:-2]) <= 193) if value[-2:] == 'cm' else False) or ((59 <= int(value[:-2]) <= 76) if value[-2:] == 'in' else False))

hcl_pattern = re.compile(r'^#[0-9a-f]{6}$')
def valid_hcl(value):
    return bool(hcl_pattern.match(value))

def valid_ecl(value):
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

pid_pattern = re.compile(r'^\d{9}$')
def valid_pid(value):
    return bool(pid_pattern.match(value))

def get_validation_fun(key):
    return getattr(sys.modules[__name__], "valid_%s" % key)

def get_fields(passport):
    passfields = passport.replace('\n', ' ').split(' ')
    return ([passfield.split(':')[0].strip(), passfield.split(':')[1].strip()] for passfield in passfields if passfield is not '')

def get_key(field):
    key, value = field
    return key

def valid(passport):
    fields = list(get_fields(passport))
    #print(*[(key, value, get_validation_fun(key)(value)) for key, value in fields if key in mandatory], sep='\n')
    #print(bool(mandatory.issubset(set(key for key,value in fields))), all(get_validation_fun(key)(value) for key, value in fields if key in mandatory))
    return mandatory.issubset(key for key,value in fields) and all(get_validation_fun(key)(value) for key, value in fields if key in mandatory)

passports = []
passport = ''
with open('input4.txt') as f:
    for line in f:
        passport += line
        if (line == '\n'):
            passports.append(passport)
            passport = ''
    passports.append(passport)
f.closed

print(sum(1 for passport in passports if valid(passport)))