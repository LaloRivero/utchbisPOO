from datetime import datetime

text = "La idea de ir a Talpa salió de mi hermano Tanilo. A él se le ocurrió primero que a nadie. Desde hacía años que estaba pidiendo que lo llevaran. Desde hacía años. Desde aquel día en que amaneció con unas ampollas moradas repartidas en los brazos y las piernas. Cuando después las ampollas se le convirtieron en llagas por donde no salía nada de sangre y sí una cosa amarilla como goma de copal que destilaba agua espesa. Desde entonces me acuerdo muy bien que nos dijo cuánto miedo sentía de no tener ya remedio. Para eso quería ir a ver a la Virgen de Talpa; para que Ella con su mirada le curara sus llagas. Aunque sabía que Talpa estaba lejos y que tendríamos que caminar mucho debajo del sol de los días y del frío de las noches de marzo, así y todo quería ir. La Virgencita le daría el remedio para aliviarse de aquellas cosas que nunca se secaban. Ella sabía hacer eso: lavar las cosas, ponerlo todo nuevo de nueva cuenta como un campo recién llovido. Ya allí, frente a Ella, se acabarían sus males; nada le dolería ni le volvería a doler más. Eso pensaba él."
vowels_to_replace = ['e','é','E','i','í','I','o','ó','O','u','ú','U']


def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Time elapsed {time_elapsed.total_seconds()}s')
    return wrapper

@execution_time
def run():
    global text
    for vowel in vowels_to_replace:
        text = text.replace(vowel, 'a')
    print(text)


if __name__ == "__main__":
    run()