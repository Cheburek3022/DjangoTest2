function sendData(){
     $("#update_post").click(function (){
        $.ajax("/ajax/", {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                 'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val(),
                 'name': $('#username').val(),
                 'password': $('#password').val(),
            },
            'success': function(data){
               alert(data.status)
            }
        })
     })
}
$(document).ready(function(){
     sendData();
})