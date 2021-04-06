<template>
  <v-app-bar app fixed elevate-on-scroll color="white" light>
    <router-link to="/">
      <v-img src="../../public/resized_logo.png" />
    </router-link>

    <v-btn @click="$router.push({ path: '/tags' })" text>Tags</v-btn>
    <v-btn @click="$router.push({ path: 'aboutme' })" text>About Me</v-btn>
    <v-btn text> ASMR Sound </v-btn>

    <v-spacer />

    <div class="gcse-searchbox-only"></div>
  </v-app-bar>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component
export default class Menu extends Vue {}
</script>
