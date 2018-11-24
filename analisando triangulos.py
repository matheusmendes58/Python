print('====' * 30)
print('ANALISADOR DE TRIANGULOS')
print('====' * 30)
s1 = float(input('Primeiro segmento:'))
s2 = float(input('Segundo segmento: '))
s3 = float(input('terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos FORMAM TRIANGULO  ')
else:
    print('os segmentos NÃO FORMAM UM TRIANGULO')
