import xml.etree.ElementTree as ET

def parse_xml(file):
    ns = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
    try:
        tree = ET.parse(file)
        root = tree.getroot()

        nfe = root.find('.//nfe:NFe', ns)
        if nfe is None:
            raise ValueError("Elemento <NFe> não encontrado.")

        ide = nfe.find('.//nfe:ide', ns)
        det = nfe.find('.//nfe:det', ns)
        prod = det.find('.//nfe:prod', ns) if det is not None else None
        emit = nfe.find('.//nfe:emit', ns)

        numero_nf = ide.find('nfe:nNF', ns).text if ide is not None else 'N/A'
        descricao = prod.find('nfe:xProd', ns).text if prod is not None else 'N/A'
        valor = float(prod.find('nfe:vProd', ns).text) if prod is not None else 0.0
        fornecedor = emit.find('nfe:xNome', ns).text if emit is not None else 'Desconhecido'
        ncm_elem = prod.find('nfe:NCM', ns) if prod is not None else None
        ncm = ncm_elem.text if ncm_elem is not None else 'N/A'
        quantidade = prod.find('nfe:qCom', ns).text if prod is not None else '0'

        return {
            "numero_nf": numero_nf,
            "descricao": descricao,
            "valor": valor,
            "fornecedor": fornecedor,
            "ncm": ncm,
            "quantidade": quantidade,
        }

    except Exception as e:
        print(f"Erro: {e}")
        return {
            "numero_nf": "Erro ao ler XML",
            "descricao": "Erro ao ler XML",
            "valor": 0.0,
            "fornecedor": "Desconhecido",
            "ncm": "N/A",
            "quantidade": "0"
        }
