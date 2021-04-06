<template>
  <div id="app">
    <Menu />
    <div>Hello, {{ name }}</div>
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <div>This is just test page for home view</div>
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
