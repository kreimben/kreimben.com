<template>
  <v-app>
    <Menu v-if="$vuetify.breakpoint.mobile === false" />
    <MenuMobile v-else />
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

import Menu from "./components/Menu.vue";
import MenuMobile from "./components/MenuMobile";

@Component({
  components: {
    Menu,
    MenuMobile,
  },
})
export default class App extends Vue {}
</script>
