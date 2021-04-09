<template>
  <v-app-bar app fixed elevate-on-scroll color="white" light>
    <router-link to="/">
      <v-img src="../../public/resized_logo.png" />
    </router-link>

    <v-btn @click="$router.push({ path: '/tags' })" text>Tags</v-btn>
    <v-btn @click="$router.push({ path: '/aboutme' })" text>About Me</v-btn>

    <v-spacer />

    <v-btn v-if="isAvailableToken()" @click="$router.push({ path: '/manage_posts' })" text
      >Manage Posts</v-btn
    >

    <v-btn icon>
      <v-icon v-if="!isAvailableToken()" @click="login"
        >mdi-login</v-icon
      >
      <v-icon v-else @click="logout">mdi-logout</v-icon>
    </v-btn>

    <div class="gcse-searchbox-only"></div>
  </v-app-bar>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component
export default class Menu extends Vue {
  login(): void {
    window.location.href = "https://strapi.kreimben.com/connect/google";
  }

  logout(): void {
    console.log("implement again!");
  }

  isAvailableToken(): boolean {
    let result = false;
    result = (Vue.prototype.$token !== undefined);
    console.log(`isAvailableToken result: ${result}`)
    return result;
  }
}
</script>
