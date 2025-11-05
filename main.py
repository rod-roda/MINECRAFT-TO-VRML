import nbtlib
import os

nbt = nbtlib.load("arquivo_teste.schem")
schematic = nbt["Schematic"]

width = schematic["Width"]
height = schematic["Height"]
length = schematic["Length"]

print(f"Largura: {width}, Altura: {height}, Comprimento: {length}")

palette = schematic["Blocks"]["Palette"]
block_data = schematic["Blocks"]["Data"]

print("Blocos no palette:", palette)
print("Tamanho dos dados:", len(block_data))
