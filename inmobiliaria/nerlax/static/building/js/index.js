function list_building(){
    $.ajax({
       url: "/nerlax/list_building/",
       type: "get",
       dataType: "json",
       success: function(response){
            $('#building_table tbody').html("")
            for (let i = 0; i < response.length; i++){
                let row = '<tr>';
                row += '<td>' + response[i]['fields']['name'] + '</td>';
                row += '<td>' + response[i]['fields']['address'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;">' + response[i]['fields']['amenities'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;">' + response[i]['fields']['unit_qty'] + '</td>';
                row += '<td><a href="/nerlax/update/'+response[i]['pk']+'"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2 align-middle"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg></a>';
                row += '<a href="#" onclick="open_modal_building(\'/nerlax/delete/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash align-middle"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></a></td>';
                row += '</tr>';
                $('#building_table tbody').append(row);
            }
            $('#building_table').DataTable();
       },
       error: function(error){
            console.log(error);
       }
    });
}

function update_building(){
//    activate_button();
    $.ajax({
        data: $('#edit_building_form').serialize(),
        url: $('#edit_building_form').attr('action'),
        type: $('#edit_building_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_building();
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function delete_building(pk){
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#delete_building_form').attr('action'),
        type: $('#delete_building_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_building();
            $('#buildingModalDelete').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function open_modal_building(url){
    $('#buildingModalDelete').load(url, function(){
        $(this).modal('show');
   });
}

function addSupplier_form(url){
    $('#addSupplier').load(url, function(){
        $(this).modal('show');
    });
}

$(document).ready(function(){
    list_building();
});

//Unit
var $ = jQuery.noConflict()
function list_unit(){
    $.ajax({
       url: "/nerlax/list_unit/",
       type: "get",
       dataType: "json",
       success: function(response){
            $('#unit_table tbody').html("")
            for (let i = 0; i < response.length; i++){
                let row = '<tr>';
                row += '<td>' + response[i]['fields']['name'] + '</td>';
                row += '<td>' + response[i]['fields']['building_id'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;">' + response[i]['fields']['meter_qty'] + '</td>';
                row += '<td>' + response[i]['fields']['renter'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;">' + response[i]['fields']['init_date'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;">' + response[i]['fields']['expiration_date'] + '</td>';
                row += '<td><a href="/nerlax/update_unit/'+response[i]['pk']+'"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2 align-middle"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg></a>';
                row += '<a href="#" onclick="deleteUnitForm(\'/nerlax/delete_unit/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash align-middle"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></a></td>';
                row += '</tr>';
                $('#unit_table tbody').append(row);
            }
            $('#unit_table').DataTable();
       },
       error: function(error){
            console.log(error);
       }
    });
}

function edit_unit(){
    $.ajax({
        data: $('#edit_unit_form').serialize(),
        url: $('#edit_unit_form').attr('action'),
        type: $('#edit_unit_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_unit();
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function delete_unit(pk){
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#delete_unit_form').attr('action'),
        type: $('#delete_unit_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_unit();
            $('#unitModalDelete').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function deleteUnitForm(url){
    $('#unitModalDelete').load(url, function(){
        $(this).modal('show');
    });
}

$(document).ready(function(){
    list_unit();
});

//common expenses
function list_common_expenses(){
    $.ajax({
       url: "/nerlax/list_ce/",
       type: "get",
       dataType: "json",
       success: function(response){
            $('#common_expenses_table tbody').html("")
            for (let i = 0; i < response.length; i++){
                let row = '<tr>';
                row += '<td>' + response[i]['fields']['building'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;">' + response[i]['fields']['payment_date'] + '</td>';
                row += '<td style="text-align: center; vertical-align: middle;">' + response[i]['fields']['total_amount'] + '</td>';
                row += '<td><a href="/nerlax/update_ce/'+response[i]['pk']+'"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2 align-middle"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg></a>';
                row += '<a href="#" onclick="open_modal_form(\'/nerlax/delete_ce/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash align-middle"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></a></td>';
                row += '</tr>';
                $('#common_expenses_table tbody').append(row);
            }
            $('#common_expenses_table').DataTable({
                "aLengthMenu": [[6, 12, 18, 24, -1], [6, 12, 18, 24, "All"]],
                "idDisplayLength": 6
            });
       },
       error: function(error){
            console.log(error);
       }
    });
}

$(document).ready(function(){
    list_common_expenses();
});

function update_ce(){
    $.ajax({
        data: $('#edit_ce_form').serialize(),
        url: $('#edit_ce_form').attr('action'),
        type: $('#edit_ce_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_common_expenses();
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function delete_common_expenses(pk){
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#delete_ce_form').attr('action'),
        type: $('#delete_ce_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_unit();
            $('#commonExpensesModalDelete').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function open_modal_form(url){
    $('#commonExpensesModalDelete').load(url, function(){
        $(this).modal('show');
    });
}

//common expenses lines
function list_common_expenses_lines(){
    $.ajax({
       url: "/nerlax/list_ce_lines/",
       type: "get",
       dataType: "json",
       success: function(response){
            if ($.fn.DataTable.isDataTable('#ce_lines_table')){
                ($('#ce_lines_table').DataTable().destroy());
            }
            $('#ce_lines_table tbody').html("")
            for (let i = 0; i < response.length; i++){
                let row = '<tr>';
                row += '<td>' + response[i]['fields']['concept'] + '</td>';
                row += '<td style="text-align: center">' + response[i]['fields']['amount'] + '</td>';
                row += '<td><a href="#" onclick="editExpensesLinesForm(\'/nerlax/update_ce_lines/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-edit-2 align-middle"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg></a>';
                row += '<a href="#" onclick="deleteExpensesLinesForm(\'/nerlax/delete_ce_lines/'+response[i]['pk']+'\');"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-trash align-middle"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg></a></td>';
                row += '</tr>';
                $('#ce_lines_table tbody').append(row);
            }
            $('#ce_lines_table').DataTable({
                dom: 'Brtip',
                buttons:
                {
                    name: 'primary',
                    buttons: []
                }
            });
       },
       error: function(error){
            console.log(error);
       }
    });
}

$(document).ready(function(){
    list_common_expenses_lines();
});

function addExpensesLinesForm(url){
    $('#expensesLinesModal').load(url, function(){
        $(this).modal('show');
    });
}

function editExpensesLinesForm(url){
    $('#expensesLinesModalEdit').load(url, function(){
        $(this).modal('show');
    });
}

function deleteExpensesLinesForm(url){
    $('#expensesLinesModalDelete').load(url, function(){
        $(this).modal('show');
    });
}

function add_ce_Lines(){
//    activate_button();
    $.ajax({
        data: $('#form_create_data').serialize(),
        url: $('#form_create_data').attr('action'),
        type: $('#form_create_data').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_common_expenses_lines();
            $('#expensesLinesModal').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function edit_ce_Lines(){
//    activate_button();
    $.ajax({
        data: $('#form_edit_data').serialize(),
        url: $('#form_edit_data').attr('action'),
        type: $('#form_edit_data').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_common_expenses_lines();
            $('#expensesLinesModalEdit').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}

function delete_ce_lines(pk){
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: $('#delete_ce_lines_form').attr('action'),
        type: $('#delete_ce_lines_form').attr('method'),
        success: function(response){
            notificationSuccess(response.msj);
            list_unit();
            $('#expensesLinesModalDelete').modal('hide');
        },
        error: function(error){
            notificationError(error.responseJSON.msj);
        }
    });
}