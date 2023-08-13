from CODON_VALUES import CODON_VALUES, LOWEST_GENE_VALUE, HIGHEST_GENE_VALUE
from ALL_LOCUS_DATA import LOCUS_GENE_VALUES
from itertools import product

def find_gene_values_equal(number):
    codons = list(CODON_VALUES.keys())
    count = 0
    for combination in product(codons, repeat=3):
        total_value = sum(CODON_VALUES[codon] for codon in combination)
        if round(total_value, 4) == number:
            print(''.join(combination))
            count += 1
    print(f"Total number of combinations equal to {number}: {count}")
    print(f"Odds: 1 in {round(262144 / count)}")
    return count

#find_gene_values_equal(0.1179)

def check_gene_value(gene):
    gene_value = 0
    for i in range(0, len(gene), 3):
        codon = gene[i:i+3]
        if codon in CODON_VALUES:
            gene_value += CODON_VALUES[codon]

    print(f"{gene} has value: {round(gene_value, 4)}")

def get_allene_list(gene_value):
    codons = list(CODON_VALUES.keys())
    LIST_OF_ALLENES = []
    for combination in product(codons, repeat=3):
        total_value = sum(CODON_VALUES[codon] for codon in combination)
        if round(total_value, 4) == gene_value:
            LIST_OF_ALLENES.append(''.join(combination))
    return LIST_OF_ALLENES

def find_all_gene_combinations():
    START = int(LOWEST_GENE_VALUE * 1000)
    END = int(HIGHEST_GENE_VALUE * 1000)
    list = []
    for i in range(START, END):
        num = find_gene_values_equal(i / 1000)
        if num > 5 and num < 20:
            print(i / 1000, num)
            list.append(i / 1000)
    
    list.sort()
    print(list)
    
def get_allenes():
    for i in range(300, 400):
        GENE_VALUE = LOCUS_GENE_VALUES[i]
        LIST = get_allene_list(GENE_VALUE)
        print(f"LOCI_{i + 1} = {LIST}")
