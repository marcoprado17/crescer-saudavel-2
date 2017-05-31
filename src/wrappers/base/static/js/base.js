/**
 * Created by marco on 30/05/17.
 */
PRODUCT_SUCCESSFUL_ADDED_TO_CART = 'Uma unidade do produto "{0}" foi adicionada com sucesso ao seu carrinho.';
PRODUCT_ADD_TO_CART_ERROR = 'Erro ao adicionar o produto "{0}" ao carrinho. Tente novamente.';

BigNumber.config({DECIMAL_PLACES: 2});

function initAddToCartForms() {
    $("form.add-to-cart").each(function () {
        var form = $(this);
        console.log(form);
        var submit_button = form.find("button[type='submit']");
        var product_title = form.attr("data-product-title");
        var success_msg = PRODUCT_SUCCESSFUL_ADDED_TO_CART.f(product_title);
        var error_msg = PRODUCT_SUCCESSFUL_ADDED_TO_CART.f(product_title);
        var adding_text = form.find("p.adding");

        setAjaxFormHandlers({
            form: form,
            minResponseTime: 800,
            onSubmit: function () {
                submit_button.prop("disabled", true);
                adding_text.removeClass("hidden");
            },
            success: function () {
                throwSuccessOpToast(success_msg)
            },
            error: function (status, dataAsObject) {
                var msg = error_msg;
                if ("error_msg" in dataAsObject) {
                    msg = dataAsObject.error_msg
                }
                throwErrorOpToast(msg)
            },
            complete: function () {
                submit_button.prop("disabled", false);
                adding_text.addClass("hidden");
            }
        })
    });
}

(function (factory) {
    if (typeof define === 'function' && define.amd) {
        define(['moment'], factory); // AMD
    } else if (typeof exports === 'object') {
        module.exports = factory(require('../moment')); // Node
    } else {
        factory(window.moment); // Browser global
    }
}(function (moment) {
    return moment.defineLocale('pt-br', {
        months: 'Janeiro_Fevereiro_Março_Abril_Maio_Junho_Julho_Agosto_Setembro_Outubro_Novembro_Dezembro'.split('_'),
        monthsShort: 'jan_fev_mar_abr_mai_jun_jul_ago_set_out_nov_dez'.split('_'),
        weekdays: 'domingo_segunda-feira_terça-feira_quarta-feira_quinta-feira_sexta-feira_sábado'.split('_'),
        weekdaysShort: 'dom_seg_ter_qua_qui_sex_sáb'.split('_'),
        weekdaysMin: 'D_S_T_Q_Q_S_S'.split('_'),
        longDateFormat: {
            LT: 'HH:mm',
            L: 'DD/MM/YYYY',
            LL: 'D [de] MMMM [de] YYYY',
            LLL: 'D [de] MMMM [de] YYYY [às] LT',
            LLLL: 'dddd, D [de] MMMM [de] YYYY [às] LT'
        },
        calendar: {
            sameDay: '[Hoje às] LT',
            nextDay: '[Amanhã às] LT',
            nextWeek: 'dddd [às] LT',
            lastDay: '[Ontem às] LT',
            lastWeek: function () {
                return (this.day() === 0 || this.day() === 6) ?
                    '[Último] dddd [às] LT' : // Saturday + Sunday
                    '[Última] dddd [às] LT'; // Monday - Friday
            },
            sameElse: 'L'
        },
        relativeTime: {
            future: 'em %s',
            past: '%s atrás',
            s: 'segundos',
            m: 'um minuto',
            mm: '%d minutos',
            h: 'uma hora',
            hh: '%d horas',
            d: 'um dia',
            dd: '%d dias',
            M: 'um mês',
            MM: '%d meses',
            y: 'um ano',
            yy: '%d anos'
        },
        ordinal: '%dº'
    });
}));