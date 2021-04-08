<template>
  <v-app>
    <Menu v-if="$vuetify.breakpoint.mobile === false" />
    <MenuMobile v-else />
    <v-main>
      <router-view />
    </v-main>
    <Footer />
  </v-app>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

import Menu from "./components/Menu.vue";
import MenuMobile from "./components/MenuMobile.vue";
import Footer from "./components/Footer.vue";

@Component({
  components: {
    Menu,
    MenuMobile,
    Footer,
  },
})
export default class App extends Vue {}
</script>
