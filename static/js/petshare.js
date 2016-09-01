
"use strict";

var app = angular.module('petShareApp', []);

// order of $scope, $http, and $log matters
app.controller('searchController', ['$scope', '$http', '$log', function ($scope, $http, $log) {
    $scope.searchTerm = "";
    $scope.city = "";
    $scope.$log = $log;
    // $log.log("TEST");

    // console.log($scope.searchTerm);

    $scope.DisplayDogs = function () {
        $scope.searchTerm = "dogs in";

        $http.get('/display_dogs').then(function(response) {
            $scope.dogs = response.data;

            $scope.city = $scope.dogs.dog1.city;
        });
    };

    $scope.DisplayCats = function () {
        $scope.searchTerm = "cats in";


        $http.get('/display_cats').then(function(response) {
            $scope.cats = response.data;

            $scope.city = $scope.cats.cat1.city;
        });
    };


}]);

