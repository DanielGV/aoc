mandatory = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
#optional = set(['cid'])
optional = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])

def valid(passport):
    passfields = passport.replace('\n', ' ').split(' ')
    fieldkeys = set(passfield.split(':')[0].strip() for passfield in passfields)
    return mandatory.issubset(fieldkeys)

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