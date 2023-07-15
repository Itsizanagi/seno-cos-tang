import math

a = float(input('Digite um angulo: '))
seno = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tg = math.tan(math.radians(a))
print('O valor do seno vale: {:.2f} \n O valor do cosseno vale: {:.2f} \n O valor da tangente vale: {:.2f}' .format((seno), (cos),(tg)))
