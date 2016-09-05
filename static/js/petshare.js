
"use strict";

var app = angular.module('petShareApp', []);

// order of $scope, $http, and $log matters
app.controller('searchController', ['$scope', '$http', '$log', function ($scope, $http, $log) {
    $scope.searchTerm = "";
    $scope.city = " ";
    // $scope.resultsURL = "";
    $scope.$log = $log;
    // $log.log("TEST");

    // console.log($scope.searchTerm);

    $scope.DisplayPets = function (type) {
        $scope.searchTerm = type;
        $scope.ani_type = type;
        $log.log($scope.searchTerm);

        var url = "/display_pets/" + $scope.ani_type;

        $http.get(url).then(function(response) {
            $scope.pets = response.data;
            $log.log($scope.pets);

            $scope.pet_key = Object.keys($scope.pets);

            $scope.city = $scope.pets[$scope.pet_key[0]].city;
        });
    };

}]);

