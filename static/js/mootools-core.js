$(document).ready(function(){
    ip="";
    $("li.ip").click(function(){
        if ($(this).css("color") == "rgb(0, 0, 0)")
        {
            //alert($(this).css("color"));
            $(this).css("color","red")
            ip=$(this).text()
        }
        else 
        {
            //alert($(this).css("color"));
            $(this).css("color","black");
            ip="";
        }
        alert(ip);
    });

    cmd="";
    $("li.cmd").click(function(){
        if ($(this).css("color") == "rgb(0, 0, 0)")
        {
            //alert($(this).css("color"));
            $(this).css("color","red")
            cmd=$(this).text()
        }
        else
        {
            //alert($(this).css("color"));
            $(this).css("color","black");
            cmd="";
        }
        alert(cmd);
    });




});

function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


var csrftoken = getCookie('csrftoken');
function command1(){
alert("eeee");
var ee="";
$.post("/ipcmd/",
        {ip:ip, cmd:cmd, aaa:"992837373hj"}, 
        function(data){
    alert("Data loaded: " + data);   
    ee=data;
});
alert("abc");
//var ee="hello";
var obj=document.getElementById("output");
obj.innerHTML =ee;

}

    function command(){
        alert(ip);
        var obj=document.getElementById("output");
        obj.innerHTML ="eee";
        //document.write("tttttttttttttttttttttt\neeeeee");
//alert('sss');
    }
