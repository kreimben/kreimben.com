<template>
  <div id="app">
    <Menu />
    <div>Hello, {{ name }}</div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

import Menu from "../components/Menu.vue";

export default defineComponent({
  components: {
    Menu,
  },
  setup() {
    let name = "Aksidion Kreimben";

    return {
      name,
    };
  },
});
</script>
