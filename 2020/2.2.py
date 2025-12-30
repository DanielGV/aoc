

def isValidPassword(policy, password):
    policyRules = policy.split(' ')[0]
    pos1 = int(policyRules.split('-')[0])
    pos2 = int(policyRules.split('-')[1])
    policyChar = policy.split(' ')[1]

    char1 = password[pos1 - 1]
    char2 = password[pos2 - 1]

    print(pos1, pos2, policyChar, password, char1 == policyChar, char2 == policyChar, (char1 == policyChar) ^ (char2 == policyChar))
    return (char1 == policyChar) ^ (char2 == policyChar)

validPasswords = 0
with open('input2.txt') as f:
    for line in f:
        policy = line.split(':')[0]
        password = line.split(':')[1].strip()
        if (isValidPassword(policy, password)):
            validPasswords += 1
f.closed

print (validPasswords)





