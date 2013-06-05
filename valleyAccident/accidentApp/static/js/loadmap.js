var dxcord = 84.4; var dycord = 28.48; var mapzoomlevel=6;

var map = L.map('map').setView([dycord, dxcord],mapzoomlevel); //28.48, 84.4], 7);

		L.tileLayer('http://{s}.tile.cloudmade.com/{key}/22677/256/{z}/{x}/{y}.png', {
			attribution: 'Open Data Hackathon, Hotel Radisson, 2013',
			key: 'BC9A493B41014CAABB98F0471D759707'
		}).addTo(map);

		var baseballIcon = L.icon({
			iconUrl: 'baseball-marker.png',
			iconSize: [32, 37],
			iconAnchor: [16, 37],
			popupAnchor: [0, -28]
		});
var dist = {};





		var geojson;

		
		function onEachFeature(feature, layer) {
			var popupContent = "<p>";
			var i=1;
			//for(var i=0;i<feature.lblattributes.length; i++){
				//popupContent += "<b>"+ feature.lblfattributes[i]['a'+(i+1)]+" : </b> "+ feature.properties[feature.lblattributes[i]['a'+(i+1)]]+"<br/>";
			//}
			popupContent +="</p>";

			layer.on({
				//mouseover: highlightFeature,
				//mouseout: resetHighlight,
				//click: zoomToFeature
			});

			//"District: " + feature.properties.Name + "</p>" + "</p><a href='district.php?d="+feature.properties.Name+"'>See district Details</a>";
			//alert(dist[kathmandu]);
				//district=getdistrict(feature.properties.Name);
				//alert(district);
				//popupContent += district['Total number of Primary School'];	
//alert(dist[])
			if (feature.properties && feature.properties.popupContent) {
				popupContent += feature.properties.popupContent;
			}

			layer.bindPopup(popupContent);
		}
	
		function style(feature) {
	
    return {
        fillColor: '#fff000',
        weight: 2,
        opacity: 1,
        color: 'blue',
        dashArray: '3',
        fillOpacity: 0.7
    };
}


$(document).ready( 
    function(){ 

    	/*(function() { $.ajax(
					{
						type: 'GET',
						url: 'schooled/api/json/year/2069/district/Nepal/totalSchoolByLevel/',
						//data: {district:"dd", list_type:"vdc"},
						//datatype: json
						dataType: 'json',
						success: function(data)						
						{				
							//mydata=data.data.Name;
							disval = data.Data;
							
							$.each(disval, function() {
								distname=this['Name'].toLowerCase();
								//dist[distname]={};
								dist[distname]=this['Total number of Lower Secondary School'];
								//alert(dist[distname]);
							
							});				

							//showmap();
						}
					});
})(), 
*/
          (function() {
          	L.geoJson(districtmap, {

			filter: function (feature, layer) {
				if (feature.properties) {
					// If the property "underConstruction" exists and is true, return false (don't render features under construction)
					return feature.properties.underConstruction !== undefined ? !feature.properties.underConstruction : true;
				}
				return false;
			},
			style:style,
			onEachFeature: onEachFeature
		}).addTo(map);
          })(),
          
          (function() {
          	var legend = L.control({position: 'bottomright'});

		legend.onAdd = function (map) {

			var div = L.DomUtil.create('div', 'info legend');
				
var labels = [];
				labels.push(
					'<i style="background:#ff0000;"></i> Nepal');
				labels.push(
					'<i style="background:#00ff00;"></i> District');
				labels.push(
					'<i style="background:#0000ff;"></i> VDC/NP');
			

			div.innerHTML = labels.join('<br/><br/>');
			return div;
		};

		legend.addTo(map);
          	
          })()

          
                             
});



