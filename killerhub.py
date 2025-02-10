import os
import subprocess
from colorama import init, Fore, Back, Style

init(autoreset=True)

def mostrar_marca_dagua():
    marca_dagua = """
    ##################################################
    #                                                #
    #           🚨 HUB DE EXECUÇÃO DE SCRIPTS 🚨     #
    #    Selecione o script que deseja executar:     #
    #                github.com/luknojo              #
    ##################################################
    """
    print(Fore.CYAN + Back.BLACK + Style.BRIGHT + marca_dagua)

def menu():
    print(Fore.YELLOW + "1 - XSS Killer (Crawler XSS)")
    print(Fore.YELLOW + "2 - SQL Injection Killer (Crawler SQL Injection)")
    print(Fore.YELLOW + "3 - Sair")

def help_xss_killer():
    help_text = """
    🔥 XSS KILLER - Modo de Ajuda 🔥

    📌 Como usar:
    1⃣ Insira o domínio alvo quando solicitado (exemplo: http://testphp.vulnweb.com)
    2⃣ O scanner irá rastrear todas as URLs do site.
    3⃣ No final, será exibida a lista de inputs vulneráveis e você pode salvar em JSON.

    ⚠️ Importante:
    - O script **NÃO** verifica XSS em código HTML direto, apenas em campos digitáveis.
    - Todos os testes são realizados **de forma automatizada**.

    🏴‍☠️ Use com responsabilidade!
    """
    print(Fore.CYAN + help_text)

def help_sql_killer():
    help_text = """
    🔧 SQL INJECTION KILLER - Modo de Ajuda 🔧

    📌 Como usar:
    1⃣ Insira a URL alvo que contém parâmetros vulneráveis (exemplo: http://testphp.vulnweb.com/listproducts.php?cat=1)
    2⃣ O scanner tentará explorar injeção SQL nos parâmetros detectados.
    3⃣ Se vulnerável, serão exibidas informações sobre o banco de dados e tabelas.

    ⚠️ Importante:
    - O script **simula ataques** baseados em SQLMap.
    - Testes **automatizados**, mas podem haver **falsos positivos**.

    🏴‍☠️ Use com responsabilidade!
    """
    print(Fore.CYAN + help_text)

def executar_xss_killer():
    help_xss_killer()  
    input(Fore.YELLOW + "\nPressione ENTER para iniciar o XSS Killer...")
    print(Fore.GREEN + "\nIniciando o XSS Killer...\n")
    subprocess.run(["python", "xsskiller.py"])  

def executar_sql_injection_killer():
    help_sql_killer()
    input(Fore.YELLOW + "\nPressione ENTER para iniciar o SQL Injection Killer...")
    print(Fore.GREEN + "\nIniciando o SQL Injection Killer...\n")
    subprocess.run(["python", "sqlkiller.py"])  

def hub_execucao():
    while True:
        mostrar_marca_dagua()
        menu()
        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            executar_xss_killer()
        elif escolha == "2":
            executar_sql_injection_killer()
        elif escolha == "3":
            print(Fore.RED + "Saindo do Hub...")
            break
        else:
            print(Fore.RED + "Opção inválida! Tente novamente.")

if __name__ == "__main__":
    hub_execucao()
