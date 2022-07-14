#!/bin/bash

# Script para buscar y contar cadenas dentro de los ficheros de un directorio
# Sergio Alías, 20211009

### Asignación de argumentos ###

DIR=$1 #/home/salias/Desktop/tarea
STR=$2 #"@gmail.com @uam.es @upm.es @uc3m.es" 
OUTFILE=$3 #mail.txt


### Control de argumentos ###

# Deben introducirse tres argumentos
if [ ! $# -eq  3 ]; then
  echo "Incorrect number of command line arguments (3 arguments are mandatory)"
  exit
fi

# El primer argumento debe ser un directorio existente
if [ ! -d $DIR ]; then
    echo "The first argument must be an existing directory"
    exit
fi

# Si el fichero de salida ya existe, se borra y se crea uno nuevo (decisión de diseño)
if [ -e $OUTFILE ]; then
	echo "Deleting old '$OUTFILE' file..."
	rm $OUTFILE
fi
echo "Creating '$OUTFILE' file..."
touch $OUTFILE


### Programa principal ###

FILES=$( find $DIR -type f ) # Guardo el path de los ficheros que cuelgan del directorio

for file in $FILES; do # Itero por cada uno de los ficheros
    str_matches=0 # Variable para ir contando las coincidencias con las cadenas (cuento todas las cadenas en el mismo contador porque no se me ha especificado lo contrario)
    for string in $STR; do # Itero por cada una de las cadenas
        let str_matches+=$( cat $file | grep $string -o | wc -l ) # Añado el número de veces que aparece la cadena a la variable que hace de contador
    done
    if [ $str_matches -gt 0 ]; then # "Si el fichero tiene cadenas"
    	echo -e "$( basename $file )\t$( dirname $file )\t$str_matches" >> $OUTFILE # Añádelo al fichero de salida en el formato especificado por el ejercicio
    fi
done

echo "$( cat $OUTFILE | sort -g -r -k 3 )" > $OUTFILE # Ordeno las filas por número de ocurrencias (de mayor a menor)

echo "Script executed successfully"