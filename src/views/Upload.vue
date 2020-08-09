<template>
  <div class="home">
    <div class="columns">
      <div class="column is-two-thirds">
        <h1 class="is-size-1 has-text-weight-bold content">Upload data</h1>
        <Notification
          v-if="showError"
          type="error"
          title="There is a problem"
          message="The file must be in CSV (comma-separated values) format."
        />
        <Warning message="Only upload data which is not sensitive, or has been anonymised." />
        <FileUploader @showError="showError = $event" @dataValid="isButtonDisabled = $event" />
        <b-button
          class="is-success button has-text-weight-bold"
          size="is-medium"
          data-prevent-double-click
          :rounded="false"
          :disabled="isButtonDisabled"
          :loading="isButtonLoading"
          @click="submitData"
        >Save and continue</b-button>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import FileUploader from "@/components/FileUploader.vue";
import Warning from "@/components/Warning.vue";
import Notification from "@/components/Notification.vue";

export default {
  name: "upload",
  components: {
    FileUploader,
    Warning,
    Notification,
  },
  data() {
    return {
      showError: false,
      isButtonDisabled: true,
      isButtonLoading: false,
    };
  },
  methods: {
    submitData() {
      console.log("Submitting data...");
      this.isButtonLoading = true;

      // initial check - is the data valid?

      // if so - process it and continue
    },
  },
};
</script>
