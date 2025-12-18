# 🎮 Mine to VRML Converter

Um conversor simples em Python que transforma construções do Minecraft (arquivos `.schem`) em modelos 3D VRML, desenvolvido para auxiliar estudantes de computação gráfica a criar projetos visuais complexos.

## 📋 Sobre o Projeto

Este projeto foi desenvolvido durante o curso técnico em informática para facilitar a criação de modelos 3D em VRML. A ideia surgiu da necessidade de construir uma escavadeira em código VRML para um projeto de computação gráfica - em vez de programar cada bloco manualmente, este conversor permite criar o modelo no Minecraft e convertê-lo automaticamente para VRML.

> ⚠️ **Projeto em desenvolvimento ativo!** Atualmente trabalhando na implementação de geometrias especiais para cercas, muralhas e lajes (slabs). Por enquanto, esses blocos são renderizados como cubos padrão.

## ✨ Funcionalidades

- 🔄 Converte arquivos `.schem` (Minecraft Schematics) para formato VRML 2.0
- 🎨 Suporte a múltiplos blocos do Minecraft com cores precisas:
  - Concrete (16 cores)
  - Wool (16 cores)
  - Terracotta (16 cores)
  - Cercas (Fences) - 🚧 *cores suportadas, geometria em desenvolvimento*
  - Muralhas (Walls) - 🚧 *cores suportadas, geometria em desenvolvimento*
  - Lajes (Slabs) - 🚧 *em desenvolvimento*
  - Materiais base (stone, grass, dirt, sand, etc.)
- 💡 Configuração automática de iluminação e câmera
- 📦 Ignora blocos de ar automaticamente
- 🎯 Posicionamento preciso dos blocos

## 🚀 Como Usar

### Pré-requisitos

- Python 3.7 ou superior
- Ambiente virtual (recomendado)

### Instalação

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/mine-to-vrml.git
cd mine-to-vrml
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv env
# Windows
env\Scripts\activate
# Linux/Mac
source env/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Uso Básico

1. Coloque seu arquivo `.schem` na pasta do projeto
2. Edite a linha 112 do `main.py` com o nome do seu arquivo:
```python
nbt = nbtlib.load("SEU_ARQUIVO_AQUI.schem")
```

3. Execute o script:
```bash
python main.py
```

4. O arquivo `saida.wrl` será gerado automaticamente

### Visualizando o Resultado

Para visualizar o arquivo VRML gerado, você pode usar:
- **view3dscene** - [Download](https://castle-engine.io/view3dscene.php)
- **FreeWRL** - [Download](http://freewrl.sourceforge.net/)
- Navegadores com suporte a VRML (plugins necessários)

## 📁 Estrutura do Projeto

```
MINE_TO_VRML/
├── main.py                    # Script principal de conversão
├── requirements.txt           # Dependências do projeto
├── env/                       # Ambiente virtual Python
├── exemplos_construcoes/      # Exemplos de arquivos .schem
│   ├── arquivo_teste.schem
│   ├── construcao_mine.schem
│   └── escavadeira_completa.schem
└── exemplo_resultados/        # Exemplos de saída VRML
    └── saida.wrl
```

## ⚠️ Limitações Atuais

Algumas funcionalidades ainda estão em desenvolvimento:

- **Cercas e Muralhas**: Atualmente renderizadas como cubos padrão. A implementação de geometrias cilíndricas está planejada.
- **Lajes (Slabs)**: Ainda não possuem geometria customizada (metade da altura).
- **Faces Ocultas**: Todas as faces dos blocos são renderizadas, mesmo as que não são visíveis.

## 🎨 Blocos Suportados

O conversor atualmente suporta mais de 70 tipos diferentes de blocos do Minecraft com **cores corretas**, incluindo:

- **Concrete**: Todas as 16 variações de cor
- **Wool**: Todas as 16 variações de cor
- **Terracotta**: Todas as 16 variações de cor
- **Fences**: Oak, Spruce, Birch, Jungle, Acacia, Dark Oak, Mangrove, Crimson, Warped
- **Walls**: Cobblestone, Stone Brick, Granite, Diorite, Andesite, Brick, Sandstone, etc.
- **Materiais Base**: Stone, Grass, Dirt, Sand, Gravel, Planks, Glass

## 🔧 Dependências Principais

- **nbtlib** (2.0.4) - Leitura de arquivos NBT/Schematic do Minecraft
- **numpy** (2.3.4) - Manipulação de arrays e dados numéricos

## 🎓 Contexto Educacional

Este projeto foi criado para:
- Facilitar o aprendizado de computação gráfica 3D
- Demonstrar a conversão entre diferentes formatos 3D
- Tornar o desenvolvimento de projetos VRML mais acessível
- Auxiliar estudantes a cumprir requisitos de projetos acadêmicos

## 📝 Como Criar um Arquivo .schem

1. Baixe o [WorldEdit](https://www.curseforge.com/minecraft/mc-mods/worldedit) para Minecraft
2. Construa sua estrutura no Minecraft
3. Selecione a área com `//wand`
4. Copie com `//copy`
5. Salve com `//schem save nome_do_arquivo`
6. O arquivo será salvo em `.minecraft/config/worldedit/schematics/`

## 📄 Licença

Este projeto é de código aberto e está disponível para uso educacional e pessoal.

## 👨‍💻 Autor

Desenvolvido por @rod-roda para ajudar colegas do curso técnico em informática.

## 🔮 Melhorias Futuras

### Em Desenvolvimento Ativo
- [ ] **Geometria customizada para cercas** (cilindros finos)
- [ ] **Geometria customizada para muralhas** (cilindros médios)
- [ ] **Suporte a lajes** (slabs com metade da altura)

### Planejado
- [ ] Suporte a texturas
- [ ] Otimização de geometria (faces ocultas)
- [ ] Suporte a outros formatos de exportação (OBJ, STL)
- [ ] API REST para conversão online

