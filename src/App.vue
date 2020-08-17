<template>
  <div id="app">
    <Navbar />
    <div class="container">
      <router-view />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Navbar from "@/components/Navbar.vue";

export default {
  name: "app",
  components: {
    Navbar,
  },
};
</script>

<style lang="scss">
@import "src/styles/custom.scss";

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.link {
  color: #1D70BE;
}

.link:hover {
  color: #1D70BE;
  text-decoration: underline;
}

.link:active, .link:focus {
  padding: 3px 0px 3px 0px;
  background-color: #FFDD00 !important;
  color: black !important;
  border-bottom: 3px solid black;
  text-decoration: none;
}

.back-link {
  color: black;
  text-decoration: underline;
}

.back-link:hover {
  color: black;
}

.button {
  background-color: #00703c !important;
}

.button:hover {
  background-color: #00703cf3 !important;
}

.button:active {
  border: 4px solid;
  border-color: #ffdd00 !important;
}

.button-secondary {
  background-color: #F3F2F1 !important;
}

.button-secondary:hover {
  background-color: #dbdad9 !important;
}

.button-secondary:active {
  border: 4px solid;
  border-color: #ffdd00 !important;
}

/* Medium devices (landscape tablets, 768px and down) */
@media only screen and (max-width: 768px) {
  .container {
    padding: 0px 15px 0px 15px;
  }
}
</style>
