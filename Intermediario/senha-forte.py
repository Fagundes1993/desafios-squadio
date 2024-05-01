def verificar_forca_senha(senha):
    comprimento_minimo = 8
    tem_letra_maiuscula = False
    tem_letra_minuscula = False
    tem_numero = False
    tem_caractere_especial = False
    caracteres_especiais = "!@#$%^&*()_+-=[]{}|;:,.<>?`~"

    # Verificando o comprimento da senha
    if len(senha) < comprimento_minimo:
        return f"Sua senha e muito curta. Recomenda-se no minimo 8 caracteres."

    # Verificando se a senha contém letras maiúsculas, minúsculas, números e caracteres especiais
    for char in senha:
        if char.isupper():
            tem_letra_maiuscula = True
        elif char.islower():
            tem_letra_minuscula = True
        elif char.isdigit():
            tem_numero = True
        elif char in caracteres_especiais:
            tem_caractere_especial = True

    # Verificando se todos os critérios foram atendidos
    if not (tem_letra_maiuscula and tem_letra_minuscula and tem_numero and tem_caractere_especial):
        mensagem = 'Sua senha nao atende aos requisitos de seguranca.'
        return mensagem

    return 'Sua senha atende aos requisitos de seguranca. Parabens!'

# Obtendo a senha do usuário
senha = input().strip()

# Verificando a força da senha
resultado = verificar_forca_senha(senha)

# Imprimindo o resultado
print(resultado)