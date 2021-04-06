<template>
  <v-container>
    <v-card class="yellow pa-3 mb-4"> This is MainView! </v-card>
    <v-alert v-if="$vuetify.breakpoint.mobile" text dismissable type="info">
      <div>You are mobile!</div>
      <div>Display: {{ $vuetify.breakpoint.name }}</div>
    </v-alert>
    <v-alert v-else text dismissable type="info">
      <div>You are desktop!</div>
      <div>Display: {{ $vuetify.breakpoint.name }}</div>
    </v-alert>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component
export default class MainView extends Vue {}
</script>
