# coding:utf-8
def say_hello(a):
    if a % 2 == 0:
        b = 'babies.'
    else:
        b = 'ladies.'
    print("Hello World {0} {1}".format(a, b))


for i in range(0, 100):
    say_hello(i)

print 'hello single line'

print "I'm ok, what about \"you\"?"
print r"I'm ok, what about \"you\"?"

print r'''This's the first line
    I wrote a second line here
        To show how this "label" works'''

print u'我要学好Python'

print 4 + 4 / 2 + 2 * 2 + 0.01

print True & False | True
print True and False or True
print not True or not False
print 1 != 2 and 2 == 2

# Python把0、空字符串''和None看成 False，其他数值和非空字符串都看成 True
a = True
print a and 'Hello' or 'World'
print a and '' or 'World'

monsterlist = ['Wolverine', 'Angel', 'Cherry']
print monsterlist.__len__()

monsterlist.append('kitty')
print monsterlist.__len__()

monsterlist.insert(1, 'Black')
monsterlist.insert(-2, 'Merry')

print monsterlist.pop()
print monsterlist.pop(1)

print monsterlist

fixedlist = ('Lener', 'Hooky', 'CoCo')
print fixedlist[2]

fixedsingle = (1,)
print fixedsingle[0]

t = ('a', 'b', ['A', 'B'])
print t

t[2][0] = 'X'
t[2][1] = 'Y'
print t

for i in fixedlist:
    print i

for i in range(0, fixedlist.__len__()):
    if i == 2:
        print 'Sooooooooooooooooo Great'
    elif i == 1:
        print '..............'
    else:
        print "Not bad..."
    print "{0}. {1}".format(i, fixedlist[i])
print 'END'

for age in range(0, 50):
    if age <= 6:
        print '{0} kid'.format(age)
    elif age < 18:
        print '{0} teenage'.format(age)
    else:
        print '{0} adult'.format(age)

classmates = {
    "小明": 46,
    "小红": 60,
    "Landy": 90
}
for key in classmates.keys():
    print "{0}的得分是:{1}".format(key, classmates.get(key))
    if key == '小红':
        classmates.__setitem__(key, 100)
        print '{0}的分数有误, 改为:{1}'.format(key, classmates.get(key, 0))

for key in classmates:
    print "name:", key

for name, score in classmates.items():
    print name, ":", score

list = ['cookie', 'bitch', 'sexy', 'money', 'sexy']
set = set(list)
print set
for i in set:
    print i
print 'Cookie' in set
print 'cookie' in set


def fact(n):
    if n == 1:
        return 1;
    return n * fact(n - 1)


print fact(999)


def xxx(*param):
    print param[::2]
    print param[2:]
    print param[1:2]
    print param[:-1:2]


xxx(1, 3, 4, 'x', 'six')

print 'abcdefg'[1:-1:2]

for i in enumerate(list):
    print i[0], '-', i[1], "done."

L = [(x * (x + 1)) / 3.00 for x in range(1, 100) if x % 3 == 0]
print L

group = [m + n for m in 'ABC' for n in '123']
print group