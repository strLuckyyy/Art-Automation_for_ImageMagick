import os
import sys
import shutil
import math
import subprocess
from zipfile import ZipFile

def verificar_imagemagick():
    try:
        resultado = subprocess.run(
            ["magick", "-version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if resultado.returncode == 0 and "ImageMagick" in resultado.stdout:
            print("[✓] ImageMagick encontrado.")
            return True
        else:
            print("[✗] ImageMagick não encontrado ou com problemas na instalação.")
            return False

    except FileNotFoundError:
        print("[✗] O comando 'magick' não foi encontrado. Verifique se o ImageMagick está instalado e no PATH.")
        return False


def criar_pasta(caminho):
    os.makedirs(caminho, exist_ok=True)


def mover_frames(nome_pasta, inicio, fim, raiz):
    destino = os.path.join(raiz, nome_pasta)
    criar_pasta(destino)

    print(f"[•] Movendo frames de {inicio} até {fim} para a pasta: {nome_pasta}")
    for i in range(inicio, fim + 1):
        nome_arquivo = f"{i:04}.png"
        origem = os.path.join(raiz, nome_arquivo)
        if os.path.isfile(origem):
            shutil.move(origem, os.path.join(destino, nome_arquivo))
        else:
            print(f"[!] Frame não encontrado: {nome_arquivo}")


def calcular_grade(n):
    side = math.sqrt(n)
    rows = math.floor(side)
    cols = math.ceil(n / rows)
    melhor_rows, melhor_cols = rows, cols
    melhor_diferenca = abs(cols - rows)

    for r in range(rows + 1, cols + 1):
        c = math.ceil(n / r)
        diferenca = abs(c - r)
        if c * r >= n and diferenca < melhor_diferenca:
            melhor_diferenca = diferenca
            melhor_rows = r
            melhor_cols = c

    return melhor_cols, melhor_rows


def criar_spritesheets(raiz, nome_sprite):
    for nome_pasta in os.listdir(raiz):
        caminho = os.path.join(raiz, nome_pasta)

        if os.path.isdir(caminho):
            arquivos_png = [f for f in os.listdir(caminho) if f.endswith(".png")]
            if not arquivos_png:
                continue

            total = len(arquivos_png)
            cols, rows = calcular_grade(total)
            tile = f"{cols}x{rows}"
            nome_saida = f"SS_{nome_sprite}-{nome_pasta}.png"
            comando = [
                "magick", "montage", "*",
                "-geometry", "1024x1024",
                "-tile", tile,
                "-background", "transparent",
                "-filter", "Catrom",
                nome_saida
            ]

            print(f"[→] Gerando spritesheet: {nome_saida} com {tile}...")
            subprocess.run(" ".join(comando), cwd=caminho, shell=True)


def zipar_pasta(pasta, zip_name):
    zip_path = os.path.join(os.getcwd(), f"{zip_name}.zip")

    with ZipFile(zip_path, 'w') as zipf:
        for root, _, files in os.walk(pasta):
            for file in files:
                caminho_absoluto = os.path.join(root, file)
                caminho_relativo = os.path.relpath(caminho_absoluto, pasta)
                zipf.write(caminho_absoluto, caminho_relativo)
    print(f"[✓] Pasta zipada: {zip_path}")


def organizar_e_zipar(pasta_zip, sprite_base=None, novo_nome=None):
    raiz = os.getcwd()
    zip_path = os.path.join(raiz, pasta_zip)
    criar_pasta(zip_path)
    print(f"[•] Criando pasta de organização: {pasta_zip}")

    # Mover spritesheets
    for nome_pasta in os.listdir(raiz):
        caminho = os.path.join(raiz, nome_pasta)
        if os.path.isdir(caminho):
            for arquivo in os.listdir(caminho):
                if arquivo.startswith("SS_") and arquivo.endswith(".png"):
                    origem = os.path.join(caminho, arquivo)
                    destino = os.path.join(zip_path, arquivo)
                    shutil.move(origem, destino)
                    print(f"[✓] Spritesheet movida: {arquivo}")

    # Mover sprite base
    if sprite_base:
        sprite_path = os.path.join(raiz, sprite_base)
        if os.path.isfile(sprite_path):
            novo_nome_final = novo_nome if novo_nome else sprite_base
            destino = os.path.join(zip_path, novo_nome_final)
            shutil.move(sprite_path, destino)
            print(f"[✓] Sprite base movida: {sprite_base} → {novo_nome_final}")
        else:
            print(f"[!] Sprite base '{sprite_base}' não encontrada.")

    zipar_pasta(zip_path, pasta_zip)


def exibir_ajuda():
    print("""
        [ ART - Automação de Organização de Sprites e Spritesheets para ImageMagick ]

        Comandos disponíveis:

        1- Separar e gerar spritesheets:
        Uso:
            > art <NomeSprite> <N> <Nome1> <Início1> <Fim1> <Nome2> <Início2> <Fim2> ...
        Exemplo:
            > art Player 3 Idle 1 20 Walk 21 60 Run 61 90

        O que faz:
        - Separa os frames entre os intervalos dados e move para subpastas.
        - Gera spritesheets dentro dessas subpastas usando o ImageMagick.
        - Usa como nome final: SS_<NomeSprite>-<NomeDaPasta>.png

        ⚠️ IMPORTANTE:
        - Certifique-se que o programa ImageMagick esteja instalado e acessível pelo terminal.

        ------------------------------------------------------------

        2- Organizar, mover a sprite base e zipar:
        Uso:
            > art -oaz <NomePastaZip> [SpriteBase] [NovoNomeSpriteBase]
        Exemplos:
            > art -oaz PlayerZip                                  # Apenas move os spritesheets para PlayerZip e zipa.
            > art -oaz PlayerZip SpriteBase.png                   # Move a base como está.
            > art -oaz PlayerZip SpriteBase.png NovoNomepSB.png   # Renomeia a base ao mover.

        O que faz:
        - Cria uma pasta <NomePastaZip>.
        - Move os arquivos SS_*.png das subpastas para lá.
        - Move a sprite base (se fornecida), podendo renomear.
        - Cria o arquivo zip <NomePastaZip>.zip com tudo.
          
        Sprite base é para caso precise de uma sprite base específica para o projeto, como uma imagem de referência ou template.

        ------------------------------------------------------------

        3- Ajuda:
        Uso:
            > art -help
            > art --help

        ------------------------------------------------------------
        """)


def main():
    args = sys.argv[1:]

    if not args or args[0] in ("-help", "--help"):
        exibir_ajuda()
        return

    if args[0] == "-oaz":
        if len(args) >= 2:
            nome_zip = args[1]
            sprite_base = args[2] if len(args) >= 3 else None
            novo_nome = args[3] if len(args) >= 4 else None
            organizar_e_zipar(nome_zip, sprite_base, novo_nome)
        else:
            print("[!] Uso incorreto do comando -oaz. Use -help para mais informações.")
        return

    if not verificar_imagemagick():
        print("[!] Cancelando geração de spritesheets.")
        return

    try:
        nome_sprite = args[0]
        quantidade = int(args[1])
        argumentos = args[2:]
        pasta_atual = os.getcwd()

        for i in range(quantidade):
            nome = argumentos[i * 3]
            inicio = int(argumentos[i * 3 + 1])
            fim = int(argumentos[i * 3 + 2])
            mover_frames(nome, inicio, fim, pasta_atual)
            print(f"[✓] {nome}: frames {inicio} até {fim} movidos para {nome}/")

        criar_spritesheets(pasta_atual, nome_sprite)
    except (IndexError, ValueError):
        print("[X] Erro nos argumentos. Use 'art -help' para ver a sintaxe correta.")


if __name__ == "__main__":
    main()
