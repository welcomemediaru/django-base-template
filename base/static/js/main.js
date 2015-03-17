(function ($) {
    "use strict";

    $(function () {
        $("body").width("100%").width("");

        $("[src$=svg]").svgmagic();

        Modernizr.addTest("flexboxtweener", Modernizr.testAllProps("flexAlign", "end", true));
    });
})(window.jQuery);
