# Need tensorflow 2.10 and h5py version 2.1, I had issues getting the versions right for textgenrnn
from textgenrnn import textgenrnn
import csv

with open('Spells.csv') as csvfile:
    spells = []
    spellsreader = csv.reader(csvfile, delimiter=';')
    next(spellsreader, None)
    for row in spellsreader:
        if not (row[1] == 'Unknown' or row[1] == ''):
            spell = "%s: %s" % (row[1],row[3])
            print(spell)
            spells.append(spell)

with open("spells.txt", "w") as output:
    output.write('\n'.join(spells))


spellgen = textgenrnn()
spellgen.train_from_file('spells.txt', num_epochs=2)

generated_spells = spellgen.generate(1000, temperature=0.35, return_as_list=True)


print(generated_spells)

with open('generatedSpells.txt', 'w') as f:
    for item in generated_spells:
        f.write("%s\n" % item)
