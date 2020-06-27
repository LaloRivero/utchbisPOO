def main():
    cadena = "La idea de ir a Talpa salió de mi hermano Tanilo. A él se le ocurrió primero que a nadie. Desde hacía años que estaba pidiendo que lo llevaran. Desde hacía años. Desde aquel día en que amaneció con unas ampollas moradas repartidas en los brazos y las piernas. Cuando después las ampollas se le convirtieron en llagas por donde no salía nada de sangre y sí una cosa amarilla como goma de copal que destilaba agua espesa. Desde entonces me acuerdo muy bien que nos dijo cuánto miedo sentía de no tener ya remedio. Para eso quería ir a ver a la Virgen de Talpa; para que Ella con su mirada le curara sus llagas. Aunque sabía que Talpa estaba lejos y que tendríamos que caminar mucho debajo del sol de los días y del frío de las noches de marzo, así y todo quería ir. La Virgencita le daría el remedio para aliviarse de aquellas cosas que nunca se secaban. Ella sabía hacer eso: lavar las cosas, ponerlo todo nuevo de nueva cuenta como un campo recién llovido. Ya allí, frente a Ella, se acabarían sus males; nada le dolería ni le volvería a doler más. Eso pensaba él."
    mod_cadena = []
    for letter in cadena:
        if letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            mod_cadena.append('a')
        elif letter == 'é' or letter == 'í' or letter == 'ó' or letter == 'ú':
            mod_cadena.append('a')
        elif letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
            mod_cadena.append('A')
        else:
            mod_cadena.append(letter)

    mod_cadena = ''.join(mod_cadena)

    print(mod_cadena)


if __name__ == "__main__":
    main()
