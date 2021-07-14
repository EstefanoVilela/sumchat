// OBJECTS
const msger = document.querySelector(".msger");
const msgerForm  = document.querySelector(".msger-inputarea");
const msgerInput = document.querySelector(".msger-input");
const msgerChat  = document.querySelector(".msger-chat");
const btnMinimize = document.querySelector("#btnMinimize");
const btnMaximize = document.querySelector("#btnMaximize");

// SETTINGS
const BOT_IMG = "/static/Content/img/robot.png";
const PERSON_IMG = "https://image.flaticon.com/icons/svg/145/145867.svg";
// const PERSON_IMG = "/static/Content/img/user.jpeg";
const BOT_NAME = "UNFVbot";
const PERSON_NAME = "Tú";

msgerForm.addEventListener("submit", (ev) => {
    ev.preventDefault();

    const msgText = msgerInput.value;
    msgerInput.value = "";

    if (!msgText) return;

    appendMessage(PERSON_NAME, PERSON_IMG, "right", msgText);
    botResponse(msgText);
});

function appendMessage(name, img, side, text) {
    const msgHTML = 
        `<div class="msg ${side}-msg">
            <div class="msg-img" style="background-image: url(${img})"></div>
            <div class="msg-bubble">
                <div class="msg-info">
                    <div class="msg-info-name">${name}</div>
                    <div class="msg-info-time">${formatDate(new Date())}</div>
                </div>
                <div class="msg-text">${text}</div>
            </div>
        </div>`;

    msgerChat.insertAdjacentHTML("beforeend", msgHTML);
    msgerChat.scrollTop += 500;
}

function botResponse(rawText) {
    // Bot Response
    $.get("/get", {
        msg: rawText
    }).done(function (data) {
        console.log(rawText);
        console.log(data);

        if(data == "None"){
            data = "Disculpa, no tengo una respuesta para tu pregunta";
        }

        const msgText = data;
        speak(msgText);
        appendMessage(BOT_NAME, BOT_IMG, "left", msgText);
    });

}

function formatDate(date) {
    const h = "0" + date.getHours();
    const m = "0" + date.getMinutes();

    return `${h.slice(-2)}:${m.slice(-2)}`;
}

btnMinimize.addEventListener("click", () => {
    msger.style.display = "none";
    btnMaximize.style.display = "block";
});

btnMaximize.addEventListener("click", () => {
    msger.style.display = "";
    btnMaximize.style.display = "none";
});



/*========== GRABACIÓN ==========*/
var rec;
var flag = false;

var btnStartRec = document.getElementById('btnStartRec');
var textInput = document.getElementById('textInput');

if(!("webkitSpeechRecognition" in window)){
    alert("Disculpas, no puedes usar la API");
}else{
	console.log("Todo bien!");
    rec = new webkitSpeechRecognition();
    // rec.lang = "es-PE";
	rec.lang = 'es-ES';
    rec.continuous = true;
    rec.interim = true;
	// rec.interimResults = true;

    rec.addEventListener("result", (event) => {
		console.log('\n\n==========\n\nonresult\n----------\n');
		
		let voice = event.results[event.results.length-1][0];
		
		textInput.value = voice.transcript;
		console.log('Transcript: ' + voice.transcript);
		console.log('Confidence: ' + voice.confidence);
	});
    
	rec.addEventListener("error", (event) => {
		console.error("errorGrabacion");
		console.log(event);
		console.log(event.error);
	});
	
	rec.addEventListener("nomatch", (event) => {
		speak('No entendí');
	});
}

btnStartRec.addEventListener('click', () => {
    if(flag == false){
        // no se está grabando, empezaremos a grabar
        rec.start();
        console.log('start');
        flag = true;
    }else{
        // sí se está grabando, pararemos la grabación
        rec.stop();
        console.log('stop');
        flag = false;
    }
});

/*========== VOZ ==========*/
var speech = new SpeechSynthesisUtterance();

function speak(textToAloud){
    speech.text = textToAloud;
    speech.volume = 1;
    speech.rate = 1;
    speech.pitch = 1;

    window.speechSynthesis.speak(speech);
}