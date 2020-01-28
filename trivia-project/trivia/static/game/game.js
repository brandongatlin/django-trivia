$(document).ready(function() {
    console.log('game js loaded');

    function hiLight(el) {
        el.addClass('hilight');
        el.siblings().removeClass('hilight')
    }

    $('.choice').on('click', function(e) {
        hiLight($(this))
        const qId = $(this).parent().parent().attr('id');
        const choice = $(this).text();
    });

    // $('#submit-answers').on('click', function(e) {
    //     e.preventDefault();
    //     // $('.q-box').each(function(id) {
    //     //     console.log(id);
    //     //     const choice = $('#' + id).siblings()[0]
    //     //     console.log(choice);
    //     // });
    // })

});