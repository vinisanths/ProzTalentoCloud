// const logo = document.getElementById("logo")
 
// console.log(logo)
 
const autores = document.getElementsByClassName("post-autor")
 
// console.log(autores[0].innerText)
 
// const post02 = document.getElementById("post02")
// console.log(post02.innerText)
 
const dataPost = document.getElementsByTagName("section");
// console.log(dataPost[0])
 
const formulario = document.getElementById("formulario")
// console.log(formulario.innerText)
 
const listaRedes = document.getElementsByClassName("lista_redes")
// console.log(listaRedes)
 
 
const post02 = document.querySelector("#post02 h3")
// console.log(post02)
 
const datas = document.querySelectorAll(".post-data")
// console.log(datas)
 
const linkPost1 = document.querySelector("#post01 a")
// console.log(linkPost1)
 
const linkPost2 = document.querySelector("#post02 strong")
// console.log(linkPost2)
 
const autoresPost = document.querySelectorAll(".post .post-autor")
// console.log(autoresPost)
 
const datasPost = document.querySelectorAll(".post .post-data")
// console.log(datasPost)
 
const titulos = document.querySelectorAll("footer .lista_redes a" )
// console.log(titulos)
 
function imprimiTexto(lista) {
    for ( let i =0; i < lista.length; i++) {
        console.log(lista[i].innerText)
    }
 
}
 
imprimiTexto(titulos)