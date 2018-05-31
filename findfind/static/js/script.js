document.write("checking something....")
  $('#my_button').on('click', function(){
                alert('Button clicked. Disabling...');
                $('#like_button').attr("disabled", true);
            });