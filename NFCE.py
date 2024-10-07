from bs4 import BeautifulSoup
import json

class NFCE:
    def __init__(self, html):
        self.html = BeautifulSoup(html, "lxml")


        self.chave = {}
        self.emissor_data = {}
        self.itens_data = []
        self.total_data = {}
        self.infos_data = {}

        self._conteudo = self.html.find('div', id='conteudo')
        self._emissor = self._conteudo.find('div', class_='txtCenter')
        self._tab_result = self._conteudo.find('table')
        self._total_nota = self._conteudo.find('div', id='totalNota')
        self._infos = self.html.find('div', id='infos')

    def chave_de_acesso(self):
        self.chave["chave"] = (self.html.find('span', class_='chave').text).replace(" ", "")

        return self.chave

    def emissor(self):
        contents = self._emissor.contents
        estabelecimento_tag = self._emissor.find('div', id='u20').text

        self.emissor_data["estabelecimento"] = estabelecimento_tag
        self.emissor_data["cnpj"] = ' '.join((contents[1].text).split())
        self.emissor_data["endereco"] = ' '.join((contents[2].text).split())
        
        return self.emissor_data

    def tabela_itens(self):
        itens = self._tab_result.findAll('tr')

        for item in itens:
            tags = item.td
            self.itens_data.append({
                'nome': tags.select('.txtTit')[0].text,
                'unidade': tags.select('.RUN')[0].strong.next_sibling,
                'valor_unidade': ' '.join((tags.select('.RvlUnit')[0].strong.next_sibling).split()),
                'quantia': tags.select('.Rqtd')[0].strong.next_sibling,
                'valor_total': item.select('.valor')[0].text

            })

        return self.itens_data

    def resumo(self):
        totais = self._total_nota.findAll('div', id='linhaTotal')

        for item in totais[:-1]:
            if item.label:
                self.total_data[' '.join((item.label.text).split())] = item.span.text

        return self.total_data
    
    def informacoes_gerais_da_nota(self):
        mapa_chaves = {
            "Número:": "numero",
            "Série:": "serie",
            "Emissão:": "emissao",
            "Protocolo de Autorização:": "protocolo_de_autorizacao"
        }
        for strong in self._infos.find('li').findAll('strong'):
            
            chave_temp = (strong.text).strip()

            if chave_temp in mapa_chaves:

                self.infos_data[mapa_chaves[chave_temp]] = ' '.join(str(strong.next_sibling).split())
        
        return self.infos_data
    
    def json_data(self):
        self.emissor()
        self.tabela_itens()
        self.resumo()
        self.informacoes_gerais_da_nota()
        self.chave_de_acesso()


        return json.dumps({"emissor": self.emissor_data, "itens": self.itens_data, "resumo": self.total_data, "info": self.infos_data, "chave": self.chave["chave"]})
