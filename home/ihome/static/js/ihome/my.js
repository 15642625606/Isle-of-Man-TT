
function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

function logout() {
    $.ajax({
        url:'/api/v1.0/session',
        type:'delete',
        headers: {
            "X-CSRFToken": getCookie("csrf_token")
        },
        dataType: "json",
        success:function (resp) {
            if ("0"==resp.errno){
                location.href='/index.html';
            }
        }
    })
}

$(document).ready(function(){
    $.get('/api/v1.0/user',function (res) {
        if ("4101"==res.errno){
            location.href='/login.html';
        }
        else if ("0"==res.errno){
            $("#user-name").html(res.data.name);
            $("#user-mobile").html(res.data.mobile);
            if (res.data.avatar){
                $("#user-avatar").attr("src",res.data.avatar);

            }
        }
    },"json");

})