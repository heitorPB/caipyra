# coding: utf-8


dados = {
    'pacoquinha': {
        'desc': 'paçoquinhas',
        'ano': {2016: 400,
                2017: 825,
                2018: 1625}},
    'sonhos': {
        'desc': 'sonhos',
        'ano': {2016: 696000,
                # como não foi informado o valor de sonhos em 2017
                # calculou-se a estimativa da quantidade de sonhos na
                # razão de  crescimento do consumo de paçoquinhas
                2017: 1435500,
                # extrapolação linear + arredondamento para o número
                # ficar bonitinho :)
                2018: 2871666}},
    'quentao': {
        'desc': 'quentão',
        'ano': {2016: 125,
                2017: 30,
                2018: 40}},
    'carreta_furacao': {
        'desc': 'carreta furacão',
        'ano': {2016: 55,
                2017: 90,
                # não teve em Sanca, mas teve pyBar :)
                2018: 137}}
}


def estatistica(ano):
    msg_titulo = 'Em {0} foram:'.format(ano)
    print(msg_titulo)
    for item in dados:
        msg_ano = dados[item]['ano'][ano]
        msg_item = dados[item]['desc']
        msg_complemento = ''
        if (item == 'quentao'):
            msg_complemento = 'litros de '
        if (item == 'carreta_furacao'):
            msg_complemento = 'pessoas na '
        msg_conteudo = '    {0} {1}{2}!'.format(
            msg_ano, msg_complemento, msg_item)
        print(msg_conteudo)


def pacoquinhas(self):
    print('Juntos somos mais fortes, em 2016 comemos 400 paçoquinhas!')
    print('Em 2017 extrapolamos, comemos 825 paçoquinhas! Precisamos malhar!')
    print('Em 2018, näo definimos meta, mas dobramos o número de paçoquinhas e comemos 1625!')


def quentao(self):
    print('Em 2016 bebemos juntos 125 litros de quentão, avante!')
    print('Em 2017 foram apenas 30 litros de quentão :-(')
    print('Em 2018, bebmos 40 litros. Quase o número ideal!')


def sonhos(self):
    print('Em 2016 foram realizados 696 mil sonhos, e não eram os de goiabada')


def carreta_furacao(self):
    print('Em 2016 existiam 55 doidos na carreta furacão.')
    print('Em 2017, 90 doidos faziam isso, socorro!')
    print('Em 2018, não teve carreta furacão, mas teve greve dos caminhão.')
