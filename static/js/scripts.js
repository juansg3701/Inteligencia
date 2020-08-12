$(document).on('click', '#hit', function(event) {
    $.ajax({
        url: "./index.py",
        success: function(data) {
            $(data).find('a').attr('href', function(i, val) {
                if (val.match(/\.(jpe?g|png|gif)$/)) {
                    counter += 1;
                    $('#catalogue').append(component + counter + '" src="' + val + '"></div>');
                }
            });
        },
    });
});


function botones(id){

    alert(id);

/*
   console.log("click");
    $.ajax({
        method: 'POST',
        url: '/datos/numero',
        data: {
            'id1': id 
        },
        dataType: "json",
        success: function(response) {
            alert("siiiiii");
        }
    }); 
    */
    /*
    data=id;
        $.post( "/postmethod", {
            javascript_data: data,
             success: function(response) {
            console.log("holi :3");
        }
        });
*/

var xhr= new XMLHttpRequest();   
    xhr.open("GET" ,"/postmethod?holi="+id);
    xhr.onreadystatechange= function(){
        if(xhr.readyState===4)
        {
           var response = xhr.responseText;
           console.log(response+"holi");
          
        }
    };
    xhr.send(null);

}
