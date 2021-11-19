function show_map(latitude, longitude) {
    var widget_map = L.map('map');
    widget_map.setView([latitude, longitude], 13);
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(widget_map);
}

$(function() {
    $(document).change(function () {
        var latitude = $("[name=latitude]").val();
        var longitude = $("[name=longitude]").val();
        console.log(latitude, longitude);
        show_map(latitude, longitude);
    });
    $(document).change(function () {
        var latitude = $("[name=latitude]").val();
        var longitude = $("[name=longitude]").val();
        console.log(latitude, longitude);
        show_map(latitude, longitude);
    });
});