import nbtlib

#APLICAR PARA ACEITAR CERCAS E MURALHAS E SLABS
# def geometry_for_block(block_name):
#     # Detecta cercas e muralhas
#     if "fence" in block_name:
#         return "Cylinder { height 1 radius 0.15 }"
#     elif "wall" in block_name:
#         return "Cylinder { height 1 radius 0.3 }"
#     else:
#         return "Box { size 1 1 1 }"

def color_for_block(block_name):
    colors = {
        # --- CONCRETE ---
        "minecraft:white_concrete": (0.83, 0.83, 0.83),
        "minecraft:orange_concrete": (0.85, 0.43, 0.05),
        "minecraft:magenta_concrete": (0.70, 0.22, 0.73),
        "minecraft:light_blue_concrete": (0.36, 0.55, 0.95),
        "minecraft:yellow_concrete": (0.90, 0.85, 0.10),
        "minecraft:lime_concrete": (0.35, 0.75, 0.10),
        "minecraft:pink_concrete": (0.95, 0.50, 0.65),
        "minecraft:gray_concrete": (0.25, 0.25, 0.25),
        "minecraft:light_gray_concrete": (0.60, 0.60, 0.60),
        "minecraft:cyan_concrete": (0.20, 0.50, 0.60),
        "minecraft:purple_concrete": (0.45, 0.20, 0.65),
        "minecraft:blue_concrete": (0.15, 0.25, 0.70),
        "minecraft:brown_concrete": (0.35, 0.20, 0.05),
        "minecraft:green_concrete": (0.15, 0.30, 0.15),
        "minecraft:red_concrete": (0.60, 0.10, 0.10),
        "minecraft:black_concrete": (0.05, 0.05, 0.05),

        # --- WOOL ---
        "minecraft:white_wool": (0.95, 0.95, 0.95),
        "minecraft:orange_wool": (0.95, 0.55, 0.15),
        "minecraft:magenta_wool": (0.85, 0.35, 0.85),
        "minecraft:light_blue_wool": (0.55, 0.65, 0.95),
        "minecraft:yellow_wool": (0.95, 0.90, 0.25),
        "minecraft:lime_wool": (0.55, 0.85, 0.25),
        "minecraft:pink_wool": (0.95, 0.60, 0.75),
        "minecraft:gray_wool": (0.35, 0.35, 0.35),
        "minecraft:light_gray_wool": (0.75, 0.75, 0.75),
        "minecraft:cyan_wool": (0.25, 0.55, 0.60),
        "minecraft:purple_wool": (0.55, 0.25, 0.75),
        "minecraft:blue_wool": (0.25, 0.35, 0.80),
        "minecraft:brown_wool": (0.45, 0.30, 0.10),
        "minecraft:green_wool": (0.25, 0.45, 0.15),
        "minecraft:red_wool": (0.75, 0.15, 0.15),
        "minecraft:black_wool": (0.05, 0.05, 0.05),

        # --- TERRACOTTA ---
        "minecraft:white_terracotta": (0.85, 0.76, 0.67),
        "minecraft:orange_terracotta": (0.77, 0.39, 0.15),
        "minecraft:magenta_terracotta": (0.70, 0.32, 0.60),
        "minecraft:light_blue_terracotta": (0.45, 0.47, 0.70),
        "minecraft:yellow_terracotta": (0.80, 0.62, 0.16),
        "minecraft:lime_terracotta": (0.55, 0.70, 0.22),
        "minecraft:pink_terracotta": (0.85, 0.52, 0.60),
        "minecraft:gray_terracotta": (0.25, 0.20, 0.17),
        "minecraft:light_gray_terracotta": (0.60, 0.55, 0.50),
        "minecraft:cyan_terracotta": (0.32, 0.40, 0.42),
        "minecraft:purple_terracotta": (0.47, 0.30, 0.50),
        "minecraft:blue_terracotta": (0.35, 0.35, 0.55),
        "minecraft:brown_terracotta": (0.40, 0.25, 0.15),
        "minecraft:green_terracotta": (0.30, 0.35, 0.15),
        "minecraft:red_terracotta": (0.65, 0.25, 0.20),
        "minecraft:black_terracotta": (0.20, 0.10, 0.10),

        # --- MATERIAIS BASE ---
        "minecraft:stone": (0.55, 0.55, 0.55),
        "minecraft:grass_block": (0.35, 0.60, 0.25),
        "minecraft:dirt": (0.50, 0.35, 0.20),
        "minecraft:sand": (0.95, 0.90, 0.60),
        "minecraft:gravel": (0.60, 0.60, 0.60),
        "minecraft:oak_planks": (0.75, 0.60, 0.35),
        "minecraft:glass": (0.75, 0.90, 0.95),

        # --- CERCAS (fences) ---
        "minecraft:oak_fence":           (0.75, 0.60, 0.35),
        "minecraft:spruce_fence":        (0.55, 0.40, 0.20),
        "minecraft:birch_fence":         (0.82, 0.75, 0.50),
        "minecraft:jungle_fence":        (0.65, 0.50, 0.35),
        "minecraft:acacia_fence":        (0.85, 0.50, 0.30),
        "minecraft:dark_oak_fence":      (0.40, 0.30, 0.20),
        "minecraft:mangrove_fence":      (0.60, 0.45, 0.30),
        "minecraft:crimson_fence":       (0.60, 0.10, 0.10),
        "minecraft:warped_fence":        (0.25, 0.60, 0.60),

        # --- MURALHAS (walls) ---
        "minecraft:cobblestone_wall":        (0.50, 0.50, 0.50),
        "minecraft:mossy_cobblestone_wall":  (0.45, 0.60, 0.45),
        "minecraft:stone_brick_wall":        (0.60, 0.60, 0.60),
        "minecraft:mossy_stone_brick_wall":  (0.55, 0.65, 0.55),
        "minecraft:granite_wall":            (0.65, 0.45, 0.35),
        "minecraft:diorite_wall":            (0.75, 0.75, 0.75),
        "minecraft:andesite_wall":           (0.70, 0.70, 0.70),
        "minecraft:brick_wall":              (0.65, 0.25, 0.20),
        "minecraft:sandstone_wall":          (0.90, 0.80, 0.60),
        "minecraft:red_sandstone_wall":      (0.80, 0.40, 0.30),
        "minecraft:prismarine_wall":         (0.35, 0.65, 0.60),
        "minecraft:nether_brick_wall":       (0.40, 0.10, 0.10),
        "minecraft:red_nether_brick_wall":   (0.55, 0.15, 0.15),
        "minecraft:blackstone_wall":         (0.15, 0.15, 0.20),
        "minecraft:polished_blackstone_wall":(0.20, 0.20, 0.25),
        "minecraft:end_stone_brick_wall":    (0.85, 0.80, 0.60),
    }

    # retorna cor correspondente ou branco se não encontrar
    return colors.get(block_name, (1.0, 1.0, 1.0))


nbt = nbtlib.load("escavadeira_enzo.schem")
schematic = nbt["Schematic"]

width = schematic["Width"]
height = schematic["Height"]
length = schematic["Length"]

print(f"Largura: {width}, Altura: {height}, Comprimento: {length}")

palette = schematic["Blocks"]["Palette"]
block_data = schematic["Blocks"]["Data"]

print("Blocos no palette:", palette)
print("Tamanho dos dados:", len(block_data))

palette_inverse = {v: k for k, v in palette.items()}

blocks = []

for y in range(height):
    for z in range(length):
        for x in range(width):
            index = y * width * length + z * width + x
            block_id = block_data[index]
            block_name = palette_inverse.get(block_id, "minecraft:air")
            if block_name != "minecraft:air":  # ignora blocos de ar
                blocks.append((x, y, z, block_name))

print(f"Total de blocos sólidos: {len(blocks)}")
print("Primeiros blocos:", blocks[:5])

output_path = "saida.wrl"

# ---  Posição da Câmera ---
center_x = width / 2
center_y = height / 2
center_z = length / 2
camera_distance = max(width, height, length) * 1.2

with open(output_path, "w") as f:
    f.write("#VRML V2.0 utf8\n\n")

    f.write(f"""
Viewpoint {{
  position {center_x} {center_y + height * 0.3} {center_z + camera_distance}
  orientation 0 1 0 0
  description "Vista centralizada"
}}

# Luz ambiente e direcional
DirectionalLight {{
  direction -0.3 -1 -0.3
  intensity 1.0
}}
PointLight {{
  location {center_x} {center_y + height} {center_z}
  intensity 0.9
}}
""")

    f.write("Group {\n  children [\n")

    for x, y, z, block in blocks:
        r, g, b = color_for_block(block)
        f.write(f"""
    Transform {{
      translation {x} {y} {z}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{
              diffuseColor {r} {g} {b}
              ambientIntensity 0.5
              shininess 0.2
            }}
          }}
          geometry Box {{ size 1 1 1 }}
        }}
      ]
    }}
""")

    f.write("  ]\n}\n")

print(f"Arquivo VRML criado com sucesso: {output_path}")