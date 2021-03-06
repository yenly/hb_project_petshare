"use strict";
function initMap() {

var userLocation = {
                'San Francisco': {lat: 37.7749, lng: -122.4194},
                'Oakland': {lat: 37.8280, lng: -122.2501}
};

var zipcode = {
            '94103':{lat: 37.7726, lng: -122.4099},
            '94110':{lat: 37.7486, lng: -122.4184},
            '94121':{lat: 37.7726, lng: -122.4977},
            '94610':{lat: 37.8104, lng: -122.2399},
            '94611':{lat: 37.8336, lng: -122.2030},
            '94612':{lat: 37.8113, lng: -122.2682}
};

var shiftDelta = 0.001;
var zipCount = {};


// create map obj
var map = new google.maps.Map(document.getElementById('map'), {
    center: userLocation[user_city],
    zoom: 13
});

// for pop with pet name and picture
var infoWindow = new google.maps.InfoWindow({
    width: 150,
    height: 150
});

var jsonUrl = "/petmap.json?ani_type=" + ani_type;


// Retrieving the information with AJAX
$.get(jsonUrl, function (pets) {

    var pet, marker, html;

    for (var key in pets) {
        pet = pets[key];

        if (pet.zipcode in zipCount) {
            zipCount[pet.zipcode]++;
        }
        else{
            zipCount[pet.zipcode] = 1;
        }

        if (zipCount[pet.zipcode] % 2 === 0){
            zipcode[pet.zipcode].lng = zipcode[pet.zipcode].lng + (zipCount[pet.zipcode] * shiftDelta);
        }
        else{
            zipcode[pet.zipcode].lat = zipcode[pet.zipcode].lat + (zipCount[pet.zipcode] * shiftDelta);
        }




        marker = new google.maps.Marker({
            position: zipcode[pet.zipcode],
            map: map,
            icon: "/static/images/opaw_icon.png"
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


