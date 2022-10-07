# 13. Uma senha deve ser criada a partir da seguinte regra:
# Dois primeiros números
# Um caracter especial
# Cinco letras
# Faça uma função/método para verificar esta senha esta correta ou não, use FATIAMENTO DE STR Aqui deverá ocorrer, PASSAGEM DE PARÂMETRO POR VALOR.

def verifica_senha(s):
    if s[0].isdigit() and s[1].isdigit():
        x = False;
        for i in range(len(s)):
            if not s[i].isalpha() and not s[i].isdigit():
                x = True;
        if x:
            letras = 0;
            for i in range(len(s)):
                if s[i].isalpha():
                    letras += 1;
            if letras >= 5 and len(s)>= 8:
                print("A senha está VALIDADA")
            else:
                 print("A senha deve conter pelo menos 5 caracteres normais...")   
        else:
            print("A senha deve conter um caracter especial...")
    else:
        print("Os dois primeiros digitos DEVEM ser números...");
        

def main():
    s = input("Digite uma senha: ");
    verifica_senha(s);
    
main();