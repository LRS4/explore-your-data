/* eslint-disable semi */
<template>
  <section class="uploader-section">
    <div class="columns is-gapless is-vcentered" v-for="(file, index) in dropFiles" :key="index">
      <div class="column is-one-quarter">
        <b-icon v-if="showError == false" icon="check-bold" size="is-medium"></b-icon>
        <b-icon v-else icon="alert" size="is-medium"></b-icon>
      </div>
      <div class="column is-one-quarter">
        <span class="has-text-weight-bold">{{ file.name }}</span>
      </div>
      <div class="column is-one-half">
        <b-button class="is-pulled-right button-secondary is-light is-medium" @click="deleteDropFile(index)">
          <span>Remove</span>
        </b-button>
      </div>
    </div>
    <hr />
    <b-field>
      <b-upload v-model="dropFiles" 
        multiple 
        native 
        drag-drop 
        expanded 
        type="is-dark">
        <section class="section">
          <div class="content has-text-centered">
            <p>
              <b-icon icon="upload" size="is-large"></b-icon>
            </p>
            <p>Drop your files here or click to upload</p>
          </div>
        </section>
      </b-upload>
    </b-field>
  </section>
</template>

<script>
export default {
  name: 'fileuploader',
  data () {
    return {
      dropFiles: [],
      showError: false
    };
  },
  methods: {
    deleteDropFile (index) {
      this.dropFiles.splice(index, 1);
    }
  },
  watch: {
    /**
     * Watches dropFiles property to check if file is CSV
     * @return {Boolean} Emits true or false to parent component to display error
     */
    dropFiles: function () {
      if (this.dropFiles.length > 0) {
        if (!this.dropFiles[0].name.includes(".csv")) {
          this.showError = true;
          this.$emit('showError', this.showError);
          this.$emit('dataValid', true);
        } else {
          this.showError = false;
          this.$emit('showError', this.showError);
          this.$emit('dataValid', false);
        }
      } else {
        this.$emit('dataValid', true);
      }
    }
  }
};
</script>

<style scoped lang="scss">
.uploader-section {
  margin-bottom: 35px;
}

.columns {
  margin-bottom: 0px !important;
}

hr {
  margin-top: 3px;
}

.file-name {
  margin-top: 1px;
}
</style>
