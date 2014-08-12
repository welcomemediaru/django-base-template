(function ($) {
    "use strict";

    $(function () {
        $("body").width("100%").width("");

        $("[src$=svg]").svgmagic();
    });
})(window.jQuery);
