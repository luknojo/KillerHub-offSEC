import requests
import urllib.parse
from bs4 import BeautifulSoup
from tqdm import tqdm
import json

def get_inputs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.find_all(["input", "textarea"]), soup

def crawl_inputs(domain):
    visited = set()
    queue = [domain]
    inputs_encontrados = {}

    while queue:
        url = queue.pop(0)
        if url in visited:
            continue

        print(f"\n🔎 Rastejando: {url}")
        visited.add(url)

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            inputs, _ = get_inputs(url)
            if inputs:
                inputs_encontrados[url] = [input_tag.get("name") or "(sem nome)" for input_tag in inputs]
                print(f"   📝 Encontrado {len(inputs)} campos digitáveis.")

            for link in soup.find_all("a", href=True):
                full_url = urllib.parse.urljoin(domain, link["href"])
                if domain in full_url and full_url not in visited:
                    queue.append(full_url)

        except requests.exceptions.RequestException:
            print(f"❌ Erro ao acessar {url}")

    return inputs_encontrados

if __name__ == "__main__":
    target_domain = input("🌐 Digite o domínio para varredura (ex: http://testphp.vulnweb.com): ")
    
    inputs_encontrados = crawl_inputs(target_domain)
    
    if inputs_encontrados:
        print("\n🚀 VARREDURA CONCLUÍDA! CAMPOS DIGITÁVEIS ENCONTRADOS:")
        for url, inputs in inputs_encontrados.items():
            print(f"\n🔗 {url}")
            for input_name in inputs:
                print(f"   📝 Campo: {input_name}")

        salvar_json = input("\n💾 Deseja salvar os resultados em JSON? (s/n): ").strip().lower()
        if salvar_json == "s":
            with open("inputs_encontrados.json", "w", encoding="utf-8") as f:
                json.dump(inputs_encontrados, f, indent=4)
            print("✅ Resultados salvos em 'inputs_encontrados.json'")
    else:
        print("\n✅ Nenhum campo digitável encontrado.")

    print("\n✅ Varredura concluída!")
