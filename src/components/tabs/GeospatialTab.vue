<template>
  <section>
    <div class="columns">
      <div class="column">Map</div>
      <div class="column is-four-fifths">
        <div id="mapContainer"></div>  
      </div>
    </div>
  </section>
</template>

<script>
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import authService from "../../services/authService";
const data = require("../../assets/test.json");

export default {
  name: "geospatial",
  data() {
    return {
      filename: sessionStorage["sessionId"],
      timestamp: Date.now(),
      uri: authService.getEnvironmentURI(),
    };
  },
  methods: {
    setupLeafletMap: function () {
      console.log('Setting up map');
      const mapDiv = L.map("mapContainer", {
        fullscreenControl: true,
        fullscreenControlOptions: {
          position: "topleft",
        },
      }).setView([53.909, -2.61], 6);
      L.tileLayer(
        "http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png",
        {
          maxZoom: 18,
          minZoom: 3,
          attribution:
            'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
            '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
            'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
          id: "mapbox/streets-v11",
        }
      ).addTo(mapDiv);

      var geojsonLayer = new L.GeoJSON(data, { style: this.style });

      geojsonLayer.addTo(mapDiv);
    },
    importFullScreenMode() {
      console.log('Importing full screen');
      let script = document.createElement("script");
      script.setAttribute(
        "src",
        "https://api.mapbox.com/mapbox.js/plugins/leaflet-fullscreen/v1.0.1/Leaflet.fullscreen.min.js"
      );
      script.setAttribute("id", "leafletFullMapScript");
      document.head.appendChild(script);
    },
    numberWithCommas(number) {
      return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    },
    getColors(d) {
      return d > 1000
        ? "#800026"
        : d > 500
          ? "#BD0026"
          : d > 200
            ? "#E31A1C"
            : d > 100
              ? "#FC4E2A"
              : d > 50
                ? "#FD8D3C"
                : d > 20
                  ? "#FEB24C"
                  : d > 10
                    ? "#FED976"
                    : "#FFEDA0";
    },
    style(feature) {
      return {
        fillColor: this.getColors(feature.properties["2018 people per sq. km"]),
        weight: 2,
        opacity: 1,
        color: "white",
        dashArray: "3",
        fillOpacity: 0.7,
      };
    },
  },
  mounted() {
    this.importFullScreenMode()
    setTimeout(() => {
      this.setupLeafletMap();
    }, 200)
  },
  computed: {
    metadata() {
      return this.$store.state.metadata;
    },
    categoricalDescriptions() {
      return JSON.parse(this.$store.state.metadata.cat_describe);
    },
  },
};
</script>

<style scoped>
@import "https://api.mapbox.com/mapbox.js/plugins/leaflet-fullscreen/v1.0.1/leaflet.fullscreen.css";

#mapContainer {
  width: 100%;
  height: 80vh;
}
</style>
