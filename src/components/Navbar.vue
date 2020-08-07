<template>
  <div class="nav">
    <b-navbar type="is-black">
      <template slot="brand">
        <b-navbar-item tag="router-link" :to="{ path: '/' }">
          <h2>Explore Your Data</h2>
        </b-navbar-item>
      </template>
      <template slot="start">
        <b-navbar-item tag="router-link" :to="{ path: '/' }">Home</b-navbar-item>
        <b-navbar-item tag="router-link" :to="{ path: '/api' }">API Sample</b-navbar-item>
        <b-navbar-dropdown label="Info">
          <b-navbar-item href="#">About</b-navbar-item>
          <b-navbar-item href="#">Contact</b-navbar-item>
        </b-navbar-dropdown>
      </template>

      <!-- <template slot="end">
                <b-navbar-item tag="div">
                    <div class="buttons">
                        <a class="button is-primary">
                            <strong>Sign up</strong>
                        </a>
                        <a class="button is-light">
                            Log in
                        </a>
                    </div>
                </b-navbar-item>
      </template>-->
    </b-navbar>

    <div class="thin-blue-strip" />
  </div>
</template>

<script>
export default {
  name: "Navbar",
};
</script>

<style scoped>
.nav {
  margin-bottom: 40px;
}

h2 {
  font-size: 20px;
  font-weight: bold;
}

.thin-blue-strip {
  height: 10px;
  background-color: #005ea5;
  margin-top: -1px;
  margin-right: 50px;
  margin-left: 50px;
  position: relative;
  z-index: -1;
}
</style>
