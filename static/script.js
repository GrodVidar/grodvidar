$(document).ready(function() {
    $('.select2Field').select2();

    var providers = JSON.parse(localStorage.getItem('providers'));
    if(providers) {
        $('input[type="checkbox"]').each(function() {
            if (providers.includes($(this).val())) {
                $(this).prop('checked', true);
            }
        });
    }

    $('input:checked').each(function(index) {
        $(this).parents('label').css('border', 'green solid 2px');
    });

    $(':checkbox').change(function() {
        if($(this).is(':checked')) {
            $(this).parents('label').css('border', 'green solid 2px');
        }
        else {
            $(this).parents('label').css('border', '');
        }
    });

    for (const provider in providers) {
        $('')
    }
});

$('#movieForm').submit(function(event) {
    var providers = [];
    $("input[type='checkbox']:checked").each(function() {
        providers.push($(this).val());
    });
    localStorage.setItem('providers', JSON.stringify(providers));
});