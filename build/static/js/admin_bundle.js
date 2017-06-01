DEFAULT_RESPONSE_TIME = 500;
SUCCESS_TOAST_TIME_OUT = 3500;
ERROR_TOAST_TIME_OUT = 10000;
WARNING_TOAST_TIME_OUT = 8000;
INFO_TOAST_TIME_OUT = 10000;

String.prototype.format = String.prototype.f = function () {
    var s = this,
        i = arguments.length;

    while (i--) {
        s = s.replace(new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]);
    }
    return s;
};

function initFacebookLoginButton() {
    $("button.btn-facebook").each(function () {
        var button = $(this);
        var errorMsg = button.attr("data-error-msg");
        var loadingText = button.siblings(".loading-text");
        var connectFbUrl = button.attr("data-connect-url");
        console.log(connectFbUrl);
        var homeUrl = button.attr("data-home-url");
        button.click(function () {
            FB.login(function (response) {
                if (response.authResponse) {
                    button.prop("disabled", true);
                    loadingText.removeClass("hidden");
                    $.ajax({
                        type: "POST",
                        url: connectFbUrl,
                        data: response.authResponse["accessToken"],
                        processData: false,
                        contentType: 'application/octet-stream; charset=utf-8',
                        success: function (result) {
                            window.location.href = homeUrl;
                        },
                        error: function (result) {
                            dataAsObject = getDataAsObject(result.responseText);
                            if (dataAsObject != null && "error" in dataAsObject) {
                                throwErrorOpToast(dataAsObject.error)
                            }
                            else {
                                throwErrorOpToast(errorMsg);
                            }
                        },
                        complete: function () {
                            button.prop("disabled", false);
                            loadingText.addClass("hidden");
                        }
                    })
                } else {
                    throwErrorOpToast(errorMsg);
                }
            }, {scope: "email"});
        })
    })
}


function initVerticalFluid() {
    $(document).ready(function () {
        var siblingsTotalOuterHeight = 0;
        var verticalFluids = $(".vertical-fluid");
        var verticalFluid = verticalFluids.first();
        verticalFluid.next().removeClass("hidden");
        var parentHeight = verticalFluid.parent().height();
        verticalFluid.siblings().each(function () {
            var sibling = $(this);
            if (!sibling.hasClass("vertical-fluid")) {
                siblingsTotalOuterHeight += sibling.outerHeight(true)
            }
        });
        var verticalFluidHeight = (parentHeight - siblingsTotalOuterHeight) / 2;
        verticalFluids.each(function () {
            var verticalFluid = $(this);
            verticalFluid.height(verticalFluidHeight);
        });
    });
}


function initAllDateTimePickers() {
    $(".datetimepicker").each(function () {
        dateAsString = $(this).find("input").attr("data-date-as-string");
        date = new Date(dateAsString);
        if (dateAsString == "") {
            date = new Date();
        }
        $(this).datetimepicker({
            locale: "pt-br",
            format: "DD/MM/YYYY"
        });
        $(this).data("DateTimePicker").date(moment(date));
    });
}


function getDataAsObject(data) {
    try {
        return JSON.parse(data)
    } catch (e) {
        return null
    }
}


function setAjaxButtonHandlers(data) {
    var button = data.button;
    var url = data.url;
    var method = data.method;
    var minResponseTime = data.minResponseTime;
    var confirmMessage = data.confirmMessage;
    var onClick = data.onClick;
    var success = data.success;
    var error = data.error;
    var complete = data.complete;

    button.click(function (event) {
        if (confirmMessage) {
            var c = confirm(confirmMessage);
            if (!c) {
                return false;
            }
        }
        if (!minResponseTime) {
            minResponseTime = 0;
        }
        var requestData = onClick();
        button.clickTime = (new Date()).getTime();
        $.ajax({
            url: url,
            method: method,
            data: requestData,
            contentType: 'application/json;charset=UTF-8',
            async: true,
            success: function (data) {
                console.log(data);
                var postReturnTime = (new Date()).getTime();
                var delay = minResponseTime - (postReturnTime - button.clickTime);
                setTimeout(function () {
                    success(getDataAsObject(data));
                    if (complete) {
                        complete();
                    }
                }, delay);
            },
            error: function (jqXHR) {
                var postReturnTime = (new Date()).getTime();
                var delay = minResponseTime - (postReturnTime - button.clickTime);
                setTimeout(function () {
                    error(jqXHR.status, getDataAsObject(jqXHR.responseText));
                    if (complete) {
                        complete();
                    }
                }, delay);
            }
        });
        return true;
    });
}


function setAjaxFormHandlers(data) {
    var form = data.form;
    var minResponseTime = data.minResponseTime;
    var confirmMessage = data.confirmMessage;
    var onSubmit = data.onSubmit;
    var success = data.success;
    var error = data.error;
    var complete = data.complete;

    var submit = form.find("button[type='submit']");

    form.submit(function (event) {
        event.preventDefault();
        if (confirmMessage) {
            var c = confirm(confirmMessage);
            if (!c) {
                return false;
            }
        }
        if (!minResponseTime) {
            minResponseTime = 0;
        }
        submitReturn = onSubmit();
        if (submitReturn == false) {
            return false;
        }
        form.clickTime = (new Date()).getTime();
        $.ajax({
            url: form.attr("action"),
            method: form.attr("method"),
            data: form.serialize(),
            async: true,
            success: function (data) {
                var postReturnTime = (new Date()).getTime();
                var delay = minResponseTime - (postReturnTime - form.clickTime);
                setTimeout(function () {
                    success(getDataAsObject(data));
                    if (complete) {
                        complete();
                    }
                }, delay);
            },
            error: function (jqXHR) {
                var postReturnTime = (new Date()).getTime();
                var delay = minResponseTime - (postReturnTime - form.clickTime);
                setTimeout(function () {
                    error(jqXHR.status, getDataAsObject(jqXHR.responseText));
                    if (complete) {
                        complete();
                    }
                }, delay);
            }
        });
        return true;
    });
}


function throwSuccessOpToast(message) {
    toastr.options.closeButton = false;
    toastr.options.timeOut = SUCCESS_TOAST_TIME_OUT;
    toastr.success(message);
}


function throwInfoOpToast(message) {
    toastr.options.closeButton = true;
    toastr.options.timeOut = INFO_TOAST_TIME_OUT;
    toastr.info(message);
}


function throwWarningOpToast(message) {
    toastr.options.closeButton = true;
    toastr.options.timeOut = WARNING_TOAST_TIME_OUT;
    toastr.warning(message);
}


function throwErrorOpToast(message) {
    toastr.options.closeButton = true;
    toastr.options.timeOut = ERROR_TOAST_TIME_OUT;
    toastr.error(message);
}


function initTooltips() {
    $(document).ready(function () {
        $('[data-toggle="tooltip"]').tooltip();
    });
}


function initDynamicSelects() {
    $("select.dynamic").each(function () {
        var dependent_select = $(this);
        var determinant_select = dependent_select.closest("form").find("#{0}".f(dependent_select.attr("depends_on")));
        var dependent_choices_string = dependent_select.attr("dependent_choices");
        var dependent_choices = JSON.parse(dependent_choices_string);

        var old_value = dependent_select.val();

        var new_value = determinant_select.find("option:selected").attr('value');
        var options = dependent_choices[new_value];
        dependent_select.empty();
        options.forEach(function (option) {
            dependent_select.append($("<option></option>").attr("value", option[0]).text(option[1]));
        });

        options.forEach(function (option) {
            if (option[0] == old_value) {
                dependent_select.val(old_value);
            }
        });

        determinant_select.change(function () {
            var new_value = determinant_select.find("option:selected").attr('value');
            var options = dependent_choices[new_value];
            dependent_select.empty();
            options.forEach(function (option) {
                dependent_select.append($("<option></option>").attr("value", option[0]).text(option[1]));
            });
        });
    })
}


function clearErrors(form) {
    form.find("span.error").remove();
    form.find(".has-error").removeClass("has-error");
}


function showFormErrors(form, errors) {
    clearErrors(form);
    for (var key in errors) {
        if (errors.hasOwnProperty(key)) {
            input = form.find("input[name='{0}']".f(key));
            select = form.find("select[name='{0}']".f(key));
            textarea = form.find("textarea[name='{0}']".f(key));
            arrayOfErrors = errors[key];
            if (input.length == 1) {
                input.parent().addClass("has-error");
                for (var i = 0; i < arrayOfErrors.length; i++) {
                    input.after("<span class='help-block error'>{0}</span>".f(arrayOfErrors[i]))
                }
            }
            else if (select.length == 1) {
                select.parent().addClass("has-error");
                for (var i = 0; i < arrayOfErrors.length; i++) {
                    select.after("<span class='help-block error'>{0}</span>".f(arrayOfErrors[i]))
                }
            }
            else if (textarea.length == 1) {
                textarea.parent().addClass("has-error");
                for (var i = 0; i < arrayOfErrors.length; i++) {
                    textarea.after("<span class='help-block error'>{0}</span>".f(arrayOfErrors[i]))
                }
            }
        }
    }
}

function initSaveForms() {
    $("form.save").each(function () {
        var form = $(this);
        var submit_input = form.find("input[type='submit']");
        var save_text = form.attr("data-save-text");
        var saving_text = form.attr("data-saving-text");
        var error_msg = form.attr("data-error-msg");
        var success_msg = form.attr("data-success-msg");

        setAjaxFormHandlers({
            form: form,
            minResponseTime: 800,
            onSubmit: function () {
                submit_input.val(saving_text);
                submit_input.prop("disabled", true);
            },
            success: function () {
                clearErrors(form);
                throwSuccessOpToast(success_msg)
            },
            error: function (status, dataAsObject) {
                if (status == 400 && dataAsObject != null && "errors" in dataAsObject) {
                    showFormErrors(form, dataAsObject.errors);
                }
                throwErrorOpToast(error_msg)
            },
            complete: function () {
                submit_input.val(save_text);
                submit_input.prop("disabled", false);
            }
        })
    });
}

function initAllTelInput() {
    $("input.tel").each(function () {
        var input = $(this);
        input.keypress(function (e) {
            if (e.keyCode == 13)
                return true;
            var chr = String.fromCharCode(e.which);
            if ("0123456789".indexOf(chr) < 0)
                return false;
            var input_length = input.val().length;
            if (input_length == 0) {
                input.val("(")
            }
            else if (input_length == 3) {
                input.val(input.val() + ") ")
            }
            else if (input_length == 9) {
                input.val(input.val() + "-")
            }
            else if (input_length == 14 && input.val()[10] != "-") {
                old_tel = input.val();
                sub_1 = old_tel.substring(0, 9);
                sub_2 = old_tel.substring(11);
                input.val(sub_1 + old_tel[10] + "-" + sub_2)
            }
        });

        input.keyup(function () {
            var input_length = input.val().length;
            if (input_length >= 11 && input_length < 15 && input.val()[10] == "-") {
                old_tel = input.val();
                sub_1 = old_tel.substring(0, 9);
                sub_2 = old_tel.substring(11);
                input.val(sub_1 + "-" + old_tel[9] + sub_2);
            }
            else if (input_length == 10 && input.val()[9] != "-") {
                old_tel = input.val();
                sub_1 = old_tel.substring(0, 9);
                input.val(sub_1 + "-" + old_tel[9]);
            }
        });
    });
}

function initAllCepInput() {
    $("input.cep").each(function () {
        var input = $(this);
        input.keypress(function (e) {
            if (e.keyCode == 13)
                return true;
            var chr = String.fromCharCode(e.which);
            if ("0123456789".indexOf(chr) < 0)
                return false;
            var input_length = input.val().length;
            if (input_length == 5) {
                input.val(input.val() + "-")
            }
            else if (input_length == 9) {
                return false;
            }
        });
    });
}

function bigNumberToFormattedPrice(value) {
    s = "R$ ";
    s += value.toFixed(2).replace(".", ",");
    return s;
}

function initPriceWithDiscountCalc() {
    $("input[type=checkbox].change-price-with-discount").bind("change", function () {
        if (this.checked) {
            recalcPriceWithDiscount();
        }
        else {
            var priceWithDiscountInput = $("input.price-with-discount");
            priceWithDiscountInput.val("-")
        }
    });
    $("input[type=number].change-price-with-discount").bind("keyup mouseup", function () {
        if($("input[type=checkbox].change-price-with-discount").prop("checked")){
            recalcPriceWithDiscount();
        }
    });
    $("input[type=text].change-price-with-discount").bind("keyup", function () {
        if($("input[type=checkbox].change-price-with-discount").prop("checked")){
            recalcPriceWithDiscount();
        }
    });
}

function recalcPriceWithDiscount() {
    console.log("Recalculando preço com desconto");
    var priceWithDiscountInput = $("input.price-with-discount");
    var price = $("input.price").val();
    var discountPercentage = $("input.discount-percentage").val();
    var url = priceWithDiscountInput.attr("data-url");
    priceWithDiscountInput.val("Calculando...");
    $.ajax({
        url: url,
        method: "post",
        data: {
            price: price,
            discount_percentage: discountPercentage
        },
        success: function (data) {
            dataAsObject = getDataAsObject(data);
            priceWithDiscountInput.val(dataAsObject.price_with_discount);
        },
        error: function () {
            priceWithDiscountInput.val("Erro!");
        }
    });
}
/**
 * Created by marco on 09/05/17.
 */
function initAllMarkdownTextArea() {
    $("button.markdown.preview").each(function () {
        var button = $(this);
        var modal = $("{0}".f(button.attr("data-target")));
        var url = button.attr("data-url");
        var loading_message = button.attr("data-loading-message");
        var error_message = button.attr("data-error-message");
        var modal_body = modal.find(".modal-body");
        var textarea = $("{0}".f(button.attr("data-textarea")));

        setAjaxButtonHandlers({
            button: button,
            url: url,
            method: "post",
            contentType: 'application/json;charset=UTF-8',
            minResponseTime: 900,
            onClick: function () {
                modal_body.html(loading_message);
                console.log("onClick");
                return JSON.stringify({"markdown_text": textarea.val()}, null, '\t')
            },
            success: function (data) {
                if (data != null && "markdown_html" in data) {
                    modal_body.html(data.markdown_html);
                }
                else {
                    modal_body.html(error_message);
                }
            },
            error: function () {
                console.log("error");
                modal_body.html(error_message);
            }
        })
    });
}

function initAllDynamicSelects() {
    $("select.dynamic").each(function () {
        var dynamicSelect = $(this);
        var determinantSelect = $("select[id={0}]".f(dynamicSelect.attr("determinant-select-id")));
        onDeterminantSelectChange(dynamicSelect, determinantSelect);
        determinantSelect.on("change", function () {
            onDeterminantSelectChange(dynamicSelect, determinantSelect);
        });
    });
}

function onDeterminantSelectChange(dynamicSelect, determinantSelect) {
    var newDeterminantSelectValue = determinantSelect.val();
    if(newDeterminantSelectValue != null){
        var dynamicChoicesData = JSON.parse(dynamicSelect.attr("dynamic-choices-data"));
        options = [];
        dynamicChoicesData[newDeterminantSelectValue.toString()].forEach(function (element) {
            options.push(new Option(element[1], parseInt(element[0])));
        });
        dynamicSelect.find("option[value]").remove();
        dynamicSelect.append(options).val("").trigger("change");
    }
}
