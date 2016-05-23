import Planting from 'plantingjs';
import jquery from 'jquery';

jquery(function() {
  const PlantingInstance = new Planting( {
    container: document.querySelector('.viewport'),
    manifestoUrl: '/manifesto.json',
    googleApiKey: 'AIzaSyD9fmhpMCKGM6BCMtsnn05GfxEK77jRHjc',
  });

  const PlantingInstanceViewer = new Planting( {
    container: document.querySelector('.viewport-viewer'),
    manifestoUrl: '/manifesto.json',
    googleApiKey: 'AIzaSyD9fmhpMCKGM6BCMtsnn05GfxEK77jRHjc',
  });

  const loadPlanting = function(url) {
    return fetch(url)
      .then(function(res) {
        return res.json()
          .then(function(plant) {
            PlantingInstanceViewer.initViewer(plant);
          });
      });
  };

  loadPlanting('/forview.json');

  const $header = jquery('.js-header');
  const headerOffset = $header.offset().top + $header.height();
  const $firstSection = jquery('.section').first();

  jquery(document).on('click', '.js-page-scroll', function(e) {
    const offset = jquery(this.hash).offset();
    e.preventDefault();

    jquery('html, body').animate({
      scrollTop: offset.top - headerOffset,
    }, 500, function() {
      location.hash = this.hash;
    }.bind(this));
  });

  jquery(window).on('scroll', function() {
    const val = jquery(this).scrollTop();
    const fixed = val > headerOffset - headerOffset / 2;

    jquery(document.body).toggleClass('is-header-fixed', fixed);
    $firstSection.css('margin-top', fixed ? headerOffset : 'auto');
  });
});
