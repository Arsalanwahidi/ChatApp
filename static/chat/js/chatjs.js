
//Ajax implamention post and get request

$(document).ready(function () {
    var counter = 1;
    var idGroup = $('#groupName').text();
    var d = new Date();
    $(document).on('submit', '#form_data', function (e) {
        e.preventDefault();
        
        if($('#id_messages').val() != ""){
            $.ajax({
                type: 'POST',
                url: `/postdata/${idGroup}`,
                data: {
                    user: $('#userName').text(),
                    messages: $('#id_messages').val(),
                    date: `${d.getUTCHours()}`,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                },
                success: function (response) {
                    $('#id_messages').val('');
                },
                error: function (err) {
                    console.log(err)
                },
            });
        };

        // setTimeout(() => {
        //     $.ajax({
        //         type: 'GET',
        //         url: `/getdata/${counter}`,
        //         success: function (response) {
        //             for(let key in response.messages){
        //                 counter++;
        //                 $('#getData').append("" + response.messages[key].messages + '<br>');
        //             }
        //         },
        //         error: function (err) {
        //             console.log(err);
        //         },
        //     });
        // }, 1400);
    });

    setInterval(() => {
        $.ajax({
            type: 'GET',
            url: `/getdata/${counter}`,
            success: function (response) {
                for(let key in response.messages){
                     counter++;
                     $('#getData').append(
                         "<div style='width: 350px;' class='container text-center p-2 bg-primary rounded '>" + 
                        response.messages[key].messages + "  " + response.messages[key].date +
                     ` <span style="background-color: aqua;font-size: 9px;">` + response.messages[key].user + `</span>` + '</div><hr/>');
                 }
            },
            error: function (err) {
                console.log(err);
            },
        });
    }, 2200);

});