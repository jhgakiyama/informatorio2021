function correcto(a, c) {
    document.getElementById(a).style.backgroundColor = "#d1e7dd";
    let nodes = document.getElementById(c).getElementsByTagName('*');
    for(let i = 0; i < nodes.length; i++){
        nodes[i].disabled = true;
    }
}
function incorrecto(b, c) {
    document.getElementById(b).style.backgroundColor = "#f8d7da";
    let nodes = document.getElementById(c).getElementsByTagName('*');
    for(let i = 0; i < nodes.length; i++){
        nodes[i].disabled = true;
    }
}