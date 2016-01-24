/*
* Craftyslide
* Автор: Abid Din - http://craftedpixelz.co.uk
* Версия: 1.0
* Права: Crafted Pixelz
* Лицензия: MIT
* Обновлено: 07 июня 2011
*/

(function ($) {
    $.fn.craftyslide = function (options) {
        var defaults = {
            "width": 600,
            "height": 500,
            "pagination": false,
            "fadetime": 350,
            "delay": 5000
        };
        var options = $.extend(defaults, options);
        
            return this.each(function () {

            // Переменные
            var $this = $(this);
            var $slides = $this.find("ul li");

            $slides.not(':first').hide();

            // Страницы
            function paginate() {
                $this.append("<ol id='pagination' />");
                
                var i = 1;
                $slides.each(function () {
                    $(this).attr("id", "slide" + i);
                    $("#pagination")
                    .append("<li><a href='#slide" + i + "'>" + i + "</a></li>");
                    i++;
                });
                
                $("#pagination li a:first").addClass("active");
            }

            // Добавляем подписи
            function captions() {
                $slides.each(function () {
                    $caption = $(this).find("img").attr("title");
                    if ($caption !== undefined) {
                        $(this).prepend("<p class='caption'>" + $caption + "</p>");
                    }
                    $slides.filter(":first").find(".caption").css("bottom", 0);
                });
            }

            // Ручной режим
            function manual() {
                var $pagination = $("#pagination li a");
                $pagination.click(function (e) {
                    e.preventDefault();
                    var $current = $(this.hash);
                    if ($current.is(":hidden")) {
                        $slides.fadeOut(options.fadetime);
                        $current.fadeIn(options.fadetime);
                        $pagination.removeClass("active");
                        $(this).addClass("active");
                        $(".caption").css("bottom", "-37px");
                        $current.find(".caption").delay(300).animate({
                            bottom: 0
                        }, 300);
                    }
                });
            }

            // Автоматический режим
            function auto() {
                setInterval(function () {
                    $slides.filter(":first-child")
                    .fadeOut(options.fadetime)
                    .next("li")
                    .fadeIn(options.fadetime)
                    .end()
                    .appendTo("#slideshow ul");

                    $slides.each(function () {
                        if ($slides.is(":visible")) {
                            $(".caption").css("bottom", "-37px");
                            $(this).find(".caption").delay(300).animate({
                                bottom: 0
                            }, 300);
                        }
                    });

                }, options.delay);
            }

            // Ширина
            $this.width(options.width);
            $this.find("ul, li img").width(options.width);

            // Высота
            $this.height(options.height);
            $this.find("ul, li").height(options.height);

            // Проверка 
            if (options.pagination === true) {
                paginate();
            } else {
                auto();
            }

            captions(); manual();

        });
    };
})(jQuery);