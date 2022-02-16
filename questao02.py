"""
Quastão 02
Débora se inscreveu em uma rede social para se manter em contato com seus amigos.
A página de cadastro exigia o preenchimento dos campos de nome e senha, porém a senha precisa ser forte.

O site considera uma senha forte quando ela satisfaz os seguintes critérios:
Possui no mínimo 6 caracteres.
Contém no mínimo 1 digito.
Contém no mínimo 1 letra em minúsculo.
Contém no mínimo 1 letra em maiúsculo.
Contém no mínimo 1 caractere especial. Os caracteres especiais são: !@#$%^&*()-+

Débora digitou uma string aleatória no campo de senha, porém ela não tem certeza se é uma senha forte.
Para ajudar Débora, construa um algoritmo que informe qual é o número mínimo de caracteres que devem ser adicionados para uma string qualquer ser considerada segura.
"""


fraca = True

while fraca:
    senha = input('Insira uma senha forte de, no mínimo, 6 caractéres:\n')
    if len(senha) < 6:
        print('Senha não atingiu o número de caractéres necessários, tente novamente.')
    else:
        if not any(x.isdigit() for x in senha):
            print('Senha não possui, pelo menos, um digito. Tente novamente.')
        else:
            if not any(x.isupper() for x in senha):
                print('Senha não possui, pelo menos, uma letra maiúscula. Tente novamente.')
            else:
                if not any(x.islower() for x in senha):
                    print('Senha não possui, pelo menos, uma letra minuscula. Tente novamente.')
                else:
                    if senha.find('!') >= 0:
                        print('Você tem uma senha forte!')
                        fraca = False
                    elif senha.find('@') >= 0:
                        print('Você tem uma senha forte!')
                        fraca = False
                    elif senha.find('#') >= 0:
                        print('Você tem uma senha forte!')
                        fraca = False
                    elif senha.find('$') >= 0:
                        print('Você tem uma senha forte!')
                        fraca = False
                    elif senha.find('%') >= 0:
                        print('Você tem uma senha forte!')
                        fraca = False
                    elif senha.find('^') >= 0:
                        print('Você tem uma senha forte!')
                        fraca = False
                    elif senha.find('&') >= 0:
                        print('Você tem uma senha forte!')
                        fraca = False
                    elif senha.find('*') >= 0:
                        print('Você tem uma senha forte!')
                        fraca = False
                    elif senha.find('(') >= 0:
                        print('Você tem uma senha forte!')
                        fraca = False
                    elif senha.find(')') >= 0:
                        print('Você tem uma senha forte!')
                        fraca = False
                    elif senha.find('-') >= 0:
                        print('Você tem uma senha forte!')
                        fraca = False
                    elif senha.find('+') >= 0:
                        print('Você tem uma senha forte!')
                        fraca = False
                    else:
                        print('Senha não possui, pelo menos, um caractére especial. Tente novamente.')