function getCookies() {
    var arr = document.cookie.split(/; /);
    var cookies = new Map();
    arr.forEach(function(item){
       var cook = item.split('=');
       cookies.set(cook[0], cook[1]);
    });
    return cookies;
}

var csrftoken = getCookies().get('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if(!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function validRegistration(){
    var form = $('#menu_auth')[0];
    var inputs = form.querySelectorAll('.form-control');
    var error_block = form.querySelector('.error-message');
    var i = 0;
    var regHash = {
        lastName: /[A-Z][a-z]{2,30}/,
        firstName: /[A-Z][a-z]{2,30}/,
        login: /\w{4,20}/,
        password: /\w{4,20}/,
        phoneNumber: /\d{6,15}/
    };
    var mesHash = {
        lastName: 'wrong surname',
        firstName: 'wrong name',
        login: 'wrong login',
        password: 'wrong password',
        phoneNumber: 'wrong phoneNumber'
    };
    var error = false;
    var error_message = '';
    for (i; i < inputs.length; i++){
        if (!regHash[inputs[i].name].test(inputs[i].value)){
            error = true;
            error_message += mesHash[inputs[i].name];
            error_message += '<br>';
        }
    }
    if (error){
        error_block.innerHTML = error_message;
    }
    return !error;
}

$(document).ready( function() {
    var a = true;
    var registration = false;
    var login = false;
    if(a) {
        $(".fading").fadeIn(1000);
        a = false;
    }
    $("#content").bind('click', function(){
        $('.pop-up').fadeOut();
        registration = false;
        login = false;
    });

    $('.pop-up').bind('click', function(e){
        e.stopPropagation();
    });
    $("#main_img").cycle();
    $("#register_fade").click(function () {
        if(login == false) {
            if(registration == false) {
               $("#registration_window").fadeIn();
                registration = true;
            }
            else {
                $("#registration_window").fadeOut();
                registration = false;
            }

        }
    });
    $("#register_submit").click(function(e){
        if(!validRegistration()){
            e.preventDefault();
        }
    });
    $("#sign-in-fade").click(function() {
        if(registration == false) {
            if(login == false) {
                $("#sign-in-window").fadeIn();
                login = true;
            }
            else {
                $("#sign-in-window").fadeOut();
                login = false;
            }
        }
    });
    $('#log-in-button').bind('click', function(e) {
        var form = $('#sign-in-window form')[0];
        var login = form.querySelector('input[name=login]').value;
        var password = form.querySelector('input[name=password]').value;
        var data = { login: login, password: password };
        $.ajax({
          method: "POST",
          url: "http://127.0.0.1:8000/signin/",
          data: data
        })
        .done(function(data) {
            console.log(data);
            if(data.logged) {
                $('#sign-in-error-block').html('');
                $('#sign-in-window').fadeOut();
                window.location.reload();
            } else {
                $('#sign-in-error-block').html('Wrong login or password');
            }
        });
        e.preventDefault();
    });
});