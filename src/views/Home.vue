<template>
  <Menu current="this is value" />
  <div>Hello, {{ name }}</div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

import Menu from "../components/Menu.vue";

export default defineComponent({
  components: {
    Menu,
  },
  data() {
    return {
      name: "Aksidion Kreimben!",
    };
  },
});
</script>
