<template>
  <div class="back-link-area">
    <a href="#" @click="goBack" class="link back-link"> 
        <b-icon icon="chevron-left" size="is-small"></b-icon>Back
    </a>
  </div>
</template>

<script>
import $router from "../router";

export default {
  name: "backlink",
  methods: {
    goBack() {
      $router.back();
    }
  },
};
</script>

<style scoped>
.back-link-area {
    margin-bottom: 10px;
}
</style>
