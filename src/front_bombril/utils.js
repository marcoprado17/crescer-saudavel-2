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
    console.log("parentHeight:" + parentHeight);
    console.log("siblingsTotalOuterHeight:" + siblingsTotalOuterHeight);
    var verticalFluidHeight = (parentHeight-siblingsTotalOuterHeight)/2;
    verticalFluids.each(function(){
        var verticalFluid = $(this);
        verticalFluid.height(verticalFluidHeight);
    });
});
