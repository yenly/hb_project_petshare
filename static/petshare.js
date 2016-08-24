"use strict";

var app = angular.module('petShareApp', []);

app.controller('searchController', function ($scope) {
    $scope.searchTerm = "direwolf";
});