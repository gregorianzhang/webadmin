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
	

	alert(ip+cmd);
//	alert($('input:checked').val());
	
}
