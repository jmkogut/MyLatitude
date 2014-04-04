require.config({
    baseUrl: '/static/js',
    paths: {
      'ol': 'ol/ol',
    },
    shim: {
      'ol': {
        'exports': 'ol'
      }
    }
});

require(['jquery', 'ol'], function ($, ol) {
    console.log("Map plugin loaded.");

    // Asign a document ready handler to create and populate a map.
    $( document ).ready(function(){

        div = $("#map").first();
        div.css( "width",  "100%"  );
        div.css( "height", "500px" );

        var map = new ol.Map({
            target: "map",

            layers: [
              new ol.layer.Tile({
                source: new ol.source.MapQuest({layer: 'sat'})
              }) ],

            view: new ol.View2D({
                center: ol.proj.transform(
                  [37.41, 8.82],
                  'EPSG:4326',
                  'EPSG:3857'),
                  zoom: 4
            })
        });
  });

})
