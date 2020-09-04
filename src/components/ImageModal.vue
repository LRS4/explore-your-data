<template>
  <section>
    <b-modal :active="isActive" :can-cancel="true" :on-cancel="closeModal" :full-screen="false">
      <p class="image is-4by3">
        <img :src="imageUrl" />
      </p>
    </b-modal>
  </section>
</template>

<script>
export default {
  name: "modal",
  props: {
    isActive: Boolean,
    imageUrl: String,
  },
  methods: {
    closeModal() {
      this.$emit("onModalClose", false);
    },
  },
};
</script>
