var app = angular.module('app', ['ngRoute','ngResource']);

app.controller('materias',function($scope,datos){
    $scope.lista=datos.get();
});
//Definir el factory que retorne datos de un web service
app.factory('datos',['$resource',function($resource){
    return $resource('http://127.0.0.1:8000/materia/',{},
        {get:{method:'GET',pararms:{},isArray:true}
});
}
]);



