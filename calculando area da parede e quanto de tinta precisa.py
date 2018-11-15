larg = float(input('largura da parede: '))  # larg = largura
alt = float(input('altura da parede : '))   # alt = altura
tinta = larg*alt
print('sua parede tem a dimensão {}x{} e sua area é de {}m²'.format(larg, alt, larg*alt))
print('para pintar essa parede, você precisara de {}L de tinta '.format(tinta / 2))
