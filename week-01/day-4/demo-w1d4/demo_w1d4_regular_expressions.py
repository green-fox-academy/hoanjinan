import re

my_string = "hi! hello world!"

p = re.compile("hello")

print(p.match(my_string))
print(p.search(my_string))

# character set [](^)
print(re.match("[abc]", "a")) #if a in the set a, b, c
print(re.match("[^abc]", "a")) #if a not in the set a, b, c
print(re.match("[a-z]", "a")) #if a in the set from a to z
print(re.match("[\w]", "a")) #if a in the set from a to z
print(re.match(r"\\section", "\section"))

#predifined character sets \w\W, \d\D, \s\S
print(re.match("\S", "tad"))

#repetition +(one or more), *(zero or more), ?(zero or one), {m, n}(between m and n inclusive)
print(re.match("a+", "aaaaa"))
print(re.match("a?b", "b"))
print(re.match("a{1,2}b", "aab"))
print(re.match("[abc]+", "abc"))
print(re.search("[abc]+", "tv abc"))

#matching (match, search, findall, finditer)
print(re.search("[abc]+", "abcacde abchgz"))
print(re.findall("[abc]+", "abcacde abchgz"))

#match object(None, group, start, end, span)
my_string = "This is Zilan: 93874629036 from Canton"
m = re.search("[\d]+", my_string)
print(m.end(), m.start(), m.group(), m.span())
print(m)

#module-level functions(match, search, findall)
#compile first then match (for loop is faster)
p = re.compile("[abc]")
for i in range(10000):
    p.match("a")

#compile and match at the same time (compiles 10000 times - very slow)
for i in range(10000):
    re.match("[abc]", "a")

#replacing match (sub)
my_string = "This is Zilan: 93874629036 from Canton post code: 510000"
a = re.sub("[\d]+", "<sensitive data>", my_string)#(can put count and flag in the end)
print(a)

#groups (non-capturing)
my_string = "The weather is is nice"
b = re.search(r"(\w+)\s\1", my_string)#r = raw string, braces() = group, \1 = refer to the first group
print(b)

match = re.search(r"^(?:https?://)?(?:www\.)?(\w+(?:\.\w+)+)$", "https:www.epam.com")
print(match)