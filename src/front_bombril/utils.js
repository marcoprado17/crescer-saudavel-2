DEFAULT_RESPONSE_TIME = 500;
SUCCESS_TOAST_TIME_OUT = 3500;
ERROR_TOAST_TIME_OUT = 10000;

String.prototype.format = String.prototype.f = function () {
    var s = this,
        i = arguments.length;

    while (i--) {
        s = s.replace(new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]);
    }
    return s;
};

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

function setAjaxButtonHandlers(data) {
    var button = data.button;
    var url = data.url;
    var method = data.method;
    var contentType = data.contentType;
    var minResponseTime = data.minResponseTime;
    var confirmMessage = data.confirmMessage;
    var onClick = data.onClick;
    var success = data.success;
    var error = data.error;
    var complete = data.complete;

    button.click(function (event) {
        if(typeof request_data == "function"){
            console.log("function type");
            request_data = request_data();
            console.log(request_data);
        }
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
            contentType: contentType,
            async: true,
            success: function (data) {
                var postReturnTime = (new Date()).getTime();
                var delay = minResponseTime - (postReturnTime - button.clickTime);
                setTimeout(function () {
                    success(data);
                    if (complete) {
                        complete();
                    }
                }, delay);
            },
            error: function (jqXHR) {
                var postReturnTime = (new Date()).getTime();
                var delay = minResponseTime - (postReturnTime - button.clickTime);
                setTimeout(function () {
                    error(jqXHR.status);
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

function throwErrorOpToast(message) {
    toastr.options.closeButton = true;
    toastr.options.timeOut = ERROR_TOAST_TIME_OUT;
    toastr.error(message);
}

function init_dynamic_selects() {
    $("select.dynamic").each(function () {
        var dependent_select = $(this);
        var determinant_select = $("#{0}".f(dependent_select.attr("depends_on")));
        var dependent_choices_string = dependent_select.attr("dependent_choices");
        var dependent_choices = JSON.parse( dependent_choices_string );

        var old_value = dependent_select.val();

        var new_value = determinant_select.find("option:selected").attr('value');
        var options = dependent_choices[new_value];
            dependent_select.empty();
        options.forEach(function(option){
            dependent_select.append($("<option></option>").attr("value", option[0]).text(option[1]));
        });

        options.forEach(function(option){
            if(option[0] == old_value){
                dependent_select.val(old_value);
            }
        });

        determinant_select.change(function () {
            var new_value = determinant_select.find("option:selected").attr('value');
            var options = dependent_choices[new_value];
            dependent_select.empty();
            options.forEach(function(option){
                dependent_select.append($("<option></option>").attr("value", option[0]).text(option[1]));
            });
        });
    })
}