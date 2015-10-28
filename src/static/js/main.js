$(function() {
    var PlantingInstance = new Planting( {
        container: document.querySelector('.viewport'),
        manifestoUrl: '/manifesto.json',
        googleApiKey: 'AIzaSyD9fmhpMCKGM6BCMtsnn05GfxEK77jRHjc'
    });


    var load_plant = function(url) {
        return fetch(url)
            .then(function(res) {
                return res.json()
                    .then(function(plant) {
                        PlantingInstanceViewer.initViewer(plant);
                    });
            });
    };

    var PlantingInstanceViewer = new Planting( {
        container: document.querySelector('.viewport-viewer'),
        manifestoUrl: '/manifesto.json',
        googleApiKey: 'AIzaSyD9fmhpMCKGM6BCMtsnn05GfxEK77jRHjc'
    });
    load_plant('/forview.json');

    var $header = $('.js-header');
    var headerOffset = $header.offset().top + $header.height();
    var $firstSection = $('.section').first();

    $(document).on('click', '.js-page-scroll', function(e) {
        var offset = $(this.hash).offset();
        e.preventDefault();

        $('html, body').animate({
            scrollTop: offset.top - headerOffset
        }, 500, function() {

            location.hash = this.hash;
        }.bind(this));
    });

    $(window).on('scroll', function() {
        var val = $(this).scrollTop();
        var fixed = val > headerOffset - headerOffset / 2;

        $(document.body).toggleClass('is-header-fixed', fixed);
        $firstSection.css('margin-top', fixed ? headerOffset : 'auto');
    });
});
