from bs4 import BeautifulSoup # importar módulo BeautifulSoup para manipular dados do HTML
import requests # importar módulo requests para acessar HTML

import csv # importar módulo csv para salvar e/ou manipular arquivos .csv

# o código pode ser modificado para a inserção de outras urls
# entretanto, atente-se a dinâmica do site pois em certas ocasiões a estrutura HTML não será interpretada corretamente

url = 'https://www.lojadomecanico.com.br/produto/141283/36/314/mascara-respiratoria-semifacial-n95-antiviral-pff2-s-sem-valvula-alliance-ual200700#'
html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')
price = soup.find('span', id='product-price').text
print(f'Atualmente, o preço da unidade da máscara PFF2 Alliance, no site www.lojadomecanico.com.br, é {price}')

url2 = 'https://magazinemedica.com.br/produtos/mascara-descartavel-pff2-n95-protecao-94-a-un-descarpack/'
html2 = requests.get(url2)
soup2 = BeautifulSoup(html2.content, 'html.parser')
price2 = soup2.find('strong', class_='text-primary price').text
price2 = price2.replace(' ','')
print(f'Atualmente, o preço da unidade da máscara PFF2 Descarpack, no site www.magazinemedica.com.br, é {price2}')

price3 = None
while price3 == None: # precisei inserir um loop para repetir a requisição até conseguir o valor
    url3 = 'https://www.amazon.com.br/M%C3%A1scaras-9820-PFF2-V%C3%A1lvula-Unidades/dp/B09451ZD4K/ref=pd_vtp_5/146-8757633-3267625?pd_rd_w=Dswjn&pf_rd_p=460b1bd2-2dd3-4463-8569-0282c9641107&pf_rd_r=PRZ8VTWZV4GYMQHY58WF&pd_rd_r=25cc8b3b-36f8-4ed7-94b1-3f4d4950c517&pd_rd_wg=Ya5Lp&pd_rd_i=B09451ZD4K&psc=1'
    html3 = requests.get(url3)
    soup3 = BeautifulSoup(html3.content, 'html.parser')
    price3 = soup3.find('span', class_='a-offscreen')

price3 = soup3.find('span', class_='a-offscreen').text
print(f'Atualmente, o preço de 10 unidades da máscara PFF2 3M 9820, no site www.amazon.com.br, é {price3}')

price4 = None
while price4 == None: # precisei inserir um loop para repetir a requisição até conseguir o valor
    url4 = 'https://www.amazon.com.br/M%C3%A1scara-Hospitalar-KSN-10-02MH-10/dp/B094NYYXFN'
    html4 = requests.get(url4)
    soup4 = BeautifulSoup(html4.content, 'html.parser')
    price4 = soup4.find('span', class_='a-offscreen')
    
price4 = soup4.find('span', class_='a-offscreen').text
print(f'Atualmente, o preço de 10 unidades da máscara PFF2 KSN 10.02MH, no site www.amazon.com.br, é {price4}')

url5 = 'https://magazinemedica.com.br/produtos/mascara-respiratoria-pff2-n95-9920-contra-risco-biologico-3m/'
html5 = requests.get(url5)
soup5 = BeautifulSoup(html5.content, 'html.parser')
price5 = soup5.find('strong', class_="text-primary price").text
price5 = price5.replace(' ','')
print(f'Atualmente, o preço da unidade da máscara PFF2 3M 9920, no site www.magazinemedica.com.br, é {price5}')

price6 = None
while price6 == None: # precisei inserir um loop para repetir a requisição até conseguir o valor
    url6 = 'https://www.amazon.com.br/M%C3%A1scara-Aura-9320-Respirador-V%C3%A1lvula/dp/B09C122T2M/ref=coffee_espresso_sports_4/146-7119833-6306412?pd_rd_w=rzDPE&pf_rd_p=3d41a91b-ede6-43e2-b1be-9420728090c4&pf_rd_r=GM2053C0SYJ66ZWX9FMH&pd_rd_r=b49e7cfb-0ae7-4d46-bf5e-2dc116f3a368&pd_rd_wg=NPsK6&pd_rd_i=B09C122T2M&th=1'
    html6 = requests.get(url6)
    soup6 = BeautifulSoup(html6.content, 'html.parser')
    price6 = soup6.find('span', class_='a-offscreen')

price6 = soup6.find('span', class_='a-offscreen').text
print(f'Atualmente, o preço de 10 unidades da máscara PFF2 3M 9320+BR, no site www.amazon.com.br, é {price6}')

url7 = 'https://www.coutinhoepi.com/kit-10-mascaras-3m-aura-9320br-com-espuma-no-clipe-nasal-ca-30592'
html7 = requests.get(url7)
soup7 = BeautifulSoup(html7.content, 'html.parser')
price7 = soup7.find('span', class_='total').text
price7 = price7.replace(' ','')
print(f'Atualmente, o preço de 10 unidades da máscara PFF2 3M 9320, no site www.coutinhoepi.com, é {price7}')

url8 = 'https://magazinemedica.com.br/produtos/mascara-cirurgica-tripla-celastico-canvisa-50un-descarpack/'
html8 = requests.get(url8)
soup8 = BeautifulSoup(html8.content, 'html.parser')
price8 = soup8.find('strong', class_='text-primary price').text
price8 = price8.replace(' ','')
print(f'Atualmente, o preço de 50 unidades da máscara descartável Descarpack, no site www.magazinemedica.com, é {price8}')

price9 = None
while price9 == None: # precisei inserir um loop para repetir a requisição até conseguir o valor
    url9 = 'https://www.amazon.com.br/Mascara-Descartavel-Tripla-Elastico-Nasal/dp/B091CSXBL3/ref=pd_sbs_3/146-7119833-6306412?pd_rd_w=ZIhLi&pf_rd_p=cd87be50-d82a-47b7-ba72-5e5ad9968f57&pf_rd_r=APKY7JFF45VF3KSTSRG3&pd_rd_r=770b371d-0ca0-49b7-b1fe-e3491ab3acc6&pd_rd_wg=vrVI0&pd_rd_i=B091CYDSTB&th=1'
    html9 = requests.get(url9)
    soup9 = BeautifulSoup(html9.content, 'html.parser')
    price9 = soup9.find('span', class_='a-offscreen')

price9 = soup9.find('span', class_='a-offscreen').text
print(f'Atualmente, o preço de 50 unidades da máscara descartável QueroShoes, no site www.amazon.com.br, é {price9}')

url10 = 'https://loja.medixbrasil.com.br/products/mascara-tripla-descartavel-com-filtro-bfe-95-preta-caixa-50-un?currency=BRL&variant=39481671647311&utm_medium=cpc&utm_source=google&utm_campaign=Google%20Shopping&gclid=EAIaIQobChMIw6KLoNH49QIVlYaRCh2bIA0FEAQYEyABEgLVuvD_BwE'
html10 = requests.get(url10)
soup10 = BeautifulSoup(html10.content, 'html.parser')
price10 = soup10.find('div', class_='price-list').text
price10 = price10.replace(' ','')
print(f'Atualmente, o preço de 50 unidades da máscara descartável Medix, no site loja.medixbrasil.com.br, é {price10}')

price11 = None
while price11 == None: # precisei inserir um loop para repetir a requisição até conseguir o valor
    url11 = 'https://www.amazon.com.br/M%C3%81SCARA-CIR%C3%9ARGICA-TRIPLA-EL%C3%81STICO-DESCARPACK/dp/B00P4II6I6/ref=coffee_espresso_sports_2/146-7119833-6306412?pd_rd_w=Ett2J&pf_rd_p=3d41a91b-ede6-43e2-b1be-9420728090c4&pf_rd_r=G1JTRBXJ5PKCF9VVDFF2&pd_rd_r=56f727e7-f90d-4745-b457-3dc9fd39b512&pd_rd_wg=8V7eL&pd_rd_i=B00P4II6I6&psc=1'
    html11 = requests.get(url11)
    soup11 = BeautifulSoup(html11.content, 'html.parser')
    price11 = soup11.find('span', class_='a-offscreen')

price11 = soup11.find('span', class_='a-offscreen').text
print(f'Atualmente, o preço de 50 unidades da máscara descartável Descarpack, no site www.amazon.com.br, é {price11}')

price12 = None
while price12 == None: # precisei inserir um loop para repetir a requisição até conseguir o valor
    url12 = 'https://www.amazon.com.br/Mascara-Descartavel-Tripla-Camada-Elastico/dp/B0937NKVMY/ref=pd_sbs_2/146-7119833-6306412?pd_rd_w=ZIhLi&pf_rd_p=cd87be50-d82a-47b7-ba72-5e5ad9968f57&pf_rd_r=APKY7JFF45VF3KSTSRG3&pd_rd_r=770b371d-0ca0-49b7-b1fe-e3491ab3acc6&pd_rd_wg=vrVI0&pd_rd_i=B0937NKVMY&psc=1'
    html12 = requests.get(url12)
    soup12 = BeautifulSoup(html12.content, 'html.parser')
    price12 = soup12.find('span', class_='a-offscreen')

price12 = soup12.find('span', class_='a-offscreen').text
print(f'Atualmente, o preço de 50 unidades da máscara descartável Protector, no site www.amazon.com.br, é {price12}')

price13 = None
while price13 == None: # precisei inserir um loop para repetir a requisição até conseguir o valor
    url13 = 'https://www.amazon.com.br/M%C3%A1scara-Descart%C3%A1vel-Prote%C3%A7%C3%A3o-Com-Antibacteriana-El%C3%A1stico-Unissex/dp/B088HTLXFB?th=1'
    html13 = requests.get(url13)
    soup13 = BeautifulSoup(html13.content, 'html.parser')
    price13 = soup13.find('span', class_='a-offscreen')

price13 = soup13.find('span', class_='a-offscreen').text
print(f'Atualmente, o preço de 50 unidades da máscara descartável Proteconfort, no site www.amazon.com.br, é {price13}')

url14 = 'https://www.hetmed.com.br/mascara-cirurgica-hospitalar-descartavel-em-tiras-pacote-100-unid'
html14 = requests.get(url14)
soup14 = BeautifulSoup(html14.content, 'html.parser')
price14 = soup14.find('div', class_='price-big').text
price14 = price14.replace(' ','')
price14 = price14.replace('\n','') # precisei inserir esse replace adicional pra eliminar o pulo de linha
print(f'Atualmente, o preço de 100 unidades da máscara descartável HetMed, no site www.hetmed.com.br, é {price14}')

url15 = 'https://www.insiderstore.com.br/products/mascara-comfort?variant=40816682041493&currency=BRL&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&utm_campaign=gs-2021-04-28&utm_source=google&utm_medium=smart_campaign&gclid=EAIaIQobChMIwqaYzefV9gIVCwWRCh2yDgWdEAQYAiABEgKauPD_BwE'
html15 = requests.get(url15)
soup15 = BeautifulSoup(html15.content, 'html.parser')
price15 = soup15.find('span', class_='ProductMeta__Price Price Price--highlight Text--subdued u-h4').text
price15 = price15.replace(' ','')
print(f'Atualmente, o preço da unidade da máscara de pano Insider, no site www.insiderstore, é {price15}'+',00')