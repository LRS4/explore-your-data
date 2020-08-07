<template>
  <div class="home">
    <div class="columns">
      <div class="column is-two-thirds">
        <HelloWorld msg="Welcome" />
      </div>
      <div class="column is-one-third">
        <Help />
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import Help from "@/components/Help.vue";

export default {
  name: "home",
  components: {
    HelloWorld,
    Help,
  },
};
</script>
