# MUBBC
**MUBBC** stands for Máster Universitario en Bioinformática y Biología Computacional, the Spanish way of saying **MSc in Bioinformatics and Computational Biology**.

Here you can find some of the scripts that I had to write in order to complete the assignments of the Master:

- ``API-rest-exercises.ipynb``: Jupyter Notebook for the Master's Programmatic Access to Databases course. Three simple exercises using the [Ensembl Rest API](https://rest.ensembl.org/).
- ``busca.sh``: Script for the Master's basic Linux course. We were asked to create a script that search in the directories from a given directory the files that contain any of the strings wanted. The script will generate a single file that will contain the following information arranged in columns: ``basename_file  path_file ocurrences``. The columns will be separated by tabs and the rows ordered by number of occurrences.
- ``CpG_island_finder.py``: Script for the Master's Sequence Analysis course. We were given some basic functions to read a FASTA file and count nucleotide and dinucleotide frequencies, and we were asked to write an script that looks for CpG islands in a given DNA sequence. Just in case you don't remember what a CpG island is, [here](https://www.sciencedirect.com/topics/neuroscience/cpg-island) you have a reminder.
- ``dna-toolkit.py``: A really simple, object-oriented toolkit for the Master's basic Python course. The main idea was to build a simple DNA Toolkit that allows to create, validate and mutate DNA chains, analyse frequencies, search subsequencies and data persistence. And yes, I'm aware that some—not to say all—of the utilities of the toolkit are biologically useless, but the assignment was not intended to be useful but rather a good Python practice exercise.
- ``dp-algorithms.ipynb``: Jupyter Notebook for the Master's Algorithms course. I implemented some algorithms using Dynamic Programming.
- ``pmdm_assignment2.ipynb``: Jupyter Notebook for the Master's advanced Python course. We were asked to generate a protein translation table from scratch using biological data.
- ``rare-diseases-database.sql``: A simple SQL database of rare diseases for the Master's Relational Databases course. Code includes tables creation, data inserts, some basic queries and a couple of triggers.
- ``regex-exercises.ipynb``: Jupyter Notebook for the Master's Text Mining course. 30 basic regular expression exercises.
- ``systems-biology.ipynb``: Jupyter Notebook for the Master's Systems Biology course. Basically I plot the [Hill equation](https://en.wikipedia.org/wiki/Hill_equation_(biochemistry)) and integrate a system of ordinary differential equations using [SciPy's odeint function](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html).
