$(document).ready(function() {
    let i = 0
    $("#btnClick").click(function(e){
        e.preventDefault();
        i++;
        $('.inputs').append(`<p class=pinp${i}><label for="inp${i}">Obj${i}</label><input id="inp${i}" name="inp${i}" type="text"></p>`);
    });
    $("#btnClick2").click(function(e){
        e.preventDefault();
        if (i > 0){
            $(`.pinp${i}`).remove();
            i--;
        }
    });
});