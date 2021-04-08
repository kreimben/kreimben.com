<template>
  <v-app-bar app fixed elevate-on-scroll color="white" light>
    <router-link to="/">
      <v-img src="../../public/resized_logo.png"/>
    </router-link>

    <v-btn @click="$router.push({ path: '/tags' })" text>Tags</v-btn>
    <v-btn @click="$router.push({ path: '/aboutme' })" text>About Me</v-btn>
    <v-btn text> ASMR Sound </v-btn>

    <v-spacer />

    <v-btn
      v-if="isAuthCredentialEmpty()"
      @click="$router.push({ path: '/manage_posts' })"
      text
      >Manage Posts</v-btn
    >

    <v-btn icon>
      <v-icon v-if="!$auth.isAuthenticated" @click="login()">mdi-login</v-icon>
      <v-icon v-else @click="logout()">mdi-logout</v-icon>
    </v-btn>

    <div class="gcse-searchbox-only"></div>
  </v-app-bar>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component
export default class Menu extends Vue {
  login() {
    this.$auth.loginWithRedirect();
  }

  logout() {
    this.$auth.logout({
      returnTo: window.location.origin,
    });
  }

  isAuthCredentialEmpty(): boolean {
    console.log(`this.$auth.user: ${this.$auth.user}`);
    return this.$auth.user !== undefined;
  }
}
</script>
