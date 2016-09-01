$(document).ready(function(){
    $('form').on('submit', function(event) {
//        event.stopPropagation();
        event.preventDefault();

//        var form = $('form');
//        var formdiv =  $('.form');
        $.ajax({
            url: 'http://swapi.co/api/people/',
            method: 'GET',
            dataType: 'json',
            timeout: 3000,
            success: function(response, textStatus){
                    if (response) {
                        console.log(response)
                    }
//                    if (response.is_e) {
//                        var msg = $('<div class="alert alert-danger" role="alert"></div>');
//                        msg.append(response.e);
//
//                        $('.alert.alert-danger').remove();
//                        formdiv.prepend(msg).fadeIn();
//                    } else {
//                        form.remove();
//
//                        var msg = $('<div class="alert alert-success" role="alert"></div>');
//                        msg.append("<p>Dear " + response.username + ".</p>");
//                        msg.append("<p>Search result will be sent on your e-mail address " + response.email + " as soon as search finished.</p>");
//
//                        formdiv.hide().html(msg).fadeIn();
//                    }
                },
            error: function(request, errorType, errorMessage){
//                    form.remove();
//
//                    var msg = $('<div class="alert alert-danger" role="alert"></div>');
//                    msg.append('Error: ' + errorType + '  with message: ' + errorMessage);
//
//                    formdiv.html(msg).fadeIn();
                }
        });
    });
});