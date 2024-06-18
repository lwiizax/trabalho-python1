tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para o download (MB): "))
velocidade_internet_mbps = float(input("Digite a velocidade do link de internet (MBPS): "))

tempo_download_minutos = (tamanho_arquivo_mb / (velocidade_internet_mbps / 8)) / 60
print("O tempo de download sera de aproximadamente: ", tempo_download_minutos, "minutos.")