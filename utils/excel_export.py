from io import BytesIO
import pandas as pd

def exportar_para_excel(df):
    """
    Exporta um DataFrame pandas para um arquivo Excel em memória (BytesIO).

    Args:
        df (pandas.DataFrame): DataFrame com os dados a serem exportados.

    Returns:
        BytesIO: objeto em memória contendo o arquivo Excel gerado.
    """
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Classificação')
    output.seek(0)
    return output
