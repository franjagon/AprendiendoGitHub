# Modulo 1 - Programa 4
#
#    Instrucciones
#        - contar los caracteres de un texto
#        - contar vocales y consonantes
#        - contar mayúsculas y minúsculas
#
#    Restricciones
#        - usar diccionarios
#
#    Especificaciones
#        - crear cuantas funciones convenga

# Definición de funciones


# Declaración de constantes
_TEXTO = """En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en
astillero, adarga antigua, rocín flaco y galgo corredor. Una olla de algo más vaca que carnero, salpicón las más noches, duelos y quebrantos
los sábados, lantejas los viernes, algún palomino de añadidura los domingos, consumían las tres cuartas partes de su hacienda. El resto della
concluían sayo de velarte, calzas de velludo para las fiestas, con sus pantuflos de lo mesmo, y los días de entresemana se honraba con su
vellorí de lo más fino. Tenía en su casa una ama que pasaba de los cuarenta, y una sobrina que no llegaba a los veinte, y un mozo de campo y
plaza, que así ensillaba el rocín como tomaba la podadera. Frisaba la edad de nuestro hidalgo con los cincuenta años; era de complexión recia,
seco de carnes, enjuto de rostro, gran madrugador y amigo de la caza. Quieren decir que tenía el sobrenombre de Quijada, o Quesada, que en
esto hay alguna diferencia en los autores que deste caso escriben; aunque, por conjeturas verosímiles, se deja entender que se llamaba
Quejana. Pero esto importa poco a nuestro cuento; basta que en la narración dél no se salga un punto de la verdad. Es, pues, de saber que este
sobredicho hidalgo, los ratos que estaba ocioso -que eran los más del año-, se daba a leer libros de caballerías, con tanta afición y gusto
que olvidó casi de todo punto el ejercicio de la caza, y aun la administración de su hacienda; y llegó a tanto su curiosidad y desatino en
esto, que vendió muchas hanegas de tierra de sembradura para comprar libros de caballerías en que leer, y así, llevó a su casa todos cuantos
pudo haber dellos. Y, de todos, ningunos le parecían tan bien como los que compuso el famoso Feliciano de Silva, porque la claridad de su
prosa y aquellas entricadas razones suyas le parecían de perlas; y más cuando llegaba a leer aquellos requiebros y cartas de desafíos, donde
en muchas partes hallaba escrito: La razón de la sinrazón que a mi razón se hace, de tal manera mi razón enflaquece, que con razón me quejo de
la vuestra fermosura. Y también cuando leía: los altos cielos que de vuestra divinidad divinamente con las estrellas os fortifican, y os hacen
merecedora del merecimiento que merece la vuestra grandeza."""
_TEXTO2="""名前を覚えたくないラマンチャの場所では、デラのイダルゴ以来長い時間はありませんでした造船所、古いバックル、細い馬とガルゴの廊下。
羊よりも牛の鍋、サルピコンより多くの夜、決闘と損失 土曜日、金曜日の金曜日、日曜日のパロミノ、農場の4分の3を消費しました。残りの彼らは彼らのドレス、
休日のための毛深いブリーチ、同じものの彼らのスリッパで終えました、そして週の日は彼らの名誉を与えられました 最高級のベロリ。彼は40代の頃の家に愛人、
20歳未満の姪、そして田舎の少年とそれが剪定せん断をしたので馬車を鞍にした広場。フリサバ私たちの紳士の年齢、50年。彼は体格が良かった、乾いた肉、細身の顔、
早い鳥、そして狩りの友達。彼らはそれがチーズのニックネームを持っていたと言いたいのですがこの事件を書いた著者には違いがあります。もっともらしい推測では、
それが呼ばれたと理解されていますがケジャナしかし、これは私たちの話にはほとんど関係ありません。彼のナレーションの中に真実の点が出てこないので十分です。
それで、これを知っているのはイダルゴの上、彼が遊んでいた時代、それは一年の大半でした、彼はとても愛と味で、騎士道の本を読みました彼が狩猟の行使、
さらには彼の農場の運営さえもほとんどすべての点で忘れていたこと。そして彼の好奇心とナンセンスはこれを読んで、
彼は騎士道の本を買うためにたくさんの種まきの土地を売ったので、家に持っていった。それらがあるかもしれません。そして、何よりも、
それらのどれも有名な人が構成したものほど良くなかった散文と彼のそれらの謎めいた理由は真珠のように見えました。
そして彼がそれらの挑戦と挑戦の手紙を読むようになったとき、もっと多くの場所で私は書かれているとわかった：私の理由が作られているという不当な理由の理由、
そのようにして私の理由が弱まっている理由で私は文句を言うあなたの名声そしてまた私が読む時には、「あなたの神性のものは星と神聖に結びついているのです。
あなたの偉大さに値するメリットに値する。"""

_CARACTER = 0
_ASCII = 1
_ACUM = 2

_ASCII_MAY = (65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 192, 193, 194, 195, 196, 197, 199, 200, 201, 202, 203, 204, 205, 206, 207, 209, 210, 211, 212, 213, 214, 216, 217, 218, 219, 220, 221, 376)
_ASCII_MIN = (97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 224, 225, 226, 227, 228, 229, 231, 232, 233, 234, 235, 236, 237, 238, 239, 241, 242, 243, 244, 245, 246, 248, 249, 250, 251, 252, 253, 255)
_ASCII_VOC = (65, 69, 73, 79, 85, 97, 101, 105, 111, 117, 192, 193, 194, 195, 196, 197, 200, 201, 202, 203, 204, 205, 206, 207, 210, 211, 212, 213, 214, 216, 217, 218, 219, 220, 224, 225, 226, 227, 228, 229, 232, 233, 234, 235, 236, 237, 238, 239, 242, 243, 244, 245, 246, 248, 249, 250, 251, 252)
_ASCII_CON = (66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90, 98, 99, 100, 102, 103, 104, 106, 107, 108, 109, 110, 112, 113, 114, 115, 116, 118, 119, 120, 121, 122, 199, 209, 221, 231, 241, 253, 255, 376)

# Procesamiento de Datos

'''Genero un diccionario en vacío para poder cargar en él cada carácter del texto a analizar, como una clave bajo la cual acumular el número
de veces que aparece en el texto.'''

caracteres = {}

'''Itero el texto carácter a carácter y para cada uno pregunto si ya lo he incluido como clave en el diccionario, si es así, summo uno a su
valor asociado y si no, genero su clave como nueva con su valor inicializado a uno.'''

for char in _TEXTO:
    if char in caracteres:
        caracteres[char] += 1        
    else:
        caracteres[char] = 1

'''Para conseguir las equivalencias ascii y sus acumuladores itero la lista de claves del diccionario y para cada una monto un elemento
lista (tripleta) de tres elementos: la clave, su codigo ascii y su acumulador. Este elemento lista lo cargo en otra lista.'''

listaKOA = []

for k in caracteres.keys():
    chars = []
    chars.append(k)
    chars.append(ord(k))
    chars.append(caracteres[k])
    listaKOA.append(chars)

'''Para conseguir el número total de vocales, consonantes, mayúsculas y minúsculas, itero la lista de tripletas y voy añadiendo los
acumuladores a los totales correspondientes si los códigos ascii se correponden con los de las tuplas definidas para cada característica.'''

mayusculas = 0
minusculas = 0
vocales = 0
consonantes = 0

for tripleta in listaKOA:
    if tripleta[_ASCII] in _ASCII_MAY:
        mayusculas += tripleta[_ACUM]
        
    if tripleta[_ASCII] in _ASCII_MIN:
        minusculas += tripleta[_ACUM]
        
    if tripleta[_ASCII] in _ASCII_VOC:
        vocales += tripleta[_ACUM]
        
    if tripleta[_ASCII] in _ASCII_CON:
        consonantes += tripleta[_ACUM]

# Presentación de resultados

'''Presento primero todos los acumuladores. Cada caracter del texto analizado junto a las veces que aparece en él.'''

for char, cant in sorted(caracteres.items()):
    print(char, " --> ", cant)

'''Presento al final los cuatro acumulados de mayúsculas, minúsculas, vocales y consonantes.'''

print("\nMayúsculas:\t\t{}\nMinúsculas:\t\t{}\nVocales:\t\t{}\nConsonantes:\t\t{}".format(mayusculas, minusculas, vocales, consonantes))
