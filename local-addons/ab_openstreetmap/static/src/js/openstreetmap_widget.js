odoo.define("ab_openstreetmap.openstreetmap_widget", function (require) {
  "use strict";
  var fieldRegistry = require("web.field_registry");
  var abstractField = require("web.AbstractField");

  var openstreetmap = abstractField.extend({
    template: "openstreetmap_template",
    start: function () {
      var self = this;
      this._super();
      self._initMap();
    },
    _initMap: function () {
      console.log("init map");
      console.log(this.value);
      console.log(this.hasOwnProperty("map"));
      var self = this
      $(document).ready(function () {
        setTimeout(() => {
          
          var lat = -33.45413198048182;
          var lng = -70.59354128229793;
          self.map = L.map('mapid').setView([lat, lng], 13);
          
          L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
            attribution:
            '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
          }).addTo(self.map);

          var lat_lon = self.value.split(",").map(Number);
          console.log("AAAA");
          console.log(lat_lon);
          self.renderMapMarker(lat_lon);

          // this.map = mymap;

          // var edit = self.mode == "edit" ? true : false;
          // self.marker = L.marker([lat, lng]).addTo(mymap);
          
          // marker.on("dragend", function (e) {
          //   var latlng = e.target._latlng;
          //   self.trigger_up("field_changed", {
          //     dataPointID: self.dataPointID,
          //     changes: {
          //       lat: latlng.lat,
          //       lng: latlng.lng,
          //     },
          //     viewType: self.viewType,
          //   });
          // });
          
          // if (edit) {
          //   var geocode = L.Control.geocoder({
          //     defaultMarkGeocode: false,
          //   }).addTo(mymap);
            
          //   geocode.on("markgeocode", function (e) {
          //     var lat = e.geocode.center.lat;
          //     var lng = e.geocode.center.lng;
              
          //     mymap.flyTo([lat, lng]);
          //     marker.setLatLng(new L.LatLng(lat, lng));
          //     self.trigger_up("field_changed", {
          //       dataPointID: self.dataPointID,
          //       changes: {
          //         lat: lat,
          //         lng: lng,
          //       },
          //       viewType: self.viewType,
          //     });
          //   });
          // }

          var interval = setInterval(() => {
            if (self.map && self.map._size.x > 0){
              clearInterval(interval);
            } else if (!document.getElementById("mapid")) {
              clearInterval(interval);
            }
            window.dispatchEvent(new Event("resize"));
          }, 500);
        }, 100);

      });
    },
    renderMapMarker: function (lat_lon) {
      if (this.hasOwnProperty("map") & (lat_lon[0] !==0) & (lat_lon[1] !== 0) ) {
        // console.log("render read only");
        // lat_lon = lat_lon.split(",").map(Number);
        this.map.setView(lat_lon, 16);
        if (this.marker != undefined) {
          this.map.removeLayer(this.marker);
        }        
        this.marker = L.marker(lat_lon).addTo(this.map);
      }
    },

    _renderReadonly: function () {
      if (this.hasOwnProperty("map")) {
        console.log("render read only");
        var lat_lon = this.value.split(",").map(Number);
        this.renderMapMarker(lat_lon);
        
        
        // if ((lat_lon[0] !==0) & (lat_lon[1] !== 0)) {
        //   this.map.setView(lat_lon, 16);
        //   if (this.marker != undefined) {
        //     this.map.removeLayer(this.marker);
        //   }        
        //   this.marker = L.marker(lat_lon).addTo(this.map);
        // }
      }
    },

    isSet: function () {
      return true;
    },
  });
  
  fieldRegistry.add("openstreetmap", openstreetmap);
});
