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
var info = "id1=" + id;
        var xhr = new XMLHttpRequest()
        xhr.open("POST", "/index.py", false);
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded", false);
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                alert("aaaa");
                createsell = xhr.responseText;
            }
        };
        xhr.send(info)
*/
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
 

}

