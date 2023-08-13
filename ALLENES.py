from ALL_LOCUS_DATA import *
from ALL_COMBOS import *
from GENERATE_DNA import generate_chromosome

# EACH LOCI CAN PRODUCE PROTEIN FOR DIFFERENT TRAITS
# EACH ALLENE CAN PRODUCE DIFFERENT PROTEINS
# EACH PROTEIN CAN HAVE DIFFERENT EFFECTS ON DIFFERENT TRAITS
# EACH TRAIT CAN HAVE DIFFERENT EFFECTS ON DIFFERENT ATTRIBUTES
# EACH ATTRIBUTE CAN HAVE DIFFERENT EFFECTS ON DIFFERENT SKILLS
# EACH SKILL CAN HAVE DIFFERENT EFFECTS ON DIFFERENT ABILITIES
# EACH ABILITY CAN HAVE DIFFERENT EFFECTS ON DIFFERENT ACTIONS
# EACH ACTION CAN HAVE DIFFERENT EFFECTS ON DIFFERENT OUTCOMES
# EACH OUTCOME CAN HAVE DIFFERENT EFFECTS ON DIFFERENT EVENTS
# EACH EVENT CAN HAVE DIFFERENT EFFECTS ON DIFFERENT STORIES
# EACH STORY CAN HAVE DIFFERENT EFFECTS ON DIFFERENT WORLDS


def calculate_chance_of_combo(loci, combo):
    probabilities = []
    for locus, gene in zip(loci, combo):
        probability = 1 / len(locus)
        probabilities.append(probability)

    total_probability = 1
    for p in probabilities:
        total_probability *= p

    print(f"Chance: {round(total_probability, 5)}")
    return total_probability

#loci = [LOCI_1, LOCI_5, LOCI_6]

def calculate_combo_multiplier(genes, gene_combos):
    genes = tuple(genes)
    return gene_combos.get(genes, 1)
    
def calculate_attribute(genes, loci):
    ATTRIBUTE = 0
    MAX_ATTRIBUTE = sum(len(l) for l in loci)

    for i in range(len(genes)):
        gene = genes[i]
        for locus in loci:
            if gene in locus:
                ATTRIBUTE += locus.index(gene)

    #print(f"Attribute: {ATTRIBUTE} / {MAX_ATTRIBUTE}")
    return ATTRIBUTE / MAX_ATTRIBUTE # A value between 0 and 1, where 0 is the shortest and 1 is the tallest, and 0.5 is average

def calculate_final_attribute(chromosome, locus_indices, combos, base, gene_range, multiplier_limit):
    genes = [chromosome[i-1] for i in gene_range]
    
    loci = [globals()[f'LOCI_{i}'] for i in locus_indices]
    
    initial_value = calculate_attribute(genes, loci)
    multiplier = calculate_combo_multiplier(genes, combos)
    final_value = initial_value * multiplier
    if multiplier == multiplier_limit:
        final_value = multiplier_limit
    attribute = base + (final_value * 60)
    return attribute

def translate_eye_color(value):
    if value < 15:
        return "hazel"
    elif value < 35 and value >= 15:
        return "brown"
    elif value < 40 and value >= 35:
        return "green"
    else:
        return "blue"

def translate_hair_color(value):
    if value < 15:
        return "black"
    elif value < 35 and value >= 15:
        return "brown"
    elif value < 40 and value >= 35:
        return "blonde"
    else:
        return "ginger"

def translate_hair_type(value):
    if value < 15:
        return "straight"
    elif value < 35 and value >= 15:
        return "wavy"
    elif value < 40 and value >= 35:
        return "curly"
    else:
        return "kinky"

def get_all_attributes(CHROMOSOME = generate_chromosome()):
    torso_length_params = {
        'chromosome': CHROMOSOME,
        'locus_indices': TORSO_LOCUS,
        'combos': TORSO_GENE_COMBOS,
        'base': 60,
        'gene_range': [TORSO_LOCUS[0], TORSO_LOCUS[1], TORSO_LOCUS[2]],
        'multiplier_limit': 2,
    }
    arm_length_params = {
        'chromosome': CHROMOSOME,
        'locus_indices': ARM_LENGTH_LOCUS,
        'combos': ARM_LENGTH_GENE_COMBOS,
        'base': 150,
        'gene_range': [ARM_LENGTH_LOCUS[0], ARM_LENGTH_LOCUS[1]],
        'multiplier_limit': 2,
    }
    leg_length_params = {
        'chromosome': CHROMOSOME,
        'locus_indices': LEG_LENGTH_LOCUS,
        'combos': LEG_LENGTH_GENE_COMBOS,
        'base': 60,
        'gene_range': [LEG_LENGTH_LOCUS[0], LEG_LENGTH_LOCUS[1]],
        'multiplier_limit': 2,
    }
    eye_color_params = {
        'chromosome': CHROMOSOME,
        'locus_indices': EYE_COLOR_LOCUS,
        'combos': EYE_COLOR_GENE_COMBOS,
        'base': 0,
        'gene_range': [EYE_COLOR_LOCUS[0], EYE_COLOR_LOCUS[1], EYE_COLOR_LOCUS[2]],
        'multiplier_limit': 2,
    }
    vision_params = {
        'chromosome': CHROMOSOME,
        'locus_indices': EYE_SIGHT_LOCUS,
        'combos': VISION_GENE_COMBOS,
        'base': 0,
        'gene_range': [EYE_SIGHT_LOCUS[0], EYE_SIGHT_LOCUS[1]],
        'multiplier_limit': 2,
    }
    hair_color_params = {
        'chromosome': CHROMOSOME,
        'locus_indices': HAIR_COLOR_LOCUS,
        'combos': HAIR_COLOR_GENE_COMBOS,
        'base': 0,
        'gene_range': [HAIR_COLOR_LOCUS[0], HAIR_COLOR_LOCUS[1]],
        'multiplier_limit': 2,
    }
    hair_type_params = {
        'chromosome': CHROMOSOME,
        'locus_indices': HAIR_TYPE_LOCUS,
        'combos': HAIR_TYPE_GENE_COMBOS,
        'base': 0,
        'gene_range': [HAIR_TYPE_LOCUS[0], HAIR_TYPE_LOCUS[1]],
        'multiplier_limit': 2,
    }
    hearing_params = {
        'chromosome': CHROMOSOME,
        'locus_indices': HEARING_LOCUS,
        'combos': HEARING_GENE_COMBOS,
        'base': 0,
        'gene_range': [HEARING_LOCUS[0], HEARING_LOCUS[1]],
        'multiplier_limit': 2,
    }
    pain_tolerance_params = {
        'chromosome': CHROMOSOME,
        'locus_indices': PAIN_TOLERANCE_LOCUS,
        'combos': PAIN_TOLERANCE_GENE_COMBOS,
        'base': 0,
        'gene_range': [PAIN_TOLERANCE_LOCUS[0], PAIN_TOLERANCE_LOCUS[1]],
        'multiplier_limit': 2,
    }
    musclulature_params = {
        'chromosome': CHROMOSOME,
        'locus_indices': MUSCLULATURE_LOCUS,
        'combos': MUSCLULATURE_GENE_COMBOS,
        'base': 0,
        'gene_range': [MUSCLULATURE_LOCUS[0], MUSCLULATURE_LOCUS[1]],
        'multiplier_limit': 2,
    }
    metabolis_params = {
        'chromosome': CHROMOSOME,
        'locus_indices': METABOLISM_LOCUS,
        'combos': METABOLISM_GENE_COMBOS,
        'base': 0,
        'gene_range': [METABOLISM_LOCUS[0], METABOLISM_LOCUS[1]],
        'multiplier_limit': 2,
    }
    flexibility_params = {
        'chromosome': CHROMOSOME,
        'locus_indices': FLEXIBILITY_LOCUS,
        'combos': FLEXIBILITY_GENE_COMBOS,
        'base': 0,
        'gene_range': [FLEXIBILITY_LOCUS[0], FLEXIBILITY_LOCUS[1]],
        'multiplier_limit': 2,
    }
    brain_type_params = {
        'chromosome': CHROMOSOME,
        'locus_indices': BRAIN_TYPE_LOCUS,
        'combos': BRAIN_TYPE_GENE_COMBOS,
        'base': 0,
        'gene_range': [BRAIN_TYPE_LOCUS[0], BRAIN_TYPE_LOCUS[1]],
        'multiplier_limit': 2,
    }
    blood_type_params = {
        'chromosome': CHROMOSOME,
        'locus_indices': BLOOD_TYPE_LOCUS,
        'combos': BLOOD_TYPE_GENE_COMBOS,
        'base': 0,
        'gene_range': [BLOOD_TYPE_LOCUS[0], BLOOD_TYPE_LOCUS[1]],
        'multiplier_limit': 2,
    }
    lung_capacity_params = {
        'chromosome': CHROMOSOME,
        'locus_indices': LUNG_CAPACITY_LOCUS,
        'combos': LUNG_CAPACITY_GENE_COMBOS,
        'base': 0,
        'gene_range': [LUNG_CAPACITY_LOCUS[0], LUNG_CAPACITY_LOCUS[1]],
        'multiplier_limit': 2,
    }
    regeneration_params = {
        'chromosome': CHROMOSOME,
        'locus_indices': REGENERATION_LOCUS,
        'combos': REGENERATION_GENE_COMBOS,
        'base': 0,
        'gene_range': [REGENERATION_LOCUS[0], REGENERATION_LOCUS[1]],
        'multiplier_limit': 2,
    }
    torso_length = calculate_final_attribute(**torso_length_params)
    leg_length = calculate_final_attribute(**leg_length_params)
    arm_length = calculate_final_attribute(**arm_length_params)
    height = torso_length + leg_length

    eye_color_value = calculate_final_attribute(**eye_color_params)
    vision_value = calculate_final_attribute(**vision_params)

    hair_color_value = calculate_final_attribute(**hair_color_params)
    hair_type_value = calculate_final_attribute(**hair_type_params)

    hearing_value = calculate_final_attribute(**hearing_params)

    pain_tolerance_value = calculate_final_attribute(**pain_tolerance_params)

    musculature_value = calculate_final_attribute(**musclulature_params)

    metabolism_value = calculate_final_attribute(**metabolis_params)

    flexibility_value = calculate_final_attribute(**flexibility_params)

    brain_type_value = calculate_final_attribute(**brain_type_params)

    blood_type_value = calculate_final_attribute(**blood_type_params)

    lung_capacity_value = calculate_final_attribute(**lung_capacity_params)

    regeneration_value = calculate_final_attribute(**regeneration_params)
    return {
        'height':round(height),
        'torso_length': round(torso_length),
        'arm_length': round(arm_length),
        'leg_length': round(leg_length),
        'eye_color_value': translate_eye_color(eye_color_value),
        'vision_value': vision_value,
        'hair_color_value': translate_hair_color(hair_color_value),
        'hair_type_value':translate_hair_type(hair_type_value),
        'hearing_value': hearing_value,
        'pain_tolerance_value': pain_tolerance_value,
        'musculature_value': round(musculature_value),
        'metabolism_value': metabolism_value,
        'flexibility_value': flexibility_value,
        'brain_type_value': round(brain_type_value),
        'blood_type_value': blood_type_value,
        'lung_capacity_value': lung_capacity_value,
        'regeneration_value': regeneration_value,
    }

'''
print(f"Height: {round(height)}cm")
print(f"Arm Length: {round(arm_length)}cm")
print(f"Eye Color: {translate_eye_color(eye_color_value)}")
print(f"Hair Color: {translate_hair_color(hair_color_value)}")
print(f"Hair Type: {translate_hair_type(hair_type_value)}")
print(f"Hearing: {round(hearing_value)}%")
print(f"Vision: {round(vision_value)}%")
print(f"Pain Tolerance: {round(pain_tolerance_value)}%")
print(f"Musclulature type: {round(musclulature_value)}")
print(f"Metabolism: {round(metabolism_value)}")
print(f"Flexibility: {round(flexibility_value)}")
print(f"Brain Type: {round(brain_type_value)}")
print(f"Blood Type: {round(blood_type_value)}")
print(f"Lung Capacity: {round(lung_capacity_value)}")
print(f"Regeneration: {round(regeneration_value)}")
'''
