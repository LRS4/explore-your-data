<template>
  <section>
    <b-tabs v-model="activeTab" :animated="false">
      <b-tab-item class="tab" label="Data">Lorem ipsum dolor sit amet.</b-tab-item>

      <b-tab-item class="tab" label="Describe">
        Lorem
        <br />ipsum
        <br />dolor
        <br />sit
        <br />amet.
      </b-tab-item>

      <b-tab-item :visible="showBooks" label="Univariate">
        What light is light, if Silvia be not seen?
        <br />What joy is joy, if Silvia be not by—
        <br />Unless it be to think that she is by
        <br />And feed upon the shadow of perfection?
        <br />Except I be by Silvia in the night,
        <br />There is no music in the nightingale.
      </b-tab-item>

      <b-tab-item label="Bivariate">
        Nunc nec velit nec libero vestibulum eleifend.
        Curabitur pulvinar congue luctus.
        Nullam hendrerit iaculis augue vitae ornare.
        Maecenas vehicula pulvinar tellus, id sodales felis lobortis eget.
      </b-tab-item>

      <b-tab-item label="Multivariate">
        Nunc nec velit nec libero vestibulum eleifend.
        Curabitur pulvinar congue luctus.
        Nullam hendrerit iaculis augue vitae ornare.
        Maecenas vehicula pulvinar tellus, id sodales felis lobortis eget.
      </b-tab-item>

      <b-tab-item label="Correlation">
        Nunc nec velit nec libero vestibulum eleifend.
        Curabitur pulvinar congue luctus.
        Nullam hendrerit iaculis augue vitae ornare.
        Maecenas vehicula pulvinar tellus, id sodales felis lobortis eget.
      </b-tab-item>
    </b-tabs>
  </section>
</template>

<script>
export default {
  name: "analysis",
  components: {
    
  },
  data() {
    return {
      activeTab: 0,
      showBooks: false,
    };
  }
};
</script>

<style lang="scss">
.tabs a {
  font-weight: 700 !important;
}

.tabs {
  background-color: #F8F8F8;
}
</style>
