"use strict";
function initMap() {

var sf = {lat: 37.7749, lng: -122.431297};
var zipcode = {
            '94103':{lat: 37.7726, lng: -122.4099},
            '94110':{lat: 37.7486, lng: -122.4184},
            '94121':{lat: 37.7726, lng: -122.497668}
};

var shiftDelta = 0.002;
var zipcount = {};


// create map obj
var map = new google.maps.Map(document.getElementById('map'), {
    center: sf,
    zoom: 13
});

// for pop with pet name and picture
var infoWindow = new google.maps.InfoWindow({
    width: 150,
    height: 150
});

// Retrieving the information with AJAX
$.get('/petmap.json', function (pets) {

    var pet, marker, html;

    for (var key in pets) {
        pet = pets[key];

        marker = new google.maps.Marker({
            position: zipcode[pet.zipcode],
            map: map,
        });


        html = (
                '<div>' +
                '<h4><a href="/pet_profile/' + pet.pet_id +'">' +
                pet.name + '</a></h4>' +
                '<img style="width:150px;" src="'+ pet.image_url +'" alt=' + pet.name +'>'+
                '</div>');

        bindInfoWindow(marker, map, infoWindow, html);
    }

});

function bindInfoWindow(marker, map, infoWindow, html) {
    google.maps.event.addListener(marker, 'click', function () {
        infoWindow.close();
        infoWindow.setContent(html);
        infoWindow.open(map, marker);
    });
}
}


