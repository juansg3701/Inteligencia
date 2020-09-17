function botones(id) {
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
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/postmethod?holi=" + id);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            var response = xhr.responseText;
            console.log(response);
        }
    };
    xhr.send(null);
}