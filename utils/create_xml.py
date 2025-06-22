import os
import random
from datetime import datetime, timedelta

# Funções auxiliares

def gerar_num(n): return ''.join(random.choices('0123456789', k=n))
def gerar_chave(): return gerar_num(44)
def gerar_data(): return (datetime.now() - timedelta(days=random.randint(0, 365))).isoformat(timespec='seconds') + "-03:00"

def gerar_nome():
    return random.choice([
        'João Silva', 'Maria Oliveira', 'Ana Costa', 'Carlos Pereira', 'Lucas Moura',
        'Paula Lima', 'Renata Souza', 'Felipe Andrade', 'Juliana Campos', 'Roberto Dias'
    ])

def gerar_empresa():
    return random.choice([
        'Max Soluções Digitais Ltda', 'Construtora Novo Horizonte', 'Agência Criativa S/A',
        'Distribuidora Rápida EIRELI', 'Serviços Integrados Ltda', 'Indústria Alfa S.A.',
        'Tecnologia e Sistemas ME', 'Gestão Proativa LTDA', 'Consultoria BlueMind S/A'
    ])

def gerar_email(nome):
    return nome.lower().replace(' ', '.') + "@exemplo.com"

def gerar_endereco():
    return random.choice([
        'Rua das Rosas, 123', 'Av. Paulista, 1500', 'Rua do Comércio, 88', 'Av. Atlântica, 2020',
        'Estrada dos Pinheiros, 999', 'Travessa da Luz, 47'
    ])

def gerar_produto():
    prefixo = random.choice([
        'Prestação de serviço de', 'Compra de', 'Pagamento referente a', 'Aquisição de',
        'Locação de', 'Consultoria em', 'Despesa com', 'Treinamento de', 'Suporte técnico de'
    ])

    termo = random.choice([
        'campanha online', 'licença de software', 'materiais de escritório', 'transporte urbano',
        'serviços advocatícios', 'manutenção preventiva', 'sistema ERP', 'equipamentos eletrônicos',
        'insumos industriais', 'estrutura de eventos', 'serviços gráficos', 'energia elétrica',
        'hospedagem de site', 'monitoramento de rede', 'planejamento estratégico'
    ])

    detalhe = random.choice([
        '', ' - mensalidade', ' - contrato de 12 meses', ' com nota fiscal', ' - urgência',
        ' para filial zona sul', ' - compra coletiva', ' via cartão corporativo'
    ])

    return f"{prefixo} {termo}{detalhe}"

# Criar pasta
os.makedirs("data", exist_ok=True)

# Geração dos 10 arquivos
for i in range(1, 15):
    chave = gerar_chave()
    cnpj_emit = gerar_num(14)
    cnpj_dest = gerar_num(14)
    nome_emit = gerar_empresa()
    nome_dest = gerar_nome()
    produto = gerar_produto()
    nProt = gerar_num(15)
    nNF = random.randint(700000, 799999)
    cEAN = gerar_num(13)
    cProd = gerar_num(10)
    quantidade = random.randint(1, 100)
    valor_unit = round(random.uniform(10, 5000), 2)
    vProd = round(quantidade * valor_unit, 2)
    vICMS = round(vProd * 0.12, 2)
    vCOFINS = round(vProd * 0.076, 2)
    vPIS = round(vProd * 0.0165, 2)
    email_dest = gerar_email(nome_dest)
    endereco_emit = gerar_endereco()
    endereco_dest = gerar_endereco()
    placa = "ABC" + gerar_num(4)
    telefone = "11" + gerar_num(8)
    cep = gerar_num(8)

    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<nfeProc xmlns="http://www.portalfiscal.inf.br/nfe" versao="4.00">
  <protNFe>
    <infProt>
      <nProt>{nProt}</nProt>
      <digVal>abc123xyz==</digVal>
      <dhRecbto>{gerar_data()}</dhRecbto>
      <Id>Id{nProt}</Id>
      <chNFe>{chave}</chNFe>
      <xMotivo>Autorizado o uso da NF-e</xMotivo>
      <cStat>100</cStat>
    </infProt>
  </protNFe>
  <NFe>
    <infNFe Id="NFe{chave}">
      <ide>
        <tpNF>1</tpNF>
        <mod>55</mod>
        <indPres>{random.randint(0, 9)}</indPres>
        <tpImp>1</tpImp>
        <nNF>{nNF}</nNF>
        <cMunFG>3550308</cMunFG>
        <procEmi>0</procEmi>
        <finNFe>1</finNFe>
        <dhEmi>{gerar_data()}</dhEmi>
        <tpAmb>1</tpAmb>
        <indFinal>1</indFinal>
        <dhSaiEnt>{gerar_data()}</dhSaiEnt>
        <idDest>1</idDest>
        <tpEmis>1</tpEmis>
        <cDV>{random.randint(0, 9)}</cDV>
        <cUF>35</cUF>
        <serie>1</serie>
        <natOp>VENDA TESTE</natOp>
        <cNF>{gerar_num(8)}</cNF>
        <verProc>TesteGerador 1.0</verProc>
      </ide>
      <emit>
        <xNome>{nome_emit}</xNome>
        <CNPJ>{cnpj_emit}</CNPJ>
        <IE>{gerar_num(12)}</IE>
        <IM>{gerar_num(6)}</IM>
        <CRT>{random.choice([1, 3])}</CRT>
        <xFant>Filial {random.randint(1, 10)}</xFant>
        <enderEmit>
          <fone>{telefone}</fone>
          <UF>SP</UF>
          <xPais>BRASIL</xPais>
          <cPais>1058</cPais>
          <xLgr>{endereco_emit.split(',')[0]}</xLgr>
          <nro>{endereco_emit.split(',')[1]}</nro>
          <xMun>SAO PAULO</xMun>
          <cMun>3550308</cMun>
          <xBairro>BAIRRO CENTRAL</xBairro>
          <CEP>{cep}</CEP>
        </enderEmit>
      </emit>
      <dest>
        <xNome>{nome_dest}</xNome>
        <CNPJ>{cnpj_dest}</CNPJ>
        <enderDest>
          <fone>{telefone}</fone>
          <UF>SP</UF>
          <xPais>BRASIL</xPais>
          <cPais>1058</cPais>
          <xLgr>{endereco_dest.split(',')[0]}</xLgr>
          <nro>{endereco_dest.split(',')[1]}</nro>
          <xMun>SAO PAULO</xMun>
          <cMun>3550308</cMun>
          <xBairro>JARDIM TESTE</xBairro>
          <CEP>{cep}</CEP>
        </enderDest>
        <indIEDest>9</indIEDest>
        <email>{email_dest}</email>
      </dest>
      <det>
        <nItem>1</nItem>
        <prod>
          <cEAN>{cEAN}</cEAN>
          <cProd>{cProd}</cProd>
          <xProd>{produto}</xProd>
          <qCom>{quantidade:.4f}</qCom>
          <vUnCom>{valor_unit:.8f}</vUnCom>
          <vProd>{vProd:.2f}</vProd>
          <uCom>UN</uCom>
          <CFOP>5101</CFOP>
          <uTrib>UN</uTrib>
          <qTrib>{quantidade:.4f}</qTrib>
          <vUnTrib>{valor_unit:.8f}</vUnTrib>
          <cEANTrib>{cEAN}</cEANTrib>
        </prod>
        <imposto>
          <ICMS>
            <ICMS00>
              <orig>0</orig>
              <CST>00</CST>
              <modBC>3</modBC>
              <vBC>{vProd:.2f}</vBC>
              <pICMS>12.0000</pICMS>
              <vICMS>{vICMS:.2f}</vICMS>
            </ICMS00>
          </ICMS>
          <PIS>
            <PISAliq>
              <CST>01</CST>
              <vBC>{vProd:.2f}</vBC>
              <pPIS>1.6500</pPIS>
              <vPIS>{vPIS:.2f}</vPIS>
            </PISAliq>
          </PIS>
          <COFINS>
            <COFINSAliq>
              <CST>01</CST>
              <vBC>{vProd:.2f}</vBC>
              <pCOFINS>7.6000</pCOFINS>
              <vCOFINS>{vCOFINS:.2f}</vCOFINS>
            </COFINSAliq>
          </COFINS>
        </imposto>
      </det>
      <total>
        <ICMSTot>
          <vProd>{vProd:.2f}</vProd>
          <vNF>{vProd:.2f}</vNF>
          <vICMS>{vICMS:.2f}</vICMS>
          <vPIS>{vPIS:.2f}</vPIS>
          <vCOFINS>{vCOFINS:.2f}</vCOFINS>
        </ICMSTot>
      </total>
      <transp>
        <modFrete>0</modFrete>
        <transporta>
          <xNome>{nome_emit}</xNome>
          <CNPJ>{cnpj_emit}</CNPJ>
          <IE>ISENTO</IE>
          <xEnder>{endereco_emit}</xEnder>
          <xMun>SAO PAULO</xMun>
          <UF>SP</UF>
        </transporta>
        <veicTransp>
          <placa>{placa}</placa>
          <UF>SP</UF>
        </veicTransp>
        <vol>
          <qVol>{random.randint(1, 50)}</qVol>
          <esp>CAIXA</esp>
          <pesoL>{random.uniform(1, 500):.3f}</pesoL>
          <pesoB>{random.uniform(1, 500):.3f}</pesoB>
        </vol>
      </transp>
      <pag>
        <detPag>
          <tPag>01</tPag>
          <vPag>{vProd:.2f}</vPag>
          <indPag>0</indPag>
        </detPag>
      </pag>
    </infNFe>
  </NFe>
</nfeProc>
'''

    with open(f"xmls_gerados/nfe_ficticia_{i:02}.xml", "w", encoding="utf-8") as f:
        f.write(xml)

print("✅ 10 arquivos XML gerados com sucesso na pasta 'xmls_gerados'.")
