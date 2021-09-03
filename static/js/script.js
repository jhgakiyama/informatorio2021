function correcto(a, c) {
    document.getElementById(a).style.backgroundColor = "#d1e7dd";
    // document.getElementById(c).disabled = true;
    let nodes = document.getElementById(c).getElementsByTagName('*');
    for(var i = 0; i < nodes.length; i++){
        nodes[i].disabled = true;
    }
}
function incorrecto(b, c) {
    document.getElementById(b).style.backgroundColor = "#f8d7da";
    // document.getElementById(c).disabled = true;
    var nodes = document.getElementById(c).getElementsByTagName('*');
    for(var i = 0; i < nodes.length; i++){
        nodes[i].disabled = true;
    }
}
