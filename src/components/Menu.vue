<template>
  <v-app-bar app fixed elevate-on-scroll color="white" light>
    <router-link to="/">
      <v-img src="../../public/resized_logo.png" />
    </router-link>

    <v-btn @click="$router.push({ path: '/tags' })" text>Tags</v-btn>
    <v-btn @click="$router.push({ path: '/aboutme' })" text>About Me</v-btn>

    <v-spacer />

    <v-btn
      v-if="isAuthCredentialEmpty()"
      @click="$router.push({ path: '/manage_posts' })"
      text
      >Manage Posts</v-btn
    >

    <v-btn icon>
      <v-icon v-if="1 === 1">mdi-login</v-icon>
      <v-icon v-else>mdi-logout</v-icon>
    </v-btn>

    <div class="gcse-searchbox-only"></div>
  </v-app-bar>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component
export default class Menu extends Vue {
  isAuthCredentialEmpty(): boolean {
    return true;
  }
}
</script>
