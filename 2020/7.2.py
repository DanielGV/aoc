import functools
import re

bag_color = re.compile(r'((?:\d* )?\w+\s\w+) bags?')

def relation(contains):
    return contains[0], [(color[2:], int(color[0])) for color in contains[1:]] if contains[1] != ' no other' else []

def rule(line):
    return relation(re.findall(bag_color, line))

contents = {}
with open('input7.txt') as f:
    for line in f:
        print(rule(line))
        source, bags = rule(line)
        contents[source] = bags
f.closed

print(contents)

def contains(bag):
    return 1 + (sum(number*contains(color) for color, number in contents[bag]) if len(contents[bag])!=0 else 0)

my_bag = 'shiny gold'
my_contents = contains(my_bag)
print(my_contents - 1)