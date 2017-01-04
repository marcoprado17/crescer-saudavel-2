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
    var verticalFluids =  $(".vertical-fluid");
    var verticalFluid = verticalFluids.first();
    verticalFluid.next().removeClass("hidden");
    var parentHeight = verticalFluid.parent().height();
    verticalFluid.siblings().each(function(){
        var sibling = $(this);
        if( ! sibling.hasClass("vertical-fluid") ){
            siblingsTotalOuterHeight += sibling.outerHeight(true)
        }
    });
    var verticalFluidHeight = (parentHeight-siblingsTotalOuterHeight)/2;
    verticalFluids.each(function(){
        var verticalFluid = $(this);
        verticalFluid.height(verticalFluidHeight);
    });
});

function setAjaxButtonHandlers(data) {
    var button = data.button;
    var url = data.url;
    var method = data.method;
    var request_data = data.request_data;
    var minResponseTime = data.minResponseTime;
    var confirmMessage = data.confirmMessage;
    var dataType = data.dataType;
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
        onClick();
        button.clickTime = (new Date()).getTime();
        $.ajax({
            url: url,
            method: method,
            data: request_data,
            dataType: dataType,
            async: true,
            success: function (data) {
                var postReturnTime = (new Date()).getTime();
                var delay = minResponseTime - (postReturnTime - button.clickTime);
                setTimeout(function () {
                    success(data);
                    if(complete){
                        complete();
                    }
                }, delay);
            },
            error: function (jqXHR) {
                var postReturnTime = (new Date()).getTime();
                var delay = minResponseTime - (postReturnTime - button.clickTime);
                setTimeout(function () {
                    error(jqXHR.status);
                    if(complete){
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
