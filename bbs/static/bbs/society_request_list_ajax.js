function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).on("click",".approval_list",addAnswer);

        function addAnswer(e){
        e.submit
        e.stopPropagation(); // 같은 영역에 속해있는 중복 클릭 방지 
        e.preventDefault();  // 이벤트 진행 중지 

        var current_url = window.location.href;
        var url = $(this).attr('href'); //선택된 요소의 부모의 name속성 캐치
        var csrf = getCookie("csrftoken");
        console.log(current_url);
        $.ajax({
               type : 'post', // post방식으로 전송
               url : url, // 서버로 보낼 url 주소
               data : {  // 서버로 보낼 데이터들 dict형식 
                'csrfmiddlewaretoken': csrf,
                },
                // 서버에서 리턴받아올 데이터 형식
               dataType : 'html',  

               //서버에서 무사히 html을 리턴하였다면 실행 
               success : function(data, textStatus, jqXHR){ 
                $('.post_list').empty();
                $('.request_text').text('게시글')
                $('.approval_list').attr('href',current_url)
                $('.approval_list').attr('class','')
               },

               //서버에서 html을 리턴해주지 못했다면 
               error : function(data, textStatus, jqXHR){
               },
               
           });
        }