nome = str(input('Qual é o seu nome?'))
if nome == 'Hta':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Eduarda' or nome == 'Maria eduarda':
    print('Seu nome é bem popular!')
elif nome in 'Lais Agatha Priscila':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))