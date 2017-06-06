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

function initHoverPopover() {
    $(".hover-popover").popover({
        trigger: "manual",
        html: true,
        animation: false,
        content: function(){
            var contentContainer = $("#{0}".f($(this).attr("data-content-id")));
            if(contentContainer.length !== 0) {
                return contentContainer.html();
            }
        }
    })
        .on("mouseenter", function () {
            var _this = this;
            $(this).popover("show");
            $(".popover").on("mouseleave", function () {
                $(_this).popover('hide');
            });
        }).on("mouseleave", function () {
        var _this = this;
        setTimeout(function () {
            if (!$(".popover:hover").length) {
                $(_this).popover("hide");
            }
        }, 300);
    });
}
