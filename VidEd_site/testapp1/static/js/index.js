function showMenu() {
    menu = document.getElementById("menu")
    menu.classList.toggle("activeMenu")
    menuBut = document.getElementById("menuBut")
    menuBut.classList.toggle("acivateBut")
    hat = document.getElementById("hat")
    hat.classList.toggle("hatBlack")
}
function goVidEd() {
    window.location.href="/VidEd/"
}
function goProg() {
    window.location.href="/Prog/"
}
function goDesign() {
    window.location.href="/Design/"
}