/**
 * Created by marco on 05/01/17.
 */
function initAllMarkdownTextArea(){
    $(".__components__.__markdown_textarea__ button.preview").each(function(){
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
                return JSON.stringify({"markdown_text": textarea.val()}, null, '\t')
            },
            success: function (data) {
                modal_body.html(data.markdown_html);
            },
            error: function () {
                modal_body.html(error_message);
            }
        })
    });
}