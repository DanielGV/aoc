import functools
import re

pattern = re.compile(r'(?P<origin>\w+\s\w+) bags? contain(?: (?P<bags>(?:\d* )?\w+\s\w+) bags?[,.])*')
bag_color = re.compile(r'(?P<origin>\w+\s\w+) bags?')


def relation(contains):
    return dict((color, contains[0]) for color in contains[1:])

def rule(line):
    return relation(re.findall(bag_color, line))

def merge(rules):
    merged = {}
    for rule in rules:
        print(rule)
        for k, v in rule.items():
            if k in merged:
                merged[k].append(v)
            else:
                merged[k] = [v]
    return merged
    

rules = []
with open('input7.txt') as f:
    for line in f:
        rules.append(rule(line))
f.closed

print(rules)
merged_rules = merge(rules)
print(merged_rules)

first = 'shiny gold'
work = ['shiny gold']
for item in work:
    if item in merged_rules:
        work.extend(merged_rules[item])

print(set(work))
print(len(set(work))-1)

