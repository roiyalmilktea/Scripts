class Person():
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getLang(self):
        return self.lang

    def getType(self):
        return self.type


pr = Person()

pr.name = "koki"
pr.age = 21
pr.lang = 'python'
pr.type = 'reversing'

a = pr.getName()
b = pr.getAge()
c = pr.getLang()
d = pr.getType()

qr = Person()

qr.name = 'roiyal'
qr.age = 18
qr.lang = 'C'
qr.type = 'pwn'

e = qr.getName()
f = qr.getAge()
g = qr.getLang()
h = qr.getType()


print(a, 'is', b, 'years.', 'favorite language is', c, 'and practice', d)
print(e, 'is', f, 'years.', 'favorite language is', g, 'and practice', h)
