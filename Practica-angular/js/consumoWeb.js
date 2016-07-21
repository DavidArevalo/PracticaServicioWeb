var app = angular.module('web',['ngResource']);

app.controller('controladorweb',function($scope,datos){
	$scope.mensaje="";
	var band=true;
	$scope.lista=datos.get();
	$scope.validar=function(){
		var ci = $scope.cedulaInput;
		for (var i=0;i<$scope.lista.length;i++){
			if($scope.lista[i].cedula==ci){
				band=false;
				window.location="materias.html";//redireccionar-----javascript
				break;
			}
		}

		if(band==true){
			$scope.mensaje="no esta el alumno";
		}
		
	}


   
});
//Definir el factory que retorne datos de un web service
app.factory('datos',['$resource',function($resource){
    return $resource('http://127.0.0.1:8000/alumno/',{},
        {get:{method:'GET',pararms:{},isArray:true}
});
}
]);
