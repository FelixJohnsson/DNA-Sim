from itertools import product
import random
from CODON_VALUES import CODON_VALUES
from ALL_LOCUS_DATA import LOCUS_GENE_VALUES

def check_gene_value(gene):
    gene_value = 0
    for i in range(0, len(gene), 3):
        codon = gene[i:i+3]
        if codon in CODON_VALUES:
            gene_value += CODON_VALUES[codon]

    return gene_value

def generate_combinations_dict():
    combinations_dict = {}
    codons = list(CODON_VALUES.keys())
    for combination in product(codons, repeat=3):
        total_value = round(sum(CODON_VALUES[codon] for codon in combination), 4)
        if total_value not in combinations_dict:
            combinations_dict[total_value] = []
        combinations_dict[total_value].append(''.join(combination))
    return combinations_dict

def generate_chromosome(length = len(LOCUS_GENE_VALUES)):
    CHROMOSOME = []
    combinations_dict = generate_combinations_dict()
    for i in range(length):
        ALLENES = combinations_dict[LOCUS_GENE_VALUES[i]]
        CHROMOSOME.append(random.choice(ALLENES))
    return CHROMOSOME
