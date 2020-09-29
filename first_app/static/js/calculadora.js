

function dis(val) {
    document.getElementById("result").value += val;
}
function solve() { 
    let x = document.getElementById("result").value 
    let y = eval(x);
    document.getElementById("result").value = y; 
}

function clr() { 
    document.getElementById("result").value = "";
}

function convert(){
    let x = document.getElementById("result").value 
    let y = eval(x);
    if(Math.sign(y) > 0){
        counter = Math.abs(y) * -1;
    }else{
        counter = Math.abs(y);
    }
    document.getElementById("result").value = counter; 
}