import pandas as pd

def criar_dataframe(caminho_arquivo):
    def extrair_informacoes_portas_abertas(saida_portas):
        portas = []
        protocolos = []
        estados = []

        linhas = saida_portas.strip().split('\n')
        for linha in linhas:
            partes = linha.split()
            if len(partes) >= 3:
                portas.append(partes[0])
                protocolos.append(partes[1])
                estados.append(partes[2])

        return portas, protocolos, estados

    ips = []
    hosts = []
    tipos = []  # Adicionamos uma lista para armazenar o tipo (Físico ou Virtual)
    portas_abertas = []

    with open(caminho_arquivo, 'r') as arquivo:
        temp_ip = None
        temp_host = None
        temp_ports = []
        temp_tipo = None  # Variável para armazenar o tipo
        capturing_ports = False
        for linha in arquivo:
            linha = linha.strip()
            if linha.startswith('IP:'):
                if temp_ip is not None and temp_host is not None:
                    ips.append(temp_ip)
                    hosts.append(temp_host)
                    tipos.append(temp_tipo)  # Adiciona o tipo à lista
                    if temp_ports:
                        portas_abertas.append(', '.join(temp_ports))
                    else:
                        portas_abertas.append('Nenhuma porta aberta encontrada')
                temp_ip, temp_host = linha.split(' - Host: ')
                temp_ip = temp_ip.replace('IP:', '').strip()
                temp_host = temp_host.strip()
                temp_ports = []
                capturing_ports = False
            elif linha.startswith('Tipo:'):
                temp_tipo = linha.split('Tipo:')[1].strip()  # Obtém o tipo
            elif linha.startswith('Open Ports:'):
                temp_ports = []
                capturing_ports = True
            elif capturing_ports and linha and not linha.startswith('-'):
                partes = linha.split()
                if len(partes) >= 3:
                    porta = partes[0]
                    servico = partes[2]
                    temp_ports.append(f"{porta}/{servico}")

    if temp_ip is not None and temp_host is not None:
        ips.append(temp_ip)
        hosts.append(temp_host)
        tipos.append(temp_tipo)  # Adiciona o tipo à lista
        if temp_ports:
            portas_abertas.append(', '.join(temp_ports))
        else:
            portas_abertas.append('Nenhuma porta aberta encontrada')

    df = pd.DataFrame({'IP': ips, 'Host': hosts, 'Tipo': tipos, 'Portas abertas': portas_abertas})
    return df

# INICIO - CAMINHOS PARA ARQUIVOS DE LEITURA ************************* IAGO  *****************************************
# Especifique os caminhos dos arquivos VDC-SESUP que você deseja ler
caminho_arquivo_dmz192_sesup = r'C:\Users\Bolsista\Downloads\PortScan-git\data\vdc-sesup\dmz192.txt'
caminho_arquivo_dmz141_sesup = r'C:\Users\Bolsista\Downloads\PortScan-git\data\vdc-sesup\dmz141.txt'
caminho_arquivo_pesquisa_sesup = r'C:\Users\Bolsista\Downloads\PortScan-git\data\vdc-sesup\pesquisa.txt'
#caminho_arquivo_hpc223_sesup = r'C:\Users\Bolsista\Downloads\PortScan\data\vdc-sesup\hpc223.txt'
#caminho_arquivo_hpc222_sesup = r'C:\Users\Bolsista\Downloads\PortScan\data\vdc-sesup\hpc222.txt'
caminho_arquivo_operacional_sesup = r'C:\Users\Bolsista\Downloads\PortScan-git\data\vdc-sesup\operacional.txt'

# Especifique os caminhos dos arquivos VDC-COIDS que você deseja ler
caminho_arquivo_dmz_coids = r'C:\Users\Bolsista\Downloads\PortScan-git\data\vdc-coids\dmz_coids.txt'
caminho_arquivo_pesquisa_coids = r'C:\Users\Bolsista\Downloads\PortScan-git\data\vdc-coids\pesquisa_coids.txt'
#caminho_arquivo_hpc_coids = r'C:\Users\Bolsista\Downloads\PortScan\data\vdc-coids\hpc_coids.txt'
caminho_arquivo_operacional_coids = r'C:\Users\Bolsista\Downloads\PortScan-git\data\vdc-coids\operacional_coids.txt'
# FIM - CAMINHOS PARA ARQUIVOS DE LEITURA ************************* IAGO  *****************************************




# INICIO - CAMINHOS PARA ARQUIVOS DE LEITURA ************************* CAIO  *****************************************
# Especifique os caminhos dos arquivos VDC-SESUP que você deseja ler
#caminho_arquivo_dmz192_sesup = r'C:\Users\Caio Lemes\Documents\PortScan\PortScan\data\vdc-sesup\dmz192.txt'
#caminho_arquivo_dmz141_sesup = r'C:\Users\Caio Lemes\Documents\PortScan\PortScan\data\vdc-sesup\dmz141.txt'
#caminho_arquivo_pesquisa_sesup = r'C:\Users\Caio Lemes\Documents\PortScan\PortScan\data\vdc-sesup\pesquisa.txt'
#caminho_arquivo_operacional_sesup = r'C:\Users\Caio Lemes\Documents\PortScan\PortScan\data\vdc-sesup\operacional.txt'
#caminho_arquivo_hpc223_sesup = r'C:\Users\Bolsista\Downloads\PortScan\data\vdc-sesup\hpc223.txt'
#caminho_arquivo_hpc222_sesup = r'C:\Users\Bolsista\Downloads\PortScan\data\vdc-sesup\hpc222.txt'

# Especifique os caminhos dos arquivos VDC-COIDS que você deseja ler
#caminho_arquivo_dmz_coids = r'C:\Users\Caio Lemes\Documents\PortScan\PortScan\data\vdc-coids\dmz_coids.txt'
#caminho_arquivo_pesquisa_coids = r'C:\Users\Caio Lemes\Documents\PortScan\PortScan\data\vdc-coids\pesquisa_coids.txt'
#caminho_arquivo_hpc_coids = r'C:\Users\Bolsista\Downloads\PortScan\data\vdc-coids\hpc_coids.txt'
#caminho_arquivo_operacional_coids = r'C:\Users\Caio Lemes\Documents\PortScan\PortScan\data\vdc-coids\operacional_coids.txt'
# FIM - CAMINHOS PARA ARQUIVOS DE LEITURA ************************* CAIO  *****************************************


# Cria os DataFrames para VDC-SESUP
df_dmz_192_sesup = criar_dataframe(caminho_arquivo_dmz192_sesup)
df_dmz_141_sesup = criar_dataframe(caminho_arquivo_dmz141_sesup)
df_pesquisa_sesup = criar_dataframe(caminho_arquivo_pesquisa_sesup)
#df_hpc_223_sesup = criar_dataframe(caminho_arquivo_hpc223_sesup)
#df_hpc_222_sesup = criar_dataframe(caminho_arquivo_hpc222_sesup)
df_operacional_sesup = criar_dataframe(caminho_arquivo_operacional_sesup)

# Cria os DataFrames para VDC-COIDS
df_dmz_coids = criar_dataframe(caminho_arquivo_dmz_coids)
df_pesquisa_coids = criar_dataframe(caminho_arquivo_pesquisa_coids)
#df_hpc_coids = criar_dataframe(caminho_arquivo_hpc_coids)
df_operacional_coids = criar_dataframe(caminho_arquivo_operacional_coids)