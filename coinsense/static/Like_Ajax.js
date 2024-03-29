
$(document).on('click','.like', like)
$(document).on('click','.book-mark', bookmark)

 function like(e){
    e.stopPropagation(); // 같은 영역에 속해있는 중복 클릭 방지 
    e.preventDefault();  // 이벤트 진행 중지 
    var pk = $(this).attr('name');
    var url = $(this).attr('href');
    var csrf = getCookie("csrftoken");
    $.ajax({ // .like 버튼을 클릭하면 <새로고침> 없이 ajax로 서버와 통신하겠다.
      type: "POST", // 데이터를 전송하는 방법을 지정
      url: url, // 통신할 url을 지정
      data: {'pk': pk, 'csrfmiddlewaretoken': csrf,}, // 서버로 데이터 전송시 옵션
      dataType: "json", // 서버측에서 전송한 데이터를 어떤 형식의 데이터로서 해석할 것인가를 지정, 없으면 알아서 판단

     // 서버측에서 전송한 Response 데이터 형식 (json)
      // {'likes_count': post.like_count, 'message': message }

      success: function(response){ // 통신 성공시 - 좋아요 갯수 변경, 유저 목록 변경
        if(response.message == 'like'){
        $("#like"+pk).attr("value","추천 "+response.like_count);
        }
        else if(response.message=='like_del'){
        $("#like"+pk).attr("value","추천 "+response.like_count);
        }
        //var users = $("#like-user-"+pk).text();
      },
     error: function(request, status, error){ // 통신 실패시 - 로그인 페이지 리다이렉트

        //  alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
      },
    });
  }

  function bookmark(e){
    e.stopPropagation(); // 같은 영역에 속해있는 중복 클릭 방지 
    e.preventDefault();  // 이벤트 진행 중지 

    var pk = $(this).attr('name');
    var url = $(this).attr('href');
    var csrf = getCookie("csrftoken");
    
    $.ajax({ // .like 버튼을 클릭하면 <새로고침> 없이 ajax로 서버와 통신하겠다.
      type: "POST", // 데이터를 전송하는 방법을 지정
      url: url, // 통신할 url을 지정
      data: {
        'pk': pk, 
        'csrfmiddlewaretoken': csrf,
      }, // 서버로 데이터 전송시 옵션

      dataType: "json", // 서버측에서 전송한 데이터를 어떤 형식의 데이터로서 해석할 것인가를 지정, 없으면 알아서 판단

     // 서버측에서 전송한 Response 데이터 형식 (json)
      // {'likes_count': post.like_count, 'message': message }

      success: function(response){ // 통신 성공시 - 좋아요 갯수 변경, 유저 목록 변경
          $(".book-mark").attr("value",response.message);
        //var users = $("#like-user-"+pk).text();
      },
     error: function(request, status, error){ // 통신 실패시 - 로그인 페이지 리다이렉트

        //  alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
      },
    });
  }