function changeColor() {
    let hue = Math.floor(Math.random() * 360);
    let color = "hsl(" + String(parseInt(hue)) + ",33%,20%)"
    document.getElementById("_body").style.backgroundColor = color;
    let elements = document.getElementsByClassName("_a");
    for (let i = 0; i < elements.length; i++) {
        elements[i].style.color = color;
    }
}