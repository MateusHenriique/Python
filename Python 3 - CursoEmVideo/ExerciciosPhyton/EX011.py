a = float(input('altura da parede: '))
l = float(input('largura da parede: '))
area = (a * l)
tinta = (
area / 2)
print('Sua parede tem dimenção de {}x{} e sua area é de {}m².'.format(a, l, area))
print('Para pintar toda a parede sera necessario {:.2f} litros de tinta.'.format(tinta))