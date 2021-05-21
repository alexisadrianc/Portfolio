
function list_academy(){
    $.ajax({
       url: "/web/list_academy/",
       type: "get",
       dataType: "json",
       success: function(response){
            $('#academy_table tbody').html("")
            for (let i = 0; i < response.length; i++){
                let row = '<tr>';
                row += '<td>' + response[i]['fields']['company'] + '</td>';
                row += '<td>' + response[i]['fields']['address'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;">' + response[i]['fields']['phone'] + '</td>';
                row += '<td>' + response[i]['fields']['email'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;"><a href="/web/edit_academy/'+response[i]['pk']+'"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2 align-middle"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg></a>';
                row += '<a href="#" onclick="openModalAcademy(\'/web/delete_academy/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash align-middle"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></a></td>';
                row += '</tr>';
                $('#academy_table tbody').append(row);
            }
            $('#academy_table').DataTable({
                responsive: true
            });
       },
       error: function(error){
            console.log(error);
       }
    });
}

$(document).ready(function(){
    list_academy();
});


function openModalAcademy(url){
    $('#academyModalDelete').load(url, function(){
        $(this).modal('show');
   });
}

function update_academy(){
//    activate_button();
    $.ajax({
        data: $('#form-edit-academy').serialize(),
        url: $('#form-edit-academy').attr('action'),
        type: $('#form-edit-academy').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_academy();
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function delete_academy(pk){
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#delete_academy_form').attr('action'),
        type: $('#delete_academy_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_academy();
            $('#academyModalDelete').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function list_lesson(){
    $.ajax({
       url: "/web/list_lesson/",
       type: "get",
       dataType: "json",
       success: function(response){
            $('#lesson_table tbody').html("")
            for (let i = 0; i < response.length; i++){
                let row = '<tr>';
                row += '<td>' + response[i]['fields']['name'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;">' + response[i]['fields']['quantity_lesson'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;">' + response[i]['fields']['price'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;">' + response[i]['fields']['state'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;"><a href="/web/edit_lesson/'+response[i]['pk']+'"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2 align-middle"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg></a>';
                row += '<a href="#" onclick="openModalLesson(\'/web/delete_lesson/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash align-middle"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></a></td>';
                row += '</tr>';
                $('#lesson_table tbody').append(row);
            }
            $('#lesson_table').DataTable({
                responsive: true
            });
       },
       error: function(error){
            console.log(error);
       }
    });
}

$(document).ready(function(){
    list_lesson();
});

function update_lesson(){
//    activate_button();
    $.ajax({
        data: $('#form-edit-lesson').serialize(),
        url: $('#form-edit-lesson').attr('action'),
        type: $('#form-edit-lesson').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_lesson();
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function openModalLesson(url){
    $('#lessonModalDelete').load(url, function(){
        $(this).modal('show');
   });
}

function delete_lesson(pk){
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#delete_lesson_form').attr('action'),
        type: $('#delete_lesson_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_lesson();
            $('#lessonModalDelete').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

