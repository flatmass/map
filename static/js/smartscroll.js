    ($.fn.smartscroll || (function($){
		var $event = $.event,
			scrollTimeout;

	    $event.special.smartscroll = {
	    	setup: function () {
	            $(this).bind("scroll", $event.special.smartscroll.handler);
	        },
	        teardown: function () {
	            $(this).unbind("scroll", $event.special.smartscroll.handler);
	        },
	        handler: function (event, execAsap) {
	            // Save the context
	            var context = this,
	            	args = arguments;
	            // set correct event type
	            event.type = "smartscroll";
	            if (scrollTimeout) { clearTimeout(scrollTimeout); }
	            scrollTimeout = setTimeout(function () {
	                $.event.dispatch.apply(context, args);
	            }, execAsap === "execAsap" ? 0 : 100);
	        }
	    };

	    $.fn.smartscroll = function (fn) {
	        return fn ? this.bind("smartscroll", fn) : this.trigger("smartscroll", ["execAsap"]);
	    };
	})(jQuery));

	($.fn.smartresize || (function($){
		var $event = $.event,
			scrollTimeout;

	    $event.special.smartresize = {
	    	setup: function () {
	            $(this).bind("resize", $event.special.smartresize.handler);
	        },
	        teardown: function () {
	            $(this).unbind("resize", $event.special.smartresize.handler);
	        },
	        handler: function (event, execAsap) {
	            // Save the context
	            var context = this,
	            	args = arguments;
	            // set correct event type
	            event.type = "smartresize";
	            if (scrollTimeout) { clearTimeout(scrollTimeout); }
	            scrollTimeout = setTimeout(function () {
	                $.event.dispatch.apply(context, args);
	            }, execAsap === "execAsap" ? 0 : 100);
	        }
	    };

	    $.fn.smartresize = function (fn) {
	        return fn ? this.bind("smartresize", fn) : this.trigger("smartresize", ["execAsap"]);
	    };
	})(jQuery));