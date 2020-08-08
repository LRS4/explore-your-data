<template>
  <div>
    <div class="thin-blue-strip" />
    <div class="has-text-left help-section">
      <h1 class="is-size-4 has-text-weight-bold content">Useful resources</h1>
      <ul>
        <li v-for="link in links" :key="link.text">
          <a class="link"
            :href="link.href"
            target="_blank">
            {{ link.text }}
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import $backend from '../backend'

export default {
  name: "Help",
  data() {
    return {
      links: null
    }
  },
  created() {
    $backend.fetchLinks()
      .then(responseData => {
        this.links = responseData.sort((a, b) => a.text.localeCompare(b.text));
      }).catch(error => {
        this.error = error.message
      })
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}

p,
ul {
  font-size: 19px;
}

.thin-blue-strip {
  height: 10px;
  background-color: #005ea5;
  margin-top: -1px;
  position: relative;
  z-index: -1;
}
</style>
