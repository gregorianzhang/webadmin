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



    function command(){
        alert(ip);
        var obj=document.getElementById("output");
        obj.innerHTML ="eee";
        //document.write("tttttttttttttttttttttt\neeeeee");
//alert('sss');
    }
