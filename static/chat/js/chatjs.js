
//Ajax implamention post and get request

$(document).ready(function () {
    var counter = 1;
    var idGroup = $('#groupName').text();
    $(document).on('submit', '#form_data', function (e) {
        e.preventDefault();
        
        if($('#id_messages').val() != ""){
            $.ajax({
                type: 'POST',
                url: `/postdata/${idGroup}`,
                data: {
                    messages: $('#id_messages').val(),
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                },
                success: function (response) {
                    $('#id_group').val('');
                },
                error: function (err) {
                    console.log(err)
                },
            });
        }
      
        setTimeout(() => {
            $.ajax({
                type: 'GET',
                url: `/getdata/${counter}`,
                success: function (response) {
                    counter++;
                    $('#getData').append("" + response.messages + '<br>');
                },
                error: function (err) {
                    console.log(err);
                },
            });
        }, 1400);
    });

    // setInterval(() => {
    //     $.ajax({
    //         type: 'GET',
    //         url: `/getdata/${counter}`,
    //         success: function (response) {
    //             counter++;
    //             $('#getData').append("" + response.messages + '<br>');
    //         },
    //         error: function (err) {
    //             console.log(err);
    //         },
    //     });
    // }, 4500);

});