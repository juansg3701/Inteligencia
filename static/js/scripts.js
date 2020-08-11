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