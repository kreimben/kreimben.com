<template>
  <div>{{ pro }}</div>
  <div>{{ element }}</div>
  <button @click="getCurrentTime" style="display: inline">
    Change Parameter!
  </button>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  setup(props) {
    const element = ref("Menu Element");
    let pro = ref(props.current ?? "default");
    const ready = ref("asdflksdjlfkajsldkf");

    function getCurrentTime() {
      pro.value = new Date().toLocaleTimeString();
    }

    return {
      element,
      ready,
      pro,

      getCurrentTime,
    };
  },
  props: {
    current: {
      type: String,
    },
  },
});
</script>

<style>
div {
  text-align: center;
}
</style>
