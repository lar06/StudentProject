$(document).ready(function () {

    var headerButton = document.getElementById("main-img_portrait");
    var yourName = document.getElementsByClassName("main-img__name")[0];

    headerButton.onclick = function() {
        var name = prompt("Enter your name:");
        // console.log(name);
        yourName.innerHTML = "welcome, "+name;
    }
})