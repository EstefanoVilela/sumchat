
from nltk.chat.util import Chat, reflections

mis_reflexiones = {
    "ir": "fui",
    "hola": "hey",
    "fut": "formato unico de matricula",
    "conseguir": "obtener"
}

pares = [
    [
        r"hola|hey|buenas",
        ["Hola", "Qué tal", "Hola que tal!",]
    ],
    [
        r"mi nombre es (.*)",
        ["Hola %1, como estás ?",]
    ],
    [
        r"(.*) tu nombre ?",
        ["Mi nombre es Botcito",]
    ],
    [
        r"(.*)como estas ?",
        ["Bien, y tú?",]
    ],
    [
        r"que (.*) quieres ?",
        ["Nada, gracias",]
    ],
    [
        r"disculpa (.*)",
        ["No pasa nada",]
    ],
    [
        r"(.*)cuando (.*) creado ?",
        ["Fui creado hoy",]
    ],
    [
        r"(.*)ue es (.*) reactualizacion de matricula(.*)",
        ["Es un proceso que habilita al estudiante a volver a retomar sus estudios academicos, convalidando cursos con la malla actual",]
    ],
    [
        r"(.*) codigo de pago (.*) reactualizacion de matricula?",
        ["En el banco de comercio el código es : 10312",]
    ],
    [
        r"(.*) asunto (.*) correo (.*) reactualizacion ?",
        ["El asunto es : REACTUALIZACION DE MATRICULA - *ESCUELA* - *CODIGO* ",]
    ],
    [
        r"(.*) boleta de notas (.*) enviar (.*)",
        ["La boleta de notas debe de ser del último ciclo del que asistió.",]
    ],
    [
        r"(.*) tiempo (.*) respuesta (.*)",
        ["Verifica el cronograma para saber la fecha en el cual te entregarán una respuesta",]
    ],
    [
        r"(.*) conseguir (.*) fut?",
        ["Puedes obtenerlo dando <a target='_blank' href='http://tramite.unfv.edu.pe/Solicitud_Tramite/'>click aquí</a>",]
    ],
    [
        r"(.*) termina (.*) reactualzacion de matricula(.*)",
        ["Se le notificará via correo, se le activará su proceso de matricula la cual deberá de seguir",]
    ],
    [
        r"(.*) proceso (.*) reactualizacion de matricula ?",
        ["1. Realizar los pagos respectivos <br>2. Preparar y llenar los documentos necesarios: solicitud de justificacion (FUT), copia del voucher, constancia de ingreso y boleta de notas <br>3. Enviar el correo de la universidad Kguizado@unfv.edu.pe <br>4. Esperar una respuesta de parte de la universidad. <br>5. Se te enviará una notificacion a tu correo institucional con la confirmación. Recuerda que debes de cumplir con los siguientes requisitos: promedio ponderado mayor a 9, no haber reprobado un mismo curso 3 veces.",]
    ],
    [
        r"(.*) actualizado (.*) malla(.*)",
        ["Según el árticulo 32 del reglamento académico, los alumnos reingresantes se matriculan de acuerdo al plan curricular vigente, previa equivalencia. La facultad determina el nivel de estudios al que se incorporan. Todo alumno reingresante debe cumplir con el plan curricular vigente al tiempo de su ingreso.",]
    ],
    [
        r"(.*) mostrar(.*) los bancos del comercio cercanos?",
        ["Puedes ubicar el Banco del Comercio más cercano a tu domicilio haciendo <a target='_blank' href='https://www.google.com/maps/search/banco+del+comercio/@-12.0822173,-77.0780708,12z'>click aquí</a>",]
    ],
    [
        r"Cual es el (.) maximo para (.) la reactualizacion de matricula?",
        ["El plazo máximo para que puedas reanudar tus estudios es de 6 años",]
    ],
    [
        r"En que momento debo (.*) la reactualizacion de matricula?",
        ["Debes hacerlo antes de que termine el año académico y antes del proceso de matrpicula del siguiente año.",]
    ],
    [
        r"chao|adios|finalizar",
        ["Fue bueno hablar contigo.",]
    ],
]


chat = Chat(pares, mis_reflexiones)