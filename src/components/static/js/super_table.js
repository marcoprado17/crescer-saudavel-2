/**
 * Created by marco on 04/01/17.
 */

function setBoolTdValue(col, row_idx, value) {
    console.log("setBoolTdValue");
    console.log("col: " + col);
    console.log("row_idx: " + row_idx);
    console.log("value: " + value);
    var td = $("#col-{0}-row-{1}".f(col, row_idx));
    console.log(td);
    var boolContainer = td.find(".bool-container");
    if (value) {
        boolContainer.removeClass("false");
        boolContainer.addClass("true");
    }
    else {
        boolContainer.addClass("false");
        boolContainer.removeClass("true");
    }
}

function setTextTdValue(col, row_idx, value) {
    var td = $("#col-{0}-row-{1}".f(col, row_idx));
    td.html(value);
}

function initSuperTable() {
    initTooltips();
    initDynamicSelects();
    initSuperTableSortMethod();
    initActionActivateDisableButtons();
}

function initActionActivateDisableButtons(){
    $(".super-table button.to-activate").each(function () {
        var to_activate_button = $(this);
        var row_idx = to_activate_button.parent().attr("data-row-idx");
        var disable_button = $("#disable-btn-{0}".f(row_idx));
        var url = to_activate_button.attr("data-url");
        var error_msg = to_activate_button.attr("data-error-msg");
        var col = to_activate_button.parent().attr("data-active-col-id");
        var to_activate_text = to_activate_button.attr("data-to-activate-text");
        var activating_text = to_activate_button.attr("data-activating-text");

        to_activate_button.html(to_activate_text);

        setAjaxButtonHandlers({
            button: to_activate_button,
            url: url,
            method: "post",
            minResponseTime: DEFAULT_RESPONSE_TIME,
            onClick: function () {
                console.log("onClick");
                to_activate_button.html(activating_text);
                to_activate_button.prop("disabled", true);
            },
            success: function () {
                console.log("success");
                to_activate_button.addClass("hidden");
                disable_button.removeClass("hidden");
                setBoolTdValue(col, row_idx, true);
            },
            error: function () {
                console.log("error");
                throwErrorOpToast(error_msg);
            },
            complete: function () {
                console.log("complete");
                to_activate_button.html(to_activate_text);
                to_activate_button.prop("disabled", false);
            }
        });

    });

    $(".super-table button.disable").each(function () {
        var disable_button = $(this);
        var row_idx = disable_button.parent().attr("data-row-idx");
        var to_activate_button = $("#to-activate-btn-{0}".f(row_idx));
        var url = disable_button.attr("data-url");
        var error_msg = disable_button.attr("data-error-msg");
        var col = disable_button.parent().attr("data-active-col-id");
        var disable_text = disable_button.attr("data-disable-text");
        var disabling_text = disable_button.attr("data-disabling-text");

        disable_button.html(disable_text);

        setAjaxButtonHandlers({
            button: disable_button,
            url: url,
            method: "post",
            minResponseTime: DEFAULT_RESPONSE_TIME,
            onClick: function () {
                disable_button.html(disabling_text);
                disable_button.prop("disabled", true);
            },
            success: function () {
                disable_button.addClass("hidden");
                to_activate_button.removeClass("hidden");
                setBoolTdValue(col, row_idx, false);
            },
            error: function () {
                throwErrorOpToast(error_msg);
            },
            complete: function () {
                disable_button.html(disable_text);
                disable_button.prop("disabled", false);
            }
        })
    });
}

function initSuperTableSortMethod(){
    $(document).ready(function () {
        select = $('select.sort-method');
        $('form.filter input.sort-method').attr("value", select.val());
    });

    $('select.sort-method').on('change', function () {
        select = $(this);
        $('form.filter input.sort-method').attr("value", select.val());
        $("form.filter input[type='submit']").click();
    });
}

function initIntWithButtonAction(forms, onSuccess) {
    forms.each(function () {
        var form = $(this);
        var input = form.find("input[type='number']");
        var submit_button = form.find("button");
        var text = submit_button.attr("data-text");
        var doing_text = submit_button.attr("data-doing-text");
        var error_4xx_msg = form.attr("data-error-4xx-msg");
        var error_5xx_msg = form.attr("data-error-5xx-msg");
        var row_idx = form.attr("data-row-idx");

        submit_button.html(text);

        setAjaxFormHandlers({
            form: form,
            minResponseTime: DEFAULT_RESPONSE_TIME,
            onSubmit: function () {
                submit_button.html(doing_text);
                submit_button.prop("disabled", true);
            },
            success: function (dataAsObject) {
                submit_button.html(text);
                submit_button.prop("disabled", false);
                onSuccess(row_idx, dataAsObject);
            },
            error: function (status) {
                if (Math.floor(status / 100) == 4) {
                    throwErrorOpToast(error_4xx_msg);
                }
                else if (Math.floor(status / 100) == 5) {
                    throwErrorOpToast(error_5xx_msg);
                }
            },
            complete: function () {
                submit_button.html(text);
                submit_button.prop("disabled", false);
                input.val("");
            }
        })
    });
}
