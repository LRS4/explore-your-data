<template>
  <section>
      <b-loading :is-full-page="isFullPage" :active.sync="isLoading" :can-cancel="false">
        <b-icon pack="fas" icon="spinner" size="is-large" custom-class="fa-pulse"></b-icon>
      </b-loading>
  </section>
</template>

<script>
export default {
  data() {
    return {
      isFullPage: true
    };
  },
  props: {
    isLoading: Boolean
  }
};
</script>
