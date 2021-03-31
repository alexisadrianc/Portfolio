function list_user(){
    $.ajax({
        url: "/list_user/",
        type: "get",
        dataType: "json",
        success: function(response){
            $('#table_users tbody').html("")
            for (let i = 0; i < response.length; i++){
                let row = '<tr>';
                row += '<td>' + response[i]['fields']['first_name'] + '</td>';
                row += '<td>' + response[i]['fields']['last_name'] + '</td>';
                row += '<td>' + response[i]['fields']['username'] + '</td>';
                row += '<td>' + response[i]['fields']['email'] + '</td>';
                row += '<td>' + response[i]['fields']['user_type'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;"><a href="/edit/'+response[i]['pk']+'"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2 align-middle"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg></a> ';
                row += '<a href="#" onclick="deleteUsersForm(\'/delete/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash align-middle"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></a></td>';
                row += '</tr>';
                $('#table_users tbody').append(row);
            }
            $('#table_users').DataTable();
        },
        error:function(error){
            console.log(error);
        }
    });
}

$(document).ready(function(){
    list_user();
});

function create_users(){
//    activate_button();
    $.ajax({
        data: $('#create_user_form').serialize(),
        url: $('#create_user_form').attr('action'),
        type: $('#create_user_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_user();
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function update_users(){
//    activate_button();
    $.ajax({
        data: $('#edit_user_form').serialize(),
        url: $('#edit_user_form').attr('action'),
        type: $('#edit_user_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_user();
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function delete_users(pk){
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#delete_users_form').attr('action'),
        type: $('#delete_users_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_user();
            $('#usersModalDelete').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function deleteUsersForm(url){
    $('#usersModalDelete').load(url, function(){
        $(this).modal('show');
    });
}