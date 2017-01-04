/**
 * Created by marco on 04/01/17.
 */

function setBoolTdValue(col, row, value) {
     var td = $("#col-{0}-row-{1}".f(col, row));
     console.log(td);
     var boolContainer = td.find(".bool-container");
     if(value) {
         boolContainer.removeClass("false");
         boolContainer.addClass("true");
     }
     else {
         boolContainer.addClass("false");
         boolContainer.removeClass("true");
     }
}