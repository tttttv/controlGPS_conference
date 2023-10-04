phones = []
with open('megafon_sims', 'r') as f:
    sts = f.readlines()
    for s in sts:
        if s != '\n':
            phones.append(s.strip())

crm_phones = []
with open('crm_sims', 'r') as f:
    sts = f.readlines()
    for s in sts:
        crm_phones.append(s.strip())


diff = []
for phone in phones:
    if phone not in crm_phones:
        diff.append(phone)

print(len(diff))

dialogue_phones = []
with open('dialogue_sims', 'r') as f:
    sts = f.readlines()
    for s in sts:
        dialogue_phones.append(s.strip())


diff_final = []
for phone in diff:
    if phone not in dialogue_phones:
        diff_final.append(phone)

print(len(diff_final))
for d in diff:
    print(d)