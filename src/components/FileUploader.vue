/* eslint-disable semi */
<template>
  <section>
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

    <div class="tags">
      <span v-for="(file, index) in dropFiles" :key="index" class="tag is-dark">
        {{file.name}}
        <button class="delete is-small" type="button" @click="deleteDropFile(index)"></button>
      </span>
    </div>
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
        } else {
          this.showError = false;
          this.$emit('showError', this.showError);
        }
      }
    }
  }
};
</script>

<style scoped lang="scss">
</style>
