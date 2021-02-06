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
const data = require("../../assets/Local_Authority_Districts_(May_2020)_Boundaries_UK_BFE.json");

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
      console.log(data);
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

      var geojsonLayer = new L.GeoJSON(
        // "http://geoportal1-ons.opendata.arcgis.com/datasets/deeb99fdf09949bc8ed4dc95c80da279_4.geojson"
        data
      );

      geojsonLayer.addTo(mapDiv);

      // events are fired when entering or exiting fullscreen.
      mapDiv.on("enterFullscreen", function () {
        console.log("entered fullscreen");
      });

      mapDiv.on("exitFullscreen", function () {
        console.log("exited fullscreen");
      });

      // you can also toggle fullscreen from map object
      mapDiv.toggleFullScreen();
    },
    importFullScreenMode() {
      let script = document.createElement("script");
      script.setAttribute(
        "src",
        "https://api.mapbox.com/mapbox.js/plugins/leaflet-fullscreen/v1.0.1/Leaflet.fullscreen.min.js"
      );
      document.head.appendChild(script);
    },
    numberWithCommas(number) {
      return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    },
  },
  mounted() {
    this.importFullScreenMode();
    this.setupLeafletMap();
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
