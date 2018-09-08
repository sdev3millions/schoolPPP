$(function () {

    $(".js-create-school").click(function () {
      $.ajax({
        url: '/school/create/',
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-school").modal("show");
        },
        success: function (data) {
          $("#modal-book .modal-content").html(data.html_form);
        }
      });
    });    
  
  });