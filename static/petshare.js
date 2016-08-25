"use strict";

var app = angular.module('petShareApp', []);

app.controller('searchController', function ($scope, $http) {

    $scope.DisplayDogs = function () {
        $http.get('/display_dogs').then(function(response) {
            $scope.dogs = response.data;
        });
    };

    $scope.DisplayCats = function () {
        $http.get('/display_cats').then(function(response) {
            $scope.cats = response.data;
        });
    };

});