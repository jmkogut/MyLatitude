$( document ).ready(function(){
    div = $("#map").first();

    div.css( "width",  "100%"  );
    div.css( "height", "400px" );


    var map = new ol.Map({
        target: "map",

        layers: [
          new ol.layer.Tile({
            source: new ol.source.MapQuest({layer: 'sat'})
          }) ],

        view: new ol.View2D({
          center: ol.proj.transform([37.41, 8.82], 'EPSG:4326', 'EPSG:3857'),
          zoom: 4 })
    });

    $(document).map = map;

    console.log("Map init complete.");
});
