for name in ['foo', 'bar', 'fuga']:
    print(name)

for i in range(3):
    print('i={}'.format(i))

for i, name in enumerate(['foo', 'bar', 'fuga']):
    print('i={}, name={}'.format(i, name))

i = 0
while i < 3:
    print('i<{}'.format(i))
    i += 1
