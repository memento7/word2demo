$( document ).ready(function() {
    $(".result").each(function(e) {
        $(this).css('border', '4px solid rgba(0, 121, 255, ' + $(this).data('acc') + ')');
    });
});