// 根据名字获取
function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function() {
    $("#mobile").focus(function(){
        $("#mobile-err").hide();
    });
    $("#password").focus(function(){
        $("#password-err").hide();
    });


    $(".form-login").submit(function(e){
        e.preventDefault(); // 阻止表单默认的提交行为
        mobile = $("#mobile").val();  // 获取值
        passwd = $("#password").val();
        if (!mobile) {
            $("#mobile-err span").html("请填写正确的手机号！");
            $("#mobile-err").show();
            return;
        } 
        if (!passwd) {
            $("#password-err span").html("请填写密码!");
            $("#password-err").show();
            return;
        }

        var data={
            mobile:mobile,
            password:passwd
        }
        var jsonData=JSON.stringify(data)
        $.ajax({
            url:'/api/v1.0/sessions',
            type:'post',
            data:jsonData,
            contentType:"application/json",
            dataType:'json',
            headers:{
                "X-CSRFToken":getCookie("csrf_token")
            },
            success:function (data) {
                if (data.errno=="0"){
                    location.href='/index.html'
                }else{
                    $('#password-err span').html(data.errmsg);
                    $('#password-err').show();
                }
            }
        })

    });
})
