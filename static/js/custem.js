
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
function command(){
//        alert("aaaaaaa");
//        var obj=document.getElementById("output");
//        obj.innerHTML ="eee";
//	document.write("abcd\n eeee");
//	$('input:checked').each(function(){alert($(this).val())});
	var ip = new Array();
	var cmd = new Array();
	$('input[type=checkbox]:checked').each(function(){
		ip.push($(this).val());
	});
	$('input[type=radio]:checked').each(function(){
		cmd.push($(this).val());
	});
	var aa = JSON.stringify(ip);
	var bb = JSON.stringify(cmd);
$.post("/do/",{ip:aa,cmd:bb},function(data){alert(data);});

//	alert(ip+cmd);
//	alert($('input:checked').val());

	
}
