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
      uri: authService.getEnvironmentURI()
    };
  },
  methods: {
    setupLeafletMap: function () {
      console.log("Setting up map");
      this.map = L.map("mapContainer", {
        fullscreenControl: true,
        fullscreenControlOptions: {
          position: "topleft",
        },
      }).setView([53.909, -2.61], 6);
      L.tileLayer(
        "http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png",
        {
          maxZoom: 10,
          minZoom: 6,
          attribution:
            'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
            '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
            'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
          id: "mapbox/streets-v11",
        }
      ).addTo(this.map);

      var geojsonLayer = new L.GeoJSON(data, { 
        style: this.style,
        onEachFeature: this.onEachFeature
      });

      geojsonLayer.addTo(this.map);
      this.geojsonLayer = geojsonLayer;

      this.setupInfoPanel();
    },
    importFullScreenMode() {
      console.log("Importing full screen");
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
        ? "#005fa6"
        : d > 500
          ? "#2f6aad"
          : d > 200
            ? "#557db8"
            : d > 100
              ? "#7e98c8"
              : d > 50
                ? "#a0b1d6"
                : d > 20
                  ? "#b0bedd"
                  : d > 10
                    ? "#c2cde5"
                    : "#d4dbed";
    },
    style(feature) {
      return {
        fillColor: this.getColors(feature.properties["2018 people per sq. km"]),
        weight: 1,
        opacity: 1,
        color: "gray",
        dashArray: "2",
        fillOpacity: 0.7,
      };
    },
    highlightFeature(e) {
      var layer = e.target;

      layer.setStyle({
        weight: 2.5,
        color: "#666",
        dashArray: "",
        fillOpacity: 0.7,
      });

      if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
      }

      this.info.update(layer.feature.properties);
    },
    resetHighlight(e) {
      this.geojsonLayer.resetStyle(e.target);
      this.info.update();
    },
    zoomToFeature(e) {
      this.map.fitBounds(e.target.getBounds());
    },
    onEachFeature(feature, layer) {
      layer.on({
        mouseover: this.highlightFeature,
        mouseout: this.resetHighlight,
        click: this.zoomToFeature,
      });
    },
    setupInfoPanel() {
      this.info = L.control();

      this.info.onAdd = function () {
        this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
        this.update();
        return this._div;
      };

      this.info.update = function (props) {
        this._div.innerHTML =
          "<h5>Population Density</h5>" +
          (props
            ? "<b>" +
              props.LAD19NM +
              "</b><br />" +
              props["Area (sq km)"] +
              " sq. km" +
              "<br />" +
              props["2018 people per sq. km"] +
              " people per sq. km" +
              "<br />" +
              props["Estimated Population mid-2018"] +
              " people total" +
              "<br />"
            : "Hover over a boundary");
      };

      this.info.addTo(this.map);
    }
  },
  mounted() {
    this.importFullScreenMode();
    setTimeout(() => {
      this.setupLeafletMap();
    }, 200);
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

<style>
@import "https://api.mapbox.com/mapbox.js/plugins/leaflet-fullscreen/v1.0.1/leaflet.fullscreen.css";

#mapContainer {
  width: 100%;
  height: 80vh;
}

.info {
    padding: 6px 8px;
    font: 14px/16px Arial, Helvetica, sans-serif;
    background: white;
    background: rgba(255,255,255,0.8);
    box-shadow: 0 0 15px rgba(0,0,0,0.2);
    border-radius: 5px;
}

.info h4 {
    margin: 0 0 5px;
    color: #777;
}
</style>
