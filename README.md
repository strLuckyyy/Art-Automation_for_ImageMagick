## Objetivo 🎯
Um utilitário em Python para facilitar a organização de sprites em subpastas e geraração de spritesheets otimizadas com o **ImageMagick** de forma automatizada. Foco para quem trabalha com animações 2D em jogos ou qualquer ferramenta visual que envolva muitos frames.

---

## O que faz? 👀
- Organiza frames em subpastas baseadas por nome e intervalo. Definidos por você.
- Cria spritesheets otimizadas, buscando sempre uma proporção quadrada (ou próxima disso) pra melhor aproveitamento e legibilidade.
- Agrupa e compacta os spritesheets com opção de incluir uma imagem base de referência caso queira.
- Totalmente controlado via terminal.
- Livre para qualquer alteração ou adaptação para casos específicos.
- Compatível com **Windows** e **Linux**.

---
## Motivação 🤔
Durante o desenvolvimento do jogo StarDusk em qual estou trabalhando atualmente, devido ao tempo para a conclusão do projeto eu decidi pesquisar alternativas mais "rápidas" para a criação das animações do jogo. 
Depois de algumas pesquisas, decidi usar o **Blender** para as animações, utilizando a técnica de cut-out, renderizando e fazendo as spritesheet com a ajuda do **ImageMagick**. Porém o processo de organização e compactação das animações após renderizar estavam custando muito tempo, disso surgiu a idea de automatizar tudo para dar mais folego no projeto.

---

## Requisitos 🛑:
* **Python 3.x** instalado e configurado no PATH do sistema.
* **ImageMagick** instalado ([https://imagemagick.org/script/download.php](https://imagemagick.org/script/download.php)) e o comando `magick` acessível no prompt.
* O arquivo `art.bat` disponível (disponível na pasta `/scripts` do repositório).

---

## Instalação no Windows 🪟
1. **Clone o repositório**

```bash
git clone https://github.com/strLuckyyy/Art-Automation_for_ImageMagick.git
cd Art-Automation_for_ImageMagick
```

2. **Adicione a pasta clonada no PATH do Windows**

* Pressione `Win + R`, digite `sysdm.cpl` e aperte Enter.
* Vá na aba **Avançado** > **Variáveis de Ambiente**.
* Em **Variáveis do sistema**, selecione `Path` e clique em **Editar**.
* Clique em **Novo** e adicione o caminho da pasta (ex: `C:\Art`).
* Confirme tudo.

3. **Reinicie o terminal ou o PowerShell para que a alteração no PATH tenha efeito.**

### Uso

Agora você pode rodar o comando `art` de qualquer pasta no terminal, seguindo o padrão:

```bash
art Nome NumeroDePastas nome1 inicio1 fim1 nome2 inicio2 fim2 ...
```

Exemplo:

```bash
art Player 2 walk 1 20 run 21 40
```

Para informações e mais comandos:

```bash
art -help
```

---

## Instalação no Linux 🐧

1. **Clone o repositório**

```bash
git clone https://github.com/strLuckyyy/Art-Automation_for_ImageMagick.git
cd Art-Automation_for_ImageMagick
```

2. **Dê permissão de execução ao script `art.sh`**

```bash
chmod +x scripts/art.sh
```

3. **(Opcional) Adicione o script ao PATH**

Para conseguir usar o comando `art` de qualquer lugar no terminal, você pode criar um link simbólico ou mover o script para uma pasta já incluída no PATH:

**Opção 1 – Link simbólico (recomendado):**

```bash
sudo ln -s $(pwd)/scripts/art.sh /usr/local/bin/art
```

**Opção 2 – Mover para o `/usr/local/bin`:**

```bash
sudo cp scripts/art.sh /usr/local/bin/art
```

4. **Certifique-se de que o Python 3 e o ImageMagick estão instalados**

```bash
python3 --version
magick --version
```

---

### Uso

Agora é só usar o comando normalmente no terminal:

```bash
art Nome NumeroDePastas nome1 inicio1 fim1 nome2 inicio2 fim2 ...
```

Exemplo:

```bash
art Player 2 walk 1 20 run 21 40
```

Para ver todos os comandos disponíveis:

```bash
art -help
```

---

