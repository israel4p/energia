$(document).ready(function() {
    // Mascara valor do kwh
    $('#valorkwh').mask('#.#####', {reverse: true});

    // Mascara data de leitura
    $('#dataleitura').mask('00/00/0000');

    // Desativa botão salvar ao ser clicado
    $('.submit').click(function() {
        $('.submit').attr('disabled', true);
    });

    // Fecha notificação
    $('.delete').click(function() {
        $('.notification').hide();
    });
});
