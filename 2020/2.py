def isValidPassword(policy, password):
    policyRules = policy.split(' ')[0]
    policyMin = int(policyRules.split('-')[0])
    policyMax = int(policyRules.split('-')[1])
    policyChar = policy.split(' ')[1]
    count = 0
    for char in password:
        if (char == policyChar):
            count += 1
    print(policyMin, policyMax, policyChar, password, count)
    return count <= policyMax and count >= policyMin

validPasswords = 0
with open('input2.txt') as f:
    for line in f:
        policy = line.split(':')[0]
        password = line.split(':')[1]
        if (isValidPassword(policy, password)):
            validPasswords += 1
f.closed

print (validPasswords)





