import base64

x = "kouse@kraziemail.ml"
y = bytes(x, 'utf-8')
print(y)

z = base64.b64encode(y)
print(z)

a=z.decode("utf-8")
print(a)