const alphabetic_order = (arr) => {
    sorted = arr.sort()
    for (i = 0; i < sorted.length; i++) {
        console.log(sorted[i])
    }
}

alphabetic_order(['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot',
    'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive'])