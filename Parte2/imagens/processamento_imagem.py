from pathlib import Path
from PIL import Image, ImageStat


def analisar_imagem():
    caminho_imagem = Path(__file__).with_name("img.jpg")

    with Image.open(caminho_imagem) as imagem:
        imagem = imagem.convert("RGB")

        largura, altura = imagem.size
        media_vermelho, media_verde, media_azul = ImageStat.Stat(imagem).mean

    vermelho = round(media_vermelho)
    verde = round(media_verde)
    azul = round(media_azul)

    if verde >= vermelho and verde >= azul:
        cor_basica = "verde"
    elif vermelho >= verde and vermelho >= azul:
        cor_basica = "vermelho"
    else:
        cor_basica = "azul"

    print("=== Análise simples da imagem ===")
    print(f"Arquivo analisado: {caminho_imagem.name}")
    print(f"Dimensões: {largura} x {altura} pixels")
    print(f"Média dos pixels RGB: vermelho={vermelho}, verde={verde}, azul={azul}")
    print(f"Cor básica predominante pela média: {cor_basica}")


if __name__ == "__main__":
    analisar_imagem()