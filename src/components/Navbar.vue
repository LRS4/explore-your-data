<template>
  <div class="nav">
    <b-navbar type="is-black">
      <template slot="brand">
        <b-navbar-item tag="router-link" :to="{ path: '/' }">
          <h2 class="nav-link">Explore Your Data</h2>
        </b-navbar-item>
      </template>
      <template slot="start">
        <b-navbar-item tag="router-link" :to="{ path: '/' }">
          <span class="nav-link has-text-weight-bold">Home</span>
        </b-navbar-item>
        <b-navbar-item tag="router-link" :to="{ path: '/api' }">
          <span class="nav-link has-text-weight-bold">API Sample</span>
        </b-navbar-item>
        <!-- <b-navbar-dropdown label="Info">
          <b-navbar-item href="#">About</b-navbar-item>
          <b-navbar-item href="#">Contact</b-navbar-item>
        </b-navbar-dropdown> -->
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

    <div class="container">
      <div class="phase-banner">
        <p class="phase-banner__content">
          <b-tag
            id="alpha-tag"
            class="has-text-weight-bold"
            type="is-info"
            :rounded="false"
            size="is-small"
          >ALPHA</b-tag>
          <span>
            This is a new service – your
            <a
              class="link"
              href="https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAYAAM-G-hxUQjlJWTc0NlgxUU9POFROWVZBUVhVWkI3MC4u"
              target="_blank"
            >feedback</a> will help us to improve it.
          </span>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Navbar",
};
</script>

<style scoped>
.nav {
  margin-bottom: 25px;
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

.phase-banner {
  margin-top: 10px;
}

#alpha-tag {
  background-color: #1d70b8 !important;
}

.nav-link:hover {
  text-decoration: underline;
}

.nav-link:active,
.link:focus {
  background-color: #ffdd00 !important;
  color: black !important;
  text-decoration: none;
}
</style>
