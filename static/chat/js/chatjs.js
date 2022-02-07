
//Ajax implamention post and get request
$(document).ready(function () {

    groupData = $('id_group').val();
    $(document).on('submit', '#form_data', function (e) {
        e.preventDefault();

        $.ajax({
            type: 'POST',
            url: '/postdata',
            data: {
                group: $('#id_group').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (response) {
                alert(`${groupData} group is created`);
                $('#id_group').val('');
            },
            error: function (err) {
                console.log(err)
            },
        });
    });

    $('#btnGet').click(function () {
        $.ajax({
            type: 'GET',
            url: '/getdata',
            success: function (response) {
                document.getElementById('getData').innerHTML = `We get the data: \'${response.data}\'`;
            },
            error: function (err) {
                console.log(err)
            },
        });
    });

    // setInterval(() => {

    // }, 2000);

})