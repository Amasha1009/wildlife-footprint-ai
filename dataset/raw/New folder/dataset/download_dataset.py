import os
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

SPECIES_CLASSES = ['leopard', 'deer', 'elephant', 'wild_boar', 'bear', 'wolf']

def create_synthetic_footprint(species_name, width=224, height=224, seed=None):
    """
    Generates a realistic synthetic footprint image on soil/sand background
    for demonstration and pipeline validation.
    """
    if seed is not None:
        np.random.seed(seed)
        
    # Generate ground background texture (sand/dirt gradient with noise)
    bg_color = np.random.randint(140, 190, size=(height, width, 3), dtype=np.uint8)
    noise = np.random.randint(-20, 20, size=(height, width, 3), dtype=np.int16)
    bg = np.clip(bg_color.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    
    img = Image.fromarray(bg).convert('RGBA')
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    cx, cy = width // 2, height // 2
    footprint_color = (60, 45, 30, 220)  # Dark indented mud tone
    
    if species_name == 'elephant':
        # Large rounded/oval pad with minor toe notches
        rx, ry = 65, 75
        draw.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=footprint_color)
        # Toe indentations around top arc
        for angle in range(-60, 70, 30):
            rad = math.radians(angle)
            tx = cx + int((rx + 5) * math.sin(rad))
            ty = cy - int((ry + 5) * math.cos(rad))
            draw.ellipse([tx - 12, ty - 12, tx + 12, ty + 12], fill=footprint_color)
            
    elif species_name == 'deer':
        # Two pointed hoof cleaves
        draw.polygon([(cx - 28, cy + 50), (cx - 5, cy - 55), (cx - 35, cy - 35)], fill=footprint_color)
        draw.polygon([(cx + 28, cy + 50), (cx + 5, cy - 55), (cx + 35, cy - 35)], fill=footprint_color)
        
    elif species_name == 'wild_boar':
        # Two main hoof cleaves + two dew claws behind
        draw.polygon([(cx - 25, cy + 30), (cx - 4, cy - 45), (cx - 32, cy - 25)], fill=footprint_color)
        draw.polygon([(cx + 25, cy + 30), (cx + 4, cy - 45), (cx + 32, cy - 25)], fill=footprint_color)
        # Dew claws
        draw.ellipse([cx - 38, cy + 38, cx - 22, cy + 62], fill=footprint_color)
        draw.ellipse([cx + 22, cy + 38, cx + 38, cy + 62], fill=footprint_color)
        
    elif species_name == 'leopard':
        # Main rounded tri-lobed pad + 4 teardrop toe pads without claws
        draw.ellipse([cx - 38, cy - 10, cx + 38, cy + 45], fill=footprint_color)
        toe_angles = [-50, -20, 20, 50]
        for angle in toe_angles:
            rad = math.radians(angle)
            tx = cx + int(52 * math.sin(rad))
            ty = cy - int(45 * math.cos(rad))
            draw.ellipse([tx - 13, ty - 16, tx + 13, ty + 16], fill=footprint_color)
            
    elif species_name == 'bear':
        # Broad wide palm pad + 5 clawed toe prints
        draw.ellipse([cx - 50, cy - 5, cx + 50, cy + 50], fill=footprint_color)
        for i in range(5):
            angle = -60 + i * 30
            rad = math.radians(angle)
            tx = cx + int(58 * math.sin(rad))
            ty = cy - int(38 * math.cos(rad))
            draw.ellipse([tx - 11, ty - 13, tx + 11, ty + 13], fill=footprint_color)
            # Claw tips
            cx_tip = cx + int(74 * math.sin(rad))
            cy_tip = cy - int(52 * math.cos(rad))
            draw.line([(tx, ty), (cx_tip, cy_tip)], fill=footprint_color, width=4)
            
    elif species_name == 'wolf':
        # Main triangular pad + 4 oval toe prints with claw marks
        draw.polygon([(cx - 30, cy + 35), (cx, cy - 10), (cx + 30, cy + 35)], fill=footprint_color)
        toe_angles = [-45, -15, 15, 45]
        for angle in toe_angles:
            rad = math.radians(angle)
            tx = cx + int(46 * math.sin(rad))
            ty = cy - int(35 * math.cos(rad))
            draw.ellipse([tx - 12, ty - 15, tx + 12, ty + 15], fill=footprint_color)
            # Claw marks
            cx_tip = cx + int(60 * math.sin(rad))
            cy_tip = cy - int(48 * math.cos(rad))
            draw.line([(tx, ty), (cx_tip, cy_tip)], fill=footprint_color, width=3)
            
    # Apply subtle Gaussian blur to imitate natural soil displacement
    overlay = overlay.filter(ImageFilter.GaussianBlur(radius=2))
    img.paste(overlay, (0, 0), overlay)
    return img.convert('RGB')

def prepare_dataset(base_dir='dataset', num_samples_per_class=30):
    """
    Generates structured train/val dataset directories.
    """
    data_dir = os.path.join(base_dir, 'data')
    print(f"Preparing dataset in {data_dir}...")
    
    for species in SPECIES_CLASSES:
        species_dir = os.path.join(data_dir, species)
        os.makedirs(species_dir, exist_ok=True)
        
        for i in range(num_samples_per_class):
            img_filename = f"{species}_{i+1:03d}.jpg"
            img_path = os.path.join(species_dir, img_filename)
            
            # Seed based on species and index for reproducible diverse images
            seed_val = hash(f"{species}_{i}") % 100000
            img = create_synthetic_footprint(species, seed=seed_val)
            img.save(img_path, quality=92)
            
        print(f"  [OK] Created {num_samples_per_class} footprint images for '{species}'")
        
    print("\nDataset generation completed successfully!")
    print(f"Total species: {len(SPECIES_CLASSES)}")
    print(f"Total samples: {len(SPECIES_CLASSES) * num_samples_per_class}")

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    dataset_dir = os.path.join(project_root, 'dataset')
    prepare_dataset(dataset_dir)
