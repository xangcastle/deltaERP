(function($) {
    $(document).ready(function() {
        const calculate = function() {
            let total_debito = 0.0;
            let total_credito = 0.0;
            $.each($('.debit input'), function(i, o) {
                total_debito += parseFloat($(o).val())
            })
            $.each($('.credit input'), function(i, o) {
                total_credito += parseFloat($(o).val())
            })
            let diferencia = Math.abs(total_credito - total_debito);
            $('#id_debit_sum').val(total_debito.toFixed(2));
            $('#id_credit_sum').val(total_credito.toFixed(2));
            $('#id_difference').val(diferencia.toFixed(2));
        };

        $(document).on('change', '.debit input', calculate);
        $(document).on('change', '.credit input', calculate);
    })
})(grp.jQuery)