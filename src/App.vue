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
</style>
