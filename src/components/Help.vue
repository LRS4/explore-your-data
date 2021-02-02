<template>
  <section>
    <div>
      <div class="thin-blue-strip" />
      <h1 class="is-size-4 has-text-weight-bold content">Useful resources</h1>
      <div class="container">
        <div class="has-text-left help-section">
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
        <b-loading :is-full-page="false" v-model="isLoading" :can-cancel="true"></b-loading>
      </div>
    </div>
    
  </section>
</template>

<script>
import resourceService from '../services/resourceService';

export default {
  name: "Help",
  data() {
    return {
      links: null,
      isLoading: true
    }
  },
  async created() {
    await resourceService.fetchLinks()
      .then(responseData => {
        this.links = responseData.sort((a, b) => a.text.localeCompare(b.text));
        this.isLoading = false;
      }).catch(error => {
        this.error = error.message;
        this.isLoading = false;
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
