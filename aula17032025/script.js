//alterar h2
const h2 = document.querySelector('h2');
h2.style.color = 'darkblue';
h2.style.fontSize = '32';
h2.style.fontFamily = 'Arial';

//alterar botões
const buttons = document.querySelectorAll('button');
const button = document.querySelector('button');
button.style.backgroundColor = 'darkblue';
button.style.color = 'white';
button.style.borderRadius = '25px';

//input errado usuario nome
const inputName = document.querySelector("#login-usuario")
inputName.classList.add("error")
const inputNameHelperText = document.querySelector(".error-text")
inputNameHelperText.classList.add("visible")

//input certo usuario e senha errado
inputName.classList.remove("error")
inputName.classList.add("correct")
 
inputNameHelperText.classList.remove("visible")
 
const inputPassword = document.querySelector("#login-senha")
inputPassword.classList.add("error")
 
const inputPasswordHelperText = document.querySelectorAll(".error-text")[1]
inputPasswordHelperText.classList.add("visible")