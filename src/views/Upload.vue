<template>
  <div class="home">
    <div class="columns">
      <div class="column is-two-thirds">
        <h1 class="is-size-1 has-text-weight-bold content">Upload data</h1>
        <Notification
          v-if="showError"
          type="error"
          title="There is a problem"
          message="The file must be CSV (comma-separated values) format"
        />
        <FileUploader @showError="showError = $event" />
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import FileUploader from "@/components/FileUploader.vue";
import Help from "@/components/Help.vue";
import Notification from "@/components/Notification.vue";

export default {
  name: "upload",
  data() {
    return {
      showError: false,
      canContinue: false
    };
  },
  components: {
    FileUploader,
    Help,
    Notification,
  },
};
</script>
