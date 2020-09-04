<template>
  <section>
    <div class="columns" v-for="column in chunkedColumns" v-bind:key="column.id">
      <div class="column is-one-third" v-for="variable in column" v-bind:key="variable.id">
        <div class="card">
          <div class="card-image">
            <figure class="image is-4by3">
              <img
                v-bind:src="'http://localhost:8080/api/plots/distribution/' + filename + '/' + variable.label"
                alt="Placeholder image"
                @click="openImageModal($event)"
              />
            </figure>
          </div>
          <div class="card-content">
            <div class="media">
              <div class="media-left">
                <figure class="image is-48x48">
                  <img src="https://bulma.io/images/placeholders/96x96.png" alt="Placeholder image" />
                </figure>
              </div>
              <div class="media-content">
                <p class="title is-4">{{ variable.label }}</p>
                <p class="subtitle is-6">Numeric</p>
              </div>
            </div>

            <div class="content">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit.
              Phasellus nec iaculis mauris.
              <a>@bulmaio</a>.
              <a href="#">#css</a>
              <a href="#">#responsive</a>
              <br />
              <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
            </div>
          </div>
        </div>
      </div>
    </div>
    <ImageModal
      :isActive="modalOpen"
      :imageUrl="selectedImageUrl"
      @onModalClose="modalOpen = $event"
    />
  </section>
</template>

<script>
import ImageModal from "@/components/ImageModal.vue";
import { mapGetters } from "vuex";
var chunk = require("chunk");

export default {
  name: "univariate",
  data() {
    return {
      modalOpen: false,
      selectedImageUrl: null,
      filename: sessionStorage['sessionId']
    };
  },
  components: {
    ImageModal,
  },
  methods: {
    openImageModal(event) {
      let newImageUrl = event.target.src;
      this.updateImageModalUrl(newImageUrl);
      this.modalOpen = true;
    },
    updateImageModalUrl(url) {
      this.selectedImageUrl = url;
    },
  },
  computed: {
    ...mapGetters(["columns"]),
    chunkedColumns() {
      return chunk(this.columns, 3);
    },
  },
};
</script>

<style scoped>
img:hover {
  cursor: pointer;
}
</style>
