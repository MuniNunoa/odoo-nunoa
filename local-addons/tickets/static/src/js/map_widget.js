odoo.define('map_widget', function (require) {
    "use strict";
    
    var AbstractField = require('web.AbstractField');
    var fieldRegistry = require('web.field_registry');
    
    var colorField = AbstractField.extend({
        className: 'etc',
        tagName: 'div',
        supportedFieldTypes: ['char'],
        events: {
            // 'change .etc': 'clickPill',
        },
        init: function () {
            console.log("init");
            this.latitude = -33.465958;
            this.longitude = -70.585642;
            // this.totalColors = 10;
            // console.log(this.value);
            // this.map = L.map("map");
            // this.$el.append($('<div>', {
            //     'id': "map",
            // }));
            this._super.apply(this, arguments);
        },
        init_map: function () {
            console.log("INIT MAP");
            
            // this.$el.append('<div id="map"></div>')
            // console.log($("#map"))
            // console.log("MAP MAP")
            this.map = L.map("map");
            this.map.setView([this.latitude, this.longitude], 13);
            L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            }).addTo(this.map);
        },
        _renderEdit: function () {
            console.log("RENDER EDIT");
            this.$el.empty();
            // for (var i = 0; i < this.totalColors; i++ ) {
            //     var className = "o_color_pill o_color_" + i;
            //     if (this.value === i ) {
            //         className += ' active';
            //     }
            //     this.$el.append($('<span>', {
            //         'class': className,
            //         'data-val': i,
            //     }));
            // }
        },
        _renderReadonly: function () {
            this.$el.empty();
            console.log("RENDER READONLY");
            this.latitude, this.longitude = this.value.split(",").map(Number)
            
            // hacer despues de renderizar::
            this.init_map();

            
            // this.$el.append($('<div>', {
            //     'id': "map",
            // }));
            // this.$el.append($('<input>', {
            //     'value': this.value,
            //     'class': "latlon_hidden",
            //     // 'type': "hidden"
            // }));
            // var className = "o_color_pill active readonly o_color_" + this.value;
        },
        // start: function() {
        //     console.log('START');
        //     self = this;
        //     this._super.apply(this, arguments).then(
        //         function() {
        //             self.init_map();
        //         }
                
        //     );
        //     // this.init_map();
        // },
        clickPill: function (ev) {
            this.init_map();
            // var $target = $(ev.currentTarget);
            // var data = $target.data();
            // this._setValue(data.val.toString());
        },

    
    });
    
    fieldRegistry.add('latlon_map', colorField);
    
    return {
        colorField: colorField,
    };
    });