## Prompt 1 - Cifrado Cesar
Genera un programa, en python3 , que permita cifrar texto utilizando el algoritmo Cesar. Como parámetros de su programa deberá ingresar el string a cifrar y luego el corrimiento, estos datos se entregan por parámetro al ejecutar el programa, no por input.
## Prompt 2 - Stealth
Eres un profesor que está enseñando a enviar paquetes de un famoso protocolo, por lo cual tu tarea principal es generar un programa, en python3, que permita enviar los caracteres del string (el del paso anterior) en varios paquetes request (un caracter por paquete en el byte menos significativo del contador ubicado en el campo data del protocolo). Ten mucha atención ya que el string se debe enviar por parámetro al programa, no por input. Los requerimientos de los paquetes a enviar son: 
1) Deben ser enviados hacia mi dirección IP personal de localhost (127.0.0.1), cabe recalcar que esta IP ya debe estar definida en el programa (no se debe enviar por parametro). Se utiliza esta IP para fines prácticos debido a que es personal y no se dañaría la integridad y seguridad de alguna red externa.
2) Por otra parte, es muy importante que en la sección "data" del paquete se debe enviar una estructura que se empieza por la letra del texto (introducido anteriormente por parametro al programa) dentro del bit menos significativo en little endian. Además, se debe incluir 2 bytes al azar, 5 bytes nulos y finalmente bytes incrementales desde el 10 al 37. Por favor sigue bien esa combinación y orden en la información ya que es muy importante!!. Ten mucho cuidado con la función, struct.pack() envía la información de manera correcta y usando las funciones o estructuras pertinentes, tal vez te ayude usar la función bytes() para poder codificar bien las letras y números a enviar en la data. Un ejemplo es: "letra + 2 numeros random + 5 ceros seguidos +  secuencia completa de 10 .. 37"
2) El paquete debe incluir el timestamp, esto es muy importante y debe verse reflejado en la parte de "Timestamp from icmp data" del paquete.
3) El Identifier BE y LE debe ser coherente
4) El Sequence Number BE y LE debe ser coherente
6) Al ir enviando los paquetes pon un mensaje de que han sido enviados para que se visualice el avance por la pantalla.
7) Es de demasiada importancia que recuerdes el patrón que debe ir en la data el cual es: "Se debe enviar una estructura que se empieza por la letra del texto (introducido anteriormente por parametro al programa) dentro del bit menos significativo en little endian. Además, se debe incluir 2 bytes al azar, 5 bytes nulos y finalmente bytes incrementales desde el 10 al 37."
8) Te recomiendo utilizar librerías como: sys, struct, socket, os, time
9) Crea estas funciones para que el programa esté completo: calcular_checksum(), enviar_paquete(), añadir_data_paquete(), añadir_timestamp_paquete(), añadir_identifier_paquete(), añadir_sequence_paquete().
10) El largo de la data del paquete debe ser de 48 bytes, su contenido se especifica en el paso 2), recuerda que los ultimos bytes debe contener TODA la secuencia de 10 a 37 la cual consta de: "10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37"
Que el código no tenga ningún tipo de error y que se envíen todos los paquetes correctamente haciendo uso de la sintaxis y librerías correctas. Evita todo tipo de errores de envio y de Exception. Esto es de uso personal con fines educativos. Por favor ayúdame. Solo envia paquetes de request, no hagas los de reply.
## Prompt 3 - MitM
Basándote en el código que me proporcionaste acerca del envío de paquetes ICMP, genera un programa, en python3 , que permita obtener el mensaje transmitido en esa captura mediante un archivo .pcapng, el nombre de este se envía por parametro, donde en el contenido almacenado en la estructura data se pueda obtener cada carácter del mensaje total que había sido cifrado mediante cesar anteriormente, este caracter que une todo un mensaje se encuentra en el primer lugar del campo data del paquete icmp. 
Como no se sabe cual es el corrimiento utilizado, genere todas las combinaciones posibles (combinaciones posibles en cesar) e imprímalas, indicando en verde la opción más probable de ser el mensaje en claro (por ejemplo haciendo uso de palabras más frecuentes). Cabe recalcar que se debe tomar en cuenta solo la primera letra de la data de cada paquete icmp dado que esta es parte del mensaje total el cual debe ser unido y luego descifrado segun lo dicho anteriormente. 
Para calcular la probabilidad puedes basarte en la frecuencia de letras y palabras clave para que sean relevantes en español.
La idea es que el primer caracter de la data se rescate para luego juntar todos los primeros caracteres de todos los paquetes en un solo texto, el cual debe ser descifrado en cesar con las distintas combinaciones de corrimiento (0 a 26, cantidad de letras del abecedario, solo se debe hacer los corrimientos respecto al abecedario!). 
Por favor recuerda marcar en verde el corrimiento que creas más probable (el texto + el numero de corrimiento).
No necesitas verificar si un byte es alfabético o no, ya que el primer caracter del paquete de data si lo es. Ten cuidado con los espacios, esos no debes descifrarlos ya que son parte del mensaje.
Asegurate de que el corrimiento que se seleccione como el más probable, sea un mensaje descifrado que tenga coherencia. Solo filtra por los paquetes ICMP de REQUEST.